from django.urls import path
from .views import *
urlpatterns =[
                path("teacher/register/",TeacherRegister.as_view()) ,
                path("student/register/",StudentRegister.as_view()) ,
                path("all/user/",AllUserView.as_view()) ,
                path("logout/",LogoutView.as_view()) ,
                path("category_add/",CategoryAddView.as_view()) ,
                path("courses_add/", CourseAddView.as_view()) ,
                path("courses_update/<int:course_id>/", coursePutVeiw) ,
                path("course_video_update/<int:course_video_id>/", courseVideoPutVeiw) ,
                path("course_video_get/<int:check_number>/<int:course_id>/", student_course_video) ,
                path("course_video_add/",CourseVideoAddView.as_view()) ,
                path("login/",CustomLoginView.as_view() , name="auth_token"), ]