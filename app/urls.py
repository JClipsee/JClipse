from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="homePage"),
    path('about/', views.about_page, name="aboutPage"),
    path('portfolio/', views.portfolio_page, name="portfolioPage"),
    path('services/', views.services_page, name="servicesPage"),
    path('contact/', views.contact_page, name="contactPage"),

    path('database/', views.database_page, name="databasePage"),

    path('appointment/', views.appointment_page, name="appointmentPage"),
    path('client/', views.client_page, name="clientPage"),
    path('photographer/', views.photographer_page, name="photographerPage"),
    path('adminClient/', views.aclient_page, name="adminClientPage"),
    path('offer/', views.offer_page, name="adminOfferPage"),
    path('a_appointment/', views.a_appointment_page, name="adminAppointmentPage"),

    path('photographer/<int:pk>/edit/', views.update_photographer, name='updatePhotographer'),
    path('delete_photographer/<int:pk>/edit/', views.delete_photographer, name='deletePhotographer'),

    path('client/<int:pk>/edit/', views.update_client, name='updateClient'),
    path('delete_client/<int:pk>/edit/', views.delete_client, name='deleteClient'),

    path('offer/<int:pk>/edit/', views.update_offer, name='updateOffer'),
    path('delete_offer/<int:pk>/edit/', views.delete_offer, name='deleteOffer'),

    path('appointment/<int:pk>/edit/', views.update_appointment, name='updateAppointment'),
    path('delete_appointment/<int:pk>/edit/', views.delete_appointment, name='deleteAppointment'),


]