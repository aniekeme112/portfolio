from rest_framework.generics import ListAPIView
from .models import FeaturedProject
from .serializers import FeaturedProjectSerializer

class FeaturedProjectListAPIView(ListAPIView):
    queryset = FeaturedProject.objects.all()
    serializer_class = FeaturedProjectSerializer
