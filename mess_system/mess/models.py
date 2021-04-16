from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mess_balance = models.IntegerField(null=True, blank=True)
    # location = models.CharField(max_length=30, blank=True)
    # birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.student.save()
    

class Buffet(models.Model):
    name = models.CharField(max_length=50)
    meal_time = models.CharField(max_length=10)
    meal_type = models.CharField(max_length=1, help_text="v,n")
    price = models.IntegerField()
    class Meta:
        db_table = 'Buffet'
    def __str__(self):
        return self.name

class AlaCarte(models.Model):
    name = models.CharField(max_length=50)
    meal_time = models.CharField(max_length=10)
    price = models.IntegerField()
    class Meta:
        db_table = 'AlaCarte'
    def __str__(self):
        return self.name
    
class Meal(models.Model):
    id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=150)
    meal_name = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=150)
    total_price = models.IntegerField()
    class Meta:
        db_table = 'Order'


class MealOrder(models.Model):
    id = models.AutoField(primary_key=True)
    meal_id = models.ForeignKey(Meal,on_delete=models.CASCADE, null=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)



