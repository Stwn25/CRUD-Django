from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from . forms import PelangganForm, AdminForm, PemesananForm

def login_page(request):
    return render(request, 'base/login.html')

# VIEW OWNER -------------------------------------------------------------------------------------------

def owner_dashboard(request):
    data_pelanggan = Pelanggan.objects.all()
    data_pemesanan = DetailPemesanan.objects.all()
    
    context = {
        'data_pemesanan': data_pemesanan,
        'data_pelanggan': data_pelanggan
    }
    
    return render(request, 'owner/dashboard.html', context) 

##Data Pelanggan
def data_pelanggan_owner(request):
    data_pelanggan = Pelanggan.objects.all()

    context = {
        'data_pelanggan': data_pelanggan
    }

    return render(request, 'owner/data-pelanggan.html', context)

##Data Admin

def data_admin(request):
    data_admin = Admin.objects.all()

    context = {
        'data_admin': data_admin
    }

    return render(request, 'owner/data-admin.html', context)

def create_data_admin(request):

    form = AdminForm()
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/data-admin')

    context = {
        'form': form
    }
    return render(request, 'owner/create-data-admin.html', context)

def update_data_admin(request, id):
    admin = Admin.objects.get(id_admin=id)
    form = AdminForm(instance=admin)
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = AdminForm(request.POST, instance=admin)
        if form.is_valid():
            form.save()
            return redirect('/data-admin')

    return render(request, 'owner/update-data-admin.html', context)

def delete_data_admin(request, id):
    admin = Admin.objects.get(id_admin=id)
    if request.method == 'POST':
        admin.delete()
        return redirect('/data-admin')
    context = {
        'admin': admin
    }
    return render(request, 'owner/delete-data-admin.html', context)

# VIEW ADMIN -------------------------------------------------------------------------------------------

def admin_dashboard(request):
    data_pelanggan = Pelanggan.objects.all()
    data_pemesanan = DetailPemesanan.objects.all()
    
    context = {
        'data_pemesanan': data_pemesanan,
        'data_pelanggan': data_pelanggan
    }

    return render(request, 'admin/dashboard.html', context)

##Data Pelanggan
def data_pelanggan(request):
    data_pelanggan = Pelanggan.objects.all()

    context = {
        'data_pelanggan': data_pelanggan
    }

    return render(request, 'admin/data-pelanggan.html', context)

def create_data_pelanggan(request):

    form = PelangganForm()
    if request.method == 'POST':
        form = PelangganForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/data-pelanggan')

    context = {
        'form': form
    }
    return render(request, 'admin/create-data-pelanggan.html', context)

def update_data_pelanggan(request, id):
    pelanggan = Pelanggan.objects.get(id_customer=id)
    form = PelangganForm(instance=pelanggan)
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = PelangganForm(request.POST, instance=pelanggan)
        if form.is_valid():
            form.save()
            return redirect('/data-pelanggan')

    return render(request, 'admin/update-data-pelanggan.html', context)

def delete_data_pelanggan(request, id):
    pelanggan = Pelanggan.objects.get(id_customer=id)
    if request.method == 'POST':
        pelanggan.delete()
        return redirect('/data-pelanggan')
    context = {
        'pelanggan': pelanggan
    }
    return render(request, 'admin/delete-data-pelanggan.html', context)

# Data pemesanan

def create_data_pemesanan(request):

    form = PemesananForm()
    if request.method == 'POST':
        form = PemesananForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard-admin')
        
    context = {
        'form': form
    }

    return render(request, 'admin/data-pemesanan/create-data.html', context)