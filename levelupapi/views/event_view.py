"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event, Game, Gamer


class EventView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type
        """
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def list(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        organizer = Gamer.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.data["game"])

        event = Event.objects.create(
            title=request.data["title"],
            organizer=organizer,
            game=game,
            date_time=request.data["date_time"],
            location=request.data["location"]
        )
        serializer = EventSerializer(event)
        return Response(serializer.data)
    
class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gamer
        fields = ('id','full_name')

class EventGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title')

class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for customers"""
    organizer = OrganizerSerializer(many=False)
    game = EventGameSerializer(many=False)

    class Meta:
        model = Event
        fields = ('id', 'title', 'organizer', 'game', 'date_time', 'location')


