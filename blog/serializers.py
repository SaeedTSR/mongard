from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'description', 'image', 'url']
        read_only_fields = ['author']
        
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
        return rep