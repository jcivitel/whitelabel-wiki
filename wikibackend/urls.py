from django.urls import path

from .views import wiki_page, dashboard, upload_image

urlpatterns = [
    path('upload_image/<int:customer_id>/', upload_image, name='upload_image'),
    path("wiki/<int:customer_id>/", dashboard, name="dashboard"),
    path("wiki/<int:customer_id>/<str:url>", wiki_page, name="wiki_page"),
]
