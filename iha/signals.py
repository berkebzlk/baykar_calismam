from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver, Signal
from .models import IHA, UserActions
from enum import Enum


@receiver(post_save, sender=IHA)
def iha_created_handler(sender, instance, **kwargs):
    try:
        request = kwargs['request']
        UserActions(user=request.user, iha=instance, action_type="INSERT").save()
        print('added action')
    except Exception as e:
        print('hataya düştük')
        print(str(e))
        pass

"""
@receiver(pre_delete, sender=IHA)
def iha_deleted_handler(sender, instance, **kwargs):
    try:
        request = kwargs['request']
        print('silme signali')
        user = UserActions(user=request.user, iha=instance, action_type="DELETE").save()
        print(user)
    except Exception as e:
        pass
"""


@receiver(post_save, sender=IHA)
def iha_updated_handler(sender, instance, **kwargs):
    try:
        request = kwargs['request']
        UserActions(user=request.user, iha=instance, action_type="UPDATE").save()
    except Exception as e:
        pass
