from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    # Password defined by django lacks functionality (like write_only)
    password = serializers.CharField(write_only=True, required=False)
    # Users should not be able to change their username
    username = serializers.CharField(read_only=True)

    # Create function is run every time a post request is sent to the users serializer
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)

        user.save()

        return user

    class Meta:
        model = User
        fields = ["url", "id", "username", "email",
                  "first_name", "last_name", "password"]
