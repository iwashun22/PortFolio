from rest_framework import viewsets, generics
from rest_framework.decorators import action
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import LikeSerializer, CareerSerializer, TagSerializer
from .models import SiteLikes, Career, Tag


# SiteLikesモデルのAPI
class LikesViewSet(viewsets.ViewSet):
    """サイトがいいねされた時の記録とその数をレスポンス"""
    serializer_class = LikeSerializer
    
    def list(self, request):
        """いいねされた数を返す"""
        return Response({"counter":SiteLikes.objects.count()})

    def create(self, request):
        """いいねを追加する"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            column = SiteLikes()
            column.save()

            return Response({"counter":SiteLikes.objects.count()})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

# TagモデルのAPI
class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


# CareerモデルのAPI
class CareerViewSet(viewsets.ViewSet):
    serializer_class = CareerSerializer

    def list(self, request):
        json = Career.objects.all().order_by("StartWork")[::-1]
        serializer = CareerSerializer(json, many=True)

        return Response(serializer.data)
    
    def retrieve(self, request, pk, group_pk=None):
        queryset = Career.objects.all()
        json = get_object_or_404(queryset, pk=pk)
        serializer = CareerSerializer(json)

        return Response(serializer.data)
    
    # GET /api/career/min_career/
    # 最新の３つのに内容をひぱってくれる
    @action(detail=False)
    def min_career(self, request):
        json = Career.objects.all().order_by("StartWork")[::-1][:3]
        serializer = CareerSerializer(json, many=True)

        return Response(serializer.data)
