from django.db import models
from phone_field import PhoneField


class Banner(models.Model):
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="banner/")
    quality_uz = models.CharField(max_length=100)
    quality_ru = models.CharField(max_length=100)


class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = PhoneField(help_text='Contact phone number')
    created = models.DateTimeField(auto_now_add=True)




class Product(models.Model):
    name_uz = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="products/")
    price = models.DecimalField(max_digits=25,decimal_places=2)
    sale = models.DecimalField(max_digits=25,decimal_places=2, null=True, blank=True)
    is_sale = models.BooleanField(default=False)


class About_Product(models.Model):
    img = models.ImageField(upload_to="about_product/")
    text_uz = models.TextField()
    text_ru = models.TextField()


class Advice_Title(models.Model):
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)


class Advice_item(models.Model):
    advice_uz = models.CharField(max_length=100)
    advice_ru = models.CharField(max_length=100)



class About_Company(models.Model):
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    img = models.ImageField(upload_to="about_company/")
    text_uz = models.TextField()
    text_ru = models.TextField()


class Instruction(models.Model):
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    text_uz = models.TextField()
    text_ru = models.TextField()


class Fact_Title(models.Model):
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)


class Fact_item(models.Model):
    description_uz = models.CharField(max_length=100)
    description_ru = models.CharField(max_length=100)
    number = models.FloatField()


class Info(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="logo/")
    description_uz = models.CharField(max_length=100, null=True, blank=True)
    description_ru = models.CharField(max_length=100, null=True, blank=True)
    telegram = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    youtube = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)




