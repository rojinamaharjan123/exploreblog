from django.urls import *
from .views import *

app_name = "exploreapp"
urlpatterns = [
	path("", HomeView.as_view(), 
		name="clienthome"),
]