from django.contrib import admin
from .models import Dog, Favorite, Notification

@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ['name', 'breed', 'size', 'life_stage', 'continent', 'is_available']
    list_filter = ['is_available', 'size', 'life_stage', 'continent', 'gender']
    search_fields = ['name', 'breed']

admin.site.register(Favorite)
admin.site.register(Notification)