from rest_framework import serializers

from users.models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = '__all__'
