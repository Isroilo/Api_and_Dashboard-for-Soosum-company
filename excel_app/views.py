from django.shortcuts import render, redirect
from main.models import Order
from django.views.generic.base import TemplateView
from xlutils.copy import copy
from xlrd import open_workbook
import xlwt
from django.http import HttpResponse
import os


class ExcelPageView(TemplateView):
    template_name = "excel_home.html"

# writing to existing workbook using xlwt 


def export_write_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'
    
    path = os.path.dirname(__file__)
    file = os.path.join(path, 'sample.xls')

    rb = open_workbook(file, formatting_info=True)
    r_sheet = rb.sheet_by_index(0)

    wb = copy(rb)
    ws = wb.get_sheet(0)

    row_num = 0
    rows = Order.objects.all().values_list('name','phone','created',)
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num,str(row[col_num]))
    wb.save(response)
    return response
