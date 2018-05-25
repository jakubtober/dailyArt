from django.shortcuts import render, HttpResponse
from django.views import View
from names_api.models import Person
from .create_database import fill_database
from rest_framework.generics import ListAPIView, RetrieveAPIView
from names_api.serializers import NamesSerializer

# Create your views here.

class CreateNamesInDatabase(View):
    def get(self, request):
        list_of_person_objects = Person.objects.all()

        # create default database if not created yet
        if not list_of_person_objects:
            fill_database()

        ctx = {
            'list_of_person_objects': list_of_person_objects,
        }

        return HttpResponse('Looks like your database is set. :)')

    def post(self, request):
        pass


class NamesEditView(View):
    def get(self, request):
        list_of_person_objects = Person.objects.all()

        ctx = {
            'list_of_person_objects': list_of_person_objects,
        }
        return render(request, 'home.html', ctx)


class NamesListAPIView(ListAPIView) :
    queryset = Person.objects.all()
    serializer_class = NamesSerializer


class PersonDetailAPIView(RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = NamesSerializer
