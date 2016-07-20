from django.http import HttpResponse
from django.shortcuts import render

#from .forms import NameForm


def your_pnrno(request):
	if request.method == 'POST':
		no = request.POST.get("pnrno", "")
		execfile('polls/new.py')
		f = open('data')
		no1 = f.readlines()
		f.close()
		return render(request, 'polls/thanks.html', {"number" : no1},)
def post_list(request):
    return render(request, 'polls/post_list.html', {})
	
