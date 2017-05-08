from django.db import models
from django.utils.translation import ugettext as _


class Stage(models.Model):
    name = models.CharField(
        max_length=200,
    )
    distance = models.DecimalField(
        help_text=_('distance in kilometers'),
        max_digits=5,
        decimal_places=3,
    )

    def __str__(self):
        return '%s (%s km)' % (self.name, self.distance)


class Event(models.Model):
    name = models.CharField(
        max_length=100,
    )
    date = models.DateField()
    stages = models.ManyToManyField(
        Stage,
        through='EventStage',
    )

    def __str__(self):
        return self.name


class EventStage(models.Model):
    stage = models.ForeignKey(
        Stage,
        on_delete=models.CASCADE,
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
    )
    ordering = models.PositiveSmallIntegerField()

    def __str__(self):
        return '%s, %s. %s' % (self.event, self.ordering, self.stage)

    class Meta:
        ordering = ['ordering']


class Team(models.Model):
    name = models.CharField(
        max_length=100,
    )
    event = models.ForeignKey(
        Event
    )

    def __str__(self):
        return '%s - %s' % (self.name, self.event)


class Runner(models.Model):
    name = models.CharField(
        max_length=100,
    )
    time_estimated = models.DurationField(
        help_text=_('hh:mm:ss'),
    )
    team = models.ForeignKey(
        Team
    )
    event_stage = models.ForeignKey(
        EventStage,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
