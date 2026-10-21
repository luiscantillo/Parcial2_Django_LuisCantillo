from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()

    # Con este metodo el admin podrá mostrar el nombre del proyecto
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    # Con este metodo el admin puede mostrar el titulo que tienen las tareas
    def __str__(self):
        return self.title