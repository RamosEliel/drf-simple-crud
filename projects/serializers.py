from rest_framework import serializers
from .models import project

class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields = '__all__'
        field = ('id','title','description','tecnology','created_at')
        read_only_fields = ('created_at', )
        

        


