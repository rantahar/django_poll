from django.forms import ModelForm, Textarea
from poll.models import Topic


class TopicAdminForm(ModelForm):
    class Meta:
        model = Topic
        fields = ('title','description')
        widgets = {
            'description': Textarea(attrs={'cols': 60, 'rows': 10}),
        }
