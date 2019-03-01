# coding:utf-8
from rest_framework import serializers
from login.models import Movie

class MovieSerializer(serializers.Serializer):
    # 声明模型的字段
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)
    movie_cate = serializers.CharField(max_length=30)
    movie_img = serializers.CharField(max_length=300)
    release_date = serializers.DateField()
    viewed = serializers.BooleanField(default=False)

    # 声明模型创建的方法
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    # 声明模型更新的方法
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.movie_cate = validated_data.get('movie_cate', instance.movie_cate)
        instance.movie_img = validated_data.get('movie_img', instance.movie_img)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.viewed = validated_data.get('viewed', instance.viewed)
        instance.save()
        return instance

class MovieSerializerNew(serializers.ModelSerializer):
    class Meta:
        # 指定序列化器需要作用的模型
        model = Movie
        # 指定序列化器的模型字段
        fields = (
            'id',
            'name',
            'movie_cate',
            'movie_img',
            'release_date',
            'viewed',
            'created',
        )
