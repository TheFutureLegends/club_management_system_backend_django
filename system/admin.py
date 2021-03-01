# Register your models here.
from django.contrib import admin

from .models import Event
from .models import Member
from .models import KPI


# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'student_id', 'role']


@admin.register(KPI)
class KPIAdmin(admin.ModelAdmin):
    list_display = ['member', 'event', 'communication', 'timeliness', 'quality_of_work', 'daily_communication',
                    'helpful_teammate']
