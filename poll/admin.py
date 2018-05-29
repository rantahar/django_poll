from django.contrib import admin
from poll.models import ClinicTopic


# Register your models here.
@admin.register(ClinicTopic)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )
