from django.db import models

# Create your models here.
class Owner(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model Admin
class Admin(models.Model):
    id_admin = models.AutoField(primary_key=True)
    nama_admin = models.CharField(max_length=100)
    username_admin = models.CharField(max_length=20, unique=True)
    password_admin = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_admin

# Model Kategori Mobil
class KategoriMobil(models.Model):
    id_kategori = models.AutoField(primary_key=True)
    nama_kategori = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_kategori

# Model Jenis Layanan
class JenisLayanan(models.Model):
    id_jenis_layanan = models.AutoField(primary_key=True)
    nama_layanan = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_layanan

# Model Layanan Sewa
class LayananSewa(models.Model):
    id_layanan = models.AutoField(primary_key=True)
    id_kategori = models.ForeignKey(KategoriMobil, on_delete=models.CASCADE, related_name='layanan')
    id_jenis_layanan = models.ForeignKey(JenisLayanan, on_delete=models.CASCADE, related_name='layanan')
    harga_layanan = models.FloatField()

    def __str__(self):
        return f"{self.id_jenis_layanan.nama_layanan} - {self.id_kategori.nama_kategori}"

# Model Pelanggan
class Pelanggan(models.Model):
    id_customer = models.AutoField(primary_key=True)
    nama_pelanggan = models.CharField(max_length=100)
    alamat = models.CharField(max_length=200)
    nomor_hp = models.CharField(max_length=20)

    def __str__(self):
        return self.nama_pelanggan
    
class StatusPemesanan(models.Model):
    id_status = models.AutoField(primary_key=True)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status  

# Model Detail Pemesanan (Relasi Many-to-Many)
class DetailPemesanan(models.Model):
    id_pemesanan = models.AutoField(primary_key=True)
    tanggal_pengerjaan = models.DateField()
    tanggal_pemesanan = models.DateField()
    admin = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True, related_name='pemesanan')
    pelanggan = models.ForeignKey(Pelanggan, on_delete=models.SET_NULL, null=True, related_name='pemesanan')
    layanan_sewa = models.ForeignKey(LayananSewa, on_delete=models.CASCADE, related_name='pemesanan')
    status = models.ForeignKey(StatusPemesanan, on_delete=models.SET_NULL, null=True, related_name='pemesanan')

    def __str__(self):
        return f"Pemesanan #{self.id_pemesanan} oleh {self.pelanggan.nama_pelanggan} - Status: {self.status.status if self.status else 'Tidak Ada Status'}"

    @property
    def harga(self):
        return self.layanan_sewa.harga_layanan