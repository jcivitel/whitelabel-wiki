from django.urls import path
from .views import wiki_page

urlpatterns = [
    path("wiki/<int:customer_id>/", wiki_page, name="wiki_page"),
]
