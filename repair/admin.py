from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea

from .models import Order, OrderStatus


class OrderStatusForm(admin.StackedInline):
    model = OrderStatus
    fields = ['text']
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 80})}
    }


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderStatusForm]
    search_fields = ['number']
    list_display = ['number', 'created_at']


# Register your models here.
admin.site.register(Order, OrderAdmin)