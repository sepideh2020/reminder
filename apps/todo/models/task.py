# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):  # The Category table name that inherits models.Model
    name = models.CharField(max_length=100, verbose_name='name')  # Like a varchar
    slug = models.SlugField(max_length=100, verbose_name="Slug")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name  # name to be shown when called


class Task(models.Model):  # Task list able name that inherits models.Model
    title = models.CharField('Title', max_length=250, unique=True)  # a varchar
    slug = models.SlugField(max_length=100, verbose_name="Slug")
    description = models.TextField('Description', blank=True)  # a text field
    PRIORITY_CHOICE = [('H', 'high'), ('M', 'middle'), ('L', 'low')]
    priority = models.CharField('Priority', max_length=1, blank=True, choices=PRIORITY_CHOICE)
    due_date = models.DateTimeField('Due Date And Time')  # a date
    category = models.ForeignKey('Category', default="general", on_delete=models.PROTECT)  # a foreignkey
    done = models.BooleanField('Done', default=False)

    class Meta:
        ordering = ["-due_date"]  # ordering by the created field

    def __str__(self):
        return self.title  # name to be shown when called
