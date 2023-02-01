from django.urls import path
from .views import *


urlpatterns = [
    path("", home_view, name='home_url'),
    path('banner-view/', banner_view, name='banner_view'),
    path('create-banner/', create_banner, name='create_banner'),
    path('delete-banner/<int:pk>/', delete_banner, name='delete_banner_url'),
    path('change-banner/<int:pk>/', change_banner, name='change_banner'),
    path('order-view/', order_view, name='order_view'),
    path('create-order/', create_order, name='create_order'),
    path('delete-order/<int:pk>/', delete_order, name='delete_order'),
    path('change-order/<int:pk>/', change_order, name='change_order'),
    path('product-view/', product_view, name='product_view'),
    path('create-product/', create_product, name='create_product'),
    path('delete-product/<int:pk>/', delete_product, name='delete_product'),
    path('change-product/<int:pk>/', change_product, name='change_product'),
    path('about-product-view/', about_product_view, name='about_product_view'),
    path('create-about-product/', create_about_product, name='create_about_product'),
    path('delete-about-product/<int:pk>/', delete_about_product, name='delete_about_product'),
    path('change-about-product/<int:pk>/', change_about_product, name='change_about_product'),
    path('advice-view/', advice_view, name='advice_view'),
    path('create-advice/', create_advice, name='create_advice'),
    path('delete-advice/<int:pk>/', delete_advice, name='delete_advice'),
    path('change-advice/<int:pk>/', change_advice, name='change_advice'),
    path('advice-item-view/', advice_item_view, name='advice_item_view'),
    path('create-advice-item/', create_advice_item, name='create_advice_item'),
    path('delete-advice-item/<int:pk>/', delete_advice_item, name='delete_advice_item'),
    path('change-advice-item/<int:pk>/', change_advice_item, name='change_advice_item'),
    path('about-company-view/', about_company_view, name='about_company_view'),
    path('create-about-company/', about_company_view, name='about_company_view'),
    path('delete-about-company/<int:pk>/', delete_about_company, name='delete_about_company'),
    path('change-about-company/<int:pk>/', change_about_company, name='change_about_company'),
    path('instruction-view/', instruction_view, name='instruction_view'),
    path('create-instruction/', create_instruction, name='create_instruction'),
    path('delete-instruction/<int:pk>/', delete_instruction, name='delete_instruction'),
    path('change-instruction/<int:pk>/', change_instruction, name='change_instruction'),
    path("fact-title-view/", fact_title_view, name='fact_title_view'),
    path('create-fact-title/', create_fact_title, name='create_fact_title'),
    path('delete-fact-title/<int:pk>/', delete_fact_title, name='delete_fact_title'),
    path('change-fact-title/<int:pk>/', change_fact_title, name='change_fact_title'),
    path('fact-item-view/', fact_item_view, name='fact_item_view'),
    path('create-fact-item/', create_fact_item, name='create_fact_item'),
    path('delete-fact-item/<int:pk>/', delete_fact_item, name='delete_fact_item'),
    path('change-fact-item/<int:pk>/', change_fact_item, name='change_fact_item'),
    path('info-view/', info_view, name='info_view'),
    path('create-info/', create_info, name='create_info'),
    path('delete-info/<int:pk>/', delete_info, name='delete_info'),
    path('delete-info/<int:pk>/', delete_info, name='delete_info'),
]