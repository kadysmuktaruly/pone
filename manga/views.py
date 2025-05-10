from django.shortcuts import render, redirect
from .models import Manga
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
