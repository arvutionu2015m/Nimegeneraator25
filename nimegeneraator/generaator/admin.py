from django.contrib import admin
from .models import GeneratedName

@admin.register(GeneratedName)
class GeneratedNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'keyword', 'is_favorite', 'created_at')   # 🖥️ Veerud listivaates
    list_filter = ('is_favorite', 'created_at')                      # 🔎 Filtrid küljeribal
    search_fields = ('name', 'keyword')                              # 🔍 Otsing nime ja märksõna järgi
    list_editable = ('is_favorite',)                                 # 🖊️ Lemmiku muutmine otse listist
    ordering = ('-created_at',)                                       # ⏰ Uuemad esimesena
