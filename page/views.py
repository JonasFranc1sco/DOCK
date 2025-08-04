from django.shortcuts import render, redirect
from page.forms import PageForm
from django.utils import timezone
from page.models import Page
from accounts.views import success
            
def post_feed(request):
    if request.user.is_authenticated:
        my_posts = Page.objects.filter(author=request.user).order_by('-publication_date')
        posts = Page.objects.filter(public_access=True).order_by('-publication_date')
        
        if request.method == 'POST':
            form = PageForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                if not post.title:
                    post.title = timezone.now().date().strftime('%d/%m/%Y')
                post.save()
                return redirect('post_feed')
        else:
            form = PageForm()
    else:
        return redirect('login')
        
    return render(request, 'page/post_feed.html', {
        'posts': posts, 
        'my_posts': my_posts,
        'form': form
        })

def user_post(request):
    if request.user.is_authenticated:
        posts = Page.objects.filter(author=request.user).order_by('-publication_date')
    else:
        return redirect('login')
    return render(request, 'page/user_posts.html', {'posts': posts})

def post_edit(request, page_id):
    page = Page.objects.get(pk=page_id)
    if request.method == 'POST':
        form = PageForm(request.POST, instance=page)
        if form.is_valid():
            form.save()
            return redirect('user_post')
    else:
        form = PageForm(instance=page)
        
    return render(request, 'page/post_edit.html', {'form': form})

def post_delete(request, page_id):
    page = Page.objects.get(pk=page_id)
    page.delete()
    return redirect('user_post')    
            