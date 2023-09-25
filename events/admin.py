from django.contrib import admin
from mapbox_location_field.admin import MapAdmin

from .models import (
    Event,
)

admin.site.register(Event, MapAdmin)

