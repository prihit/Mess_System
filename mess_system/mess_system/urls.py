
from django.contrib import admin
from django.urls import path
from mess import views


urlpatterns = [
    path('', views.Stulogin, name='login'),
    path('logou', views.logou, name='logout'),
    path('index', views.index, name='home'),
    path('order', views.order, name='order'),
    path('buforder/<str:buf>/<str:cho>', views.buforder, name = 'buforder'),
    path('orderbuf/<int:order_id>', views.orderbuf, name = 'orderbuf'),
    path('admin/', admin.site.urls),
]
