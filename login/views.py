from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

list = [{"name": 'good', 'password': 'python'}, {'name': 'learning', 'password': 'django'}]


def index(request):
    name = request.POST.get('name', None)
    password = request.POST.get('password', None)

    # 把用户和密码组装成字典
    data = {'name': name, 'password': password}
    list.append(data)
    return render(request, 'index.html',{'form': list})
    # 通过render模块把index.html这个文件返回到前端，并且返回给了前端一个变量form，在写html时可以调用这个form来展示list里的内容
