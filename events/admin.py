from django.contrib import admin
from .models import Event 

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    # Columns shown in the admin list
    list_display = ('event_name', 'event_date', 'location', 'is_approved', 'is_featured', 'user')
    # Sidebar filters
    list_filter = ('is_approved', 'is_featured', 'event_date')
    search_fields = ('event_name', 'location')
    
    actions = ['approve_events', 'unapprove_events', 'make_featured']

    @admin.action(description="Approve selected events")
    def approve_events(self, request, queryset):
        queryset.update(is_approved=True)

    @admin.action(description="Unapprove selected events")
    def unapprove_events(self, request, queryset):
        queryset.update(is_approved=False)

    @admin.action(description="Mark as Featured")
    def make_featured(self, request, queryset):
        queryset.update(is_featured=True)