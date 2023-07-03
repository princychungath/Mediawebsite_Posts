from django import forms
from .models import Post
# from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
        return super(UserLoginForm,self).clean(*args,**kwargs)
    

class UserRegisterForm(UserCreationForm):
    username=forms.EmailField(label='User Name ')
    email2=forms.EmailField(label='confirm email')
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model=User
        fields=['username','email','email2']

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms. ValidationError("Emails must match")
        email_qs= User.objects.filter(email=email) 
        if email_qs.exists():
            raise forms. ValidationError("This email has already been registered")
        return super (UserRegisterForm, self).clean (*args, **kwargs)



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Post_caption', 'image_or_video_content', 'location_post']

