from rest_framework.permissions import BasePermission

class admin_required(BasePermission):
    def has_permission(self, request, view):
        if request.user.room == 'admin':
            return True
        return False