from django.shortcuts import render
from django.http			import HttpResponseRedirect
from .forms 					import PostForm

def index(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			# return HttpResponse("data submitted successfully")
			return HttpResponseRedirect('posts/post.html')
		else:
			return render(request, 'posts/post.html', {'form': form})
	else:
		form = PostForm()
	return render(request, 'posts/post.html', {'form': form})