from django.shortcuts import render
from django.views import generic
from book.models import Book
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


class BookList(LoginRequiredMixin, generic.ListView):
    model = Book
    template_name = 'book_list.html'

class BookSearch(LoginRequiredMixin, generic.ListView):
    template_name = 'book_list.html'
    
    def get_queryset(self):
        print(self.request.GET)
        title = self.request.GET.get("title", "")
        return Book.objects.filter(title__icontains=title).order_by("title")


class BookDetailView(LoginRequiredMixin,generic.DetailView):
    model = Book
    template_name = 'book_detail.html'

class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    fields = ['title', 'book_image', 'author', 'price', 'series', 'isbn', 'subject', 'publisher_name', 'publisher_place', 'publisher_year']
    success_url = reverse_lazy("book-list")
    template_name = 'create.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Book
    success_url = reverse_lazy('book-list')
    template_name = 'delete.html'

    def form_valid(self, form):
       if  form.instance.user == self.request.user:        
           return super().form_valid(form)
    
    

    

class BookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Book
    fields = ['title', 'book_image', 'author', 'price', 'series', 'isbn', 'subject', 'publisher_name', 'publisher_place', 'publisher_year']
    template_name = 'create.html'

    def get_success_url(self):
        return reverse_lazy('book-list')
    
    def form_valid(self, form):
        if form.instance.user == self.request.user and form.instance.state in ['BT', 'VD']:
            return super().form_valid(form)
        return render(self.request, 'error.html')
            
        
    
        


class BookUpdateStateView(LoginRequiredMixin, generic.UpdateView):
    model = Book
    fields = ['state']
    template_name = 'create.html'

    def get_success_url(self):
        return reverse_lazy('book-list')


def request_verification(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.user.is_authenticated and request.user == book.user:
        book.state = "VR"
        book.save()
    return HttpResponseRedirect(reverse("book-detail", args=[book_id]))
    
def deny_verification(request, book_id):
    if request.user.is_staff:
        book = Book.objects.get(id=book_id)
        book.state = "VD"
        book.save()
    return HttpResponseRedirect(reverse("book-detail", args=[book_id]))

def verify(request, book_id):
    if request.user.is_staff:
        book = Book.objects.get(id=book_id)
        book.state = "VF"
        book.save()
    return HttpResponseRedirect(reverse("book-detail", args=[book_id]))
    
def cancel_verification(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.user.is_authenticated and request.user == book.user:
        book.state = "BT"
        book.save()
    return HttpResponseRedirect(reverse("book-detail", args=[book_id]))
    
class AllBooksBeingTranslated(LoginRequiredMixin, generic.ListView):
    template_name = 'book_list.html'
    
    def get_queryset(self):
        return Book.objects.filter(state="BT").order_by("title") 

class AllBooksVerified(LoginRequiredMixin, generic.ListView):
    template_name = 'book_list.html'
    
    def get_queryset(self):
           return Book.objects.filter(state="VF").order_by("title") 
           
class AllBooksDeniedTranslation(LoginRequiredMixin, generic.ListView):
    template_name = 'book_list.html'
    
    def get_queryset(self):
           return Book.objects.filter(state="VD").order_by("title") 

class AllBooksRequestingVF(LoginRequiredMixin, generic.ListView):
    template_name = 'book_list.html'
    
    def get_queryset(self):
           return Book.objects.filter(state="VR").order_by("title") 

class UserBooksBeingTranslated(LoginRequiredMixin, generic.ListView):
    template_name = 'book_list.html'
    
    def get_queryset(self):
        return Book.objects.filter(state="BT").filter(user=self.request.user).order_by("title") 
        
class UserBooksVerified(LoginRequiredMixin, generic.ListView):
    template_name = 'book_list.html'
    
    def get_queryset(self):
           return Book.objects.filter(state="VF").filter(user=self.request.user).order_by("title") 
           
class UserBooksDeniedTranslation(LoginRequiredMixin, generic.ListView):
    template_name = 'book_list.html'
    
    def get_queryset(self):
           return Book.objects.filter(state="VD").filter(user=self.request.user).order_by("title")
           
class UserBooksRequestingVF(LoginRequiredMixin, generic.ListView):
    template_name = 'book_list.html'
    
    def get_queryset(self):
           return Book.objects.filter(state="VR").filter(user=self.request.user).order_by("title")
