from django import forms
from .models import Question , Profile , Comment , Replies
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(label = "Password" , widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email'
                  ,'password','confirm_password']

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Password Mismatch')
        else:
            return confirm_password


class QuestionAskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['body']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
