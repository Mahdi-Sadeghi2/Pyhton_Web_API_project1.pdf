from django.contrib import admin
from .models import Cart

# Register your models here.

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('customer','status','created_at','updated_at',)
    search_fields = ('id',)


