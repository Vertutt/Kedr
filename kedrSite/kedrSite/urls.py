from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from kedrSite.views import UserConfirmEmailView
from trees.views import TreesAPIList, TreesAPIDetails, TreesAPICoordinates, TreeAPICreate, TreeAPIUpdateDestroy, TreeImageAPI
from promocodes.views import PromocodeConfirmView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/trees/',TreesAPIList.as_view(), name = 'trees'),
    path('api/v1/add_tree/',TreeAPICreate.as_view(), name = 'add tree'),
    path('api/v1/trees_coordinates/',TreesAPICoordinates.as_view(), name = 'trees coordinates'),
    path('api/v1/trees/<int:pk>/',TreesAPIDetails.as_view(), name = 'tree details'),
    path('api/v1/edit_tree/<int:pk>/', TreeAPIUpdateDestroy.as_view()),
    path('api/v1/delete_photo/', TreeImageAPI.as_view()),
    path('api/v1/djoser-auth/', include('djoser.urls')),
    path('api/v1/activate/<str:uid>/<str:token>/', UserConfirmEmailView.as_view()),
    path('api/v1/promocodes/check/<str:promo>/', PromocodeConfirmView.as_view()),
    path('djoser-auth/', include('djoser.urls.authtoken')),
    path('api/v1/djoser-auth/', include('djoser.urls.authtoken')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
