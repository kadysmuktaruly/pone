from django.db import models

class Manga(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=255, blank=True)
    cover_image = models.ImageField(upload_to='covers/')

    def __str__(self):
        return self.title

class Chapter(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='chapters')
    title = models.CharField(max_length=255)
    number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.manga.title} - Chapter {self.number}: {self.title}"

class Page(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='pages')
    image = models.ImageField(upload_to='pages/')
    page_number = models.IntegerField()

    def __str__(self):
        return f"{self.chapter} - Page {self.page_number}"
