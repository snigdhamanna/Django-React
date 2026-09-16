from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True , min_length=5, style={'input_type':'password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    # Move this out of class Meta so it aligns with the password field above
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
