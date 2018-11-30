from django import forms
from django.contrib.auth.models import User
from webapp.models import Signup,Post,Friends
from django.core.exceptions import ValidationError

class Signupform(forms.ModelForm):

	password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control",'Placeholder':'Password'}))

	username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'Placeholder':'Username'}))

	email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control"}))

	class Meta():
		
		model = User
		
		fields = ('username','email','password')

class Loginform(forms.ModelForm):

	password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control",'Placeholder':'Password'}))

	username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'Placeholder':'Username'}))

	email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control"}))

	class Meta():
		
		model = User
		
		fields = ('username','password')

	# def clean_username(self):

	# 	name = self.cleaned_data.get('username')

	# 	password = self.cleaned_data.get("password")

	# 	validate_name = User.objects.filter(username=name)

	# 	for i in validate_name:

	# 		if password!=i.password:

	# 			raise forms.ValidationError("Username/password is incorrect")


class Postform(forms.ModelForm):

	h = User.objects.all()	

	types = (('all','all'),)

	for i in h:

		types = types+((i.username,i.username),)

	print(types)

	name= forms.ChoiceField(choices=types)

	Title = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-4",'Placeholder':"Title"}))

	content = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-4",'Placeholder':"Content"}))

	class Meta():

		model = Post

		fields = ('Title','content','profile_pic','author','name')


class Friendsform(forms.ModelForm):

	class Meta():

		model = Friends

		fields = "__all__"

# class Like_dislikeform(forms.ModelForm):

# 	class Meta():

# 		model = Like_dislike

# 		fields = "__all__"