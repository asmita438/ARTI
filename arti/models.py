from django.db import models
from pages.models import Page


class Paragraph(models.Model):
    text = models.TextField()
    font_size = models.IntegerField()
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    paragraph_no = models.IntegerField(default=1)
    CENTER = 'C'
    LEFT = 'L'
    RIGHT = 'R'
    justification_choices = [
        (CENTER, 'Center'),
        (LEFT, 'Left'),
        (RIGHT, 'Right'),
    ]
    justification = models.CharField(
        max_length=6,
        choices=justification_choices,
        default=CENTER,
    )
