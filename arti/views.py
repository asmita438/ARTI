from django.shortcuts import render
from django.views import generic
from django.views import View
from book.models import Book
from pages.models import Page
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class PageList(LoginRequiredMixin, generic.ListView):
    model = Page
    template_name = 'page_list.html'

class PageDetailView(LoginRequiredMixin, generic.DetailView):
    model = Page
    template_name = 'page_detail.html'

class PageForBookCreateView(LoginRequiredMixin, View):
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        pages = book.page_set.all().order_by("page_no")
        if pages.count() > 0:
            largest_page = pages.last()
            page_no = largest_page.page_no+1
        else: page_no = 1
        
        new_page = Page.objects.create(page_no=page_no, book=book)
        new_page.save()
        return HttpResponseRedirect(self.get_success_url(new_page.id))

    def form_valid(self, form):
        if form.instance.user == self.request.user and form.instance.state in ['BT', 'VD']:
            return super().form_valid(form)
        return render(self.request, 'error.html')


    def get_success_url(self, page_id):
        return reverse_lazy('page-detail',  args=[page_id])
    
    

class PageDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Page
    
    template_name = 'delete.html'
    
    def get_success_url(self):
        return reverse_lazy('book-detail',  args=[self.object.book.id])

    def form_valid(self, form):
        if form.instance.user == self.request.user:
            return super().form_valid(form)

class PageForBookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Page
    fields = ['page_no', 'image']
    template_name = 'create.html'

    def get_success_url(self):
        return reverse_lazy('book-detail',  args=[self.object.book.id])

    def form_valid(self, form):
        if form.instance.user == self.request.user \
           and form.instance.state in ['BT', 'VD']:
            return super().form_valid(form)
        return render(self.request, 'error.html')
            
        

