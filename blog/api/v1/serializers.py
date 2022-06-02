from blogs.models import Blogs
from rest_framework import serializers
from author.models import CustomUser, AuthorPoint

# class BlogSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     content = serializers.CharField()
#     author = serializers.IntegerField()
#     created = serializers.DateField(read_only=True)

#     def create(self, validated_data):
#         return Blogs.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data('title',instance.title)
#         instance.save()
#         return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'author_points']

class AuthorPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorPoint
        fields = '__all__'

class UserForBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'is_superuser', 'password']

class BlogSerializer(serializers.ModelSerializer):
    #author = serializers.StringRelatedField(read_only=True)
    #author = UserForBlogSerializer(read_only=True)
    author = serializers.HyperlinkedRelatedField(
        read_only = True,
        view_name='user_detail'
    )

    author_id = serializers.PrimaryKeyRelatedField(
        queryset= CustomUser.objects.all(), source="author", write_only=True
        )
    class Meta:
        model = Blogs
        fields = '__all__'
        #exclude = ['content'] gonderme bunu
        #read_only_fields = ['title'] bunu sadece men sene gonderecem


