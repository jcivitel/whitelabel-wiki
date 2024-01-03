from django.urls import path
from .views import wiki_page,dashboard

urlpatterns = [
    path("wiki/<int:customer_id>/", dashboard , name="dashboard"),
    path("wiki/<int:customer_id>/<str:url>", wiki_page, name="wiki_page"),
]
