from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from gendercv.models import CV
from django.urls import reverse
# Create your views here.


data_cv = {
    "name": "LÂM QUANG PHÚ",
    "role": "DataEngineer Intern", 
    "title":"Hello, I am a data engineer intern. I possess strong research and search skills. I dedicate myself to daily self-improvement. I am quite confident in my analytical abilities. I have some experience with AWS, Cloud Formation, Kubernetes, Docker, Django, Git, Database, etc.",
    "email":"lamquangphu2176@gmail.com",
    "github":"github.com/aquariusdayroi",
    "phone":"0339254262",
    "honorrs": 
        '''
            Second Prize of the Olympic Vietnam Student Information Technology
            Third Prize of the 2022 ICPC Vietnam National Programming Contest
            Second Prize of the Olympic Vietnam Student Information Technology
            Third Prize of the 2023 ICPC Vietnam Southern Provincial Programming
        ''',
    "school":"Industrial University Of Ho Chi Minh City",
              
    "specialized":"Data Science - 3 year student",
    "gpa":"3.60/4",
    "code":"Python (Django), Java, JavaScriptC, C++,...",
    "tech":"AWS, Linux, Cloud Formation, Kubernetes, Docker, Virtual Machine,Web Scraping(Selenium, Scrapy), Git, Database,..",
}



def submit_form(request):
    if request.method == 'POST':
        # print(request.POST)  # In ra dữ liệu được gửi từ form
        # print(request.FILES)  # In ra dữ liệu của các file được gửi từ form
        name = request.POST.get('name')
        role = request.POST.get('role')
        title = request.POST.get('title')
        honorrs = request.POST.get('honorrs')
        email = request.POST.get('email')
        github = request.POST.get('github')
        phone = request.POST.get('phone')
        code = request.POST.get('code')
        tech = request.POST.get('tech')
        image = request.FILES.get('image')  # Lấy dữ liệu của trường hình ảnh
        school = request.POST.get('school')
        gpa = request.POST.get('gpa')
        specialized = request.POST.get('specialized')
        print(name, role, title, email, github, phone, code, tech, image)  # In ra các giá trị của các trường
        # Tiếp tục xử lý dữ liệu và lưu hình ảnh theo yêu cầu của bạn

        cv = CV.objects.all()
        
        if cv:
            cv.delete()
        cv = CV.objects.create(
                name=name,
                role=role,
                title=title,
                honorrs=honorrs,
                email=email,
                github=github,
                phone=phone,
                code=code,
                tech=tech,
                image=image,
                school=school,
                gpa = gpa,
                specialized = specialized,
            )
        cv.save()
    return HttpResponseRedirect(reverse('gencv', args = [2] ))



def form(request):
    return render(request, 'gendercv/form.html', )

def gencv(request, num):
    data_cv = CV.objects.all()[0]
    if num == 1:
        return render(request, 'gendercv/cv1.html',  {
            "data_cv": data_cv,
           }
        )
    else: 
        return render(request, 'gendercv/cv2.html',  {"data_cv":data_cv})
