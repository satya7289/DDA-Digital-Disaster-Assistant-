
from django.urls import path, reverse_lazy
from account.views import UserFormView
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [


   path('registration/', UserFormView.as_view(), name='registration'),
   path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
   path('logout/', LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),


]








