from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=100)
    hire_date = models.DateField()
    email = models.EmailField()
    boss = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def full_name(self):
        if self.middle_name:
            return f"{self.last_name} {self.first_name} {self.middle_name}"
        else:
            return f"{self.last_name} {self.first_name}"

    def __str__(self):
        return f"{self.position}, {self.full_name()}"

    def subordinates(self):
        return Employee.objects.filter(boss=self)

    def get_boss(self):
        if self.boss_id is not None:
            return Employee.objects.get(id=self.boss_id)
        else:
            return "Employee hasn`t boss"

    def full_info(self):
        boss_name = self.boss if self.boss else "No boss"

        return {
            'First Name': self.first_name,
            'Last Name': self.last_name,
            'Middle Name': self.middle_name if self.middle_name else "Not provided",
            'Position': self.position,
            'Hire Date': self.hire_date,
            'Email': self.email,
            'Boss': boss_name
        }
