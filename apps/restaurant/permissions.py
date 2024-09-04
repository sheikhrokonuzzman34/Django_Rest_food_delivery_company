from rest_framework.permissions import BasePermission

class IsOwnerOrEmployee(BasePermission):
    def has_permission(self, request, view):
        if request.user.role in ['owner', 'employee']:
            return True
        return False