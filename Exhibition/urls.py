from django.urls import path
from Exhibition import views

urlpatterns = [
    # create exhibition
    path('create/', views.create_new_exhibition, name="create_exhibition"),
    # stall create url
    path('create_stall/', views.create_stall, name="create_new_stall"),
    # all exhibitions
    path('exhibitions/', views.exhibition_list, name="all_exhibitions"),
    # stalls
    path('stalls/<str:pk>', views.all_stalls, name="stall_list"),
    #stall modal
    path('stall_modal/<str:pk>', views.stall_image_uploading, name="stall_modal_creation"),
    # stall purchase
    path('stall_purchase/<str:pk>', views.purchase_stall, name="buy_and_customize_stall"),
    # stall payment calculator
    path('stall_payment/', views.calculate_stall_payment, name="payment_calculation"),
    # stall payments
    path('payment_list/', views.all_payments, name="payment_list"),
    # user payments
    path('my_payments/', views.user_defined_payments, name="my_payments"),
    # my stalls
    path('my_stalls/', views.my_stalls, name="my_stalls"),

]
