from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Syllabus(models.Model):
    title=models.CharField(max_length=250)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    file=models.FileField(upload_to='pdf_files/')
    
    def __str__(self):
        return self.title
    
class Time_Table(models.Model):
    title=models.CharField(max_length=250)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    file=models.FileField(upload_to="time_table_pdf_files/")
    
    def __str__(self):
        return self.title
    

class Faculty(models.Model):
    name=models.CharField(max_length=300)
    department=models.TextField(max_length=500)
    file=models.ImageField(upload_to='faculty_images/')
    
    
    def __str__(self):
        return self.name
    
class Hackathons(models.Model):
    name=models.CharField(max_length=300)
    file=models.ImageField(upload_to='hackathon_images/')
    
    def __str__(self):
        return self.name
    

class Coding_Events(models.Model):
    name=models.CharField(max_length=300)
    file=models.ImageField(upload_to='coding_event_images/')
    
    def __str__(self):
        return self.name

class Research_cell_faculty(models.Model):
    name=models.CharField(max_length=250)
    department=models.CharField(max_length=300)
    file=models.ImageField(upload_to='research_cell_faculty_images/')
    order = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name

class Paper_published(models.Model):
    author_names=models.CharField(max_length=700)
    topic=models.CharField(max_length=500)
    link = models.URLField(max_length=600)
    
    def __str__(self):
        return f"{self.author_names} - {self.topic}"

class Alumni(models.Model):
    name=models.CharField(max_length=200)
    dept=models.TextField(max_length=500)
    batch=models.CharField(max_length=15)
    banner=models.ImageField(upload_to='alumni_students_images/')
    
    def __str__(self):
        return f"{self.name} - {self.dept} - {self.batch}"
    

