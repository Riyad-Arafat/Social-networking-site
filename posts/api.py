from .models import Post
from rest_framework import serializers


class api_posts(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
