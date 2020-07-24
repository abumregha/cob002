from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('apply_for_account/', views.apply_for_account, name='apply_for_account'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('user/', views.userPage, name='user-page'),
    path('user/view_application/<int:pk>', views.view_application, name='view_application'),
    path('user/save_to_pdf/<int:pk>', views.save_to_pdf, name='save_to_pdf'),
    path('customer_application/', views.customerApplication, name='customer_application'),
    path('bootstratp/', TemplateView.as_view(template_name='bootstrap/example.html')),


]

