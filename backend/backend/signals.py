from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@receiver(post_save, sender=User)
def send_notification(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "admin_notifications",
        {
            "type": "notification.message",
            "message": f"New user signed up: {instance.username}",
        },
    )
