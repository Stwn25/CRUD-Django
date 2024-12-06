from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Owner)
admin.site.register(Admin)
admin.site.register(Pelanggan)
admin.site.register(LayananSewa)
admin.site.register(DetailPemesanan)
admin.site.register(KategoriMobil)
admin.site.register(StatusPemesanan)
admin.site.register(JenisLayanan)