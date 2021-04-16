from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from .models import Buffet,Meal,Order,MealOrder,AlaCarte
# Create your views here.
def logou(request):
    logout(request)
    return redirect('/')

def Stulogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        if not user:
            # messages.error(request, 'Invalid Credentials')
            return redirect('/')
        else:
            login(request, user)
            # messages.success(request, 'You are Logged In')
            return redirect('/index')
    else:
        return render(request, 'login.html')

def index(request):
        return render(request, 'index.html')

def order(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            meal_type = request.POST['meal_type']
            meal_choice = request.POST['btnradio']
            return redirect('/buforder/'+meal_type+'/'+meal_choice)
        else:
            return redirect('/')
    else:
        return redirect('/index')

def buforder(request, buf, cho):
    if cho == "Buffet":
        menu = Buffet.objects.filter(meal_time=buf)
    else:
        menu = AlaCarte.objects.filter(meal_time=buf)
    c = 0
    if request.method == 'POST':
        student_name = request.user.first_name + request.user.last_name
        orde = Order.objects.create(student_name= student_name, total_price=0)
        orde.save()
        for i in menu:
            quantity = request.POST['{}'.format(i.name)]
            if int(quantity) != 0:
                meal = Meal.objects.create(student_name= student_name, meal_name=i.name, price=i.price, quantity=quantity)
                meal.save()
                mo = MealOrder.objects.create(meal_id=meal,order_id=orde)
                mo.save()
                c = c + (int(quantity)*int(i.price))
        orde.total_price = c
        request.user.student.mess_balance -= c
        request.user.save()
        orde.save()
        return redirect('/orderbuf/'+str(orde.id))
    else:    
        context = {
            'menu': menu
        }
        return render(request, "buforder.html", context)

def orderbuf(request, order_id):
    mea = []
    orde = Order.objects.filter(id=order_id)
    mealord = MealOrder.objects.filter(order_id=order_id)
    context = {
        'order': orde,
        'meal': mealord
    }
    return render(request, "showord.html" , context)