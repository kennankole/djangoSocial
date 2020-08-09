from django.contrib.auth import get_user

#Creating user profiles upon registration
class ProfileGetObjectMixin:
    '''
    A mixin to get the current user 
    '''
    def get_object(self, queryset=None):
        current_user = get_user(self.request)
        return current_user.profiles