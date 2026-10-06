from django.urls import path
from cafeapp import views
urlpatterns = [
    path ('hey/',views.hello),
    path('hello/',views.temp),
    path("", views.index),
    path("base/", views.base),
    # path("book/", views.bookin),
    path("signup/",views.signup),
    path("staff/",views.staff),
    path("view/",views.viewdata),
    path("login/",views.login),
    path('logout/', views.logout_view)
]
