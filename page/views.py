from django.shortcuts import render, redirect
from page.forms import PageForm
from django.utils import timezone
from page.models import Page
from accounts.views import success

def page_post(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('success')
    else:
        form = PageForm()
    return render(request, 'page/create_page.html', {'form': form})
            
def post_feed(request):
    posts = Page.objects.filter(publication_date__lte=timezone.now()).order_by('publication_date')
    return render(request, 'page/post_feed.html', {'posts': posts})