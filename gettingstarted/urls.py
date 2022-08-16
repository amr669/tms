from django.urls import path, include

from django.contrib import admin
from django.contrib.auth import views as auth_views

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    
    path('',hello.views.index,name='index'),
    path('mycars' , hello.views.profile, name='profile'),
    path('test/new/',hello.views.new_carTest,name='new_car2'),
    path('payment/<int:v_n>/new',hello.views.new_payment,name='new_pymnt'),
    path('p/<int:v_n1>',hello.views.pay_done,name='pay_done'),
    path("click",hello.views.click, name="click"),
    path("clic",hello.views.clic, name="click1"),
    path('signup/',hello.views.signup,name='signup'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('settings/change_password/',auth_views.PasswordChangeView.as_view(template_name='change_password.html'),name='password_change'),
    path('settings/change_password/done/',auth_views.PasswordChangeDoneView.as_view(template_name='change_password_done.html'),name='password_change_done'),
    path('account/',hello.views.UserUpdateView.as_view(),name='my_account')

]
