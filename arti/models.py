from django.db import models
from book.models import Book

class Page(models.Model):
    page_no = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pictures',max_length=255, null=True, blank=True)
