from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from sci_fi.models import SciFi

admin.site.register(SciFi, DraggableMPTTAdmin)
