from django.db import models
from ndt_laboratory.accounts.models import UserProfile


class Ndt(models.Model):
    CONCRETE = 'concrete'
    METAL = 'metal'
    UNKNOWN = 'unknown'
    NDT_TYPES = (
        (CONCRETE, 'Concrete'),
        (METAL, 'Metal'),
        (UNKNOWN, 'Unknown')
    )

    type = models.CharField(max_length=8, choices=NDT_TYPES, default=UNKNOWN)
    name = models.CharField(max_length=20, blank=False)
    standard = models.CharField(max_length=20, blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(
        upload_to='ndts',
    )
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}; {self.type}; {self.name}; {self.standard}'


class Choose(models.Model):
    ndt = models.ForeignKey(Ndt, on_delete=models.CASCADE)
    text = models.CharField(max_length=2)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Comment(models.Model):
    ndt = models.ForeignKey(Ndt, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
