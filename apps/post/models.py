from django.db.models import *
from django.contrib.auth.models import User
from apps.category.models import Category

class Post(Model):
    title = CharField('Заголовок', max_length=225)
    text = TextField('Текст', blank=True, null=True)
    image = ImageField('Фото', upload_to='PostImages', blank=True, null=True)
    category = ManyToManyField(Category, blank=True, null=True, verbose_name='Категория')
    user = ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return f'{self.title} {self.user.username}'

    class Meta():
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-id']
