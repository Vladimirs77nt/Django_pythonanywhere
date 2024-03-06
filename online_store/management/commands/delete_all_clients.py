from django.core.management.base import BaseCommand
from online_store.models import Client

class Command(BaseCommand):
    help = "Delete all clients"

    def handle(self, *args, **kwargs):
        count = 0
        clients = Client.objects.all()
        if clients:
            for client in clients:
                self.stdout.write(f'Client {client.name} [id:{client.pk}] is delete')
                client.delete()
                count += 1
            self.stdout.write(f'Total: {count} clients deleted')
        else:
            self.stdout.write('Clients record is empty...')