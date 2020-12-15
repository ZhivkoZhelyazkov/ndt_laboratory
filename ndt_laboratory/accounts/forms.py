# from django import forms
# from django.contrib.auth.forms import UserCreationForm
#
# # from ndt_laboratory.core.BootstrapFormMixin import BootstrapFormMixin
# from ndt_laboratory.accounts.models import UserProfile
#
#
# class SignUpForm(UserCreationForm):  #  , BootstrapFormMixin
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.setup_form()
#
#
# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('profile_picture',)