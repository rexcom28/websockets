"""
ASGI config for hello_world project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from app.simple_app.consumers import EchoConsumer, BingoConsumer, BMIConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_world.settings')

#application = get_asgi_application()
application = ProtocolTypeRouter({
    #Django's ASIG application to handle traditionasl HTTP requests
    "http":get_asgi_application(),

    #WebSocket handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            re_path(r"^ws/echo/$",EchoConsumer.as_asgi() ),
            re_path(r"^ws/bingo/$",BingoConsumer.as_asgi() ),
            re_path(r"^ws/bmi/$", BMIConsumer.as_asgi() ),
        ])
    ),
})

