from django.urls import path
from .views import MyTokenObtainPairView, AuthorProfileUpdate, AuthorProfilePictureUpdate, AuthorAddressUpdate, BookPrintUpdate, BookPrintPdfUpdate, BookPrintCoverUpdate, BookPublishUpdate, BookPublishPdfUpdate, BookPublishCoverUpdate, StoreBookUpdate, StoreBookPdfUpdate, StoreBookCoverUpdate, BookCopyrightUpdate, BookContributorUpdate, BookPayeeUpdate, BookReviewUpdate, BlogPostUpdate, BlogPostMainImageUpdate, BlogPostCenterImageUpdate, BlogPostCoverImageUpdate, BlogPostCommentUpdate
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [

    path('author-profile-list', views.author_profile_list,
         name='author-profile-list'),
    path('author-profile-detail/<str:pk>', views.author_profile_detail,
         name='author-profile-detail'),

    path('author-address-list', views.author_address_list,
         name='author-address-list'),
    path('author-address-detail', views.author_address_detail,
         name='author-address-detail'),

    path('book-contributor-list', views.book_contributor_list,
         name='book-contributor-list'),
    path('book-contributor-detail', views.book_contributor_detail,
         name='book-contributor-detail'),

    path('book-copyright-list', views.book_copyright_list,
         name='book-copyright-list'),
    path('book-copyright-detail', views.book_copyright_detail,
         name='book-copyright-detail'),

    path('book-payee-list', views.book_payee_list, name='book-payee-list'),
    path('book-payee-detail', views.book_payee_detail, name='book-payee-detail'),

    path('book-print-list', views.book_print_list, name='book-print-list'),
    path('book-print-detail', views.book_print_detail, name='book-print-detail'),

    path('book-publish-list', views.book_publish_list, name='book-publish-list'),
    path('book-publish-detail', views.book_publish_detail,
         name='book-publish-detail'),

    path('book-review-list', views.book_review_list, name='book-review-list'),
    path('book-review-detail', views.book_review_detail, name='book-review-detail'),

    path('store-book-list', views.store_book_list, name='store-book-list'),
    path('store-book-detail', views.store_book_detail, name='store-book-detail'),

    path('blog-post-list', views.blog_post_list, name='blog-post-list'),
    path('blog-post-detail', views.blog_post_detail, name='blog-post-detail'),



    path('author-profile-update/<str:pk>',
         AuthorProfileUpdate.as_view(), name='author-profile-update'),
    path('author-profile-picture-update/<str:pk>',
         AuthorProfilePictureUpdate.as_view(), name='author-profile-picture-update'),
    path('author-address-update/<str:pk>',
         AuthorAddressUpdate.as_view(), name='author-address-update'),
    path('book-print-update/<str:pk>',
         BookPrintUpdate.as_view(), name='book-print-update'),
    path('book-print-pdf-update/<str:pk>',
         BookPrintPdfUpdate.as_view(), name='book-print-pdf-update'),
    path('book-print-cover-update/<str:pk>',
         BookPrintCoverUpdate.as_view(), name='book-print-cover-update'),
    path('book-publish-update/<str:pk>',
         BookPublishUpdate.as_view(), name='book-publish-update'),
    path('book-publish-pdf-update/<str:pk>',
         BookPublishPdfUpdate.as_view(), name='book-publish-pdf-update'),
    path('book-publish-cover-update/<str:pk>',
         BookPublishCoverUpdate.as_view(), name='book-publish-cover-update'),
    path('store-book-update/<str:pk>',
         StoreBookUpdate.as_view(), name='store-book-update'),
    path('store-book-pdf-update/<str:pk>',
         StoreBookUpdate.as_view(), name='store-book-pdf-update'),
    path('store-book-cover-update/<str:pk>',
         StoreBookUpdate.as_view(), name='store-book-cover-update'),
    path('book-copyright-update/<str:pk>',
         BookCopyrightUpdate.as_view(), name='book-copyright-update'),
    path('book-contributor-update/<str:pk>',
         BookContributorUpdate.as_view(), name='book-contributor-update'),
    path('book-payee-update/<str:pk>',
         BookPayeeUpdate.as_view(), name='book-payee-update'),
    path('book-review-update/<str:pk>',
         BookReviewUpdate.as_view(), name='book-review-update'),
    path('blogpost-update/<str:pk>',
         BlogPostUpdate.as_view(), name='blogpost-update'),
    path('blogpost-main-image-update/<str:pk>',
         BlogPostMainImageUpdate.as_view(), name='blogpost-main-image-update'),
    path('blogpost-center-image-update/<str:pk>',
         BlogPostCenterImageUpdate.as_view(), name='blogpost-center-image-update'),
    path('blogpost-cover-image-update/<str:pk>',
         BlogPostCoverImageUpdate.as_view(), name='blogpost-cover-image-update'),
    path('blogpost-comment-update/<str:pk>',
         BlogPostCommentUpdate.as_view(), name='blogpost-comment-update'),



    path('delete-author-profile/<str:pk>',
         views.delete_author_profile, name='delete-author-profile'),
    path('delete-author-address/<str:pk>',
         views.delete_author_address, name='delete-author-address'),
    path('delete-book-print/<str:pk>',
         views.delete_book_print, name='delete-book-print'),
    path('delete-book-publish/<str:pk>',
         views.delete_book_publish, name='delete-book-publish'),
    path('delete-store-book/<str:pk>',
         views.delete_store_book, name='delete-store-book'),
    path('delete-book-copyright/<str:pk>',
         views.delete_book_copyright, name='delete-book-copyright'),
    path('delete-book-contributor/<str:pk>',
         views.delete_book_contributor, name='delete-book-contributor'),
    path('delete-book-payee/<str:pk>',
         views.delete_book_payee, name='delete-book-payee'),
    path('delete-book-review/<str:pk>',
         views.delete_book_review, name='delete-book-review'),
    path('delete-blogpost/<str:pk>',
         views.delete_blog_post, name='delete-blogpost'),
    path('delete-blogpost-comment/<str:pk>',
         views.delete_blog_post_comment, name='delete-blogpost-comment'),



    path('add-book-publish', views.addBookPublish, name="add-book-publish"),
    path('add-book-print', views.addBookPrint, name="add-book-print"),
    path('add-book-copyright', views.addBookCopyright, name="add-book-copyright"),
    path('add-book-contributor', views.addBookContributor,
         name="add-book-contributor"),



    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
