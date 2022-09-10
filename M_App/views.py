from django.http import HttpResponse
from django.shortcuts import render
import datetime



def home(request):

    isActive = False

    if request.method == 'POST':
        check = request.POST.get("check")
        print(check)
        if check is not None:
            isActive = True
        else: isActive = False



    date = datetime.datetime.now()
    
    name = 'Maidul'
    list_of_programs = [
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prime number from 1 to 100',
        'WAP to print pascals tringle'
    ]
    student = {
        'std_name': 'Maidul',
        'std_college': 'XYZ',
    }

    # sending dynamic data
    data = {
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student
    }


    return render(request,'home.html',data)


def about(request):
    return render(request, 'about.html', {})


def services(request):
    return render(request, 'services.html', {})
