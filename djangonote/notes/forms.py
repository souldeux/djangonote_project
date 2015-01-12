from django import forms
from notes.models import Note, Tag

class NoteForm(forms.ModelForm):
	
	class Meta:
		model = Note
		fields = ('label', 'body', 'tags')
		
class TagForm(forms.ModelForm):
	
	class Meta:
		model = Tag
		fields = ('label',)