from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
class News(models.Model):
    news_title = models.CharField(max_length=50)
    news_desc = HTMLField()
    news_slug = AutoSlugField(populate_from='news_title',unique=True,null=True,default=None)#how #to use AutoSlugfield to make auto dyanic link of navbar through slug
    news_image = models.FileField(upload_to='news/',max_length=250,null=True,default=None)
    class Meta:
        verbose_name_plural = "News"
# Create your models here.
