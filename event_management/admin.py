from django.contrib import admin
from .models import Event, Workshop, Staff, Volunteer, FooterPhoto, Poster , HeaderNavigationItem

admin.site.register(Event)
admin.site.register(Workshop)
admin.site.register(Staff)
admin.site.register(Volunteer)
admin.site.register(FooterPhoto)
admin.site.register(Poster)
admin.site.register(HeaderNavigationItem)