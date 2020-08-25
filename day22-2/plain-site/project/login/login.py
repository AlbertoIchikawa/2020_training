import json

from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, views
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


class LoginViewSet(views.APIView):
    Serializer_class = UserSerializer

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        # 変数の中にrequestの情報を代入する。
        # JSON形式であること、その形式で取得することが大事。
        data = json.loads(request.body)
        print(data['email'])
        user = generics.get_object_or_404(
          queryset=User.objects.all(),
          email=data['email'],  # dataの中のemailの情報を抽出
          password=data['password']  # dataの中のpasswordの情報を抽出
        )
        result = UserSerializer(instance=user)
        print(result.data)  # 確認用
        return Response(result.data)  # returnもJSON形式で返すこと
