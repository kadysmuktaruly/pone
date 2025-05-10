from django.shortcuts import render, redirect, get_object_or_404
from .models import Manga, Chapter
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def manga_detail(request, manga_id):
    manga = Manga.objects.get(id=manga_id)
    return render(request, 'manga/manga_detail.html', {'manga': manga})


from .models import Chapter

def chapter_detail(request, chapter_id):
    chapter = Chapter.objects.get(id=chapter_id)
    return render(request, 'manga/chapter_detail.html', {'chapter': chapter})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to homepage after signup
    else:
        form = UserCreationForm()
    return render(request, 'manga/signup.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    return render(request, 'manga/home.html')

def read_chapter(request, manga_id, chapter_number):
    manga = get_object_or_404(Manga, id=manga_id)
    chapter = get_object_or_404(Chapter, manga=manga, number=chapter_number)
    pages = chapter.pages.order_by('page_number')
    return render(request, 'manga/read_chapter.html', {
        'manga': manga,
        'chapter': chapter,
        'pages': pages
    })