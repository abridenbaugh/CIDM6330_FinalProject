"""
ASGI config for final_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from channels.routing import ChannelNameRouter, ProtocolTypeRouter
from django.core.asgi import get_asgi_application

from django.core.asgi import get_asgi_application

from succession_plans import consumers

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final_project.settings")

final_project_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": final_project_asgi_app, 
        "channel": ChannelNameRouter(
            {
                "succession_plan_needed": consumers.SuccessionPlanConsumer.as_asgi(),
            }
        )
    }
)

