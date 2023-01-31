from django.shortcuts import render, redirect
from main.models import *

def home_view(request):
    return render(request, 'index.html')


""" Banner """
def banner_view(request):
    context = {
        "banner": Banner.objects.last()
    }
    return render(request, '', context)


def create_banner(request):
    if request.method == "POST":
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        photo = request.POST.get('photo')
        quality = request.POST.get('quality')
        Banner.objects.create(
            title_uz=title_uz,
            title_ru=title_ru,
            photo=photo,
            quality=quality,
        )
        return redirect("banner_view")
    return redirect("banner_view")


def delete_banner(request, pk):
    banner = Banner.objects.get(id=pk)
    banner.delete()
    return redirect("banner_view")


def change_banner(request, pk):
    banner = Banner.objects.get(pk=pk)
    context = {
        "banner" : banner
    }
    if request.method == 'POST':
        title_uz = request.POST.get('title_uz')
        photo = request.FILES.get('photo')
        title_ru = request.POST.get('title_ru')
        quality = request.POST.get('quality')
        banner.title = title
        if photo is not None:
            banner.photo = photo
        else:
            pass
        banner.title_uz = title_uz
        banner.title_ru = title_ru
        banner.quality = quality
        banner.save()
    return render(request, '', context)

""" End Banner """
""" Order """

def order_view(request):
    context = {
        "order": Order.objects.all()
    }
    return render(request, '', context)


def create_order(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        Order.objects.create(
            name=name,
            phone=phone,
        )
        return redirect("order_view")
    return redirect("order_view")


def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return redirect("order_view")


def change_order(request, pk):
    order = Order.objects.get(pk=pk)
    context = {
        "order" : order
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        order.name = name
        order.phone = phone
        order.save()
    return render(request, '', context)

""" End Order"""
""" Product """

def product_view(request):
    context = {
        "product": Product.objects.all()
    }
    return render(request, '', context)


def create_product(request):
    if request.method == "POST":
        name_uz = request.POST.get('name_uz')
        name_ru = request.POST.get('name_ru')
        photo = request.FILES.get('photo')
        price = request.POST.get('price')
        sale = request.POST.get('sale')
        is_sale = request.POST.get('is_sale')
        Product.objects.create(
            name_uz=name_uz,
            name_ru=name_ru,
            photo=photo,
            price=price,
            sale=sale,
            is_sale=is_sale,
        )
        return redirect("product_view")
    return redirect("product_view")


def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect("product_view")


def change_product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        "product": product
    }
    if request.method == 'POST':
        name_uz = request.POST.get('name_uz')
        name_ru = request.POST.get('name_ru')
        photo = request.FILES.get('photo')
        price = request.POST.get('price')
        sale = request.POST.get('sale')
        is_sale = request.POST.get('is_sale')
        product.name_uz = name_uz
        product.name_ru = name_ru
        if photo is not None:
            product.photo = photo
        product.price = price
        product.sale = sale
        product.is_sale = is_sale
        product.save()
    return render(request, '', context)

""" End Product """

""" About Product """


def about_product_view(request):
    context = {
        "about_product": AboutProduct.objects.all()
    }
    return render(request, '', context)


def create_about_product(request):
    if request.method == "POST":
        img = request.FILES.get('img')
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        AboutProduct.objects.create(
            img=img,
            text_uz=text_uz,
            text_ru=text_ru,
        )
        return redirect("about_product_view")
    return redirect("about_product_view")


def delete_about_product(request, pk):
    about_product = AboutProduct.objects.get(id=pk)
    about_product.delete()
    return redirect("about_product_view")


def change_about_product(request, pk):
    about_product = AboutProduct.objects.get(pk=pk)
    context = {
        "about_product": about_product
    }
    if request.method == 'POST':
        img = request.POST.get('img')
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        if img is not None:
            about_product.photo = photo
        about_product.text_uz = text_uz
        about_product.text_ru = text_ru
        about_product.save()
    return render(request, '', context)

""" End About Product """
""" Advice """

def advice_view(request):
    context = {
        "advice": Advice.objects.all()
    }
    return render(request, '', context)


def create_advice(request):
    if request.method == "POST":
        name_uz = request.POST.get('name_uz')
        name_ru = request.POST.get('name_ru')
        Advice.objects.create(
            name_uz=name_uz,
            name_ru=name_ru,
        )
        return redirect("advice_view")
    return redirect("advice_view")


def delete_advice(request, pk):
    advice = Advice.objects.get(id=pk)
    advice.delete()
    return redirect("advice_view")


def change_advice(request, pk):
    advice = Advice.objects.get(pk=pk)
    context = {
        "advice": advice
    }
    if request.method == 'POST':
        name_uz = request.POST.get('name_uz')
        name_ru = request.POST.get('name_ru')
        advice.name_uz = name_uz
        advice.name_ru = name_ru
        advice.save()
    return render(request, '', context)


""" End Advice """

""" Advice_item  """


def advice_item_view(request):
    context = {
        "advice_item": Advice_item.objects.all()
    }
    return render(request, '', context)


def create_advice_item(request):
    if request.method == "POST":
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        Advice_item.objects.create(
            title_uz=title_uz,
            title_ru=title_ru,
        )
        return redirect("advice_item_view")
    return redirect("advice_item_view")


def delete_advice_item(request, pk):
    advice_item = Advice_item.objects.get(id=pk)
    advice_item.delete()
    return redirect("advice_item_view")


def change_advice_item(request, pk):
    advice_item = Advice_item.objects.get(pk=pk)
    context = {
        "advice_item": advice_item
    }
    if request.method == 'POST':
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        advice_item.title_uz = title_uz
        advice_item.title_ru = title_ru
        advice_item.save()
    return render(request, '', context)

""" End Advice Item """
""" About Company """


def about_company_view(request):
    context = {
        "about_company": About_Company.objects.all()
    }
    return render(request, '', context)


def create_about_company(request):
    if request.method == "POST":
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        img = request.FILES.get('img')
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        About_Company.objects.create(
            title_uz=title_uz,
            title_ru=title_ru,
            img=img,
            text_uz=text_uz,
            text_ru=text_ru,
        )
        return redirect("about_company_view")
    return redirect("about_company_view")


def delete_about_company(request, pk):
    about_company = About_Company.objects.get(id=pk)
    about_company.delete()
    return redirect("about_company_view")


def change_about_company(request, pk):
    about_company = About_Company.objects.get(pk=pk)
    context = {
        "about_company": about_company
    }
    if request.method == 'POST':
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        img = request.FILES.get('img')
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        about_company.title_uz = title_uz
        about_company.title_ru = title_ru
        if img is not None:
            about_company.img = img
        about_company.text_uz = text_uz
        about_company.text_ru = text_ru
        about_company.save()
    return render(request, '', context)

""" End About Company """

""" Instruction """

def instruction_view(request):
    context = {
        "instruction": Instruction.objects.all()
    }
    return render(request, '', context)


def create_instruction(request):
    if request.method == "POST":
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        Instruction.objects.create(
            title_uz=title_uz,
            title_ru=title_ru,
            text_uz=text_uz,
            text_ru=text_ru,
            )
        return redirect("instruction_view")
    return redirect("instruction_view")


def delete_instruction(request, pk):
    instruction = Instruction.objects.get(id=pk)
    instruction.delete()
    return redirect("instruction_view")


def change_instruction(request, pk):
    instruction = Instruction.objects.get(pk=pk)
    context = {
        "instruction": instruction
    }
    if request.method == 'POST':
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        instruction.title_uz = title_uz
        instruction.title_ru = title_ru
        instruction.text_uz = text_uz
        instruction.text_ru = text_ru
        instruction.save()
    return render(request, '', context)

""" End Instruction """
""" Fact Title """


def fact_title_view(request):
    context = {
        "fact_title": Fact_Title.objects.all()
    }
    return render(request, '', context)


def create_fact_title(request):
    if request.method == "POST":
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        Fact_Title.objects.create(
            title_uz=title_uz,
            title_ru=title_ru,
            )
        return redirect("fact_title_view")
    return redirect("fact_title_view")


def delete_fact_title(request, pk):
    fact_title = Fact_Title.objects.get(id=pk)
    fact_title.delete()
    return redirect("fact_title_view")


def change_fact_title(request, pk):
    fact_title = Fact_Title.objects.get(pk=pk)
    context = {
        "fact_title": fact_title
    }
    if request.method == 'POST':
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        fact_title.title_uz = title_uz
        fact_title.title_ru = title_ru
        fact_title.save()
    return render(request, '', context)

""" End Fact Title """
""" Fact_item  """


def fact_item_view(request):
    context = {
        "fact_item": Fact_item.objects.all()
    }
    return render(request, '', context)


def create_fact_item(request):
    if request.method == "POST":
        description_uz = request.POST.get('description_uz')
        description_ru = request.POST.get('description_ru')
        number = request.POST.get('number')
        Fact_item.objects.create(
            description_uz=description_uz,
            description_ru=description_ru,
            number=number,
            )
        return redirect("fact_item_view")
    return redirect("fact_item_view")


def delete_fact_item(request, pk):
    fact_item = Fact_item.objects.get(id=pk)
    fact_item.delete()
    return redirect("fact_item_view")


def change_fact_item(request, pk):
    fact_item = Fact_item.objects.get(pk=pk)
    context = {
        "fact_item": fact_item
    }
    if request.method == 'POST':
        description_uz = request.POST.get('description_uz')
        description_ru = request.POST.get('description_ru')
        number = request.POST.get('number')
        fact_item.description_uz = description_uz
        fact_item.description_ru = description_ru
        fact_item.number = number
        fact_item.save()
    return render(request, '', context)

""" End Fact Item """
""" Info """


def info_view(request):
    context = {
        "info": Info.objects.all()
    }
    return render(request, '', context)


def create_info(request):
    if request.method == "POST":
        name = request.POST.get('name')
        logo = request.FILES.get('logo')
        description_uz = request.POST.get('description_uz')
        description_ru = request.POST.get('description_ru')
        telegram = request.POST.get('telegram')
        instagram = request.POST.get('instagram')
        youtube = request.POST.get('youtube')
        facebook = request.POST.get('facebook')
        Info.objects.create(
            name=name,
            logo=logo,
            description_uz=description_uz,
            description_ru=description_ru,
            telegram=telegram,
            instagram=instagram,
            youtube=youtube,
            facebook=facebook,
            )
        return redirect("info_view")
    return redirect("info_view")


def delete_info(request, pk):
    info = Info.objects.get(id=pk)
    info.delete()
    return redirect("info_view")


def change_info(request, pk):
    info = Info.objects.get(pk=pk)
    context = {
        "info": info
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        logo = request.POST.get('logo')
        description_uz = request.POST.get('description_uz')
        description_ru = request.POST.get('description_ru')
        telegram = request.POST.get('telegram')
        instagram = request.POST.get('instagram')
        youtube = request.POST.get('youtube')
        facebook = request.POST.get('facebook')
        info.name = name
        if logo is not None:
            info.logo = logo
        info.description_uz = description_uz
        info.description_ru = description_ru
        info.telegram = telegram
        info.instagram = instagram
        info.youtube = youtube
        info.facebook = facebook
        info.save()
    return render(request, '', context)


""" End Info """