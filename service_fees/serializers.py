from rest_framework.serializers import ModelSerializer
from .models import BindingOption, BookSize, CoverFinish, InteriorColor, Page, PaperType


class BindingOptionSerializer(ModelSerializer):
    class Meta:
        model = BindingOption
        fields = '__all__'


class BookSizeSerializer(ModelSerializer):
    class Meta:
        model = BookSize
        fields = '__all__'


class CoverFinishSerializer(ModelSerializer):
    class Meta:
        model = CoverFinish
        fields = '__all__'


class InteriorColorSerializer(ModelSerializer):
    class Meta:
        model = InteriorColor
        fields = '__all__'


class PageSerializer(ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'


class PaperTypeSerializer(ModelSerializer):
    class Meta:
        model = PaperType
        fields = '__all__'
