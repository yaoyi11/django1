from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# list = [{"name": 'good', 'password': 'python'}, {'name': 'learning', 'password': 'django'}]
#
#
# def index(request):
#     name = request.POST.get('name', None)
#     password = request.POST.get('password', None)
#
#     # 把用户和密码组装成字典
#     data = {'name': name, 'password': password}
#     list.append(data)
#     return render(request, 'index.html',{'form': list})
#     # 通过render模块把index.html这个文件返回到前端，并且返回给了前端一个变量form，在写html时可以调用这个form来展示list里的内容
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from login.models import Movie
from login.serializers import MovieSerializer, MovieSerializerNew


# 继承HttpResponse类，定义一个返回json数据的响应类
# class JsonResponse(HttpResponse):
#     def __init__(self,data,**kwargs):
#         # 重写content属性，返回rest_framework的JSON渲染器渲染的数据
#         content = JSONRenderer().render(data)
#         # 通过kwargs设置返回的数据类型为json
#         kwargs['content_type'] = 'application/json'
#         super(JsonResponse,self).__init__(content,**kwargs)

# # 电影列表资源
# @csrf_exempt
# def movie_list(request):
#     if request.method == 'GET':
#         # 查询所有电影信息
#         movies = Movie.objects.all()
#         # 实例化一个序列化器，指示为多条数据的序列化
#         movies_serializer = MovieSerializer(movies, many=True)
#         # 返回序列化的json数据
#         return JsonResponse(movies_serializer.data)
#
#     elif request.method == 'POST':
#         # 解析http请求的数据
#         movie_data = JSONParser().parse(request)
#         # 实例化一个序列化器
#         movies_serializer = MovieSerializer(data=movie_data)
#         # 如果序列化数据有效
#         if movies_serializer.is_valid():
#             movies_serializer.save()
#             return JsonResponse(movies_serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(movies_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 电影详情资源
# 电影列表资源
@api_view(['GET','POST'])
def movie_list(request):
    if request.method == 'GET':
        # 查询所有电影信息
        movies = Movie.objects.all()
        # 实例化一个序列化器
        movies_serializer = MovieSerializerNew(movies, many=True)
        # 返回序列化的json数据
        return Response(movies_serializer.data)

    elif request.method == 'POST':
        # 解析http请求的数据
        #movie_data = JSONParser().parse(request)
        # 实例化一个序列化器
        movies_serializer = MovieSerializerNew(data=request.data)
        # 如果序列化数据有效
        if movies_serializer.is_valid():
            movies_serializer.save()
            return Response(movies_serializer.data, status=status.HTTP_201_CREATED)
        return Response(movies_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def movie_detail(request, pk):
    # 首先判断是否存在相关数据
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    # 获取电影详情资源
    if request.method == 'GET':
        movie_serializer = MovieSerializerNew(movie)
        return Response(movie_serializer.data)

    # 修改电影详情资源
    elif request.method == 'PUT':
        #movie_data = JSONParser().parse(request)
        # MovieSerializer()序列化器接收的参数的定义来源于其基类BaseSerializer
        movie_serializer = MovieSerializerNew(movie, data=request.data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return Response(movie_serializer.data)
        return Response(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 删除电影详情资源
    elif request.method == 'DELETE':
        movie.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'error': '请求方法非法'})