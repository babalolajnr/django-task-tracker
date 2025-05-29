from rest_framework import serializers
from django.contrib.auth.models import User
from user.tasks import send_welcome_email

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'confirm_password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data): # pyright:ignore
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        send_welcome_email.delay(user.email, user.username) # pyright:ignore
        return user
