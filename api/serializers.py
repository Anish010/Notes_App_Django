from rest_framework.serializers import ModelSerializer
from .models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        #fields = ['body']
        fields = '__all__' # all the objects is considered.
        
        