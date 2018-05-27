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


class HomeView(View):
    def get(self, request):
        list_of_person_objects = Person.objects.all()

        ctx = {
            'list_of_person_objects': list_of_person_objects,
        }
        return render(request, 'home.html', ctx)

    def post(self, request):
        list_of_person_objects = Person.objects.all()
        raw_new_names_to_add = request.POST.get('new_names_to_add')
        raw_new_last_names_to_add = request.POST.get('new_last_names_to_add')
        unique_id_to_delete = request.POST.get('person_to_delete')

        if raw_new_names_to_add and raw_new_last_names_to_add:
            new_names_to_add = raw_new_names_to_add.replace("\r", "").split("\n")
            new_last_names_to_add = raw_new_last_names_to_add.replace("\r", "").split("\n")
            print(new_names_to_add)
            print(new_last_names_to_add)

        if unique_id_to_delete:
            person_to_delete = Person.objects.filter(unique_id=unique_id_to_delete)
            print(person_to_delete)

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
