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
        data = json.loads(request.body)
        print('aaa')
        user = generics.get_object_or_404(
            queryset=User.objects.all(),
            email=data['email'],
            password=data['password']
        )
        print('bbb')
        result = UserSerializer(instance=user)
        print(result.data)
        return Response(result.data)
