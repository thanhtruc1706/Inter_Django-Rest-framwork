from django.urls import path
from . import views

urlpatterns = [
    # Function-based views
    path('fbv/snippets/', views.snippet_list),
    path('fbv/snippets/<int:pk>/', views.snippet_detail),

    # Class-based views
    path('cbv/snippets/', views.SnippetList.as_view()),
    path('cbv/snippets/<int:pk>/', views.SnippetDetail.as_view()),
] 