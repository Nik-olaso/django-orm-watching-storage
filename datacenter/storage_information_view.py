from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime

def storage_information_view(request):
    not_leaved = Visit.objects.filter(leaved_at__isnull=True)
    for visit in not_leaved:
        entered_at = localtime(visit.entered_at)
        who_entered = visit.passcard.owner_name
        duration = visit.get_duration()
        is_visit_long = visit.is_visit_long()
        non_closed_visits = [
            {
                'who_entered': who_entered,
                'entered_at': entered_at,
                'duration': visit.format_duration(duration) ,
                'is_strange' : is_visit_long
            }
        ]
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
