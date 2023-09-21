from django.shortcuts import render
from .models import Event, Workshop, Staff, Volunteer, FooterPhoto , Poster , HeaderNavigationItem


def event_registration(request):
    events = Event.objects.all()
    workshops = Workshop.objects.all()
    staff_members = Staff.objects.all()
    volunteers = Volunteer.objects.all()
    photos = FooterPhoto.objects.all() 
    poster = Poster.objects.first()
    nav_items = HeaderNavigationItem.objects.all()
   
    return render(request, 'event_registration.html', {
        'events': events,
        'workshops': workshops,
        'staff_members': staff_members,
        'volunteers': volunteers,
        'photos': photos,  
        'poster' : poster,
        'nav_items': nav_items,

    })
