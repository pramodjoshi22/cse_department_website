from django.shortcuts import render
from webapp.models import *


def HOME(request):
    alumni=Alumni.objects.all()
    context={
        'alumni':alumni
    }
    return render(request,'home.html',context)

def ABOUT(request):
    page_name = "About Us"
    return render(request,'about.html',{'page_name': page_name})

def SYLLABUS(request):
    
    pdf=Syllabus.objects.all()
    page_name="Syllabus"
    data={
        'pdf':pdf,
        'page_name':page_name
        
    }
    return render(request,'syllabus.html',data)



def TIMETABLE(request):
    file=Time_Table.objects.all()
    page_name="Time Table"
    context={
        'file':file,
        'page_name':page_name
        
    }
    return render(request,'time_table.html',context)

def FACULTY(request):
    page_name="Faculty"
    img=Faculty.objects.all()
    context={
        'img':img,
        'page_name':page_name
        
    }
    return render(request,'faculty.html',context)

def DEVELOPERS(request):
    page_name = "Developers"
    return render(request,'developers.html',{'page_name': page_name})

def Gallery(request):
    page_name = "Gallery"
    return render(request,'gallery.html',{'page_name': page_name})

def HACKATHONS(request):
    page_name="Hackathons"
    events=Hackathons.objects.all()
    context={
        'events':events,
        'page_name':page_name
        
    }
    return render(request,'hackathons.html',context)

def CODING_EVENTS(request):
    page_name="Coding Events"
    context={
        'page_name':page_name
    }
    return render(request,'coding_events.html',context)

def RESEARCH_CELL_faculty(request):
    page_name="Research Cell"
    img=Research_cell_faculty.objects.order_by('order')
    context={
        'img1':img,
        'page_name':page_name
    }
    
    return render(request,'researchcell.html',context)

def PAPER_PUBLISHED(request):
    page_name="Paper Published"
    
    paper=Paper_published.objects.all()
    context={
        'research_paper':paper,
        'page_name':page_name
        
    }
    return render(request,'paper_published.html',context)

def NOTICES(request):
    page_name="Notices"
    return render(request,'notices.html',{'page_name': page_name})