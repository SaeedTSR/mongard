from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from permissions import IsOwner
from .permissions import IsEpisodeOwner
from .models import Course, Episode
from .serializers import CourseSerializer, EpisodeListSerializer

class CourseListView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
class CourseRetrieveView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
class CourseUpdateView(UpdateAPIView):
    permission_classes = [IsOwner]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
class CourseDeleteView(DestroyAPIView):
    permission_classes = [IsOwner]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
   
class EpisodeRetrieveView(RetrieveAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeListSerializer
    
class EpisodeCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Episode.objects.all()
    serializer_class = EpisodeListSerializer
    
class EpisodeUpdateView(UpdateAPIView):
    permission_classes = [IsEpisodeOwner]
    queryset = Episode.objects.all()
    serializer_class = EpisodeListSerializer
    
class EpisodeDeleteView(DestroyAPIView):
    permission_classes = [IsEpisodeOwner]
    queryset = Episode.objects.all()
    serializer_class = EpisodeListSerializer