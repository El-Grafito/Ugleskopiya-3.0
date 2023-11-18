from django.db.models import *
from django.utils.text import slugify
from unidecode import unidecode 

class Category(Model):
    title = CharField('Название категории', max_length=225, unique=True)
    slug = CharField('Slug', max_length=255, blank=True, null=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug or self.title != self.slug:
            self.slug = slugify(unidecode(self.title))
            if Category.objects.filter(slug=self.slug).exclude(id=self.id).exists():
                self.slug = f"{self.slug}-{self.id}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-id']
