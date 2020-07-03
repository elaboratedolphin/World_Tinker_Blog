from django.conf.urls import url
from posts import views
from django.urls import path

urlpatterns = [
    path('', views.PostListView.as_view(),name='post_list'),
    path('faith/', views.FaithView.as_view(), name='faith'),
    path('movie/', views.MovieView.as_view(), name='movie'),
    path('food/', views.FoodView.as_view(), name='food'),
    path('life/', views.LifeView.as_view(), name='life'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('about/', views.AboutView.as_view(),name='about'),
    path('post/new/', views.CreatePostView.as_view(),name='post_new'),
    path('post/<slug:title_slug>/', views.PostDetailView.as_view(),name='post_detail'),
    #update/edit
    path('post/<slug:title_slug>/edit/', views.PostUpdateView.as_view(),name='post_edit'),
    path('post/<slug:title_slug>/delete/', views.PostDeleteView.as_view(),name='post_remove'),
    path('drafts/', views.DraftListView.as_view(),name='post_draft_list'),
    path('post/<slug:title_slug>/publish/', views.post_publish, name='post_publish'),
    path('post/<slug:title_slug>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<slug:title_slug>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<slug:title_slug>/remove/', views.comment_remove, name='comment_remove'),
]
