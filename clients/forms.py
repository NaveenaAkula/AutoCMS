from django import forms
from .models import Comment, VechicleByCustomer


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'author', ]


class VechicleForm(forms.ModelForm):
    class Meta:
        model = VechicleByCustomer
        fields = ('client', 'make', 'model', 'vin_number', 'Date_Of_Purchase',
                  'Date_Of_LastService')
