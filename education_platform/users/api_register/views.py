from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from rest_framework.generics import GenericAPIView ,ListAPIView , ListCreateAPIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from ..models import User
from ..permissions import IsStudent, IsTeacher


class TeacherRegister(GenericAPIView):
    serializer_class = TeacherSerializer
    def post(self,request , *args, **kwargs):
        serialize = self.get_serializer(data = request.data)
        serialize.is_valid(raise_exception=True)
        user = serialize.save()
        return Response(
            {"user":TeacherSerializer(user,context = self.get_serializer_context()).data,
             "token":Token.objects.get(user = user).key,
             }
        )
class StudentRegister(GenericAPIView):
    serializer_class = StudentSerializer
    def post(self,request , *args, **kwargs):
        serialize = self.get_serializer(data = request.data)
        serialize.is_valid(raise_exception=True)
        user = serialize.save()
        return Response(
            {"user":StudentSerializer(user,context = self.get_serializer_context()).data,
             "token":Token.objects.get(user = user).key,
             }
        )
class CustomLoginView(ObtainAuthToken):
    def post(self,request ,*args ,**kwargs):
        serializer = self.serializer_class(data = request.data , context={"request":request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token , creat = Token.objects.get_or_create(user=user)
        return Response({
            "token":token.key,
            "user_id":user.pk,
            "is_student":user.is_student
        })
class AllUserView(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = StudentSerializer
    queryset = User.objects.all()
class LogoutView(APIView):
    def post(self , request , form = None):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)
class CategoryAddView(ListCreateAPIView):
    permission_classes = [IsTeacher|IsAdminUser]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
class CourseAddView(ListCreateAPIView):
    permission_classes = [IsTeacher|IsAdminUser]
    serializer_class = CourseSerializer
    queryset = Courses.objects.all()
class CourseVideoAddView(ListCreateAPIView):
    permission_classes = [IsTeacher|IsAdminUser]
    serializer_class = CourseVideoSerializer
    queryset = CoursesVideo.objects.all()
@api_view(['PUT',])
@permission_classes([IsTeacher])
def coursePutVeiw(request , course_id):
    try:
        course = Courses.objects.get(id=course_id)
        teacher = TeacherModel.objects.get(user_id =request.user.id)
        if request.method == 'PUT' and teacher.id == course.teacher_id.id:
            serializer = CourseSerializer(course, request.data)
            data = {}
            if serializer.is_valid():
                serializer.save()
                data['success'] = 'update successful'
                return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
	    return Response(status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT',])
@permission_classes([IsTeacher])
def courseVideoPutVeiw(request , course_video_id):
    try:
        video = CoursesVideo.objects.get(id=course_video_id)
        teacher = TeacherModel.objects.get(user_id =request.user.id)
        if request.method == 'PUT' and teacher.id == video.course_id.teacher_id.id:
            serializer = CourseVideoSerializer(video, request.data)
            data = {}
            if serializer.is_valid():
                serializer.save()
                data['success'] = 'update successful'
                return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
	    return Response(status=status.HTTP_400_BAD_REQUEST)

def student_course(check_number,student_id,course_id ):
    course = Orders.objects.filter(check_number=check_number,student_id = student_id,course_id = course_id)
    if course :
        return True
    else:
        return False
@api_view(['GET',])
@permission_classes([IsStudent])
def student_course_video(request , check_number,course_id ):
    student_id = StudentModel.objects.get(user_id = request.user.id)
    if student_course(check_number, student_id, course_id) and request.method=='GET':
        try:
            video=CoursesVideo.objects.get(course_id=course_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=CourseVideoSerializer(video)
        return Response(serializer.data)
