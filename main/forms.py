from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Department
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content',)
        # content = forms.CharField(widgets=CKEditorWidget())

class commentForm(forms.ModelForm):

    class Meta:
         model = Comment
         fields = ( 'content',)

Department_Choices = (
    ("Education", "Education"),
    ("Economics", "Economics"),
    ("Acturial", "Acturial"),
    # ....
    ("Music", "Music"),
)
class UserCreateForm(UserCreationForm):
    department = forms.ChoiceField(choices=Department_Choices, required=True)

    class Meta:
        model = User
        fields = ("username", "password1", "password2", 'department')
