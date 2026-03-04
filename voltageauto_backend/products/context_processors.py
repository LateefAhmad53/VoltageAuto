from django.conf import settings


def contact_settings(request):
    return {
        "whatsapp_number": getattr(settings, "WHATSAPP_NUMBER", "2349150729116"),
    }
