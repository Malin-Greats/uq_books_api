from rest_framework.serializers import ModelSerializer
from .models import AuthorProfile, AuthorAddress, BookContributor, BlogPost, BlogPostComment, BookCopyright, BookPayee, BookPrint, BookPublish, BookReview, StoreBook


class AuthorProfileSerializer(ModelSerializer):
    class Meta:
        model = AuthorProfile
        fields = '__all__'


class AuthorAddressSerializer(ModelSerializer):
    class Meta:
        model = AuthorAddress
        fields = '__all__'


class BookContributorSerializer(ModelSerializer):
    class Meta:
        model = BookContributor
        fields = '__all__'


class BookCopyrightSerializer(ModelSerializer):
    class Meta:
        model = BookCopyright
        fields = '__all__'


class BookPayeeSerializer(ModelSerializer):
    class Meta:
        model = BookPayee
        fields = '__all__'


class BookPrintSerializer(ModelSerializer):
    class Meta:
        model = BookPrint
        fields = '__all__'


class BookPublishSerializer(ModelSerializer):
    class Meta:
        model = BookPublish
        fields = '__all__'


class BookReviewSerializer(ModelSerializer):
    class Meta:
        model = BookReview
        fields = '__all__'


class BlogPostSerializer(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'


class BlogPostCommentSerializer(ModelSerializer):
    class Meta:
        model = BlogPostComment
        fields = '__all__'


class StoreBookSerializer(ModelSerializer):
    class Meta:
        model = StoreBook
        fields = '__all__'
