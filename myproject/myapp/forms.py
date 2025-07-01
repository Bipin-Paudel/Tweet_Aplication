from django import forms
from .models import tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = tweet
        fields =[ 'text', 'photo']

class  UserRegistrationForm(UserCreationForm):
    emails =forms.EmailField()

    class Meta:
        model = User
        fields= ('username', 'email', 'password1', 'password2')


        # optional styling of the  form this is not mandatory
        def __init__(self, *args, **kwargs):

          super(UserRegistrationForm, self).__init__(*args, **kwargs)
          for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white'
            }) 
        