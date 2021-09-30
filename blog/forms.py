from .models import Post,Category
from django import forms

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = Post
        #fields = ['title','image','content','category','status']
        exclude = ['status',]
