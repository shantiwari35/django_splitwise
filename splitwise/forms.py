from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *
#from .models import CustomUser
#from .models import Post1

class CustomUserCreationForm(UserCreationForm):
	
	#first_name = forms.CharField(required=True)
	#last_name = forms.CharField(required=True)
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

	def save(self, commit=True):
		user=super(CustomUserCreationForm, self).save(commit=False)
		#user.first_name = first_name
		#user.last_name = last_name
		#user.email = email

		if commit:
			user.save()

		return user

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('image',)

class ReminderForm(forms.Form):
		message = forms.CharField(label="message", max_length=500)

class FriendForm(forms.Form):
	your_name = forms.CharField(label="Friend's username", max_length=100)

class GroupForm(forms.Form):
    group_name = forms.CharField(label='Group name', max_length=100)
    RANGE_SHORT = 's'
    RANGE_MID = 'm'
    RANGE_LONG = 'l'
    RANGE_CHOICES = (
        (RANGE_SHORT, 'Sho'),
        (RANGE_MID, 'Mid range'),
        (RANGE_LONG, 'Long range')
    )
    friends = forms.MultipleChoiceField(choices=[])

    def __init__(self, user, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        self.fields['friends'] = forms.MultipleChoiceField(
            choices=user
        )

class InvolvedForm(forms.Form):
	friends = forms.MultipleChoiceField(choices=[])

	def __init__(self, user, *args, **kwargs):
		super(InvolvedForm, self).__init__(*args, **kwargs)
		self.fields['friends'] = forms.MultipleChoiceField(
		choices=user
		)

class ChangeForm(forms.Form):
	friends = forms.MultipleChoiceField(choices=[])

	def __init__(self, user, *args, **kwargs):
		super(ChangeForm, self).__init__(*args, **kwargs)
		self.fields['friends'] = forms.MultipleChoiceField(
		choices=user
		)

class TransactionForm(forms.Form):
	description = forms.CharField(max_length=30)
	who_paid = forms.MultipleChoiceField(choices=[])
	amount = forms.DecimalField(decimal_places=2,max_digits=10)
	CHOICES = [
		('equal', 'Split Equally'),
		('unequal', 'Split Unequally')
	]
	split = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
	def __init__(self, involved, *args, **kwargs):
		super(TransactionForm, self).__init__(*args, **kwargs)
		self.fields['who_paid'] = forms.MultipleChoiceField(
		choices=involved
		)
		self.field_names = []
		for i in involved:
			self.fields[i[0]+' (%)'] = forms.DecimalField(decimal_places=2,max_digits=10,required = False)
			self.field_names.append(i[0]+ ' (%)')
	MOVIES = 'mv'
	FOOD = 'fd'
	TRAVEL = 'tr'
	ELECTRONICS = 'ee'
	MEDICAL = 'md'
	SHOPPING = 'sp'
	SERVICES = 'sv'
	OTHERS = 'ot'
	TAG_CHOICES= [
        (MOVIES, 'Movies'),
		(FOOD, 'Food'),
		(TRAVEL, 'Travel'),
		(ELECTRONICS, 'Electronics'),
		(MEDICAL, 'Medical'),
		(SHOPPING, 'Shopping'),
		(SERVICES, 'Services'),
		(OTHERS, 'Others')
	]
	tag = forms.ChoiceField(choices=TAG_CHOICES)
	def clean(self):
		cleaned_data = super().clean()
		#print('FFF')
		data = self.cleaned_data
		y = cleaned_data.get('split')
		if y == 'unequal':
			z = 0
			for i in self.field_names:
				x = cleaned_data.get(i)

				if x == None:
					#print('FFF')
					raise forms.ValidationError('Enter Shares')
				z = z + x
				print(z)
			if z != 100:
				raise forms.ValidationError('Total not 100')
	
	
class GroupTransactionForm(forms.Form):
	description = forms.CharField(max_length=30)
	who_paid = forms.MultipleChoiceField(choices=[])
	amount = forms.DecimalField(decimal_places=2,max_digits=10)
	field_names = []
	CHOICES = [
		('equal', 'Split Equally'),
		('unequal', 'Split Unequally')
	]
	split = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
	def __init__(self, involved, *args, **kwargs):
		super(GroupTransactionForm, self).__init__(*args, **kwargs)
		self.fields['who_paid'] = forms.MultipleChoiceField(
		choices=involved
		)
		self.field_names = []
		for i in involved:
			self.fields[i[0]+' (%)'] = forms.DecimalField(decimal_places=2,max_digits=10,required = False)
			self.field_names.append(i[0]+ ' (%)')
	MOVIES = 'mv'
	FOOD = 'fd'
	TRAVEL = 'tr'
	ELECTRONICS = 'ee'
	MEDICAL = 'md'
	SHOPPING = 'sp'
	SERVICES = 'sv'
	SETTLE = 'st'
	OTHERS = 'ot'
	TAG_CHOICES= [
        (MOVIES, 'Movies'),
		(FOOD, 'Food'),
		(TRAVEL, 'Travel'),
		(ELECTRONICS, 'Electronics'),
		(MEDICAL, 'Medical'),
		(SHOPPING, 'Shopping'),
		(SERVICES, 'Services'),
		(SETTLE, 'Settle'),
		(OTHERS, 'Others')
	]
	tag = forms.ChoiceField(choices=TAG_CHOICES)
	def clean(self):
		cleaned_data = super().clean()
		#print('FFF')
		data = self.cleaned_data
		y = cleaned_data.get('split')
		if y == 'unequal':
			z = 0
			for i in self.field_names:
				x = cleaned_data.get(i)

				if x == None:
					#print('FFF')
					raise forms.ValidationError('Enter Shares')
				z = z + x
				print(z)
			if z != 100:
				raise forms.ValidationError('Total not 100')

			

#class EditProfileForm(forms.Form):
	
#	first_name = forms.CharField(required=True)
#	last_name = forms.CharField(required=True)
#	email = forms.EmailField(required=True)
#	image = forms.ImageField(required=True)

#	class Meta:
#		model = User
#		fields = ('first_name', 'last_name', 'email', 'image')

#	def save(self, commit=True):
#		user=super(EditProfileForm, self).save(commit=False)
		#user.first_name = first_name
		#user.last_name = last_name
		#user.email = email

#		if commit:
#			user.save()

#		return user


