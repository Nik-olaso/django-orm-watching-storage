from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404

def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    all_visits = get_list_or_404(Visit, passcard=passcard)
    this_passcard_visits = []
    for visit in all_visits:
        entered_at = localtime(visit.entered_at)
        duration = visit.get_duration()
        is_visit_long = visit.is_visit_long()
        this_passcard_visits.append(
            {
                'entered_at': entered_at,
                'duration': visit.format_duration(duration),
                'is_strange': is_visit_long
            },
        )   
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
