from django.shortcuts import get_object_or_404, render

from datacenter.models import Passcard, Visit


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard,
                                 passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard,
                                  leaved_at__isnull=False)
    this_passcard_visits = []
    for visit in visits:
        duration = visit.get_duration(start=visit.entered_at,
                                      finish=visit.leaved_at)
        is_strange = visit.is_visit_long(start=visit.entered_at,
                                         finish=visit.leaved_at,
                                         minutes=60)
        visit_info = {
            'entered_at': visit.entered_at,
            'duration': visit.format_duration(duration),
            'is_strange': is_strange
        }
        this_passcard_visits.append(visit_info)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
