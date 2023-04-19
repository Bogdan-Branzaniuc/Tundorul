from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Tundorul.models import StreamSchedule
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=StreamSchedule)
def saveSegmentsOnTwitch(sender, instance, **kwargs):
    query_set = StreamSchedule.objects.all()

    for instance in query_set:
        instance_dict = {field.name: getattr(instance, field.name) for field in instance._meta.fields}
        if instance_dict.soft_deleted:
            #all records with softdeleted flag set to true will send a DELETE request
            pass
        elif instance_dict.segment_id:
            # all records with an id and field deleted=false will send a Patch request
            pass
        else:
            # all records without an ID will send a Post request , and then get their id's saved
            
            pass

    "at the end delete any soft_deleted True fields."

    print('this was runned', instance.start_time)




