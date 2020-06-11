from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from location.forms import LocationForm
from location.models import Location

# Create your views here.

#CreateView => adauga in DB
#UpdateView => modifica in DB pe baza unui pk / id dintr-o tabela
#ListView => listeaza toate elementele din modelul respectiv / tabela

class LocationsList(ListView):
    model = Location
    template_name = 'location/location_index.html'
    context_object_name = 'all_locations'

class NewLocationView(CreateView):
    model = Location
    fields = ['city', 'country']
    template_name = 'location/location_form.html'

    def get_success_url(self):
        return reverse('location:location_list')

class UpdateLocationView(UpdateView):
    model = Location
    # fields = ['city', 'country']
    form_class = LocationForm
    template_name = 'location/location_form.html'

    def get_form_kwargs(self):
        kwargs = super(UpdateLocationView, self).get_form_kwargs()
        kwargs.update({'pk': self})
        return kwargs

    def get_success_url(self):
        return reverse('location:location_list')
