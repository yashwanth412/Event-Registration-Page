from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images')
    registration_link = models.URLField()

    def __str__(self):
        return self.name

class Workshop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='workshop_images')
    registration_link = models.URLField()

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class FooterPhoto(models.Model):
    image = models.ImageField(upload_to='footer_images')
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

class Poster(models.Model):
    image = models.ImageField(upload_to='poster_images')

@receiver(pre_delete, sender=Event)
def event_delete(sender, instance, **kwargs):
    # Delete the associated image when an Event instance is deleted
    instance.image.delete(False)

@receiver(pre_delete, sender=Workshop)
def workshop_delete(sender, instance, **kwargs):
    # Delete the associated image when a Workshop instance is deleted
    instance.image.delete(False)

@receiver(pre_delete, sender=FooterPhoto)
def footerphoto_delete(sender, instance, **kwargs):
    # Delete the associated image when a FooterPhoto instance is deleted
    instance.image.delete(False)

@receiver(pre_delete, sender=Poster)
def poster_delete(sender, instance, **kwargs):
    # Delete the associated image when a Poster instance is deleted
    instance.image.delete(False)

class HeaderNavigationItem(models.Model):
    name = models.CharField(max_length=100)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name
