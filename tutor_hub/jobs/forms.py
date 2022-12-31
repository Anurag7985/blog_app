from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    subject_required = forms.charField()
    bio = forms.CharField(widget=forms.Textarea)
class Tutor(models.Model):
    tutor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject_expertise = models.CharField(max_length=255)
    bio = models.TextField(default='')
