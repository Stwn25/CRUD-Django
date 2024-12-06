from django.urls import path
from .import views

urlpatterns = [
    path('', views.login_page, name="login-page"),

    # Aktor Owner
    path('dashboard-owner/', views.owner_dashboard, name="dashboard-owner"),
    path('data-pelanggan/', views.data_pelanggan, name="data-pelanggan"),
    path('data-pelanggan-owner/', views.data_pelanggan_owner, name="data-pelanggan-owner"),
    path('create-data-pelanggan/', views.create_data_pelanggan, name="create-data-pelanggan"),
    path('update-data-pelanggan/<str:id>/', views.update_data_pelanggan, name="update-data-pelanggan"),
    path('delete-data-pelanggan/<str:id>/', views.delete_data_pelanggan, name="delete-data-pelanggan"),

    # Aktor Admin
    path('dashboard-admin/', views.admin_dashboard, name="dashboard-admin"),
    path('data-admin/', views.data_admin, name="data-admin"),
    path('create-data-admin/', views.create_data_admin, name="create-data-admin"),
    path('update-data-admin/<str:id>/', views.update_data_admin, name="update-data-admin"),
    path('delete-data-admin/<str:id>/', views.delete_data_admin, name="delete-data-admin"),

    # Data Pemesanan
    path('create-data-pemesanan/', views.create_data_pemesanan, name="create-data-pemesanan"),
]