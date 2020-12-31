from rest_framework import serializers

from api.base.user.models import User


class VerificationCodeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['email']
