from django import forms
from .models import Model_girl
from .models import Brand
from django.db import models


class ModelGirlForm(forms.Form):
    name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    height = forms.FloatField()
    age = forms.IntegerField()
    birthdate = forms.DateField(required=False)


class SearchModelGirlForm(forms.Form):
    height = forms.FloatField(required=False)


class BrandForm(forms.Form):
    name = forms.CharField(max_length=255)
    city = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)


class SearchBrandForm(forms.Form):
    name = forms.CharField(required=False)


class ClientForm(forms.Form):
    name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()


class SearchClientForm(forms.Form):
    name = forms.CharField(required=False)
