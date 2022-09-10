from django import forms

class FeedbackForm(forms.Form):
    email=forms.EmailField(label="Enter your email", max_length=200)
    nmae=forms.CharField(label="Enter your Name", max_length=200)
    feedback=forms.CharField(label="Your Feedbacke", widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
