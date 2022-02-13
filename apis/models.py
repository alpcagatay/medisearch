from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING ,related_name="user_tag", null=True)
    tag_name = models.CharField(max_length=255, null=True)
    tag_link = models.CharField(max_length = 1000, null=True)

    def __str__(self):
        return str(self.tag_name)

class PubmedDatabase(models.Model):
    id_name = models.AutoField('Article ID', primary_key=True)
    author = models.TextField('Author Name',null=True, blank=True)
    title = models.TextField ('Article Title',null=True, blank=True)
    abstracts = models.TextField('Abstracts',null=True, blank=True)
    keywords = models.TextField('Keywords',null=True, blank=True)
    tags = models.ManyToManyField('apis.Tag', blank=True)

    def __str__(self):
        return str(self.id_name)

class CrawlStatus(models.Model):
    status = models.BooleanField('Status', default=False)

    def __str__(self):
        return str(self.status)