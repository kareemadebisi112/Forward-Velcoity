from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Lead(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    service = models.CharField(max_length=40)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Service(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.TextField()
    html_id = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Hero(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # image = models.TextField()
    button_text = models.CharField(max_length=255)
    button_link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class About(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    highlight_text = models.TextField()
    year = models.IntegerField()
    mission_text = models.TextField()
    vision_text = models.TextField()
    values_text = models.TextField()

    def __str__(self):
        return self.title
    
class Image(BaseModel):
    image = models.ImageField(upload_to='static/main/assets')
    alt_text = models.CharField(max_length=255)

    def __str__(self):
        return self.alt_text