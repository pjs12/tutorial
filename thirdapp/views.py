from django.http import HttpResponse
from django.shortcuts import render
from .models import Shop, JejuOlle

def shop(request):
    shop_list = Shop.objects.all()

    return render(
        request,
        'thirdapp/shop.html',
        {'shop_list': shop_list}
    )

def jejuolle(request):
    olle = JejuOlle.objects.all()
    result = ''
    for d in olle:
        result += d.course_name
    
    return HttpResponse(result)

    # return render(
    #     request,
    #     'thirdapp/jeju_olle.html',
    #     {'olle_list': olle}
    # )

# from .models import Store
# def Storeshow(request):
#     # curriculum = Curriculum.objects.all()
#     # result=''
#     # for c in curriculum:
#     #     result += c.name + '<br>'
#     # return HttpResponse(result)

#     store = Store.objects.all()
#     return render(
#         request, 'thirdapp/store_show.html', 
#         {'store': store}
#     )