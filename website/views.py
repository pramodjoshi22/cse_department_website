from django.shortcuts import render
from webapp.models import *


def HOME(request):
    alumni=Alumni.objects.all()
    context={
        'alumni':alumni
    }
    return render(request,'home.html',context)

def ABOUT(request):
    return render(request,'about.html')

def DEVELOPERS(request):
    return render(request,'developers.html')

def SYLLABUS(request):
    pdf=Syllabus.objects.all()
    
    data={
        'pdf':pdf
    }
    return render(request,'syllabus.html',data)



def TIMETABLE(request):
    file=Time_Table.objects.all()
    context={
        'file':file
    }
    return render(request,'time_table.html',context)

def FACULTY(request):
    img=Faculty.objects.all()
    context={
        'img':img
    }
    return render(request,'faculty.html',context)

def HACKATHONS(request):
    events=Hackathons.objects.all()
    context={
        'events':events
    }
    return render(request,'hackathons.html',context)

def CODING_EVENTS(request):
    return render(request,'coding_events.html')

def RESEARCH_CELL_faculty(request):
    img=Research_cell_faculty.objects.order_by('order')
    context={
        'img1':img
    }
    
    return render(request,'researchcell.html',context)

def PAPER_PUBLISHED(request):
    paper=Paper_published.objects.all()
    context={
        'research_paper':paper
    }
    return render(request,'paper_published.html',context)

def NOTICES(request):
    return render(request,'notices.html')