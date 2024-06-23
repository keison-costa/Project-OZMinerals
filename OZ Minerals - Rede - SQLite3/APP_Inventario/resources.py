# resources.py
from import_export import resources
from django.contrib.auth.models import User, Group
from .models import MakeMessages

class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')

class GroupResource(resources.ModelResource):
    class Meta:
        model = Group
        fields = ('name',)

class MakeMessagesResource(resources.ModelResource):
    class Meta:
        model = MakeMessages
        fields = ('field1', 'field2', 'field3')  # Atualize os campos conforme o modelo MakeMessages
