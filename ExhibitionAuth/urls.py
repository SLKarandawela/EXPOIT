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
    # all exhibitors url
    path('exhibitors/', views.exhibitor_users, name="exhibitor_list"),
    path('visitors/', views.visitor_users, name="visitor_list"),

    path('exhibitor_dashboard/', views.exhibitor_home, name="exhibitor_home"),
    path('visitor_dashboard/', views.visitor_home, name="visitor_home"),
    path('admin_dashboard/', views.admin_home, name="admin_home"),

    path('logout/', views.logout_user, name="logout_user"),

]
