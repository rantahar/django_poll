from django.contrib import admin
from poll.forms import TopicAdminForm
from poll.models import ClinicTopic, Voter


# Register your models here.
@admin.register(ClinicTopic)
class ClinicTopicAdmin(admin.ModelAdmin):
    form = TopicAdminForm
    list_display = ('title', )


@admin.register(Voter)
class VoterAdmin(admin.ModelAdmin):
    list_display = ('created_time', )
