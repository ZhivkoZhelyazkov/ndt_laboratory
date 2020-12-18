from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

UserModel = get_user_model()


class Ndt(models.Model):
    CONCRETE = 'concrete'
    METAL = 'metal'
    UNKNOWN = 'unknown'
    NDT_TYPES = (
        (CONCRETE, 'Concrete'),
        (METAL, 'Metal'),
        (UNKNOWN, 'Unknown')
    )

    slug = models.SlugField(editable=False)
    type = models.CharField(max_length=8, choices=NDT_TYPES, default=UNKNOWN)
    name = models.CharField(max_length=20, blank=False)
    standard = models.CharField(max_length=20, blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(
        upload_to='ndts',
    )
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    # automated slugging
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.id}; {self.type}; {self.name}; {self.standard}'


class Choose(models.Model):
    ndt = models.ForeignKey(Ndt, on_delete=models.CASCADE)
    text = models.CharField(max_length=2)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)


class Comment(models.Model):
    ndt = models.ForeignKey(Ndt, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
