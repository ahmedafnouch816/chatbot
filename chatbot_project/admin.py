from django.contrib import admin
from django.utils.safestring import mark_safe
import json

from .models import Response


class ResponseAdmin(admin.ModelAdmin):
    list_display = ["display_text"]
    search_fields = ["text"]

    def display_text(self, obj):
        try:
            data = json.loads(obj.text)
            formatted_data = json.dumps(data, indent=4)
            return mark_safe(f"<pre>{formatted_data}</pre>")
        except json.JSONDecodeError:
            return "Invalid JSON Data"

    display_text.short_description = "Response Data"

    def get_readonly_fields(self, request, obj=None):
        # Make the 'text' field read-only
        return ["text"]


admin.site.register(Response, ResponseAdmin)
