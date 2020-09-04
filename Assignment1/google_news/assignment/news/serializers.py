from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id_user',
            'name',
            'email',
            'password'
        )


# class NewsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = News
#         fields = (
#             'title'
#         )
