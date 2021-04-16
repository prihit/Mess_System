from django.contrib import admin
from .models import Student, Buffet,AlaCarte,Order,Meal,MealOrder
# Register your models here.
admin.site.register(Student)
admin.site.register(Buffet)
admin.site.register(AlaCarte)
admin.site.register(Order)
admin.site.register(Meal)
admin.site.register(MealOrder)
