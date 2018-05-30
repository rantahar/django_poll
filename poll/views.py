from datetime import datetime, timedelta

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from poll.models import ClinicTopic
from poll.models import Voter

def index(request):
    topic_list = ClinicTopic.objects.order_by('-votes')
    time_threshold = datetime.now() - timedelta(days=1)
    voter = Voter.objects.filter(user_id=request.user.id,created_time__gt=time_threshold)
    can_vote = not voter.exists()
    if not can_vote:
        vote = voter.first().topic
    else:
        vote = -1
    context = {
        'topic_list': topic_list,
        'can_vote': can_vote,
        'vote': vote
    }
    return render(request, 'poll/index.html', context)


def vote(request, choice):
    time_threshold = datetime.now() - timedelta(days=1)
    if not Voter.objects.filter(user_id=request.user.id,created_time__gt=time_threshold).exists():
        topic = get_object_or_404(ClinicTopic, pk=choice)
        topic.votes += 1
        topic.save()
        Voter.objects.create(topic=choice, user_id=request.user.id)

    return HttpResponseRedirect(reverse('poll:index'))


def undo_vote(request):
    voter = Voter.objects.filter(user_id=request.user.id)
    if voter.exists():
        print('here')
        voter =  voter.first()
        topic = get_object_or_404(ClinicTopic, pk=voter.topic)
        topic.votes -= 1
        topic.save()
        voter.delete()

    return HttpResponseRedirect(reverse('poll:index'))
