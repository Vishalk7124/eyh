from django.urls import path
from .views import login_page ,register_page, profile_page# , activate_email
from django.contrib.auth import views as auth_views


urlpatterns = [
   path('login/' , login_page , name="v2login" ),
   path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='v2logout'),

   path('register/' , register_page , name="v2register"),
   path('profile/' , profile_page , name="v2profile"),
]