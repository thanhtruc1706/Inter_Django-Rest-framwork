from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'snippets', views.SnippetViewSet)

urlpatterns = [
    # Function-based views
    path('fbv/snippets/', views.snippet_list),
    path('fbv/snippets/<int:pk>/', views.snippet_detail),

    # Class-based views
    path('cbv/snippets/', views.SnippetList.as_view()),
    path('cbv/snippets/<int:pk>/', views.SnippetDetail.as_view()),

    # Router URLs
    path('', include(router.urls)),
] 