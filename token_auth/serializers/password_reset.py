from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_jwt.serializers import PasswordField


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)
    redirect_url = serializers.CharField(max_length=500, required=False)
    class Meta:
        fields = ['email']
