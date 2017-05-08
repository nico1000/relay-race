from django.contrib import admin

from .models import Event, Stage, EventStage


class StageAdmin(admin.ModelAdmin):
    pass


class EventStageInline(admin.TabularInline):
    model = EventStage


class EventAdmin(admin.ModelAdmin):
    inlines = [
        EventStageInline,
    ]


    

admin.site.register(Stage, StageAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventStage)
