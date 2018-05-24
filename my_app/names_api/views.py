from django.shortcuts import render, HttpResponse
from django.views import View
from names_api.models import Person
from .create_database import create_default_database

# Create your views here.

class CreateNamesInDatabase(View):
    def get(self, request):
        list_of_person_objects = Person.objects.all()

        # create default database if not created yet
        if not list_of_person_objects:
            create_default_database()

        ctx = {
            'list_of_person_objects': list_of_person_objects,
        }

        return render(request, 'home.html', ctx)

    def post(self, request):
        pass
