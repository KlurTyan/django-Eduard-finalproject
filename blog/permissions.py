from rest_framework.permissions import BasePermission
from .models import User

class IsCourier(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.COURIER    
    
class IsSeller(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.SELLER 

class IsSuperAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.SUPERADMIN

class IsAssembler(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.ASSEMBLER   

class IsBasic(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.BASIC   