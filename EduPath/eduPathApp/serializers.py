# from rest_framework import serializers
# from .models import Subject, Material
# from django.contrib.auth.models import User

# class SubjectSerializer(serializers.ModelSerializer):
#     class Meta:
#       model = Subject
#       fields = ['id', 'name', 'description']

# class MaterialSerializer(serializers.ModelSerializer):
#     currentUser = serializers.ReadOnlyField(source='currentUser.username')
#     class Meta:
#       model = Material
#       fields = ['id', 'subject', 'title', 'file', 'created_at', 'currentUser']