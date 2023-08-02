from rest_framework import serializers
from .models import Course, Episode

class CourseSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    episodes = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
        fields = ['id', 'author', 'title', 'description', 'image', 'price', 'created_date', 'url', 'episodes']
        read_only_fields = ['author']
        
    def get_episodes(self, obj):
        result = obj.episodes.all()
        return EpisodeListSerializer(instance=result, many=True).data
        
    def get_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    
    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('url', None)
        else:
            rep.pop('description', None)
            rep.pop('episodes', None)
        return rep
        
class EpisodeListSerializer(serializers.ModelSerializer):
    # url = serializers.SerializerMethodField()
    course_name = serializers.SerializerMethodField()
    read_only_fields = ['course_name']
    
    class Meta:
        model = Episode
        fields = ['id', 'course', 'course_name', 'title', 'video']
    
    def get_course_name(self, obj):
        return obj.course.title
    
    # def get_url(self, obj):
    #     request = self.context.get('request')
    #     return request.build_absolute_uri(obj.pk)