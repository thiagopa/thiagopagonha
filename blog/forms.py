from django.forms import ModelForm

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        
        
    