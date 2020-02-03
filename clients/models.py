from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, default=' ')
    address = models.CharField(max_length=50, blank=True, null=True, default=' ')
    city = models.CharField(max_length=50, default=' ')
    state = models.CharField(max_length=50, default='NE')
    zipcode = models.CharField(max_length=10, default='00000')
    email = models.EmailField(max_length=100, default=' ')
    cell_phone = models.CharField(max_length=50, default='(402)000-0000')
    acct_number = models.CharField(max_length=50, blank=True, null=True, default='00000')
    notes = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('client_detail', args=[str(self.id)])


class Comment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE,
                               related_name='comments', null=True)
    comment = models.TextField(max_length=140, default='', blank=True, null=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return 'Comment {} '.format(self.comment)

    def get_absolute_url(self):
        return reverse('Client_detail')


class VechicleByCustomer(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='vechicles',
    )
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    vin_number = models.CharField(max_length=50)
    Date_Of_Purchase = models.DateTimeField(default='', null=True, blank=True)
    Date_Of_LastService = models.DateTimeField(default='', null=True, blank=True)

    def __str__(self):
        return '{} has vechicle make {}, model {}, vin_number {}, Date_Of_Purchase {} and its last service date is {}'.\
            format(self.client.name, self.make, self.model,self.vin_number, self.Date_Of_Purchase, self.Date_Of_Purchase)
