from rest_framework.permissions import BasePermission
from .models import TeacherModel
class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_student)
class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        try:
            teacher = TeacherModel.objects.get(user_id = request.user.id)
        except:
            teacher=False
        return bool(request.user and request.user.is_teacher and teacher.is_active)