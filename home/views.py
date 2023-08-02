from rest_framework.response import Response
from rest_framework.views import APIView
from django.urls import reverse

class HomeView(APIView):
    def get(self, request):
        cou_url = reverse('courses:list')
        blo_url = reverse("blog:list")
        courses = f'http://127.0.0.1:8000{cou_url}'
        blog = f'http://127.0.0.1:8000{blo_url}'
        result = {'blog':blog, 'courses':courses}
        return Response({'result':result})