from django.shortcuts import render, redirect, get_object_or_404
from page.forms import PageForm, DiaryForm
from django.utils import timezone
from page.models import Page, Diary
from accounts.views import success

# Função listagem do Feed de publicações dos usuários
def feed(request):
    if request.user.is_authenticated:
        my_diary = Diary.objects.filter(author=request.user).order_by('-public_access_date')
        diaries = Diary.objects.filter(public_access=True).order_by('-public_access_date')
        
    else:
        return redirect('login')
        
    return render(request, 'page/feed.html', {
        'diaries': diaries, 
        'my_diary': my_diary})
    
# Função para criar um diário
def diary_create(request):
    if request.method == 'POST':
        page_form = PageForm(request.POST)
        diary_form = DiaryForm(request.POST)
        if page_form.is_valid() and diary_form.is_valid():
            diary = diary_form.save(commit=False)
            diary.author = request.user
            diary.save()
                
            page = page_form.save(commit=False)
            page.diary = diary
            if not page.title:
                page.title = timezone.now().date().strftime('%d/%m/%Y')
            page.save()
                
            return redirect('user_diaries')
    else:
        page_form = PageForm()
        diary_form = DiaryForm()
        
    return render(request, 'page/diary_create.html', {'page_form': page_form,'diary_form': diary_form})

# Função listagem de Diários apenas do usuário
def user_diaries(request):
    if request.user.is_authenticated:
        diaries = Diary.objects.filter(author=request.user).order_by('-diary_creation_date')
    else:
        return redirect('login')
    return render(request, 'page/user_diaries.html', {'diaries': diaries})

# Função para atualizar os dados do diário
def diary_update(request, diary_id):
    diary = get_object_or_404(Diary, id=diary_id)
    if diary.author != request.user:
        return redirect('feed')
    if request.method == 'POST':
        form = DiaryForm(request.POST, instance=diary)
        if form.is_valid():
            form.save()
            return redirect('user_diaries')
    else:
        form = DiaryForm(instance=diary)
    return render(request, 'page/diary_update.html', {'form': form, 'diary': diary})

# Função para atualizar os dados da página
def page_update(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    diary = page.diary
    if request.method == 'POST':
        form = PageForm(request.POST, instance=page)
        if form.is_valid():
            form.save()
            return redirect('user_diaries')
    else:
        form = PageForm(instance=page)
    return render(request, 'page/page_update.html', {'form': form, 'diary': diary, 'page_num': page.page_num})
            
def page_add(request, diary_id):
    diary = get_object_or_404(Diary, id=diary_id)
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.diary = diary
            page.page_num = diary.pages.count() + 1
            page.save()
            return redirect('feed')
    else:
        form = PageForm()
        
    return render(request, 'page/page_add.html', {'form': form, 'diary': diary})

def page_delete(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    if page.author != request.user:
        return redirect('feed')
    page.delete()
    return redirect('user_diaries')

def diary_delete(request, diary_id):
    diary = get_object_or_404(Diary, id=diary_id)
    if diary.author != request.user:
        return redirect('feed')
    diary.delete()
    return redirect('user_diaries')

def diary_view(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    
    # Verifica se o usuário tem permissão para ver o diário
    if not diary.public_access:
        # Se for privado, só o autor pode ver
        if not request.user.is_authenticated or diary.author != request.user:
            return redirect('feed')
    
    # Se chegou até aqui, pode ver o diário (público ou privado do próprio autor)
    
    # Busca todas as páginas do diário ordenadas por número
    pages = diary.pages.all().order_by('page_num')
    
    # Informações extras para o template
    context = {
        'diary': diary,
        'pages': pages,
        'total_pages': pages.count(),
        'is_owner': request.user.is_authenticated and request.user == diary.author,
    }
    
    return render(request, 'page/diary_view.html', context)