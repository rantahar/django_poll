from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from poll.models import ClinicTopic


def index(request):
    topic_list = ClinicTopic.objects.order_by('-votes')
    context = {
        'topic_list': topic_list,
    }
    return render(request, 'poll/index.html', context)


def vote(request, choice):
    topic = get_object_or_404(ClinicTopic, pk=choice)
    topic.votes += 1
    topic.save()
    return HttpResponseRedirect(reverse('poll:index'))
