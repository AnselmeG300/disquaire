from django.contrib import admin

from .models import Booking, Contact, Album, Artist
# Register your models here.

class BookingInline(admin.TabularInline):
    verbose_name = "Réservation"
    verbose_name_plural = "Réservations"
    model = Booking
    fieldsets = [(None, {'fields': ['album', 'contacted']})] # list columns
    readonly_fields = ["created_at", "contacted", "album"]
    extra = 1

    def has_add_permission(self, request):
        return False

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

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    search_fields = ['reference', 'title']

    def has_add_permission(self, request):
        return False

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ['created_at', 'contacted']
    readonly_fields = ["created_at", "contact", 'album', 'contacted']