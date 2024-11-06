from rest_framework import serializers
from .models import Course


# # Create your normal serializers here.
# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = ('id', 'name', 'language', 'price')
        
        
# Create your serializers here. - it add url to each object
class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'url', 'name', 'language', 'price')