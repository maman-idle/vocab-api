import imp
from django.contrib import admin
from .models import word

class wordsAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'word', 'translate')

admin.site.register(word, wordsAdmin)
