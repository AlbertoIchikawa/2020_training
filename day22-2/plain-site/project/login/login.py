from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import responses
from .models import User
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer
import json
from django.http.response import JsonResponse


@csrf_exempt
def login(request):
    user_agent = request.META.get('HTTP_USER_AGENT', None)
    # axiosがPOSTの場合の処理
    if request.method == 'POST':
        # 変数の中にrequestの情報を代入する。
        # JSON形式であること、その形式で取得することが大事。
        data = json.loads(request.body)
        email = {'data': data['email']}  # dataの中のemailの情報を抽出
        password = {'data': data['password']}  # dataの中のpasswordの情報を抽出
        print(email)  # 確認用
        print(password)  # 確認用
    return JsonResponse(email)  # returnもJSON形式で返すこと

    # DB内の情報の引き出し
    # user = User.objects.all()
    # serializer = UserSerializer(user, many=True)
    # print(serializer.data)
