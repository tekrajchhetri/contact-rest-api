from rest_framework import permissions

class UpdateOwnContact(permissions.BasePermission):
    """Update own contact"""

    def has_permission(self, request, view):
        """Check if user is trying to update own contact"""