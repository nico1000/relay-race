from django.contrib import admin
from django import forms

from . import models


class StageAdmin(admin.ModelAdmin):
    pass


class EventStageInline(admin.TabularInline):
    model = models.EventStage


class EventAdmin(admin.ModelAdmin):
    inlines = [
        EventStageInline,
    ]


class RunnerAdminForm(forms.ModelForm):

    class Meta:
        model = models.Runner
        exclude = []

    def __init__(self, *args, **kwargs):
        super(RunnerAdminForm, self).__init__(*args, **kwargs)
        self.fields['event_stage'].queryset = models.EventStage.objects.filter(event=self.instance.team.event)


class RunnerAdmin(admin.ModelAdmin):
    form = RunnerAdminForm


class RunnerInline(admin.TabularInline):
    model = models.Runner


class TeamAdmin(admin.ModelAdmin):
    inlines = [
        RunnerInline,
    ]

admin.site.register(models.Stage, StageAdmin)
admin.site.register(models.Event, EventAdmin)
admin.site.register(models.EventStage)
admin.site.register(models.Runner, RunnerAdmin)
admin.site.register(models.Team, TeamAdmin)
