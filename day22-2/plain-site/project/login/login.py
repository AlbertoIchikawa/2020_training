from rest_framework.response import responses

from .models import User
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    if request.method == 'POST':
        print('test')
        print(request)
        print('\n')
    else:
        print('test test')
    # response = HttpResponse('')
    # print(responses)
    # user = User.objects.all()
    # serializer = UserSerializer(user, many=True)

    return responses

