from rest_framework.permissions import BasePermission

class IsAdminOrAuthor(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and (
            request.user == obj.author or
            request.user.is_staff == True 
        )