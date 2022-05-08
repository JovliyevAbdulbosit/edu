from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50 , unique=True )
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    phone = models.CharField(max_length=20)
    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.username
@receiver(post_save , sender = settings.AUTH_USER_MODEL)
def create_token(sender , instance=None , created = False , **kwargs):
    if created :
        Token.objects.create(user = instance)

class TeacherModel(models.Model):
    user = models.OneToOneField(User ,related_name="teacher", on_delete=models.CASCADE)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    profession = models.CharField(max_length=40,blank=True , null=True)
    experience = models.TextField(blank=True , null=True)
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
class StudentModel(models.Model):
    user = models.OneToOneField(User ,related_name="student", on_delete=models.CASCADE)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.user.username
class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name
class Courses(models.Model):
    category_id = models.ForeignKey(Category ,on_delete=models.CASCADE)
    teacher_id =  models.ForeignKey(TeacherModel ,on_delete=models.CASCADE)
    course_name = models.CharField(max_length=20)
    course_price = models.BigIntegerField(default=0)
    is_free = models.BooleanField(default=False)
    def __str__(self):
        return self.course_name
class Orders(models.Model):
    check_number = models.BigIntegerField()
    student_id = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    pay = models.BigIntegerField(default=0)
    def __str__(self):
        return self.student_id.first_name

class CoursesVideo(models.Model):
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    course_video = models.FileField(upload_to="video")
    course_image = models.ImageField(upload_to="image")
    def __str__(self):
        return self.course_id.course_name
