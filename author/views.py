from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import filters
from datetime import datetime
from django.contrib.humanize.templatetags.humanize import naturalday
from django.contrib.humanize.templatetags.humanize import naturaltime


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from .models import AuthorProfile, AuthorAddress, BookContributor, BookCopyright, BookPayee, BookPrint, BookPublish, BookReview, StoreBook, BlogPost, BlogPostComment
from .serializers import AuthorProfileSerializer, AuthorAddressSerializer, BookContributorSerializer, BookCopyrightSerializer, BookPayeeSerializer, BookPrintSerializer, BookPublishSerializer, BookReviewSerializer, StoreBookSerializer, BlogPostSerializer, BlogPostCommentSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # custom claims
        token['username'] = user.username
        token['phone'] = user.profile.phone
        token['email'] = user.email
        token['id'] = user.id
        token['is_staff'] = user.is_staff

        # token['profile_image'] = user.profile.profile_image
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/author/token',
        'author/token/refresh'
    ]
    return Response(routes)


##### AUTHOR APP GET REQUESTS #####

# GET ALL AUTHORS

@api_view(['GET'])
def author_profile_list(request):
    if request.method == 'GET':
        qs = AuthorProfile.objects.all().order_by('-created_at')
        serializer = AuthorProfileSerializer(qs, many=True)
        return Response(serializer.data)

# GET AUTHOR BY ID


@api_view(['GET'])
def author_profile_detail(request, pk):
    if request.method == 'GET':
        qs = AuthorProfile.objects.get(id=pk)
        serializer = AuthorProfileSerializer(qs)
        return Response(serializer.data)


# GET ALL ADDRESSES
@api_view(['GET'])
def author_address_list(request):
    if request.method == 'GET':
        qs = AuthorAddress.objects.all()
        serializer = AuthorAddressSerializer(qs, many=True)
        return Response(serializer.data)


# GET ADDRESS BY ID
@api_view(['GET'])
def author_address_detail(request, pk):
    if request.method == 'GET':
        qs = AuthorAddress.objects.get(id=pk)
        serializer = AuthorAddressSerializer(qs)
        return Response(serializer.data)


# GET ALL CONTRIBUTORS
@api_view(['GET'])
def book_contributor_list(request):
    if request.method == 'GET':
        qs = BookContributor.objects.all()
        serializer = BookContributorSerializer(qs, many=True)
        return Response(serializer.data)


# GET CONTRIBUTOR DETAILS BY ID
@api_view(['GET'])
def book_contributor_detail(request, pk):
    if request.method == 'GET':
        qs = BookContributor.objects.get(id=pk)
        serializer = BookContributorSerializer(qs)
        return Response(serializer.data)


# GET ALL BOOKS COPYRIGHTS
@api_view(['GET'])
def book_copyright_list(request):
    if request.method == 'GET':
        qs = BookCopyright.objects.all()
        serializer = BookCopyrightSerializer(qs, many=True)
        return Response(serializer.data)


# GET BOOK COPYRIGHTS BY ID
@api_view(['GET'])
def book_copyright_detail(request, pk):
    if request.method == 'GET':
        qs = BookCopyright.objects.get(id=pk)
        serializer = BookCopyrightSerializer(qs)
        return Response(serializer.data)


# GET ALL BOOK PAYEES
@api_view(['GET'])
def book_payee_list(request):
    if request.method == 'GET':
        qs = BookPayee.objects.all()
        serializer = BookPayeeSerializer(qs, many=True)
        return Response(serializer.data)


# GET BOOK PAYEE BY ID
@api_view(['GET'])
def book_payee_detail(request, pk):
    if request.method == 'GET':
        qs = BookPayee.objects.get(id=pk)
        serializer = BookPayeeSerializer(qs)
        return Response(serializer.data)


# GET ALL BOOKS UNDER PRINT
@api_view(['GET'])
def book_print_list(request):
    if request.method == 'GET':
        qs = BookPrint.objects.all()
        serializer = BookPrintSerializer(qs, many=True)
        return Response(serializer.data)


# GET BOOK PRINT BY ID
@api_view(['GET'])
def book_print_detail(request, pk):
    if request.method == 'GET':
        qs = BookPrint.objects.get(id=pk)
        serializer = BookPrintSerializer(qs)
        return Response(serializer.data)


# GET ALL BOOKS UNDER PUBLISH
@api_view(['GET'])
def book_publish_list(request):
    if request.method == 'GET':
        qs = BookPublish.objects.all()
        print(qs)
        serializer = BookPublishSerializer(qs, many=True)
        return Response(serializer.data)


# GET BOOK UNDER PUBLISH BY ID
@api_view(['GET'])
def book_publish_detail(request, pk):
    if request.method == 'GET':
        qs = BookPublish.objects.get(id=pk)
        serializer = BookPublishSerializer(qs)
        return Response(serializer.data)


# GET ALL BOOK REVIEWS
@api_view(['GET'])
def book_review_list(request):
    if request.method == 'GET':
        qs = BookReview.objects.all()
        serializer = BookReviewSerializer(qs, many=True)
        return Response(serializer.data)


# GET A REVIEW BY ID
@api_view(['GET'])
def book_review_detail(request, pk):
    if request.method == 'GET':
        qs = BookReview.objects.get(id=pk)
        serializer = BookReviewSerializer(qs)
        return Response(serializer.data)


# GET ALL BOOK FOR STORE
@api_view(['GET'])
def store_book_list(request):
    if request.method == 'GET':
        qs = StoreBook.objects.all()
        serializer = StoreBookSerializer(qs, many=True)
        return Response(serializer.data)


# GET STORE BOOK BY ID
@api_view(['GET'])
def store_book_detail(request, pk):
    if request.method == 'GET':
        qs = StoreBook.objects.get(id=pk)
        serializer = StoreBookSerializer(qs)
        return Response(serializer.data)

# GET ALL BLOG POST


@api_view(['GET'])
def blog_post_list(request):
    if request.method == 'GET':
        qs = BlogPost.objects.all()
        serializer = BlogPostSerializer(qs, many=True)
        return Response(serializer.data)


# GET BLOG POST BY ID
@api_view(['GET'])
def blog_post_detail(request, pk):
    if request.method == 'GET':
        qs = BlogPost.objects.get(id=pk)
        serializer = BlogPostSerializer(qs)
        return Response(serializer.data)


##### AUTHOR APP POST REQUESTS #####


# ADD A BOOK FOR PUBLISH
@api_view(['POST'])
def addBookPublish(request):
    serializer = BookPublishSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response('serializer not valid')
    return Response(serializer.data)


# ADD A BOOK FOR PRINT
@api_view(['POST'])
def addBookPrint(request):
    serializer = BookPrintSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response('serializer not valid')
    return Response(serializer.data)

# ADD A BOOK FOR PUBLISH COPYRIGHT


@api_view(['POST'])
def addBookCopyright(request):
    serializer = BookCopyrightSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response('serializer not valid')
    return Response(serializer.data)


# ADD A BOOK CONTRIBUTOR
@api_view(['POST'])
def addBookContributor(request):
    serializer = BookContributorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response('serializer not valid')
    return Response(serializer.data)


##### AUTHOR APP PATCH REQUESTS #####

class AuthorProfileUpdate(APIView):
    def patch(self, request, pk):
        author_profile = AuthorProfile.objects.get(id=pk)
        data = request.data

        author_profile.name = data.get('name', author_profile.name)
        author_profile.email = data.get('email', author_profile.email)
        author_profile.phone = data.get('phone', author_profile.phone)

        author_profile.save()
        serializer = AuthorProfileSerializer(author_profile)
        return Response(serializer.data)


class AuthorProfilePictureUpdate(APIView):
    def patch(self, request, pk):
        author_profile = AuthorProfile.objects.get(id=pk)
        data = request.data

        author_profile.profile_picture = data.get(
            'profile_picture', author_profile.profile_picture)

        author_profile.save()
        serializer = AuthorProfileSerializer(author_profile)
        return Response(serializer.data)


class AuthorAddressUpdate(APIView):
    def patch(self, request, pk):
        author_address = AuthorAddress.objects.get(id=pk)
        data = request.data

        author_address.building = data.get('building', author_address.building)
        author_address.street = data.get('street', author_address.street)
        author_address.city = data.get('city', author_address.city)
        author_address.country = data.get('country', author_address.country)
        author_address.postal_code = data.get(
            'postal_code', author_address.postal_code)
        author_address.isDefault = data.get(
            'isDefault', author_address.isDefault)

        author_address.save()
        serializer = AuthorAddressSerializer(author_address)
        return Response(serializer.data)


class BookPrintUpdate(APIView):
    def patch(self, request, pk):
        book_print = BookPrint.objects.get(id=pk)
        data = request.data

        book_print.title = data.get('title', book_print.title)
        book_print.description = data.get(
            'description', book_print.description)
        book_print.language = data.get('language', book_print.language)
        book_print.category = data.get('category', book_print.category)
        book_print.pages = data.get('pages', book_print.pages)
        book_print.price = data.get('price', book_print.price)
        book_print.size = data.get('size', book_print.size)
        book_print.color = data.get('color', book_print.color)
        book_print.binding = data.get('binding', book_print.binding)
        book_print.isbn = data.get('isbn', book_print.isbn)
        book_print.cover_finish = data.get(
            'cover_finish', book_print.cover_finish)
        book_print.print_cost = data.get('print_cost', book_print.print_cost)
        book_print.queue_status = data.get(
            'queue_status', book_print.queue_status)

        book_print.save()
        serializer = BookPrintSerializer(book_print)
        return Response(serializer.data)


class BookPrintPdfUpdate(APIView):
    def patch(self, request, pk):
        book_print = BookPrint.objects.get(id=pk)
        data = request.data

        book_print.book_pdf = data.get('book_pdf', book_print.book_pdf)

        book_print.save()
        serializer = BookPrintSerializer(book_print)
        return Response(serializer.data)


class BookPrintCoverUpdate(APIView):
    def patch(self, request, pk):
        book_print = BookPrint.objects.get(id=pk)
        data = request.data

        book_print.cover = data.get('cover', book_print.cover)

        book_print.save()
        serializer = BookPrintSerializer(book_print)
        return Response(serializer.data)


class BookPublishUpdate(APIView):
    def patch(self, request, pk):
        book_publish = BookPublish.objects.get(id=pk)
        data = request.data

        book_publish.title = data.get('title', book_publish.title)
        book_publish.description = data.get(
            'description', book_publish.description)
        book_publish.contributor_notes = data.get(
            'contributor_notes', book_publish.contributor_notes)
        book_publish.table_of_contents = data.get(
            'table_of_contents', book_publish.table_of_contents)
        book_publish.language = data.get('language', book_publish.language)
        book_publish.category = data.get('category', book_publish.category)
        book_publish.bisac_category1 = data.get(
            'bisac_category1', book_publish.bisac_category1)
        book_publish.bisac_category2 = data.get(
            'bisac_category2', book_publish.bisac_category2)
        book_publish.bisac_category3 = data.get(
            'bisac_category3', book_publish.bisac_category3)
        book_publish.keywords = data.get('keywords', book_publish.keywords)
        book_publish.audience = data.get('audience', book_publish.audience)
        book_publish.color = data.get('color', book_publish.color)
        book_publish.binding = data.get('binding', book_publish.binding)
        book_publish.paper = data.get('paper', book_publish.paper)
        book_publish.cover_finish = data.get(
            'cover_finish', book_publish.cover_finish)
        book_publish.isbn = data.get('isbn', book_publish.isbn)
        book_publish.pages = data.get('pages', book_publish.pages)
        book_publish.size = data.get('size', book_publish.size)
        book_publish.price = data.get('price', book_publish.price)
        book_publish.global_upload = data.get(
            'global_upload', book_publish.global_upload)
        book_publish.has_explicit_content = data.get(
            'has_explicit_content', book_publish.has_explicit_content)
        book_publish.is_active = data.get('is_active', book_publish.is_active)
        book_publish.is_banned = data.get('is_banned', book_publish.is_banned)
        book_publish.book_pdf = data.get('book_pdf', book_publish.book_pdf)

        book_publish.save()
        serializer = BookPublishSerializer(book_publish)
        return Response(serializer.data)


class BookPublishPdfUpdate(APIView):
    def patch(self, request, pk):
        book_publish = BookPublish.objects.get(id=pk)
        data = request.data

        book_publish.book_pdf = data.get('book_pdf', book_publish.book_pdf)

        book_publish.save()
        serializer = BookPublishSerializer(book_publish)
        return Response(serializer.data)


class BookPublishCoverUpdate(APIView):
    def patch(self, request, pk):
        book_publish = BookPublish.objects.get(id=pk)
        data = request.data

        book_publish.cover = data.get('cover', book_publish.cover)

        book_publish.save()
        serializer = BookPublishSerializer(book_publish)
        return Response(serializer.data)


class StoreBookUpdate(APIView):
    def patch(self, request, pk):
        store_book = StoreBook.objects.get(id=pk)
        data = request.data

        store_book.title = data.get('title', store_book.title)
        store_book.description = data.get(
            'description', store_book.description)

        store_book.language = data.get('language', store_book.language)
        store_book.category = data.get('category', store_book.category)
        store_book.keywords = data.get('keywords', store_book.keywords)
        store_book.audience = data.get('audience', store_book.audience)
        store_book.pages = data.get('pages', store_book.pages)
        store_book.size = data.get('size', store_book.size)
        store_book.price = data.get('price', store_book.price)
        store_book.has_explicit_content = data.get(
            'has_explicit_content', store_book.has_explicit_content)
        store_book.is_approved = data.get(
            'is_approved', store_book.is_approved)

        store_book.save()
        serializer = StoreBookSerializer(store_book)
        return Response(serializer.data)


class StoreBookPdfUpdate(APIView):
    def patch(self, request, pk):
        store_book = StoreBook.objects.get(id=pk)
        data = request.data

        store_book.book_pdf = data.get('book_pdf', store_book.book_pdf)

        store_book.save()
        serializer = StoreBookSerializer(store_book)
        return Response(serializer.data)


class StoreBookCoverUpdate(APIView):
    def patch(self, request, pk):
        store_book = StoreBook.objects.get(id=pk)
        data = request.data

        store_book.cover = data.get('cover', store_book.cover)

        store_book.save()
        serializer = StoreBookSerializer(store_book)
        return Response(serializer.data)


class BookCopyrightUpdate(APIView):
    def patch(self, request, pk):
        book_copyright = BookCopyright.objects.get(id=pk)
        data = request.data

        book_copyright.subtitle = data.get('subtitle', book_copyright.subtitle)
        book_copyright.edition = data.get('edition', book_copyright.edition)
        book_copyright.edition_statement = data.get(
            'edition_statement', book_copyright.edition_statement)
        book_copyright.rights_reserved = data.get(
            'rights_reserved', book_copyright.rights_reserved)
        book_copyright.holder_name = data.get(
            'holder_name', book_copyright.holder_name)

        book_copyright.save()
        serializer = BookCopyrightSerializer(book_copyright)
        return Response(serializer.data)


class BookContributorUpdate(APIView):
    def patch(self, request, pk):
        book_contributor = BookContributor.objects.get(id=pk)
        data = request.data

        book_contributor.first_name = data.get(
            'first_name', book_contributor.first_name)
        book_contributor.last_name = data.get(
            'last_name', book_contributor.last_name)
        book_contributor.role = data.get('role', book_contributor.role)
        book_contributor.email = data.get('email', book_contributor.email)
        book_contributor.phone = data.get('phone', book_contributor.phone)

        book_contributor.save()
        serializer = BookContributorSerializer(book_contributor)
        return Response(serializer.data)


class BookPayeeUpdate(APIView):
    def patch(self, request, pk):
        book_payee = BookPayee.objects.get(id=pk)
        data = request.data

        book_payee.first_name = data.get('first_name', book_payee.first_name)
        book_payee.last_name = data.get('last_name', book_payee.last_name)
        book_payee.email = data.get('email', book_payee.email)
        book_payee.phone = data.get('phone', book_payee.phone)
        book_payee.paypal_email = data.get(
            'paypal_email', book_payee.paypal_email)
        book_payee.is_organization = data.get(
            'is_organization', book_payee.is_organization)

        book_payee.save()
        serializer = BookPayeeSerializer(book_payee)
        return Response(serializer.data)


class BookReviewUpdate(APIView):
    def patch(self, request, pk):
        book_review = BookReview.objects.get(id=pk)
        data = request.data

        book_review.name = data.get('name', book_review.name)
        book_review.email = data.get('email', book_review.email)
        book_review.title = data.get('title', book_review.title)
        book_review.review = data.get('review', book_review.review)
        book_review.rating = data.get('rating', book_review.rating)
        book_review.is_approved = data.get(
            'is_approved', book_review.is_approved)

        book_review.save()
        serializer = BookReviewSerializer(book_review)
        return Response(serializer.data)


class BlogPostUpdate(APIView):
    def patch(self, request, pk):
        blog_post = BlogPost.objects.get(id=pk)
        data = request.data

        blog_post.title = data.get('title', blog_post.title)
        blog_post.category = data.get('category', blog_post.category)
        blog_post.headline = data.get('headline', blog_post.headline)
        blog_post.sub_headline1 = data.get(
            'sub_headline1', blog_post.sub_headline1)
        blog_post.sub_headline2 = data.get(
            'sub_headline2', blog_post.sub_headline2)
        blog_post.sub_headline3 = data.get(
            'sub_headline3', blog_post.sub_headline3)
        blog_post.intro = data.get('intro', blog_post.intro)
        blog_post.summary = data.get('summary', blog_post.summary)
        blog_post.paragraph1 = data.get('paragraph1', blog_post.paragraph1)
        blog_post.paragraph2 = data.get('paragraph2', blog_post.paragraph2)
        blog_post.paragraph3 = data.get('paragraph3', blog_post.paragraph3)
        blog_post.blockqoute1 = data.get('blockqoute1', blog_post.blockqoute1)
        blog_post.blockqoute2 = data.get('blockqoute2', blog_post.blockqoute2)
        blog_post.blockqoute3 = data.get('blockqoute3', blog_post.blockqoute3)
        blog_post.video = data.get('video', blog_post.video)
        blog_post.status = data.get('status', blog_post.status)
        blog_post.is_approved = data.get('is_approved', blog_post.is_approved)
        blog_post.has_video = data.get('has_video', blog_post.has_video)

        blog_post.save()
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data)


class BlogPostMainImageUpdate(APIView):
    def patch(self, request, pk):
        blog_post = BlogPost.objects.get(id=pk)
        data = request.data

        blog_post.main_image = data.get('main_image', blog_post.main_image)

        blog_post.save()
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data)


class BlogPostCenterImageUpdate(APIView):
    def patch(self, request, pk):
        blog_post = BlogPost.objects.get(id=pk)
        data = request.data

        blog_post.center_image = data.get(
            'center_image', blog_post.center_image)

        blog_post.save()
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data)


class BlogPostCoverImageUpdate(APIView):
    def patch(self, request, pk):
        blog_post = BlogPost.objects.get(id=pk)
        data = request.data

        blog_post.cover_image = data.get('cover_image', blog_post.cover_image)

        blog_post.save()
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data)


class BlogPostCommentUpdate(APIView):
    def patch(self, request, pk):
        blog_post_comment = BlogPostComment.objects.get(id=pk)
        data = request.data

        blog_post_comment.name = data.get('name', blog_post_comment.name)
        blog_post_comment.email = data.get('email', blog_post_comment.email)
        blog_post_comment.comment = data.get(
            'comment', blog_post_comment.comment)
        blog_post_comment.title = data.get('title', blog_post_comment.title)

        blog_post_comment.save()
        serializer = BlogPostCommentSerializer(blog_post_comment)
        return Response(serializer.data)


##### AUTHOR APP DELETE REQUESTS #####


@api_view(['DELETE'])
def delete_author_profile(request, pk):
    author_profile = AuthorProfile.objects.get(id=pk)
    author_profile.delete()
    return Response('Author profile deleted successfully')


@api_view(['DELETE'])
def delete_author_address(request, pk):
    author_address = AuthorAddress.objects.get(id=pk)
    author_address.delete()
    return Response('Author address deleted successfully')


@api_view(['DELETE'])
def delete_book_print(request, pk):
    book_print = BookPrint.objects.get(id=pk)
    book_print.delete()
    return Response('Book for print deleted successfully')


@api_view(['DELETE'])
def delete_book_publish(request, pk):
    book_publish = BookPublish.objects.get(id=pk)
    book_publish.delete()
    return Response('Book for publish deleted successfully')


@api_view(['DELETE'])
def delete_store_book(request, pk):
    store_book = StoreBook.objects.get(id=pk)
    store_book.delete()
    return Response('Store book deleted successfully')


@api_view(['DELETE'])
def delete_book_copyright(request, pk):
    book_copyright = BookCopyright.objects.get(id=pk)
    book_copyright.delete()
    return Response('Book copyright deleted successfully')


@api_view(['DELETE'])
def delete_book_contributor(request, pk):
    book_contributor = BookContributor.objects.get(id=pk)
    book_contributor.delete()
    return Response('Book contributor deleted successfully')


@api_view(['DELETE'])
def delete_book_payee(request, pk):
    book_payee = BookPayee.objects.get(id=pk)
    book_payee.delete()
    return Response('Book payee deleted successfully')


@api_view(['DELETE'])
def delete_book_review(request, pk):
    book_review = BookReview.objects.get(id=pk)
    book_review.delete()
    return Response('Book review deleted successfully')


@api_view(['DELETE'])
def delete_blog_post(request, pk):
    blog_post = BlogPost.objects.get(id=pk)
    blog_post.delete()
    return Response('Blog post deleted successfully')


@api_view(['DELETE'])
def delete_blog_post_comment(request, pk):
    blog_post_comment = BlogPostComment.objects.get(id=pk)
    blog_post_comment.delete()
    return Response('Blog post comment deleted successfully')
