from django.contrib import admin
from django.urls import path, include
from chat import views as chat_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', chat_views.landing_page, name='landing'),
    path('', include('chat.urls')),
    path('accounts/', include('accounts.urls')),
]
