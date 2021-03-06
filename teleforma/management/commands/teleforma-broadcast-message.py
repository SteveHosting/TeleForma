from optparse import make_option
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from jqchat.models import *


class Command(BaseCommand):
    help = "Broadcast a jqchat message on the main site room by the admin"
    args = "username text"

    def handle(self, *args, **options):
        text = args[1]
        username = args[0]
        user = User.objects.get(username=username)
        rooms = Room.objects.filter(name__contains='site')
        for room in rooms:
            message = Message.objects.create_message(user, room, text)

