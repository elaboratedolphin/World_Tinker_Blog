from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.urls import path
from django.urls import reverse_lazy
from django.contrib.postgres.search import SearchVector
from posts.models import Post, Comment
from posts.forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)

# Create your views here
class IndexView(TemplateView):
    template_name = 'posts/index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['index_inject'] = ''

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    paginate_by = 5
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class SearchResultsView(ListView):
    model = Post
    template_name = 'posts/search_results.html'
    slug_url_kwarg = 'title_slug'
    slug_field = 'slug'

    def get_queryset(self):
        query = self.request.GET.get('search')
        query_list = Post.objects.annotate(search=SearchVector('title', 'text', 'author', 'created_date'),).filter(search=query)
        return query_list

class FaithView(ListView):
    model = Post
    slug_url_kwarg = 'title_slug'
    slug_field = 'slug'
    template_name = 'posts/faith.html'

    def get_queryset(self):
        return Post.objects.filter(faith=True).filter(published_date__lte=timezone.now()).order_by('-published_date')

class FoodView(ListView):
    model = Post
    slug_url_kwarg = 'title_slug'
    slug_field = 'slug'
    template_name = 'posts/food.html'

    def get_queryset(self):
        return Post.objects.filter(food=True).filter(published_date__lte=timezone.now()).order_by('-published_date')

class MovieView(ListView):
    model = Post
    slug_url_kwarg = 'title_slug'
    slug_field = 'slug'
    template_name = 'posts/movie.html'

    def get_queryset(self):
        return Post.objects.filter(movie=True).filter(published_date__lte=timezone.now()).order_by('-published_date')

class LifeView(ListView):
    model = Post
    slug_url_kwarg = 'title_slug'
    slug_field = 'slug'
    template_name = 'posts/life.html'

    def get_queryset(self):
        return Post.objects.filter(life=True).filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post
    slug_url_kwarg = 'title_slug'
    slug_field = 'slug'

    def get_object(self):
        post = super().get_object()
        post.views += 1
        post.save()
        return post

class CreatePostView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'posts/post_detail.html'
    form_class = PostForm
    model = Post
    permission_required = ('posts.add_post')

class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'posts/post_detail.html'
    form_class = PostForm
    model = Post
    slug_url_kwarg = 'title_slug'
    slug_field = 'slug'
    permission_required = ('posts.update_post')

class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    slug_url_kwarg = 'title_slug'
    slug_field = 'slug'
    permission_required = ('posts.delete_post')

class DraftListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'posts/post_list.html'
    model = Post
    permission_required = ('posts.view_draft')

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')

##############################################
##############################################

@login_required
@permission_required('posts.publish_post')
def post_publish(request, title_slug):
    post = get_object_or_404(Post, slug=title_slug)
    post.publish()
    return redirect('post_detail', title_slug)

@login_required
def add_comment_to_post(request, title_slug):
    post = get_object_or_404(Post, slug=title_slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', title_slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'posts/comment_form.html', {'form':form})

@login_required
@permission_required('posts.approve_comment')
def comment_approve(request, title_slug):
    comment = get_object_or_404(Comment, slug=title_slug)
    comment.approve()
    return redirect('post_detail', comment.post.slug)

@login_required
@permission_required('posts.delete_comment')
def comment_remove(request, title_slug):
    comment = get_object_or_404(Comment, slug=title_slug)
    post_slug = comment.post.slug
    comment.delete()
    return redirect('post_detail', post_slug)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

################# rating/trending ####################




# @login_required
# def post_publish(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     post.publish()
#     return redirect('post_detail', pk=pk)
#
# @login_required
# def add_comment_to_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'blog/comment_form.html', {'form': form})


# @login_required
# def comment_approve(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     comment.approve()
#     return redirect('post_detail', pk=comment.post.pk)
#
#
# @login_required
# def comment_remove(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     post_pk = comment.post.pk
#     comment.delete()
#     return redirect('post_detail', pk=post_pk)
