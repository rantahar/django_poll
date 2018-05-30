from django.contrib import admin
from poll.forms import TopicAdminForm
from poll.models import Topic, Voter


# Register your models here.
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    form = TopicAdminForm
    list_display = ('title', )


@admin.register(Voter)
class VoterAdmin(admin.ModelAdmin):
    list_display = ('created_time', )
