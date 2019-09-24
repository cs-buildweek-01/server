from django.contrib import admin
from .models import Player, Room

# Register your models here.


class RoomAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'n_to', 's_to', 'e_to', 'w_to')


admin.site.register(Room, RoomAdmin)


class PlayerAdmin(admin.ModelAdmin):
    fields = ('currentRoom', 'uuid', 'user')


admin.site.register(Player, PlayerAdmin)
