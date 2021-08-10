from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import LikeSerializer, CareerSerializer, TagSerializer
from .models import SiteLikes, Career, Tag


class LikesViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    queryset = SiteLikes.objects.all()


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class CareerViewSet(viewsets.ModelViewSet):
    serializer_class = CareerSerializer
    queryset = Career.objects.all()

    # GET /api/career/min_career/
    # 最新の３つのに内容をひぱってくれる
    @action(detail=False)
    def min_career(self, request):
        min_career = Career.objects.all().order_by("StartWork")[0:3]
        page = self.paginate_queryset(min_career)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(min_career, many=True)
        return Response(serializer.data)
