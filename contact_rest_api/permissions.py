from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their onw profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class UpdateOwnContact(permissions.BasePermission):
    """Update own contact"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to update own contact"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_contact_id == request.user.id