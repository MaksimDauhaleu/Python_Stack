from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.books_authors_app.urls')),
]

