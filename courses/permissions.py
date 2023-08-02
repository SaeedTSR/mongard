from rest_framework import permissions

class IsEpisodeOwner(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return obj.course.author == request.user