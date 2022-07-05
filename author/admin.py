from django.contrib import admin
from .models import AuthorProfile, AuthorAddress, BookContributor, BookCopyright, BookPayee, BookPrint, BookPublish, BookReview, BlogPost, BlogPostComment, StoreBook


@admin.register(AuthorProfile)
class AuthorProfileAdmin(admin.ModelAdmin):
    search_fields = ("name",)

    list_display = ("id", "user", "name", "email", "phone", "profile_picture", "totalRevenue", "currentRevenue", "total_books",
                    "is_active", "is_banned", "created_at", "updated_at")


@admin.register(AuthorAddress)
class AuthorAddressAdmin(admin.ModelAdmin):
    search_fields = ("name",)

    list_display = ("id", "name", "building", "street", "city",
                    "country", "postal_code", "isDefault", "created_at", "updated_at")


@admin.register(BookContributor)
class BookContributorAdmin(admin.ModelAdmin):
    search_fields = ("book",)

    list_display = ("id", "book", "first_name", "last_name",
                    "role", "email", "phone", "created_at", "updated_at")


@admin.register(BookCopyright)
class BookCopyrightAdmin(admin.ModelAdmin):
    search_fields = ("book",)

    list_display = ("id", "book", "subtitle", "edition",
                    "edition_statement", "rights_reserved", "holder", "created_at", "updated_at")


@admin.register(BookPayee)
class BookPayeeAdmin(admin.ModelAdmin):
    search_fields = ("book",)

    list_display = ("id", "author", "book", "first_name", "last_name", "email",
                    "phone", "paypal_email", "is_organization", "created_at", "updated_at")


@admin.register(BookPrint)
class BookPrintAdmin(admin.ModelAdmin):
    search_fields = ("author",)
    list_display = ("id", "author", "title", "description", "language", "category", "book_pdf", "pages", "size", "price", "color",
                    "binding", "isbn", "cover", "cover_finish", "print_cost", "created_at", "updated_at", "queue_status", "is_printed", "is_banned")


@admin.register(BookPublish)
class BookPublishAdmin(admin.ModelAdmin):
    search_fields = ("author",)
    list_display = ("id", "author", "title", "description", "language", "category", "binding", "paper", "cover_finish", "book_pdf", "totalRevenue", "currentRevenue", "pages", "size", "price", "color",
                    "bisac_category1", "bisac_category2", "keywords", "isbn", "cover", "global_upload", "has_explicit_content", "is_active", "is_banned", "created_at", "updated_at")


@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_display = ("id", "name", "email", "book", "title",
                    "review", "rating", "is_approved", "created_at", "updated_at")


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    search_fields = ("author",)
    list_display = ("id", "title", "category", "headline", "sub_headline1", "sub_headline2", "sub_headline3", "intro", "summary", "paragraph1", "paragraph2", "paragraph3",
                    "blockqoute1", "blockqoute2", "blockqoute3", "main_image", "center_image", "cover_image", "video", "status", "has_video", "is_approved", "created_at", "updated_at")


@admin.register(BlogPostComment)
class BlogPostCommentAdmin(admin.ModelAdmin):
    search_fields = ("author",)
    list_display = ("id", "name", "email", "title", "blog_post",
                    "comment", "created_at", "updated_at")


@admin.register(StoreBook)
class StoreBookAdmin(admin.ModelAdmin):
    search_fields = ("author",)
    list_display = ("id", "author", "title", "description", "language", "category", "keywords", "audience",
                    "book_pdf", "pages", "size", "price", "cover", "is_approved", "created_at", "updated_at")
