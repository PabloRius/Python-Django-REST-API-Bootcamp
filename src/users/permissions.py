from rest_framework import permissions


class IsUserOwnerOrGetAndPostOnly(permissions.BasePermission):
    """Custom permissions for the Users viewset to only allow users to edit their own profile, otherwise, thay can only see other profiles or create a new one."""

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.user.is_anonymous:
            return request.user == obj

        return False
