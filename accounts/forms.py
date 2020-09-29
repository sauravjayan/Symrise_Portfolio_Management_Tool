from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class AccountForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email', )
    


    

