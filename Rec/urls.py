from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, re_path
from Rec import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Matches any html file 
    re_path(r'^.*\.html', views.pages, name='pages'),
    # The home page
    path('', views.index, name='home'),
    path('ques/new/', views.new_question, name='new_question'),
    path('ques/view/', views.question_view, name='view-question'),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)