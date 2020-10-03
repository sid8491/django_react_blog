# from django.urls import path
# from .views import PostList, PostDetail
from rest_framework.routers import DefaultRouter
from .views import PostList

app_name = 'blog_api'

router = DefaultRouter()
router.register('', PostList, basename='post')
urlpatterns = router.urls

# urlpatterns = [
#     path('<int:pk>/', PostDetail.as_view(), name='detail_create'),
#     path('', PostList.as_view(), name='list_create'),
# ]
