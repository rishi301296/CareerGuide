from django.db import models

class College_Basic_Detail(models.Model):
    collegeId = models.CharField(primary_key = True, max_length = 50)
    name = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    courses = models.CharField(max_length = 500)
    
    def __unicode__(self):
        return self.collegeId

class College_Placement_Detail(models.Model):
    college = models.ForeignKey(College_Basic_Detail, on_delete=models.CASCADE)
    totalStudents = models.IntegerField()
    placedStudents = models.IntegerField()
    averageSalary = models.IntegerField()
    course = models.CharField(max_length = 100)

    def __unicode__(self):
        return str(self.college)+'$'+self.course