from django.shortcuts import render, redirect
from page.forms import PageForm
from django.utils import timezone
from page.models import Page
from accounts.views import success

def post_create(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('success')
    else:
        form = PageForm()
    return render(request, 'page/post_create.html', {'form': form})
            
def post_feed(request):
    posts = Page.objects.select_related('author').all().order_by('-publication_date')
    return render(request, 'page/post_feed.html', {'posts': posts})