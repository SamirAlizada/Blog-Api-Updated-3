from .models import CustomUser, AuthorPoint
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=CustomUser)
def create_author_point(sender, instance, created, **kwargs):
    if created:
        AuthorPoint.objects.create(author=instance)
        author = instance.author()
        author_point = AuthorPoint.objects.get(author=author)
        author_point.point += 1
        author_point.save()