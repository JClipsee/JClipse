from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.core.serializers.json import DjangoJSONEncoder
import json

#Forms
from .form import AppointmentForm
from .form import ClientForm
from .form import PhotographerForm
from .form import OfferForm


def home_page(request):
    return render(request, 'pages/home.html')


def about_page(request):
    return render(request, 'pages/aboutus.html')


def portfolio_page(request):
    return render(request, 'pages/portfolio.html')


def services_page(request):
    return render(request, 'pages/services.html')


def contact_page(request):
    return render(request, 'pages/contact.html')


def photographer_page(request):
    form = PhotographerForm()
    if request.method == 'POST':
        form = PhotographerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('databasePage')
    context = {
        'form': form
    }
    return render(request, 'pages/ADMINPhotographer.html', context)


def update_photographer(request, pk):
    photographer = Photographer.objects.get(id=pk)
    form = PhotographerForm(instance=photographer)
    if request.method == 'POST':
        form = PhotographerForm(request.POST, instance=photographer)
        if form.is_valid():
            form.save()
            return redirect('databasePage')
    context = {
        'form': form,
        'photographer': photographer  # Pass the photographer to the template for context
    }
    return render(request, 'pages/UPDATEPhotographer.html', context)


def delete_photographer(request, pk):
    photographer = Photographer.objects.get(id=pk)
    if request.method == 'POST':
        photographer.delete()
        return redirect('databasePage')
    context = {
        'photographer': photographer
    }
    return render(request, 'pages/DELETEPhotographer.html', context)


def appointment_page(request):
    form = AppointmentForm()
    offers = list(Offers.objects.all().values('id', 'price', 'name'))  # Ensure `name` field is included for display
    offers_json = json.dumps(offers, cls=DjangoJSONEncoder)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            offer = form.cleaned_data['offer']
            appointment = form.save(commit=False)
            appointment.price = offer.price
            appointment.save()
            return redirect('homePage')

    context = {
        'form': form,
        'offers': offers_json
    }
    return render(request, 'pages/FORMAppointment.html', context)


def client_page(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointmentPage')
    context = {
        'form': form
    }
    return render(request, 'pages/FORMClient.html', context)


def aclient_page(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('databasePage')
    context = {
        'form': form
    }
    return render(request, 'pages/ADMINClient.html', context)


def update_client(request, pk):
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('databasePage')
    context = {
        'form': form,
        'client': client  # Pass the client to the template for context
    }
    return render(request, 'pages/UPDATEClient.html', context)


def delete_client(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('databasePage')
    context = {
        'client': client
    }
    return render(request, 'pages/DELETEClient.html', context)


def offer_page(request):
    form = OfferForm()
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('databasePage')
    context = {
        'form': form
    }
    return render(request, 'pages/ADMINOffer.html', context)


def update_offer(request, pk):
    offer = Offers.objects.get(id=pk)
    form = OfferForm(instance=offer)
    if request.method == 'POST':
        form = OfferForm(request.POST, instance=offer)
        if form.is_valid():
            form.save()
            return redirect('databasePage')
    context = {
        'form': form,
        'offer': offer
    }
    return render(request, 'pages/UPDATEOffer.html', context)


def delete_offer(request, pk):
    offer = Offers.objects.get(id=pk)
    if request.method == 'POST':
        offer.delete()
        return redirect('databasePage')
    context = {
        'offer': offer
    }
    return render(request, 'pages/DELETEOffer.html', context)


def a_appointment_page(request):
    form = AppointmentForm()
    offers = list(Offers.objects.all().values('id', 'price', 'name'))
    offers_json = json.dumps(offers, cls=DjangoJSONEncoder)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            offer = form.cleaned_data['offer']
            appointment = form.save(commit=False)
            appointment.price = offer.price
            appointment.save()
            return redirect('databasePage')

    context = {
        'form': form,
        'offers': offers_json
    }
    return render(request, 'pages/ADMINAppointment.html', context)


def update_appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    form = AppointmentForm(instance=appointment)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('databasePage')
    context = {
        'form': form,
        'appointment': appointment
    }
    return render(request, 'pages/UPDATEAppointment.html', context)


def delete_appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('databasePage')
    context = {
        'appointment': appointment
    }
    return render(request, 'pages/DELETEAppointment.html', context)


def database_page(request):

    photographers = Photographer.objects.all()
    total_photographers = photographers.count()

    clients = Client.objects.all()
    total_clients = clients.count()

    appointments = Appointment.objects.select_related('offer', 'client', 'photographer').all()
    total_appointments = appointments.count()

    offers = Offers.objects.all()
    total_offers = offers.count()

    context = {
        'photographers': photographers,
        'total_photographers': total_photographers,

        'clients': clients,
        'total_clients': total_clients,

        'appointments': appointments,
        'total_appointments': total_appointments,

        'offers': offers,
        'total_offers': total_offers,
    }

    return render(request, 'pages/database.html', context)
