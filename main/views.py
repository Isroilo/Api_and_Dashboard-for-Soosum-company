from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *


@api_view(['GET'])
def banner_view(request):
    try:
        banner = Banner.objects.last()
        serializer = BannerSerializer(banner)
        return Response(serializer.data)
    except:
        return Response({'message': 'None'})

@api_view(['GET'])
def about_product_view(request):
    about_product = About_Product.objects.all().order_by('-id')
    serializer = About_ProductSerializer(about_product, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def about_company_view(request):
    try:
        about_company = About_Company.objects.last()
        serializer = About_Company(about_company)
        return Response(serializer.data)
    except:
        return Response({'message': False})


@api_view(['GET'])
def product_view(request):
    products = Product.objects.all().order_by('id')
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def fact_title_view(request):
    titles = Fact_Title.objects.all().order_by('-id')
    serializer = Fact_TitleSerializer(titles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def fact_item_view(request):
    facts = Fact_item.objects.all().order_by('id')
    serializer = Fact_itemSerializer(facts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def advice_title_view(request):
    advice_title = Advice_Title.objects.all().order_by('-id')
    serializer = Advice_TitleSerializer(advice_title, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def advice_item_view(request):
    advices = Advice_item.objects.all().order_by('-id')
    serializer = Advice_itemSerializer(advices, many=True)
    return Response(serializer.data)


import datetime
@api_view(['POST'])
def order_add(request):
    name = request.data['name']
    phone = request.data['phone']
    print(phone)
    for i in phone:
        print(i['number'])
    # new_order = Order.objects.create(
    #     name=name,
    #     phone=phone,
    #     created=datetime.datetime.now()
    # )
    # serializer = OrderSerializer(new_order)
    return Response('serializer.data')


@api_view(['GET'])
def instruction_view(request):
    try:
        instruction = Instruction.objects.last()
        serializer = InstructionSerializer(instruction)
        return Response(serializer.data)
    except:
        return Response({'message': 'None'})

@api_view(['GET'])
def info_view(request):
    try:
        info = Info.objects.last()
        serializer = InfoSerializer(info)
        return Response(serializer.data)
    except:
        return Response({'message': 'None'})



