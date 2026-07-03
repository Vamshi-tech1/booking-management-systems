from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking1_app/booking_list.html', {'bookings': bookings})

def booking_create(request):
    if request.method == 'POST':
        Booking.objects.create(
            customer_name=request.POST['customer_name'],
            venue=request.POST['venue'],
            date=request.POST['date'],
            time=request.POST['time'],
            guests=request.POST['guests']
        )
        return redirect('booking_list')
    return render(request, 'booking1_app/booking_form.html')

def booking_update(request, id):
    booking = get_object_or_404(Booking, id=id)
    if request.method == 'POST':
        booking.customer_name = request.POST['customer_name']
        booking.venue = request.POST['venue']
        booking.date = request.POST['date']
        booking.time = request.POST['time']
        booking.guests = request.POST['guests']
        booking.save()
        return redirect('booking_list')
    return render(request, 'booking1_app/booking_form.html', {'booking': booking})
def booking_delete(request, id):
    booking = get_object_or_404(Booking, id=id)
    booking.delete()
    return redirect('booking_list')