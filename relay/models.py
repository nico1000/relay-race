from django.db import models
from django.utils.translation import ugettext as _


class Stage(models.Model):
    number = models.PositiveSmallIntegerField(
        _('Number'),
    )
    title = models.CharField(
        _('Title'),
        max_length=200,
    )
    distance = models.DecimalField(
        _('Distance [km]'),
        max_digits=5,
        decimal_places=3,
    )

    def __str__(self):
        return '%s. %s' % (self.number, self.title)



class Event(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=100,
    )
    date = models.DateField(
        _('Date'),
    )
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
        