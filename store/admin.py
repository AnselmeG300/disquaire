from django.contrib import admin

from .models import Booking, Contact, Album, Artist
# Register your models here.

admin.site.register(Booking)





class AlbumArtistInline(admin.TabularInline):
    model = Album.artists.through # the query goes through an intermediate table.
    extra = 1
class BookingInline(admin.TabularInline):
    model = Booking
    fieldsets = [
        (None, {'fields': ['album', 'contacted']})
        ] # list columns

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [BookingInline,] # list of bookings made by a contact

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumArtistInline,]