from django.contrib import admin
from .models import Expenses, Category, Currencies


admin.site.register(Expenses)
admin.site.register(Category)
admin.site.register(Currencies)
