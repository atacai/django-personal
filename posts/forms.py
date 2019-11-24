from django 			import forms
from .models	import Post

class PostForm(forms.ModelForm):
	class Meta:
		model 	= Post
		fields 	= '__all__'

	def clean(self):
		super().clean()
		username = self.cleaned_data.get('username')
		post_text = self.cleaned_data.get('post_text')

		if len(username) < 5:
			self._errors['username'] = self.error_class(['Minimum 5 characters required'])
		if len(post_text) < 10:
			self._errors['post_text'] = self.error_class(['Post Should Contain minimum 10 characters']) 

		return self.cleaned_data