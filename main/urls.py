from django.urls import path  # path to our different web pages

from . import views

urlpatterns = [
path("<int:id>", views.index, name="index"),    #if we get into this application and homepage and dont type slash we are going into views.index and surf the http response in "views" which shows tech with tim  
path("", views.home, name="home"),
path("home/", views.home, name="home"),
path("create/", views.create, name="create"),
path("view/", views.view, name="view"),
path("favourite/", views.favourite, name="favourite"),
path("jobs/", views.jobs, name="jobs"),
path("saved_jobs/", views.saved_jobs, name="saved_jobs"),
path("dream_jobs/", views.dream_jobs, name="dream_jobs"),
path("previous_jobs/", views.previous_jobs, name="previous_jobs"),
path("create2/", views.create2, name="create2"),
path("delete2/<str:pk>/", views.delete2, name="delete2"),

path("update_company/<str:pk>/", views.updateCompany, name="update_company"),
path("delete_company/<str:pk>/", views.deleteCompany, name="delete_company"),

path("search/", views.search, name='search'),


]
