from django.urls import path
from .views import *


urlpatterns = [
    path("banner/", banner_view),
    path("about_product/", about_product_view),
    path("about-company/", about_company_view),
    path("products/", product_view),
    path("order/", order_add),
    path("instruction/", instruction_view),
    path("fact_title/", fact_title_view),
    path("fact_item/", fact_item_view),
    path("advice_item/", advice_item_view),
    path("info/", info_view),
]