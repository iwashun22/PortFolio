import datetime

from rest_framework import viewsets
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, authentication

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import LikeSerializer, CareerSerializer, TagSerializer, UserSerializer
from .models import SiteLikes, Career, Tag

authentication.TokenAuthentication.keyword = 'Bearer'

# SiteLikesモデルのAPI
class LikesViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]
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

    @action(detail=False, methods=['get'])
    def get_like_each_days(self, request, pk=None):
        Like = SiteLikes.objects
        json = {}
        now = datetime.datetime.now()

        if not request.query_params.get("days") is None:
            Days = int(request.query_params.get("days"))

            for i in range(Days):
                past = now - datetime.timedelta(days = i)
                one_json = Like.filter(created_at = past)
                json.update(one_json)
            
            serializer = LikeSerializer(json, many=True)
            return Response(
                serializer.data
            )
        else:
            serializer = LikeSerializer(json, many=True)
            return Response(
                "You should to add query to url"
            , status=400)

    @action(detail=False, methods=['get'])
    def get_like(self, request, pk=None):
        json = SiteLikes.objects

        Year = request.query_params.get("year")
        Month = request.query_params.get("month")
        Day = request.query_params.get("day")
        Minus = request.query_params.get("minus")

        if not Minus is None:
            date = datetime.datetime.now()
            data = (date + datetime.timedelta(days = -(int(Minus))))
            json = json.filter(created_at__gte = data)
        else:
            if not Year is None:
                json = json.filter(created_at__year = Year)
            if not Month is None:
                json = json.filter(created_at__month = Month)
            if not Day is None:
                json = json.filter(created_at__day = Day)
        
        serializer = LikeSerializer(json, many=True)
        return Response({
            "count": len(serializer.data),
        })

# TagモデルのAPI
class TagViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


# CareerモデルのAPI
class CareerViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]
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


class SignUpView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response({"result": "fail"}, status=400)

        username = serializer.validated_data['username']
        password = serializer.validated_data["password"]
        user = User.objects.create_user(
            username=username,
            password=password
        )

        user.save()
        token = Token.objects.create(user=user)

        try:
            token = Token.objects.get(user=user)
            return Response({'token': token.key})
        except:
            return Response({'token': 'token fail'}, status=400)

class SignInView(viewsets.ViewSet):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer_class = UserSerializer
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'result': 'credential is not valid'})
        try:
            # クライアントにセットするためtokenを出力する
            token = Token.objects.get(user=user.id)
            login(request, user)
            return Response({'token': token.key})
        except:
            return Response({'result': 'token fail'}, status=400)

class LoginView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request, format=None):
        return Response(data={
            'user': {
                "id": request.user.id,
                "username": request.user.username,
                "email": request.user.email
            }
        },
            status=status.HTTP_200_OK)
