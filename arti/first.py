from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Logo
        
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        
        # Title
        actual_width = self.w - self.l_margin - self.r_margin
        self.cell(0.7*actual_width, 10, 'Name: Asmita', 1, 0, 'L')
        self.cell(0.3*actual_width, 10, 'Age: 23', 1, 1, 'L')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

# Instantiation of inherited class
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Times', '', 12)
pdf.add_page()

pdf.output('tuto4.pdf', 'F')


