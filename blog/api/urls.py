from django.urls import path
from rest_framework.routers import DefaultRouter
from blog.api.views import PostListAPIView,PostCreateView

# router = DefaultRouter()
# router.register(r'blog', PostViewSet, basename='blog')
urlpatterns = [
    path('blog/',PostListAPIView.as_view()),
    path('blog-create/',PostCreateView.as_view()),
]
