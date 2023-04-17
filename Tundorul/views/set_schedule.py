from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Tundorul.models import StreamSchedule
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=StreamSchedule)
def saveSegmentsOnTwitch(sender, instance, **kwargs):
    print('this was runned', instance.start_time)

#here goes saving the segments to twitch!! <3 <3 <3