from rest_framework.permissions import BasePermission
from .models import User

class IsCourier(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.COURIER    