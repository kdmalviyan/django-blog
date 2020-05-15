from django.db import models
from django.utils.timezone import now
# Create your models here.


class Blog(models.Model):
    title = models.TextField(max_length=50)
    category = models.TextField(max_length=100)
    created_at = models.DateField(default=now)
    updated_at = models.DateField(default=now)
    created_by = models.TextField(max_length=50)
    updated_by = models.TextField(max_length=50)
    short_description = models.TextField(max_length=300)
    content = models.TextField()
    image = models.ImageField(upload_to='blogs/images')
    def __str__(self):
        return self.title
