from django.contrib import admin
from poll.forms import TopicAdminForm
from poll.models import Topic


# Register your models here.
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    form = TopicAdminForm
    list_display = ('title', )
