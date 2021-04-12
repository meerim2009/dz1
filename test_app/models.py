from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория товара')

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название товара')
    description = models.TextField(max_length=100, verbose_name='Описание товара')
    price = models.IntegerField(max_length=100, verbose_name='Цена товара')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


    def __str__(self):
        return self.text

