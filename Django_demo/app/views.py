from django.http import JsonResponse
from django.shortcuts import render, redirect


# Create your views here.

def helloword(request):

    # return HttpResponse('{"code":200,"name":"刘程旭"}')
    return render(request,"test.html",{"email":"邮箱账号","title":"测开大佬！刘程旭","name":"昵称"})

# 这个就是重定向 重定向其他人的方法
def he(requset):
    return redirect(helloword)

# 下面这个是传入json格式的数据  第一个是正常模式  第二个是非安全模式用来处理字典外面带列表的数据
def jsonresponse(request):

    # return JsonResponse({"name":"刘程旭","age":18})
    return JsonResponse([{"name": "刘程旭", "age": 18},{"name": "泰勒", "age": 16}],safe=False)

