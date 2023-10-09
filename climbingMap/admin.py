from django.contrib import admin
from .models import ClimbingArea
from.models import RockType

class ClimbingAreaAdmin(admin.ModelAdmin):
    list_display = ('area_name', 'rock_type','type_of_climbing')
class RockTypeAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(ClimbingArea, ClimbingAreaAdmin)
admin.site.register(RockType, RockTypeAdmin)