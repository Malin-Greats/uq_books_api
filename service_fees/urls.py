from django.urls import path
from . import views
from .views import BookSizeUpdate, InteriorColorUpdate, PaperTypeUpdate, BindingOptionUpdate, CoverFinishUpdate, PageUpdate, BookSizeUpdate

urlpatterns = [


    path('interior_colors_list', views.interior_colors_list,
         name='interior_colors_list'),
    path('paper_type_list', views.paper_type_list,
         name='paper_type_list'),
    path('binding_options_list', views.binding_options_list,
         name='binding_options_list'),
    path('cover_finish_list', views.cover_finish_list,
         name='cover_finish_list'),
    path('pages_list', views.pages_list,
         name='pages_list'),
    path('book_size_list', views.book_size_list,
         name='book_size_list'),


    path('interior_color_update/<str:pk>',
         InteriorColorUpdate.as_view(), name='interior_color_update'),
    path('paper_type_update/<str:pk>',
         PaperTypeUpdate.as_view(), name='paper_type_update'),
    path('binding_options_update/<str:pk>',
         BindingOptionUpdate.as_view(), name='binding_options_update'),
    path('cover_finish_update/<str:pk>',
         CoverFinishUpdate.as_view(), name='cover_finish_update'),
    path('page_update/<str:pk>',
         PageUpdate.as_view(), name='page_update'),
    path('book_size_update/<str:pk>',
         BookSizeUpdate.as_view(), name='book_size_update')


]
