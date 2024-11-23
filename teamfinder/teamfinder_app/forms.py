from django import forms
from .models import UserProfile, User
from teamfinder_app.models import Feedback
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", "name", "major", "faculty", "year")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("username", "email", "name", "major", "faculty", "year")


class RequestMessageForm(forms.Form):
    message = forms.CharField(max_length=200)

class ImageUploadForm(forms.Form):
    class Meta:
        model = UserProfile
        fields = ['profile_image']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'communication_pt',
            'collaboration_pt',
            'reliability_pt',
            'technical_pt',
            'empathy_pt',
            'comment'
        ]

    communication_pt = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect,
    )

    collaboration_pt = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect,
    )

    reliability_pt = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect,
    )

    technical_pt = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect,
    )

    empathy_pt = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect,
    )

    comment = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False,
    )

