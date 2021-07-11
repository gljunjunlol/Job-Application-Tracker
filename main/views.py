from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item, Contact
from .forms import CreateNewList, ContactForm

from django.contrib import messages

# Create your views here.

def index(response, id):
	ls = ToDoList.objects.get(id=id)

	if ls in response.user.todolist.all():


		if response.method == "POST":   # post is like for private information e.g. password
			print(response.POST)
			if response.POST.get("save"):
				for item in ls.item_set.all():
					if response.POST.get("c" + str(item.id)) == "clicked":
						item.complete = True
					else:
						item.complete = False

					item.save()

			elif response.POST.get("newItem"):
				txt = response.POST.get("new")

			if response.POST.get("delete"):
				for item in ls.item_set.all():
					if response.POST.get("c" + str(item.id)) == "clicked":
						item.delete()
					else:
						pass

			if response.POST.get("delete_all"):
				for item in ls.item_set.all():
					if response.POST.get("c" + str(item.id)) == "clicked":
						item.complete = True
					else:
						item.complete = False

					item.delete()

					

			elif response.POST.get("newItem"):
				txt = response.POST.get("new")

				if len(txt) > 0:
					ls.item_set.create(text=txt, complete = False)
				else:
					print("invalid")

		return render(response, "main/list.html", {"ls":ls})
	return render(response, "main/view.html", {})

def create2(response):
	if response.method == "POST":
		form = CreateNewList(response.POST)

		if form.is_valid():
			n = form.cleaned_data["name"]
			t = ToDoList(name=n)
			t.save()
			response.user.todolist.add(t)

		return HttpResponseRedirect("/%i" %t.id)

	else:
		form = CreateNewList()

	return render(response, "main/create2.html", {"form":form})

def delete2(request, pk):
	item = ToDoList.objects.get(id=pk)

	if request.method =='POST':
		item.delete()
		return redirect('/')


	context= {'item':item}
	return render(request, 'main/delete2.html', context)


def home(response):
	return render(response, "main/home.html", {})

def create(request):

	if not request.user.is_authenticated:
		return redirect('/login')
	else:
		a = Contact.objects.filter(user=request.user)

		form1 = ContactForm()

		if request.method == 'POST':
			form1 = ContactForm(request.POST)
			if form1.is_valid():
				n = form1.cleaned_data["name"]
				e = form1.cleaned_data["email"]
				p = form1.cleaned_data["purpose"]
				l = form1.cleaned_data["location"]
				d = form1.cleaned_data["date"]
				m = form1.cleaned_data["message"]
				t = Contact(name=n,email=e,purpose=p,location=l,date=d,message=m)
				t.save()
				request.user.contact.add(t)

				return redirect("/")
		else:
			messages.error(request, "Your error message")
			form = ContactForm()

		context = {'contacts':a, 'form1': form1}
		
		return render(request, "main/create.html", context)


def updateCompany(request, pk):
	# pk is primary key
	b = Contact.objects.get(id=pk)

	form = ContactForm(instance=b)

	if request.method =='POST':
		form = ContactForm(request.POST, instance=b)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'main/update_company.html', context)

def deleteCompany(request, pk):
	item = Contact.objects.get(id=pk)

	if request.method =='POST':
		item.delete()
		return redirect('/')


	context= {'item':item}
	return render(request, 'main/delete_company.html', context)

	


def view(response):
	return render(response, "main/view.html", {})

def favourite(response):

	if not response.user.is_authenticated:
		return redirect('/login')
	else:
		a = Contact.objects.filter(user=response.user)


		context = {'contacts':a}

		return render(response, "main/favourite.html", context)



def jobs(request):
	job_data = None
	from bs4 import BeautifulSoup

	import grequests
	import requests
	import time
	import numpy as np

	start_time = time.time()
	

	
	
	
	all_jobs = []
	
	links = ["https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=1&startPage=1",
	 "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=2&startPage=1",
	 "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=3&startPage=1",
	 "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=4&startPage=1",
	 "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=5&startPage=1",
	 "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=6&startPage=1",
	 "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=7&startPage=1",
	 "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=8&startPage=1",
	 "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=9&startPage=1",
	 "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=10&startPage=1",
	 "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=11&startPage=1",
	 "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=12&startPage=1",
	 "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=13&startPage=1",
	 "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=14&startPage=1",
	 "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=15&startPage=1",
	 "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=16&startPage=1",
	 "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=17&startPage=1",
	 "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=18startPage=1",
	 "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=19&startPage=1",
	 "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=20&startPage=1"]
	pages = np.arange(0, 20, 1)

	reqs = (grequests.get(link) for link in links)
	resp = grequests.imap(reqs, grequests.Pool(20))
	for r in resp:
		soup = BeautifulSoup(r.text, 'html.parser')
		jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

		for jb in jobs:
			published_date = jb.find('span', class_= 'sim-posted').span.text
			company_name = jb.find('h3', class_ = 'joblist-comp-name').text.strip()
			skill = jb.find('span', class_= 'srp-skills').text.replace(' ','')
			more_info = jb.header.h2.a['href']


			all_jobs.append(published_date + company_name + skill + more_info)

	
	
	return render(request, "main/jobs.html", {'all_jobs' : all_jobs})

""" Synchronous slower method
def jobs(request):
	job_data = None
	from bs4 import BeautifulSoup

	import requests
	import numpy as np
	

	
	
	
	all_jobs = []
	
	
	
	pages = np.arange(0, 20, 1)

	for page in pages:
		page = requests.get("https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=" + str(page) + "&startPage=1")
		soup = BeautifulSoup(page.text, 'html.parser')
		jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

		for jb in jobs:
			published_date = jb.find('span', class_= 'sim-posted').span.text
			company_name = jb.find('h3', class_ = 'joblist-comp-name').text.strip()
			skill = jb.find('span', class_= 'srp-skills').text.replace(' ','')
			more_info = jb.header.h2.a['href']


			all_jobs.append(published_date + company_name + skill + more_info)

	
	
	return render(request, "main/jobs.html", {'all_jobs' : all_jobs})"""

def search(request):
	qur = request.GET.get('search').lower()
	# contacts = Contact.objects.filter(name__contains = qur)
	a = [item for item in Contact.objects.filter(user=request.user) if qur in item.name.lower() or qur in item.email.lower() or qur in item.purpose.lower() or qur in item.role.lower() or qur in item.location.lower() or qur in item.message.lower()]
	return render(request, 'main/search.html', {'contacts': a})


def saved_jobs(response):

	a = Contact.objects.filter(user=response.user)

	context = {'contacts' : a}
	return render(response, "main/saved_jobs.html", context)

def dream_jobs(response):
	

	
	
	return render(response, "main/dream_jobs.html", {})


def previous_jobs(response):


	return render(response,"main/previous_jobs.html",{})