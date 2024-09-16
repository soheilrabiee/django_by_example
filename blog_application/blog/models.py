from django.db import models
from django.utils import timezone

# from django.db.models.functions import Now


# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        # Enumeration class
        # <choice_name/member> = <value>, <readable_name/label>
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=250)
    # Slug --> letters + numbers + underscores + hyphens
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    # Similar outcome but the value is produced by a database function --> Now()
    # publish = models.DateTimeField(db_default=Now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status, default=Status.DRAFT)

    class Meta:
        ordering = ["-publish"]
        # Hyphen is used to define descending order
        # ordering will apply by default for all queries unless an order is mentioned
        indexes = [models.Index(fields=["-publish"])]

    def __str__(self):
        return self.title
