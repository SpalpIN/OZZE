from decimal import Decimal

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from datetime import datetime
from django.utils.timezone import now


# Create your models here.
class Human(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', default=2)
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия', blank=True)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=10, verbose_name='Телефон')
    adress = models.CharField(max_length=50, blank=True)
    cities = (
        ('Харьков', 'Харьков'), ('Киев', 'Киев'), ('Одеса', 'Одеса'), ('Днепр', 'Днепр'),
        ('Запорожье', 'Запорожье'), ('Львов', 'Львов'), ('Кривой Рог', 'Кривой Рог'),
        ('Николаев', 'Николаев'), ('Мариуполь', 'Мариуполь'), ('Винница', 'Винница'),
        ('Полтава', 'Полтава'), ('Чернигов', 'Чернигов'), ('Черкассы', 'Черкассы'),
        ('Хмельницкий', 'Хмельницкий'), ('Черновцы', 'Черновцы'), ('Житомир', 'Житомир'),
        ('Сумы', 'Сумы'), ('Ровно', 'Ровно'), ('Горловка', 'Горловка'), ('Ивано-Франковск', 'Ивано-Франковск'),
        ('Каменское', 'Каменское'), ('Кропивницкий', 'Кропивницкий'), ('Тернополь', 'Тернополь'),
        ('Кременчуг', 'Кременчуг'), ('Луцк', 'Луцк'), ('Белая-Церковь', 'Белая-Церковь'),
        ('Краматорск', 'Краматорск'), ('Мелитополь', 'Мелитополь'), ('Ужгород', 'Ужгород'),
        ('Никополь', 'Никополь'), ('Бердянск', 'Бердянск'), ('Бровары', 'Бровары'),
        ('Павлоград', 'Павлоград')
    )
    city = models.CharField(max_length=25, choices=cities, blank=True)
    whishlist = models.CharField(max_length=20, default='', blank=True)
    shopping_basket = models.CharField(max_length=20, default='', blank=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)

# Попытка разбить товары на разные модели - была фатальной ошибкой. Свети все к одной модели!
class Product(models.Model):
    code = models.CharField(max_length=5)
    types = (
        ('Пальто', 'Пальто'),
        ('Платье', 'Платье'),
        ('Парка', 'Парка'),
        ('Защитная маска', 'Защитная маска'),
    )
    type_product = models.CharField(max_length=14, choices=types)
    name = models.CharField(max_length=70)
    price = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    colors = (
        ('Белый', 'Белый'),
        ('Черный', 'Черный'),
        ('Бежевый', 'Бежевый'),
        ('Шоколад', 'Шоколад'),
        ('Серый', 'Серый'),
        ('Зеленый', 'Зеленый'),
        ('Красный', 'Красный'),
        ('Марсала', 'Марсала'),
        ('Розовый', 'Розовый'),
        ('Синий', 'Синий'),
    )
    color = models.CharField(max_length=7, choices=colors)
    size = models.CharField(max_length=40, default='40,42,44,46,48,50,52,54,56')
    lengths = (
        ('Длинное', 'Длинное'),
        ('Короткое', 'Короткое'),
        ('Средней длины', 'Средней длины')
    )
    length = models.CharField(max_length=13, choices=lengths)
    fabric_structure = models.CharField(max_length=40, blank=True, verbose_name='Тип ткани')
    description = models.TextField()
    sale = models.PositiveSmallIntegerField(default=0, blank=True, validators=[MaxValueValidator(90)],
                                            verbose_name='Sale %')
    #picture = models.ImageField()

    def __str__(self):
        return '{} {} {}'.format(self.code, self.type_product, self.name)


class CoatModel(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=70)
    price = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    size = models.CharField(max_length=40, default='40,42,44,46,48,50,52,54,56')
    color = models.CharField(max_length=7, choices=Product.colors)
    length = models.CharField(max_length=13, choices=Product.lengths)
    fabric_structure = models.CharField(max_length=70, blank=True, verbose_name='Тип ткани',
                                        default='63% Wool; 17% Viscoze; 5% Poly')
    length_center_back = models.CharField(max_length=7, default='90',
                                          verbose_name='Длина пальто по центру спинки')
    length_sleeve_neck = models.CharField(max_length=30, default='63-64',
                                          verbose_name='Длина рукава от горловины')
    description = models.TextField()
    sale = models.DecimalField(max_digits=7, decimal_places=2, default=None, null=True, blank=True, verbose_name='Цена со скидкой')
    # discount_price = models.DecimalField(default=0, blank=True, verbose_name='Цена со скидкой')
#     picture = models.ImageField(upload_to='coat', verbose_name='Главная картинка')
#     picture2 = models.ImageField(upload_to='coat', blank=True, null=True)
#     picture3 = models.ImageField(upload_to='coat', blank=True, null=True)
#     picture4 = models.ImageField(upload_to='coat', blank=True, null=True)
    add_date = models.DateField(default=now)
    type = models.CharField(default='Coat', verbose_name='Не менять', max_length=4)

    def __str__(self):
        return '{} {}'.format(self.code, self.name)

    # @property вызывать не image.url а эту функцию imageURL
    # def imageURL(self):
    #     try:
    #         url = self.picture.url
    #     except ValueError:
    #         url = ''
    #     return url

    class Meta:
        verbose_name = "Пальто"
        verbose_name_plural = 'Пальто'


class DressModel(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=70)
    price = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    size = models.CharField(max_length=40, default='42,44')
    color = models.CharField(max_length=7, choices=Product.colors)
    fabric_structure = models.CharField(max_length=60, blank=True, verbose_name='Тип ткани')
    description = models.TextField()
#     picture = models.ImageField(upload_to='dress', verbose_name='Главная картинка')
#     picture2 = models.ImageField(upload_to='dress', blank=True, null=True)
    add_date = models.DateField(default=now)
    type = models.CharField(default='Dress', verbose_name='Не менять', max_length=5)

    def __str__(self):
        return '{} {}'.format(self.code, self.name)

    class Meta:
        verbose_name = "Платье"
        verbose_name_plural = 'Платья'


class ParkaModel(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=70)
    price = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    size = models.CharField(max_length=40, default='40,42,44,46,48')
    color = models.CharField(max_length=7, choices=Product.colors)
    length = models.CharField(max_length=13, choices=Product.lengths)
    pockets = models.CharField(max_length=1, default='4', verbose_name='Карманы')
    fur = models.CharField(max_length=70, default='опушка:  чернобурка (искусственный). Съемный, на пуговках.',
                           verbose_name='Мех')
    linig = models.CharField(max_length=70, default='мех  овчина (искусственный). В рукавах — подкладка полиестер.',
                             verbose_name='Подкладка')
    insulation = models.CharField(max_length=40, default='Thermal Silicon Insulations', verbose_name='Утеплитель')
    length_back = models.CharField(max_length=7, default='80', verbose_name='Длина куртки')
    length_sleeve = models.CharField(max_length=30, default='64-66', verbose_name='Длина рукава')
    hood = models.CharField(max_length=10, default='втачной', verbose_name='Капюшон')
    description = models.TextField()
#     picture = models.ImageField(upload_to='parka', verbose_name='Главная картинка')
#     picture2 = models.ImageField(upload_to='parka', blank=True, null=True)
#     picture3 = models.ImageField(upload_to='parka', blank=True, null=True)
    add_date = models.DateField(default=now)
    type = models.CharField(default='Parka', verbose_name='Не менять', max_length=5)

    def __str__(self):
        return '{} {}'.format(self.code, self.name)

    class Meta:
        verbose_name = "Парка"
        verbose_name_plural = 'Парки'


class FaceMaskModel(models.Model):
    name = models.CharField(max_length=70)
    price = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    color = models.CharField(max_length=7, choices=Product.colors)
    description = models.TextField()
#     picture = models.ImageField(upload_to='face_mask')
#     picture2 = models.ImageField(upload_to='face_mask', blank=True, null=True)
    add_date = models.DateField(default=now)
    type = models.CharField(default='Face_mask', verbose_name='Не менять', max_length=9)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = "Защитная маска"
        verbose_name_plural = 'Защитные маски'


class Order(models.Model):
    customer = models.ForeignKey(Human, on_delete=models.CASCADE)

    statuses = (
        ('Заказ Оформлен', 'Заказ Оформлен'),
        ('Принят в работу', 'Принят в работу'),
        ('Отправлен', 'Отправлен'),
        ('Получен', 'Получен'),
    )
    status = models.CharField(max_length=20, choices=statuses, default='Заказ Оформлен')
    date = models.DateTimeField(default=now)
    details = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return '{} {}'.format(self.price, self.customer)


class Shipment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    arive_date = models.DateField()
    details = models.CharField(max_length=100)

    def __str__(self):
        return '{}. {}'.format(self.order.status, self.order)


class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return '{}, {} шт.'.format(self.product, self.quantity)


class CartModel(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, related_name='cart', on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40)
    types = (
        ('Coat', 'Coat'),
        ('Dress', 'Dress'),
        ('Parka', 'Parka'),
        ('Face_mask', 'Face_mask'),
    )
    product_type = models.CharField(max_length=9, choices=types, default='')
    product_id = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = 'Корзина'

    def __str__(self):
        customer = self.user
        if customer == None:
            customer = 'Аноним'
        return '{}, {}'.format(customer, self.product_type)
