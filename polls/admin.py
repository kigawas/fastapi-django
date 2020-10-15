from django.contrib import admin

from polls.models import Choice
from polls.models import Question

admin.site.register(Question)
admin.site.register(Choice)
