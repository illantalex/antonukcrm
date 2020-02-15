from django.db import models
# from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class Company(models.Model):
    name = models.CharField(verbose_name='Название компании', max_length=100)
    director = models.CharField(verbose_name='ФИО руководителя (контактного лица)', max_length=100)
    summary = models.TextField(verbose_name='Краткое описание', max_length=1000)
    date_create = models.DateField(verbose_name='Дата создания', auto_now_add=True, editable=False)
    date_update = models.DateField(verbose_name='Дата обновления', auto_now=True)
    adress = models.CharField(verbose_name='Адрес', max_length=100)
    email = models.EmailField()
    phone = models.CharField(verbose_name='Телефон', max_length=13)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Project(models.Model):
    name = models.CharField(verbose_name='Название проекта', max_length=100)
    summary = models.TextField(verbose_name='Описание', max_length=1000)
    project_start = models.DateField(verbose_name='Сроки начала')
    project_end = models.DateField(verbose_name='Срок окончания')
    project_cost = models.IntegerField(verbose_name='Стоимость')
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Manager(models.Model):
    photo = models.ImageField(verbose_name='Фото', upload_to='media', blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    # def get_absolute_url(self):
    #     return reverse('manager_page', args=str(self.user.manager.pk))

    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'


class Message(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50, blank=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

    CHANNELS = (
        ('z', 'Заявка'),
        ('p', 'Письмо'),
        ('s', 'Сайт'),
        ('v', 'Входящее письмо'),
        ('i', 'Инициатива компании')
    )

    MARK = (
        ('l', 'Like'),
        ('d', 'Dislike')
    )
    channel = models.CharField(verbose_name='Канал обращения', max_length=1, choices=CHANNELS, blank=True, default='z')
    manager = models.ForeignKey('Manager', on_delete=models.CASCADE, verbose_name='Менеджер')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    mark = models.CharField(max_length=1, choices=MARK, verbose_name='Оценка')
    kwords = models.ManyToManyField('Keyword', verbose_name='Ключевые слова', blank=True)

    def __str__(self):
        return f"{self.description[:20]}..."

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Keyword(models.Model):
    word = models.CharField(verbose_name="Ключевое слово", max_length=30)

    def __str__(self):
        return f"{self.word}"

    class Meta:
        verbose_name = 'Ключевое слово'
        verbose_name_plural = 'Ключевые слова'
