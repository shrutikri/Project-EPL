from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('home.html',views.home,name="home"),
    path('register.html',views.register, name="register"),
    path('login.html',views.login, name="login"),
    path('logout.html',views.logout, name="logout"),
    path('billing.html',views.billing, name="billing"),
    path('monitor.html',views.monitor, name="monitor"),
    path('appliances.html',views.appliances, name="appliances"),
    path('units.html',views.units, name="units"),
    path('invoices.html',views.history, name="history"),
    path('invoice-view.html',views.invoices, name="invoices"),
    path('profile-settings.html',views.settings, name="settings"),
    path('change-password.html',views.change, name="change"),
    path('about-us.html',views.about, name="about"),
    path('forgot-password.html',views.forgot, name="forgot"),
    path('privacy-policy.html',views.privacy, name="privacy"),
    path('term-condition.html',views.term, name="term")
]