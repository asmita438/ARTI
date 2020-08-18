from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.TextField()
    book_image = models.ImageField(upload_to='pictures',max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    BT = 'BT'
    VR = 'VR'
    VF = 'VF'
    VD = 'VD'
    
    state_of_the_book = [
        (BT, 'Being translated'),
        (VR, 'Verification requested'),
        (VF, 'Verified'),
        (VD, 'Verification denied')
    ]
    state = models.CharField(
        max_length=20,
        choices = state_of_the_book,
        default= BT,
    )
    author = models.CharField(max_length=100, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, default="")

    publisher_name = models.CharField(max_length=100, default="")
    publisher_place = models.CharField(max_length=100, default="")
    publisher_year  = models.IntegerField(default=0)
    
    series = models.CharField(max_length=100, default="")
    isbn = models.IntegerField(default=0)
    subject = models.TextField(default="")
    
    def get_state_name(self):
        current_state = list(filter(lambda tpl: tpl[0]==self.state, self.state_of_the_book))[0][1]
        return current_state
    
    def get_all_pages(self):
        return self.page_set.all().order_by("page_no")
    
