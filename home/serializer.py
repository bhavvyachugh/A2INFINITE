from rest_framework import serializers
from .models import Topic, SubTopic

class SubTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTopic
        fields = "__all__"
    
class TopicSerializer(serializers.ModelSerializer):
    subtopics = SubTopicSerializer(source='topic', many=True)
    class Meta:
        model = Topic
        fields = "__all__"