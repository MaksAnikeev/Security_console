import django
from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.models import Visit


def storage_information_view(request):
    inner_visitors = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    current_time = django.utils.timezone.localtime()
    for visitor in inner_visitors:
        duration = visitor.get_duration(start=visitor.entered_at,
                                        finish=current_time)
        is_strange = visitor.is_visit_long(start=visitor.entered_at,
                                           finish=current_time,
                                           minutes=60)
        visitor_info = {
            'who_entered': visitor.passcard.owner_name,
            'entered_at': visitor.entered_at,
            'duration': visitor.format_duration(duration),
            'is_strange': is_strange}
        non_closed_visits.append(visitor_info)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
