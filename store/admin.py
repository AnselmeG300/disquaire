from django.contrib import admin

from .models import Booking, Contact, Album, Artist
# Register your models here.

admin.site.register(Booking)

class BookingInline(admin.TabularInline):
    verbose_name = "Réservation"
    verbose_name_plural = "Réservations"
    model = Booking
    fieldsets = [(None, {'fields': ['album', 'contacted']})] # list columns
    extra = 1
    
class AlbumArtistInline(admin.TabularInline):
    verbose_name = "Disque"
    verbose_name_plural = "Disques"
    model = Album.artists.through # the query goes through an intermediate table.
    extra = 1

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [BookingInline,] # list of bookings made by a contact

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumArtistInline,]