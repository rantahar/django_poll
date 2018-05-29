from django.contrib import admin
from poll.models import ClinicTopic
from poll.models import Voter


# Register your models here.
@admin.register(ClinicTopic)
class ClinicTopicAdmin(admin.ModelAdmin):
    list_display = ('title', )


@admin.register(Voter)
class VoterAdmin(admin.ModelAdmin):
    list_display = ('created_time', )
