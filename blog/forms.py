from django import forms
from django.contrib.auth.models import User
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'content', 'image', 'published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Title of your story...'}),
            'excerpt': forms.Textarea(attrs={'class': 'input-field', 'rows': 3, 'placeholder': 'A short, catchy summary...'}),
            'content': forms.Textarea(attrs={'class': 'input-field', 'rows': 10, 'placeholder': 'Tell your full story...'}),
            'image': forms.FileInput(attrs={'class': 'file-input'}),
        }

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'hello@example.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '••••••••'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user