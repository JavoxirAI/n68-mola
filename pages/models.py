from django.db import models


class ContactModel(models.Model):
    full_name = models.CharField(max_length=128)
    email = models.EmailField()
    phone_number = models.CharField(
        max_length=15, null=True, blank=True
    )
    subject = models.CharField(
        max_length=255, null=True, blank=True
    )
    message = models.TextField()

    is_read = models.BooleanField(default=False)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'




class BlogCategoryModel(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog-Category'
        verbose_name_plural = 'Blog-Categories'

class BlogTagModel(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog-Tag'
        verbose_name_plural = 'Blog-Tags'

class BlogAuthorModel(models.Model):
    full_name = models.CharField(max_length=64)
    avatar = models.ImageField(upload_to='blog-author/', null=True, blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Blog-Author'
        verbose_name_plural = 'Blog-Authors'

class BlogPostModel(models.Model):
    picture = models.ImageField(upload_to='blog-post/')
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        BlogAuthorModel,
        on_delete=models.CASCADE,
        related_name='author_posts'
    )
    category = models.ManyToManyField(
        BlogCategoryModel,
        related_name='category_posts'
    )
    tag = models.ManyToManyField(
        BlogTagModel,
        related_name='tag_posts'
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog-Post'
        verbose_name_plural = 'Blog-Posts'