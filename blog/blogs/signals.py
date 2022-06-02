from author.models import AuthorPoint
from .models import Blogs
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Blogs)
def create_author_point(sender, instance, created, **kwargs):
    if created:
        author_point = AuthorPoint.objects.get(author = instance.author)
        author_point.point += 1
        author_point.save()