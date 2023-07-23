from .models import Status, Poem, Comment
from django.forms import ModelForm

class PostPoem(ModelForm):
    class Meta:
        model = Poem
        fields = ["title","body"]

class WriteComment(ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_body"]

class WriteStatus(ModelForm):
    class Meta:
        model = Status
        fields = ["status_body"]