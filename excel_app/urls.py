from django.urls import path
from excel_app import views

urlpatterns = [
    path('export/export-write-xls', views.export_write_xls, name='export_write_xls'),
]
