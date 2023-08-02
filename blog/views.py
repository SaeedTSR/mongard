from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from permissions import IsOwner
from .models import Post
from .serializers import PostSerializer

class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
class PostRetrieveView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostUpdateView(UpdateAPIView):
    permission_classes = [IsOwner]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostDeleteView(DestroyAPIView):
    permission_classes = [IsOwner]
    queryset = Post.objects.all()
    serializer_class = PostSerializer