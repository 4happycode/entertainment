from django.contrib import admin
from .models import Movies, Genre, MPAARating


# Custom Movie Admin
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'duration', 'language', 'userRating', 'display_genres', 'display_mpaa_rating')
    search_fields = ('name', 'language', 'userRating')
    list_filter = ('language', 'userRating')

    def display_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genre.all()])
    
    display_genres.short_description = 'Genres'

    def display_mpaa_rating(self, obj):
        return ", ".join(["{}({})".format(mpaa.type, mpaa.label) for mpaa in obj.mpaaRating.all()])
    
    display_mpaa_rating.short_description = 'MPAA Rating'


# Custom Genre Admin
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


# Custom MpaaRating Admin
class MPAARatingAdmin(admin.ModelAdmin):
    list_display = ('type', 'label')


# Register Model With Custom Obj
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movies, MovieAdmin)
admin.site.register(MPAARating, MPAARatingAdmin)
