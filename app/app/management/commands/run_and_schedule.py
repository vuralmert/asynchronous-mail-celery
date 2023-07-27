import time
from django.core.management.base import BaseCommand
from subprocess import Popen

class Command(BaseCommand):
    help = 'Custom command to run multiple commands with a delay'

    def handle(self, *args, **kwargs):
        Popen(["celery", "-A", "app.celery", "worker", "--pool=solo", "-l", "info"])

        time.sleep(5)

        Popen(["celery", "-A", "app.celery", "beat", "-l", "info"])

        time.sleep(5)

        Popen(["celery", "-A", "app.celery", "flower", "--address=127.0.0.6", "--port=5555", "--persistent=True", "--db=flower.db"])
