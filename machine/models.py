from django.db import models

class Machine(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Standard(models.Model):
    name = models.CharField(max_length=20)
    value_safe_min = models.FloatField()
    value_safe_max = models.FloatField()
    value_alarm_min = models.FloatField()
    value_alarm_max = models.FloatField()
    value_danger_min = models.FloatField()
    value_danger_max = models.FloatField()
        
    def get_severity(self, x, y, z):
        if (self.value_safe_min <= x <= self.value_safe_max and
            self.value_safe_min <= y <= self.value_safe_max and
            self.value_safe_min <= z <= self.value_safe_max):
            return 'Safe'
        elif (self.value_alarm_min <= x <= self.value_alarm_max or
            self.value_alarm_min <= y <= self.value_alarm_max or
            self.value_alarm_min <= z <= self.value_alarm_max):
            return 'Alarm'
        else:
            return 'Danger'
    
    def __str__(self):
        return self.name
       
class MeasurementPoint(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
class Report(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)
    measurement_points = models.ForeignKey(MeasurementPoint, on_delete=models.CASCADE)
    value_x = models.IntegerField()
    value_y = models.IntegerField()
    value_z = models.IntegerField()
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    
    @property
    def overall_severity(self):
        severities = [self.standard.get_severity(self.value_x, self.value_y, self.value_z)]
        
        if 'Danger' in severities:
            return 'Danger'
        elif 'Alarm' in severities:
            return 'Alarm'
        else:
            return 'Safe'



    

# Create your models here.
