from django.contrib import admin
from core.models import (
    Pizza, Feedback
)
# Register your models here.

admin.site.register(Pizza)
admin.site.register(Feedback)