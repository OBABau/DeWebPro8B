from django.core.management.base import BaseCommand
from NFL.models import Stadium, Team, Player


class Command(BaseCommand):
    help = 'Load sample NFL data'

    def handle(self, *args, **options):
        Stadium.objects.all().delete()
        Team.objects.all().delete()
        Player.objects.all().delete()

        stadiums = [
            Stadium.objects.create(name="Lambeau Field", capacity=81441, box_size="Premium"),
            Stadium.objects.create(name="AT&T Stadium", capacity=80000, box_size="Luxury"),
            Stadium.objects.create(name="Soldier Field", capacity=61500, box_size="Standard"),
            Stadium.objects.create(name="Arrowhead Stadium", capacity=76416, box_size="Premium"),
        ]

        teams = [
            Team.objects.create(name="Green Bay Packers", venue="Green Bay, WI", owner_name="Mark Murphy", stadium=stadiums[0]),
            Team.objects.create(name="Dallas Cowboys", venue="Arlington, TX", owner_name="Jerry Jones", stadium=stadiums[1]),  
            Team.objects.create(name="Chicago Bears", venue="Chicago, IL", owner_name="Virginia McCaskey", stadium=stadiums[2]),
            Team.objects.create(name="Kansas City Chiefs", venue="Kansas City, MO", owner_name="Clark Hunt", stadium=stadiums[3]),
        ]

        players_data = [
            ("Aaron Rodgers", 12, "Quarterback", teams[0]),
            ("Davante Adams", 17, "Wide Receiver", teams[0]),
            ("Aaron Jones", 33, "Running Back", teams[0]),
            ("Dak Prescott", 4, "Quarterback", teams[1]),
            ("Ezekiel Elliott", 21, "Running Back", teams[1]),
            ("CeeDee Lamb", 88, "Wide Receiver", teams[1]),
            ("Justin Fields", 1, "Quarterback", teams[2]),
            ("David Montgomery", 32, "Running Back", teams[2]),
            ("DJ Moore", 2, "Wide Receiver", teams[2]),
            ("Patrick Mahomes", 15, "Quarterback", teams[3]),
            ("Travis Kelce", 87, "Tight End", teams[3]),
            ("Tyreek Hill", 10, "Wide Receiver", teams[3]),
        ]

        for name, number, position, team in players_data:
            Player.objects.create(name=name, number=number, position=position, team=team)

        self.stdout.write(self.style.SUCCESS('Successfully loaded NFL sample data'))
