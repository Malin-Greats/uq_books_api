import queue
from sre_parse import WHITESPACE
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta


def upload_to(instance, filename):
    return filename.format(filename=filename)


# AUTHOR'S PROFILE MODEL
class AuthorProfile(models.Model):
    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=100)
    profile_picture = models.ImageField(
        upload_to=upload_to, blank=True, null=True)
    totalRevenue = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    currentRevenue = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    total_books = models.IntegerField(blank=True, null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_banned = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# RECEIVER TO TRIGGER CREATION OF PROFILE AFTER NEW USER IS CREATED


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = AuthorProfile.objects.create(user=instance)
        profile.save()
    else:
        instance.profile.save()


# AUTHOR ADDRESS MODEL
class AuthorAddress(models.Model):
    name = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    building = models.CharField(max_length=200, null=True, blank=True)
    street = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    # state = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    postal_code = models.CharField(
        max_length=25, default=0000, null=True, blank=True)
    isDefault = models.BooleanField(default=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


# BOOK FOR PRINT MODEL
class BookPrint(models.Model):
    author = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True,
                             blank=True, default="default data title")
    description = models.TextField(
        max_length=1000, null=True, blank=True, default="default data description")
    language = models.CharField(
        max_length=200, null=True, blank=True, default="default data language")
    category = models.CharField(
        max_length=200, null=True, blank=True, default="default data category")
    book_pdf = models.FileField(upload_to=upload_to, null=True, blank=True,)
    pages = models.IntegerField(default=0, null=True, blank=True)
    size = models.CharField(max_length=50, blank=True,
                            null=True, default="default data size")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0.0)
    color = models.CharField(max_length=100, blank=True,
                             null=True, default="default data color")
    binding = models.CharField(
        max_length=100, blank=True, null=True, default="default data binding")
    isbn = models.CharField(max_length=100, blank=True,
                            null=True, default="default data isbn")
    cover = models.ImageField(upload_to=upload_to, blank=True, null=True)
    cover_finish = models.CharField(
        max_length=100, blank=True, null=True, default="default data coverFinish")
    print_cost = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True,)
    created_at = models.DateTimeField(
        auto_now_add=True, null=True, blank=True,)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True,)
    queue_status = models.CharField(
        max_length=100, blank=True, null=True, default="queued")
    is_printed = models.BooleanField(default=False, null=True, blank=True)
    is_banned = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ('-created_at',)


# BOOK FOR PUBLISH  MODEL
class BookPublish(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    contributors = models.ManyToManyField(
        'BookContributor', related_name='bookpublish_contributors', blank=True, null=True)
    title = models.CharField(max_length=200, null=True,
                             blank=True, default="title")
    description = models.TextField(
        max_length=1000, null=True, blank=True, default="description")
    contributor_notes = models.TextField(
        max_length=1000, null=True, blank=True, default="contributor_notes")
    table_of_contents = models.TextField(
        max_length=1000, null=True, blank=True, default="table_of_contents")
    language = models.CharField(
        max_length=200, null=True, blank=True, default="language")
    category = models.CharField(
        max_length=200, null=True, blank=True, default="category")
    bisac_category1 = models.CharField(
        max_length=200, null=True, blank=True, default="bisac_category1")
    bisac_category2 = models.CharField(
        max_length=200, null=True, blank=True, default="bisac_category2")
    bisac_category3 = models.CharField(
        max_length=200, null=True, blank=True, default="bisac_category3")
    keywords = models.TextField(
        max_length=500, null=True, blank=True, default="keywords")
    audience = models.TextField(
        max_length=500, null=True, blank=True, default="audience")
    color = models.CharField(max_length=100, blank=True,
                             null=True, default="color")
    binding = models.CharField(
        max_length=100, blank=True, null=True, default='Binding')
    paper = models.CharField(max_length=100, blank=True,
                             null=True, default='Binding')
    cover_finish = models.CharField(
        max_length=100, blank=True, null=True, default='Binding')
    isbn = models.CharField(max_length=100, blank=True,
                            null=True, default="isbn")
    book_pdf = models.FileField(upload_to=upload_to, null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True, default=0)
    size = models.CharField(max_length=50, blank=True,
                            null=True, default="size")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    totalRevenue = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    currentRevenue = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    cover = models.ImageField(upload_to=upload_to, blank=True, null=True)
    global_upload = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    has_explicit_content = models.BooleanField(
        default=False, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_banned = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)


# BOOK FOR STORE MODEL  ***these need no publishing
class StoreBook(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, null=True, blank=True)
    language = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    keywords = models.TextField(max_length=500, null=True, blank=True)
    audience = models.TextField(max_length=500, null=True, blank=True)
    book_pdf = models.FileField(upload_to=upload_to, null=True, blank=True)
    pages = models.IntegerField(default=0)
    size = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cover = models.ImageField(upload_to=upload_to, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    has_explicit_content = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=True)
    # is_banned = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)


# BOOK COPYRIGHT MODEL **works only on published books
class BookCopyright(models.Model):
    # author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    book = models.ForeignKey(BookPublish, null=True, on_delete=models.CASCADE)
    contributors = models.ManyToManyField(
        'BookContributor', related_name='bookcopyright_contributors', blank=True)
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    edition = models.CharField(max_length=200, null=True, blank=True)
    edition_statement = models.CharField(max_length=200, null=True, blank=True)
    rights_reserved = models.BooleanField(default=False)
    holder = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book.title


# BOOK COONTRIBUTOR MODEL **works only on published books
class BookContributor(models.Model):
    # author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    book = models.ForeignKey(BookPublish, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


# BOOK PAYEE MODEL **works only on published books
class BookPayee(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    book = models.ForeignKey(BookPublish, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    paypal_email = models.EmailField(max_length=150, blank=True, null=True)
    is_organization = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


# BOOK REVIEW MODEL **works only on published books in the store
class BookReview(models.Model):
    # author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=150, blank=True, null=True)
    book = models.ForeignKey(BookPublish, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    review = models.TextField(max_length=1000, null=True, blank=True)
    rating = models.IntegerField(default=0, blank=True, null=True)
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# BLOG POST MODEL
class BlogPost(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=True, blank=True)
    category = models.CharField(max_length=150, null=True, blank=True)
    headline = models.CharField(max_length=150, null=True, blank=True)
    sub_headline1 = models.CharField(max_length=150, null=True, blank=True)
    sub_headline2 = models.CharField(max_length=150, null=True, blank=True)
    sub_headline3 = models.CharField(max_length=150, null=True, blank=True)
    intro = models.TextField(max_length=1000, null=True, blank=True)
    summary = models.TextField(max_length=1000, null=True, blank=True)
    paragraph1 = models.TextField(max_length=1000, null=True, blank=True)
    paragraph2 = models.TextField(max_length=1000, null=True, blank=True)
    paragraph3 = models.TextField(max_length=1000, null=True, blank=True)
    blockqoute1 = models.CharField(max_length=200, null=True, blank=True)
    blockqoute2 = models.CharField(max_length=200, null=True, blank=True)
    blockqoute3 = models.CharField(max_length=200, null=True, blank=True)
    main_image = models.ImageField(
        upload_to=upload_to, blank=True, null=True)
    center_image = models.ImageField(
        upload_to=upload_to, blank=True, null=True)
    cover_image = models.ImageField(
        upload_to=upload_to, blank=True, null=True)
    video = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    has_video = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# BLOG COMMENT MODEL
class BlogPostComment(models.Model):
    # author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=150, blank=True, null=True)
    blog_post = models.ForeignKey(
        BlogPost, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    comment = models.TextField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
