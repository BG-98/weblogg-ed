from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.

Category_Choices = (
    ('question','Post a Question'),
    ('city', 'Around the City'),
    ('secret','Secret Post'),
    ('none','None'),
)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    datep = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=15, choices=Category_Choices, default='none')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_pics/',blank=True,null=True)
    likes = models.ManyToManyField(User,related_name='likes',blank=True)
    # video = models.FileField(upload_to='post_videos/',blank=True,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return #

    # def total_likes(self):
    #     return self.likes.count()

    # @property
    # def video_url(self):
    #     if self.video and hasattr(self.video, 'url'):
    #         return self.video.url
    #     return #

    def save(self, *args, **kwargs):
        super(Post, self).save( *args, **kwargs)

        if self.image and hasattr(self.image, 'url'):
            img = Image.open(self.image.path)
            if img.height>800 or img.width>800:
                output_size = (800,800)
                img.thumbnail(output_size)
                img.save(self.image.path)

class comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    # def approved_comments(self):
    #     return self.comments.filter(approved_comment=True)
    