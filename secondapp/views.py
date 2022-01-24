from django.shortcuts import redirect, render
from django.http import HttpResponse

from secondapp.forms import CourseForm
from .models import Course
from .models import ArmyShop

# Create your views here.
def main(request):
    return HttpResponse('<u>Main</u>')

def insert(request):
    Course.objects.create(name='데이터 분석', cnt=30)
    Course(name='데이터 수집', cnt=20).save()
    Course(name='웹개발', cnt=25).save()
    Course(name='인공지능', cnt=20).save()
    
    return HttpResponse('데이터 입력 완료')

def show(request):
    course = Course.objects.all()
    # result = ''
    # for c in course:
    #     # result += c.name + '<br>'
    #     result += '%s %s<br>' % (c.name, c.cnt)
    
    
    return render(
        request, 'secondapp/show.html',
        { 'data': course }
    )

def army_shop(request):
    # armyshop = ArmyShop.objects.all()
    # prd = request.GET.get('prd', '')        # 부작용 side effect
    
    prd = request.GET.get('prd', '')        # 부작용 side effect
    # prd = request.POST.get('prd', '')        # 부작용 side effect
    try:
        armyshop = ArmyShop.objects.filter(name__contains=prd)
    except:
        armyshop = ArmyShop.objects.all()
    
    return render(
        request, 'secondapp/army_shop.html',
        { 'data': armyshop }
    )

def army_shop2(request, year, month):
    armyshop = ArmyShop.objects.filter(year=year, month=month)
    
    # result = ''
    # for i in armyshop:
    #     result += '%s %s %s<br>' %(i.year, i.month, i.name)

    result = [ '%s %s %s<br>' %(i.year, i.month, i.name) for i in armyshop ]

    return HttpResponse(''.join(result))

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.forms.models import model_to_dict
@csrf_exempt
def ajaxGet(request):

    # QuerySet []
    c = Course.objects.all()
    data = []

    # model_to_dict - 조회된 데이터를 dict 형태로 변경
    for a in c:
        d = model_to_dict(a)
        data.append(d)

    return JsonResponse( data, safe=False )

def ajaxExam(request):
    return render(request, 'secondapp/ajax_exam.html')

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def ajaxPost(request):
    c = Course.objects.all()
    data = []

    # model_to_dict - 조회된 데이터를 dict 형태로 변경
    for a in c:
        d = model_to_dict(a)
        data.append(d)

    return JsonResponse( data, safe=False )

@csrf_exempt
def ajaxJson(request):
    c = Course.objects.all()
    data = []

    # model_to_dict - 조회된 데이터를 dict 형태로 변경
    for a in c:
        d = model_to_dict(a)
        data.append(d)

    return JsonResponse( data, safe=False )

def course_create(request):
    if request.method == 'POST':
        # form 미사용시 작성되는 코드
        # name = request.Post.get('name')
        # cnt = request.Post.get('cnt')
        # c = Course(name = name, cnt = cnt)
        # c.save()

        # 1. 입력된 데이터(요청 데이터)를 한꺼번에 저장
        # 2. 유효성 검사 결과 저장
        form = CourseForm(request.POST)
        if form.is_valid():
            # 데이터 저장
            course = form .save(commit = False)
            course.save()
            # 어딘가로 이동, 메시지 출력, ...
            
            return redirect('secondapp:show')

    else:
        form = CourseForm()

    return render(request, 'secondapp/course_create.html', 
        {'form' : form})