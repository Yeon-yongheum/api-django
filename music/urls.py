from django.urls import path
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = 'musics'


schema_view = get_schema_view(
   openapi.Info(
      title="Music API",
      default_version='v1',
      description="Music, Artist 정보",
   ),
)

urlpatterns = [
    path('musics/', views.index, name='index'),
    path('musics/<int:music_pk>/', views.detail, name='detail'),
    path('musics/<int:music_pk>/reviews/', views.review_create, name='review_create'),
    path('reviews/<int:review_pk>/', views.review_update_delete, name='review_update_delete'),
    path('artists/', views.artist_index, name='artist_index'),
    path('artists/<int:artist_pk>/', views.artist_detail, name='artist_detail'),

    path('redoc/', schema_view.with_ui('redoc'), name='schema-redoc'),
    path('swagger/', schema_view.with_ui('swagger'), name='schema-swagger-ui'),
]
