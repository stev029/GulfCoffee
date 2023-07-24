from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = "Editing/delete is restricted to author only."

    def has_object_permission(self, request, view, obj):
        print(obj)
        if request.user == obj.user:
            return True
        return False
