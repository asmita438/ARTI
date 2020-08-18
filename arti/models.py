from django.db import models
from fpdf import FPDF
from book.models import Book
from pages.models import Page

from django.conf import settings
import os

class BookPDF(FPDF):
    def __init__(self, book):
        self.book = book
        super().__init__()
    
    def header(self):
        if self.page_no() == 1:
            return
        self.set_font('Helvetica', 'B', 14)
        self.cell(0, 10,
                  "Title - " + str(self.book.title), ln=1, align='L')
    
    def footer(self):
        if self.page_no() == 1:
            return
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()-1) + '/{nb}', 0, 0, 'C')
    
    def create(self):
        self.alias_nb_pages()
        self.add_page()
        self.set_font('Arial','', 50)

        if self.book.book_image:
            image_location = os.path.join(settings.BASE_DIR, "media/" + self.book.book_image.name)
            self.image(image_location, self.l_margin, 10, self.w-self.l_margin-self.r_margin, self.h-10-10)
        x = (self.w-self.l_margin-self.r_margin)/2
        w = self.get_string_width(self.book.title)
        x = x-w/2
        
        y = 10  + 25
        self.set_xy(x, y)
        self.cell(0, 0, self.book.title)
         
        self.add_page()
        for page in self.book.page_set.all():
            for paragraph in page.paragraph_set.all():
                self.set_font('Helvetica', 'B', paragraph.font_size)
                self.multi_cell(0, paragraph.font_size/2, paragraph.text, align=paragraph.justification)
                
        file_location = "pdfs/{}.pdf".format(self.book.id)
        d= settings.STATICFILES_DIRS[0]
        output_file = os.path.join(d, file_location)
        self.output(output_file)
        return file_location

# ~ pdf = NewBook(book_i1.d)
# ~ pdf.alias_nb_pages()
# ~ pdf.add_page()
# ~ pdf.set_font('Times', '', 12)


# ~ pdf.output('new.pdf', 'F')

