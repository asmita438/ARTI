from django.shortcuts import render
from django.views import generic
from paragraph.models import Paragraph
from pages.models import Page
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



class ParagraphList(LoginRequiredMixin, generic.ListView):
    model = Paragraph
    template_name = 'paragraph_list.html'


class ParagraphForPageCreateView(LoginRequiredMixin, generic.CreateView):
    model = Paragraph
    fields = ['text', 'font_size', 'justification']
    template_name = 'create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.page = Page.objects.get(id=self.kwargs['page_id'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


    def get_success_url(self):
        return reverse_lazy('page-detail',  args=[self.kwargs['page_id']])

    def form_valid(self, form):
        if form.instance.user == self.request.user and form.instance.state in ['BT', 'VD']:
            return super().form_valid(form)
        return render(self.request, 'error.html')


class ParagraphDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Paragraph
    template_name = 'delete.html'


    def get_success_url(self):
        return reverse_lazy('page-detail',  args=[self.object.page.id])

    def form_valid(self, form):
        if form.instance.user == self.request.user:
            return super().form_valid(form)
        

class ParagraphForPageUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Paragraph
    fields = ['font_size', 'text', 'paragraph_no', 'justification']
    template_name = 'create.html'

    def get_success_url(self):
        return reverse_lazy('page-detail',  args=[self.object.page.id])

    def form_valid(self, form):
        if form.instance.user == self.request.user \
           and form.instance.state in ['BT', 'VD']:
            return super().form_valid(form)
        return render(self.request, 'error.html')
