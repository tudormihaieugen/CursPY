from django import forms
from location.models import Location

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = {'city', 'country'}

    def __init__(self,pk , *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)
        self.pk = pk

    def clean(self):
        cleaned_data = self.cleaned_data
        cityVal = cleaned_data.get('city')  #accesam valorile din input html
        countryVal = cleaned_data.get('country')
        # Location.objects.get()  #returneaza un singur rezultat iar in cazul in care retunreaza mai multe sau niciun obiect apare eroare
        # Location.objects.filter()  #returneaza o lista de obiecte si nu apare eroare in caz de mai multe obiecte/nule
        if Location.objects.filter(city=cityVal, country=countryVal).exists():
            msg = 'City and country already exist'
            self._errors['city'] = self.error_class([msg])
        return cleaned_data
