from django.db.models import *
from PIL import Image
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class UserDop(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    image = ImageField('Фото', upload_to='UserImages', default='../media/default/default_coal.png')
    bio = CharField('О себе', max_length=100, default='Сладкий котик ~(=^‥^)/')
    important = BooleanField('Важность чела', default=False)

    def __str__(self):
        return self.bio

    class Meta:
        verbose_name = 'Фото и описание пользователя'
        verbose_name_plural = 'Фото и описании полоьзователей'
        ordering = ['-id']
        
@receiver(post_save, sender=UserDop)
def crop_image(sender, instance, created, **kwargs):
    if instance.image:
        img = Image.open(instance.image.path)
        width, height = img.size
        min_size = min(width, height)
        left = (width - min_size) / 2
        top = (height - min_size) / 2
        right = (width + min_size) / 2
        bottom = (height + min_size) / 2
        img = img.crop((left, top, right, bottom))
        output_size = (200, 200)
        img.thumbnail(output_size)
        img.save(instance.image.path)

@receiver(post_save, sender=User)
def create_userdop(sender, instance, created, **kwargs):
    if created:
        UserDop.objects.create(user=instance)

