from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone


# Create your models here.


        
        
class Netposts(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    post_author = models.PositiveBigIntegerField()
    post_date = models.DateTimeField(default=timezone.now)
    post_date_gmt = models.DateTimeField(default=timezone.now)
    post_content = HTMLField(blank=True, default="", db_collation='utf8mb4_persian_ci')
    post_title = models.TextField(db_collation='utf8mb4_persian_ci')
    post_excerpt = models.TextField(db_collation='utf8mb4_persian_ci')
    post_status = models.CharField(max_length=20)
    comment_status = models.CharField(max_length=20)
    ping_status = models.CharField(max_length=20)
    post_password = models.CharField(max_length=255)
    post_name = models.CharField(max_length=200, db_collation='utf8mb4_persian_ci')
    to_ping = models.TextField(blank=True, default="")
    pinged = models.TextField(blank=True, default="")
    post_modified = models.DateTimeField(default=timezone.now)
    post_modified_gmt = models.DateTimeField(default=timezone.now)
    post_content_filtered = models.TextField(db_collation='utf8mb4_persian_ci')
    post_parent = models.PositiveBigIntegerField()
    guid = models.CharField(max_length=255)
    menu_order = models.IntegerField(blank=True, default="")
    post_type = models.CharField(max_length=20)
    post_mime_type = models.CharField(max_length=100)
    comment_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'netposts'


class posts(models.Model):
    post_author = models.PositiveBigIntegerField()
    post_date = models.DateTimeField()
    post_date_gmt = models.DateTimeField()
    post_content = HTMLField(blank=True, default="",db_collation='utf8mb4_persian_ci')
    post_title = models.TextField(max_length=255, blank=True, default="",db_collation='utf8mb4_persian_ci')
    post_description = models.TextField(blank=True, default="",db_collation='utf8mb4_persian_ci')
    post_status = models.CharField(max_length=20)
    comment_status = models.CharField(max_length=20)
    ping_status = models.CharField(max_length=20)
    post_password = models.CharField(max_length=255, blank=True, default="")
    post_name = models.CharField(max_length=200,db_collation='utf8mb4_persian_ci')
    to_ping = models.TextField(blank=True, default="")
    pinged = models.TextField(blank=True, default="")
    post_modified = models.DateTimeField()
    post_modified_gmt = models.DateTimeField()
    post_keywords = models.TextField(blank=True, default="",db_collation='utf8mb4_persian_ci')
    post_parent = models.PositiveBigIntegerField()
    guid = models.CharField(max_length=255)
    menu_order = models.IntegerField()
    post_type = models.CharField(max_length=20)
    post_mime_type = models.CharField(max_length=100, blank=True, default="c")
    comment_count = models.BigIntegerField()

    def __str__(self):
        return str(self.pk) + "----->" + self.post_title


class comments(models.Model):
    author_name = models.CharField(max_length=100, default="", blank=True,db_collation='utf8mb4_persian_ci')
    author_email = models.CharField(max_length=100, default="", blank=True)
    author_url = models.CharField(max_length=200, default="", blank=True)
    # Field name made lowercase.
    author_ip = models.CharField(max_length=100, default="", blank=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
    date_gmt = models.DateTimeField(default=timezone.now, blank=True)
    content = models.TextField( default="", blank=True,db_collation='utf8mb4_persian_ci')
    post_id = models.IntegerField(default="", blank=True)
    approved = models.BooleanField(max_length=20, default=False)
    agent = models.CharField(max_length=255, default="", blank=True)
    type = models.CharField(max_length=20, default="", blank=True)

    def __str__(self):
        return str(self.pk) + "----->" + self.author_name


class Article(models.Model):

    post_title = models.CharField(max_length=200,db_collation='utf8mb4_persian_ci')
    subtitle = models.CharField(max_length=200, default="", blank=True,db_collation='utf8mb4_persian_ci')
    article_slug = models.SlugField("Article slug", blank=True)
    post_content = HTMLField(blank=True, default="",db_collation='utf8mb4_persian_ci')
    notes = HTMLField(blank=True, default="",db_collation='utf8mb4_persian_ci')
    published = models.DateTimeField("Date published", default=timezone.now)
    modified = models.DateTimeField("Date modified", default=timezone.now)

    def __str__(self):
        return str(self.pk) + "----->" + self.post_title





class antena(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    post_author = models.PositiveBigIntegerField()
    post_date = models.DateTimeField(default=timezone.now)
    post_date_gmt = models.DateTimeField(default=timezone.now)
    post_content = HTMLField(blank=True, default="", db_collation='utf8mb4_persian_ci')
    post_title = models.TextField(db_collation='utf8mb4_persian_ci')
    post_excerpt = models.TextField(db_collation='utf8mb4_persian_ci')
    post_status = models.CharField(max_length=20)
    comment_status = models.CharField(max_length=20)
    ping_status = models.CharField(max_length=20)
    post_password = models.CharField(max_length=255)
    post_name = models.CharField(max_length=200, db_collation='utf8mb4_persian_ci')
    to_ping = models.TextField(blank=True, default="")
    pinged = models.TextField(blank=True, default="")
    post_modified = models.DateTimeField(default=timezone.now)
    post_modified_gmt = models.DateTimeField(default=timezone.now)
    post_content_filtered = models.TextField(db_collation='utf8mb4_persian_ci')
    post_parent = models.PositiveBigIntegerField()
    guid = models.CharField(max_length=255)
    menu_order = models.IntegerField(blank=True, default="")
    post_type = models.CharField(max_length=20)
    post_mime_type = models.CharField(max_length=100)
    comment_count = models.BigIntegerField()