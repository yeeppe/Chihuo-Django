from django import forms
import datetime



class RSVPCreateEventFormStep1(forms.Form):
	title = forms.CharField(max_length=30)
	date = forms.DateField(initial=datetime.date.today)
	num_attendance = forms.IntegerField(help_text='Number of people attending')
	place = forms.CharField(max_length=30)

class RSVPCreateEventFormStep2(forms.Form):
	image = forms.FileField()
	description = forms.CharField(widget=forms.Textarea())

class RSVPCreateEventFormStep3(forms.Form):
	email_nofitication = forms.EmailField(help_text='A notification email address, please.')