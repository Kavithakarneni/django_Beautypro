from django.urls import path
from Beautyapp import views
from django.contrib.auth import views as v

urlpatterns = [
    path('home/',views.home,name="Home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('login/',v.LoginView.as_view(template_name="Beautyapp/login.html"),name="login"),
    path('reg/',views.regi,name="rg"),
    path('dash/',views.dashboard,name="ds"),
    path('pro/',views.profile,name="pro"),
    path('myb/<int:id>/',views.myb,name="myb"),
    path('ser/',views.services,name="ser"),
    path('book/',views.booking,name="book"),
    path('lgo/',v.LogoutView.as_view(template_name="Beautyapp/logout.html"),name="lgot"),
    path('ads/',views.ads,name="ads"),
    path('del/<int:id>/',views.delete,name="delete"),
    path('user_edit/<int:id>/',views.user_edit,name="user_edit"),
    path('alus/',views.Allus,name="allus"),
    path('Adel/<int:id>/',views.Admin_delete,name="Adel"),
    path('Admin_edit/<int:id>/',views.Admin_edit,name="A_edit"),
    path('All_books/',views.All_book,name='alb'),
    path('bdel/<int:id>/',views.Bdel,name='bdel'),
    path('pay/<int:id>/',views.payment,name='pay'),
    path('st/<int:id>/',views.St,name='st')
]
