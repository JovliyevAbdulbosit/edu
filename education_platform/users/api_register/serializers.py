from rest_framework import serializers
from users.models import *

class TeacherSerializer(serializers.ModelSerializer):
    password2 =  serializers.CharField(
        write_only = True,
        style = {'input_type': 'password'}
    )
    class Meta:
        model = User
        fields=["password", "password2", "username","first_name", "last_name","phone" ,"email"]
        extra_kwargs ={
            "password":{"write_only":True}
        }
    def save(self , **kwargs):
        user = User(
            username = self.validated_data["username"],
            first_name = self.validated_data["first_name"],
            last_name = self.validated_data["last_name"],
            phone = self.validated_data["phone"],
            email = self.validated_data["email"],
            password=self.validated_data["password"]
        )
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2 :
            raise serializers.ValidationError({"error":"pasword error"})

        user.set_password(password)
        user.is_teacher = True
        self.validated_data.pop("password2")

        user.save()
        teacher  = TeacherModel()
        teacher.user_id = user.id
        teacher.first_name = user.first_name
        teacher.last_name = user.last_name
        teacher.phone = user.phone
        teacher.email = user.email
        teacher.save()


        return user
class StudentSerializer(serializers.ModelSerializer):
    password2 =  serializers.CharField(
        write_only = True,
        style = {'input_type': 'password'}
    )
    class Meta:
        model = User
        fields=["password", "password2", "username","first_name", "last_name","phone" ,"email"]
        extra_kwargs ={
            "password":{"write_only":True}
        }
    def save(self , **kwargs):
        user = User(
            username = self.validated_data["username"],
            first_name = self.validated_data["first_name"],
            last_name = self.validated_data["last_name"],
            phone = self.validated_data["phone"],
            email = self.validated_data["email"],
            password=self.validated_data["password"]
        )
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2 :
            raise serializers.ValidationError({"error":"pasword error"})
        user.set_password(password)
        user.is_student = True
        self.validated_data.pop("password2")
        user.save()
        student  = StudentModel()
        student.user_id = user.id
        student.first_name = user.first_name
        student.last_name = user.last_name
        student.phone = user.phone
        student.email = user.email
        student.save()
        return user
class CourseSerializer(serializers.ModelSerializer):
    class Meta :
        model = Courses
        fields ="__all__"
class CourseVideoSerializer(serializers.ModelSerializer):
    class Meta :
        model = CoursesVideo
        fields ="__all__"
class CategorySerializer(serializers.ModelSerializer):
    class Meta :
        model = Category
        fields ="__all__"
class OrdersSerializer(serializers.ModelSerializer):
    class Meta :
        model = Orders
        fields ="__all__"