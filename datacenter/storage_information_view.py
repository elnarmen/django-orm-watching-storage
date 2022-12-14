from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = [
        {
            'who_entered': visit.passcard,
            'entered_at': visit.entered_at,
            'duration': visit.get_duration(),
        } for visit in Visit.objects.filter(leaved_at=None)
    ]
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
