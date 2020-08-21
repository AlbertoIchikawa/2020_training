from rest_framework.response import responses

from .models import User
from .serializers import UserSerializer


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

