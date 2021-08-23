from django.db import models
# Работа с БД
# Create your models here.
class EventsConfig(models.Model):
    event_image = models.ImageField(upload_to='event_images/') # TODO картинки
    event_text = models.CharField(max_length=300) # TODO текст