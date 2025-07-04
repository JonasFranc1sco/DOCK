from django.shortcuts import render, redirect
from page.forms import PageForm
from django.utils import timezone
from page.models import Page
from accounts.views import success

def post_create(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_feed')
    else:
        form = PageForm()
    
    return render(request, 'page/post_create.html', {'form': form})
            
def post_feed(request):
    posts = Page.objects.select_related('author').all().order_by('-publication_date')
    return render(request, 'page/post_feed.html', {'posts': posts})

def user_post(request):
    if request.user.is_authenticated:
        posts = Page.objects.filter(author=request.user)
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
            