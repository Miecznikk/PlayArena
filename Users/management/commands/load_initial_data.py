from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Load initial data into the database'
    file_names = [
        'team.json',
        'position.json',
        'stadium.json',
        'user.json',
        'player.json',
        'referee.json'
    ]

    def handle(self, *args, **options):
        from django.core.management import call_command
        for file in self.file_names:
            print(f"LOADING {file}")
            call_command('loaddata',f'fixtures/{file}')