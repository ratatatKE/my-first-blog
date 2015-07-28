from django.shortcuts import render
from django.http  import  HttpResponse
from django.views.generic import ListView, View
from contacts.models import Contact

# Create your views here, can you imagine, we are using what are called class based views
class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello World")

class ListContactView(ListView):
    model = Contact #this model lists all the contacts in our database
    template_name = 'contact_list.html'