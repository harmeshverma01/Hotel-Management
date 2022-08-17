from multiprocessing.dummy import Manager
from rest_framework.permissions import BasePermission

class admin_required(BasePermission):
    def has_permission(self, request, view):
        if request.user.admin == 'admin':
            return True
        return False
    
    
class manager_required(BasePermission):
    def has_permission(self, request, view):
        if request.user.Manager == 'Manager':
            return True
        return False   