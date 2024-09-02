from django.urls import path
from .views import PostListView, PostUserListView,  PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .import views

urlpatterns = [
    path('', PostListView.as_view(), name='recipe-home'), 
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/list/', PostUserListView.as_view(), name='post-list'),
    path('about/',views.about, name='recipe-about'),
]