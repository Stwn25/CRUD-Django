from django.forms import ModelForm
from . models import *

class  PelangganForm(ModelForm):
    class Meta:
        model = Pelanggan
        fields = '__all__'

class AdminForm(ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'

class PemesananForm(ModelForm):
    class Meta:
        model = DetailPemesanan
        fields = '__all__'
