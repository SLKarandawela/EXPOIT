from django.urls import path
from ExhibitionAuth import views
urlpatterns = [
    # home page url
    path('', views.exhibition_home_page, name="exhibition_home_page"),
    # login url
    path('signin/', views.user_login_feature, name="exhibition_login"),
    # visitor signup url
    path('visitor_signup/', views.visitor_register_view, name="reg_as_visitor"),
    # exhibitor signup url
    path('exhibitor_signup/', views.exhibitor_register_view, name="reg_as_exhibitor"),

]
