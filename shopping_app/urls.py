from django.urls import path

from shopping_app import views

urlpatterns=[
    path('',views.root),
    path('home',views.home),
    path('addBanner',views.add_banners),
    path('addcompanyinfo',views.add_company_info),
    path('addproducts',views.add_products),
    # path('user_sign_in',views.user_sign_in),
    path('user_signup',views.user_signup),
    path('add_products',views.add_products),
]