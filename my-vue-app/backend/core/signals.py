from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FeaturedProject
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .serializers import FeaturedProjectSerializer

@receiver(post_save, sender=FeaturedProject)
def send_realtime_project_update(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "projects",
            {
                "type": "project.update",
                "data": {
                    "message": "New project added",
                    "projects": FeaturedProjectSerializer(FeaturedProject.objects.all(), many=True).data
                }
            }
        )
