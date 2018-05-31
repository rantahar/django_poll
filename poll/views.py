from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from poll.models import Topic


def index(request):
    """ The list view showing each topic, description, vote count
        and vote buttons. Uses templates/poll/index.html
    """
    topic_list = Topic.objects.order_by('-votes')

    can_vote = 'vote' not in request.COOKIES
    if not can_vote:
        vote = int(request.COOKIES.get('vote'))
    else:
        vote = -1

    print('vote:'+str(vote))
    context = {
        'topic_list': topic_list,
        'can_vote': can_vote,
        'vote': vote
    }
    return render(request, 'poll/index.html', context)


def vote(request, choice):
    """ Process a vote and redirect to index

    Parameters
    ----------
    choice : type
        The id of the choice to vote for

    """
    response = HttpResponseRedirect(reverse('poll:index'))

    if 'vote' not in request.COOKIES:
        topic = get_object_or_404(Topic, pk=choice)
        topic.votes += 1
        topic.save()

        midnight = datetime.replace(datetime.now(), hour=23, minute=59, second=59)
        expires = datetime.strftime(midnight, "%a, %d-%b-%Y %H:%M:%S GMT")
        response.set_cookie('vote', choice, expires=expires)

    return response


def undo_vote(request):
    """ Undo an existing vote and delete the voter reference
        to allow voting again
    """
    response = HttpResponseRedirect(reverse('poll:index'))

    if 'vote' in request.COOKIES:
        vote = request.COOKIES.get('vote')
        topic = get_object_or_404(Topic, pk=vote)
        topic.votes -= 1
        topic.save()
        response.delete_cookie('vote')

    return response
