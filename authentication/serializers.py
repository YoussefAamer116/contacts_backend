from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def validate(self, attrs):
        email = attrs.get('email','')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':('Email is already exist')})
        return super().validate(attrs)    
    
    def create(self, validated_data):
        return super().create(**validated_data)