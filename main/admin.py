from tinymce.widgets import TinyMCE
from django.contrib import admin
from .models import Tutorial

# Register your models here.

class TutorialAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {"fields": ["tutorial_title", "tutorial_published"]}),
        ("contain", {"fields": ["tutorial_contain"]})
    ]

admin.site.register(Tutorial, TutorialAdmin)