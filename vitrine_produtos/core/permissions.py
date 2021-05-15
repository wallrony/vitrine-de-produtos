from rest_framework import permissions
from vitrine_produtos.accounts.models import Profile


class UserHavePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user and request.user.is_authenticated:
            profile = Profile.objects.get(user_id=request.user.id)

            return profile.role == 2

        return False
