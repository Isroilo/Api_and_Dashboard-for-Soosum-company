from django.shortcuts import render, redirect
from main.models import *
from django.db.models import Q
from datetime import datetime, timedelta
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models.functions import ExtractDay, ExtractMonth
import calendar
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def user_update(request):
    if request.method == 'POST':
        user = request.user
        username = request.POST['username']
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        user.username = username
        if password is not None:
            if password == password_confirm:
                user.set_password(password)
            else:
                user.save()
        user.save()
        return redirect('user_update_url')
    context = {
        'user': request.user
    }
    return render(request, 'update-user.html', context)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request, usr)
            return redirect("home_url")
    return render(request, 'login.html')


@login_required(login_url='login_url')
def logout_view(request):
    logout(request)
    return redirect("login_url")


@login_required(login_url='login_url')
def home_view(request):
    order = Order.objects.all().order_by('-id')
    count = Order.objects.all().count()
    today = datetime.today() - timedelta(days=1)
    month = datetime.today() - timedelta(days=30)
    day = Order.objects.filter(created__gte=today).count()
    months = Order.objects.filter(created__gte=month).count()
    qs = Order.objects.filter(
        created__gte=month
    ).annotate(
        day=ExtractDay("created"),
        mon=ExtractMonth('created'),
    ).values(
        'day', 'mon'
    ).annotate(
        n=Count('pk')
    ).order_by('mon')
    mon_list = []
    orders_list = []
    for i in qs:
        i['mon'] = (calendar.month_abbr[i['mon']])
        orders_list.append(i['n'])
        if len(mon_list) >= 30:
            del mon_list[0]
            mon_list.append(i)
        else:
            mon_list.append(i)
    m_num = max(orders_list)
    l_num = min(orders_list)
    context = {
        "all_apps": order,
        "count": count,
        "day": day,
        "m_num": m_num,
        "l_num": l_num,
        "month": months,
        "qs": mon_list,
    }
    return render(request, 'index.html', context)


""" Search """


@login_required(login_url='login_url')
def search_view(request):
    if request.method == "POST":
        search = request.POST['search']
        info = Q(Q(name_uz__icontains=search) | Q(name_ru__icontains=search))
        product = Product.objects.filter(info)
        context = {
            "search": product
        }
        return render(request, '', context)


""" End Search """
""" Banner """


@login_required(login_url='login_url')
def banner_view(request):
    context = {
        "banner": Banner.objects.last()
    }
    return render(request, 'banner.html', context)


@login_required(login_url='login_url')
def create_banner(request):
    if request.method == "POST":
        title_uz = request.POST['title_uz']
        title_ru = request.POST['title_ru']
        quality_uz = request.POST['quality_uz']
        quality_ru = request.POST['quality_ru']
        photo = request.FILES.get('photo')
        Banner.objects.create(
            title_uz=title_uz,
            title_ru=title_ru,
            quality_uz=quality_uz,
            quality_ru=quality_ru,
            photo=photo,
        )
        return redirect("banner_url")
    return redirect("banner_url")


@login_required(login_url='login_url')
def delete_banner(request, pk):
    banner = Banner.objects.get(pk=pk)
    banner.delete()
    return redirect("banner_url")


@login_required(login_url='login_url')
def change_banner(request, pk):
    if request.method == 'POST':
        banner = Banner.objects.get(pk=pk)
        title_uz = request.POST['title_uz']
        title_ru = request.POST['title_ru']
        quality_uz = request.POST['quality_uz']
        quality_ru = request.POST['quality_ru']
        photo = request.FILES.get('photo')
        banner.title_uz = title_uz
        banner.title_ru = title_ru
        banner.quality_uz = quality_uz
        banner.quality_ru = quality_ru
        if photo is not None:
            banner.photo = photo
        banner.save()
        return redirect("banner_url")
    return redirect("banner_url")


""" End Banner """
""" Order """

def PagenatorPage(List, num ,request):
    paginator = Paginator(List, num)
    pages = request.GET.get('page')
    try:
        list = paginator.page(pages)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return list

@login_required(login_url='login_url')
def order_view(request):
    orders = Order.objects.all().order_by('-id')
    context = {
        "orders": PagenatorPage(orders, 5, request)
    }
    return render(request, 'order.html', context)


@login_required(login_url='login_url')
def create_order(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        Order.objects.create(
            name=name,
            phone=phone,
        )
    return redirect("order_url")


@login_required(login_url='login_url')
def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return redirect("order_url")


@login_required(login_url='login_url')
def change_order(request, pk):
    if request.method == 'POST':
        order = Order.objects.get(pk=pk)
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        order.name = name
        order.phone = phone
        order.save()
    return redirect('order_url')


""" End Order"""
""" Product """


def PagenatorPage(List, num ,request):
    paginator = Paginator(List, num)
    pages = request.GET.get('page')
    try:
        list = paginator.page(pages)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return list

@login_required(login_url='login_url')
def product_view(request):
    products = Product.objects.all().order_by('id')
    context = {
        "products": PagenatorPage(products, 6, request)
    }
    return render(request, 'products.html', context)


@login_required(login_url='login_url')
def create_product(request):
    if request.method == "POST":
        name_uz = request.POST['name_uz']
        name_ru = request.POST['name_ru']
        photo = request.FILES['photo']
        price = request.POST['price']
        sale = request.POST.get('sale')
        new_product = Product.objects.create(
            name_uz=name_uz,
            name_ru=name_ru,
            photo=photo,
            price=price,
            sale=sale,
        )
        if sale is not None:
            new_product.is_sale=True
            new_product.save()
    return redirect("product_url")


@login_required(login_url='login_url')
def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect("product_url")


@login_required(login_url='login_url')
def change_product(request, pk):
    if request.method == 'POST':
        product = Product.objects.get(pk=pk)
        name_uz = request.POST['name_uz']
        name_ru = request.POST['name_ru']
        photo = request.FILES.get('photo')
        price = request.POST.get('price')
        sale = request.POST.get('sale')
        product.name_uz = name_uz
        product.name_ru = name_ru
        product.price = price
        product.sale = sale
        t_list = []
        if sale is not None:
            product.is_sale = True
        if photo is not None:
            product.photo = photo
        product.save()
    return redirect('product_url')


""" End Product """
""" About Product """


@login_required(login_url='login_url')
def about_product_view(request):
    context = {
        "about_product": About_Product.objects.all().order_by('-id')
    }
    return render(request, 'about-product.html', context)


@login_required(login_url='login_url')
def create_about_product(request):
    if request.method == "POST":
        img = request.FILES.get('photo')
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        About_Product.objects.create(
            img=img,
            text_uz=text_uz,
            text_ru=text_ru,
        )
    return redirect("about_product_url")


@login_required(login_url='login_url')
def delete_about_product(request, pk):
    about_product = About_Product.objects.get(id=pk)
    about_product.delete()
    return redirect("about_product_url")


@login_required(login_url='login_url')
def change_about_product(request, pk):
    if request.method == 'POST':
        about_product = About_Product.objects.get(pk=pk)
        photo = request.FILES.get('photo')
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        if photo is not None:
            about_product.img = photo
        about_product.text_uz = text_uz
        about_product.text_ru = text_ru
        about_product.save()
    return redirect("about_product_url")

""" End About Product """
""" Advice Item """
@login_required(login_url='login_url')
def create_advice_item(request):
    if request.method == "POST":
        advice_uz = request.POST.get('advice_uz')
        advice_ru = request.POST.get('advice_ru')
        Advice_item.objects.create(
            advice_uz=advice_uz,
            advice_ru=advice_ru,
        )
    return redirect("advice_url")


@login_required(login_url='login_url')
def delete_advice_item(request, pk):
    advice_item = Advice_item.objects.get(id=pk)
    advice_item.delete()
    return redirect("advice_url")


@login_required(login_url='login_url')
def change_advice_item(request, pk):
    if request.method == 'POST':
        advice_item = Advice_item.objects.get(pk=pk)
        advice_uz = request.POST.get('advice_uz')
        advice_ru = request.POST.get('advice_ru')
        advice_item.advice_uz = advice_uz
        advice_item.advice_ru = advice_ru
        advice_item.save()
    return redirect('advice_url')


""" End Advice Item """

""" Advice Title  """


@login_required(login_url='login_url')
def advice_view(request):
    context = {
        "advice_title": Advice_Title.objects.last(),
        "advice_item": Advice_item.objects.all().order_by('-id'),
    }
    return render(request, 'advice.html', context)


@login_required(login_url='login_url')
def create_advice_title(request):
    if request.method == "POST":
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        Advice_Title.objects.create(
            title_uz=title_uz,
            title_ru=title_ru,
        )
    return redirect("advice_url")


@login_required(login_url='login_url')
def delete_advice_title(request, pk):
    advice_title = Advice_Title.objects.get(id=pk)
    advice_title.delete()
    return redirect("advice_url")


@login_required(login_url='login_url')
def change_advice_title(request, pk):
    if request.method == 'POST':
        advice_title = Advice_Title.objects.get(pk=pk)
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        advice_title.title_uz = title_uz
        advice_title.title_ru = title_ru
        advice_title.save()
    return redirect("advice_url")


""" End Advice Title """
""" About Company """


@login_required(login_url='login_url')
def about_company_view(request):
    context = {
        "about_company": About_Company.objects.last()
    }
    return render(request, 'about_company.html', context)


@login_required(login_url='login_url')
def create_about_company(request):
    if request.method == "POST":
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        img = request.FILES.get('photo')
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        About_Company.objects.create(
            title_uz=title_uz,
            title_ru=title_ru,
            img=img,
            text_uz=text_uz,
            text_ru=text_ru,
        )
    return redirect("about_company_url")


@login_required(login_url='login_url')
def delete_about_company(request, pk):
    about_company = About_Company.objects.get(pk=pk)
    about_company.delete()
    return redirect("about_company_url")


@login_required(login_url='login_url')
def change_about_company(request, pk):
    if request.method == 'POST':
        about_company = About_Company.objects.get(pk=pk)
        title_uz = request.POST['title_uz']
        title_ru = request.POST['title_ru']
        img = request.FILES.get('photo')
        text_uz = request.POST['text_uz']
        text_ru = request.POST['text_ru']
        about_company.title_uz = title_uz
        about_company.title_ru = title_ru
        if img is not None:
            about_company.img = img
        about_company.text_uz = text_uz
        about_company.text_ru = text_ru
        about_company.save()
    return redirect('about_company_url')


""" End About Company """
""" Instruction """

@login_required(login_url='login_url')
def instruction_view(request):
    context = {
        "instruction": Instruction.objects.last()
    }
    return render(request, 'scroll.html', context)


@login_required(login_url='login_url')
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
        return redirect("instruction_url")
    return redirect("instruction_url")


@login_required(login_url='login_url')
def delete_instruction(request, pk):
    instruction = Instruction.objects.get(id=pk)
    instruction.delete()
    return redirect("instruction_url")


@login_required(login_url='login_url')
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
        return redirect("instruction_url")
    return redirect("instruction_url")


""" End Instruction """
""" Fact Title """

@login_required(login_url='login_url')
def fact_view(request):
    context = {
        "facts": Fact_item.objects.all().order_by('-id'),
        "fact_title": Fact_Title.objects.last()
    }
    return render(request, 'facts.html', context)


@login_required(login_url='login_url')
def create_fact_title(request):
    if request.method == "POST":
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        Fact_Title.objects.create(
            title_uz=title_uz,
            title_ru=title_ru,
            )
    return redirect("fact_url")


@login_required(login_url='login_url')
def delete_fact_title(request, pk):
    fact_title = Fact_Title.objects.get(id=pk)
    fact_title.delete()
    return redirect("fact_url")


@login_required(login_url='login_url')
def change_fact_title(request, pk):
    if request.method == 'POST':
        fact_title = Fact_Title.objects.get(pk=pk)
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        fact_title.title_uz = title_uz
        fact_title.title_ru = title_ru
        fact_title.save()
    return redirect('fact_url')


""" End Fact Title """
""" Fact_item  """
@login_required(login_url='login_url')
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
    return redirect("fact_url")



@login_required(login_url='login_url')
def delete_fact_item(request, pk):
    fact_item = Fact_item.objects.get(id=pk)
    fact_item.delete()
    return redirect("fact_url")


@login_required(login_url='login_url')
def change_fact_item(request, pk):
    if request.method == 'POST':
        fact_item = Fact_item.objects.get(pk=pk)
        description_uz = request.POST.get('description_uz')
        description_ru = request.POST.get('description_ru')
        number = request.POST.get('number')
        fact_item.description_uz = description_uz
        fact_item.description_ru = description_ru
        fact_item.number = number
        fact_item.save()
    return redirect('fact_url')


""" End Fact Item """
""" Info """


@login_required(login_url='login_url')
def info_view(request):
    context = {
        "info": Info.objects.last()
    }
    return render(request, 'info.html', context)


@login_required(login_url='login_url')
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
        return redirect("info_url")
    return redirect("info_url")


@login_required(login_url='login_url')
def delete_info(request, pk):
    info = Info.objects.get(pk=pk)
    info.delete()
    return redirect("info_url")


@login_required(login_url='login_url')
def change_info(request, pk):
    info = Info.objects.get(pk=pk)
    context = {
        "info": info
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        logo = request.FILES.get('logo')
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
        return redirect("info_url")

    return redirect("info_url")



""" End Info """