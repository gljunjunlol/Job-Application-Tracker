from django.contrib import admin
from .models import ToDoList, Item, Contact
# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Item)
admin.site.register(Contact)
