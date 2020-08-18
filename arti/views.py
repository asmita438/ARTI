from django.shortcuts import render, redirect
from .models import BookPDF
from book.models import Book

def generate_pdf(self, book_id):
    if Book.objects.filter(id=book_id).exists():
        b = Book.objects.get(id=book_id)
        books = BookPDF(b)
        location = books.create()
        print(location)
        return redirect("/static/" + location)
