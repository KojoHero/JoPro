from django.contrib.auth import login
from django.db.models import Model
from rest_framework import generics, filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from knox.views import LoginView as KnoxLoginView
from rest_framework.response import Response

from .models import BlogModel, DocxModel, FAQModel, ListModel
from .serializers import RegSerializers, LogSerializer, BlogSerializer, DocxSerializer, FAQSerializer, ListSerializer


class RegView(generics.CreateAPIView):
    serializer_class = RegSerializers


class LoginView(KnoxLoginView):
    serializer_class = LogSerializer
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)


class BlogView(generics.ListAPIView):
    serializer_class = BlogSerializer
    queryset = BlogModel.objects.all()


class DocxView(generics.CreateAPIView):
    serializer_class = DocxSerializer
    queryset = DocxModel.objects.all()
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FAQView(generics.ListAPIView):
    serializer_class = FAQSerializer
    queryset = FAQModel.objects.all()
    permission_classes = [AllowAny,]
    filter_backends = [filters.SearchFilter]
    search_fields = ['question', 'answer']


class ListView(generics.ListAPIView):
    queryset = ListModel.objects.all()
    serializer_class = ListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['topic__title', 'status__status', 'user__username']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, status=self.request.status, title=self.request.title)




