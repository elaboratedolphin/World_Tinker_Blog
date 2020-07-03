from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.models import auth
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex

# class User(auth.models.User,auth.models.PermissionsMixin):
#
#     def __str__(self):
#         return "@{}".format(self.username)


#Blog Article Post attributes
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    text = RichTextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(default="default-title")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)
    views = models.PositiveIntegerField(default=0)
    food = models.BooleanField(default=False)
    movie = models.BooleanField(default=False)
    faith = models.BooleanField(default=False)
    life = models.BooleanField(default=False)

    #creates slug outside of admin console
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    #saves published post
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #returns comments for approval
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    #sends to post once posted
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'title_slug':self.slug})

    #returns the title
    def __str__(self):
        return self.title

# need to change to log in required
# Comment attributes
class Comment(models.Model):
    post = models.ForeignKey('posts.Post',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    slug = models.SlugField(default="default-title")
    created_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    #comment approval
    def approve(self):
        self.approved_comment = True
        self.save()

    #sends to the list of posts
    def get_absolute_url(self):
        return reverse('post_list')

    #returns post
    def __str__(self):
        return self.text
