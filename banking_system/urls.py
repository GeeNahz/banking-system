from django.contrib import admin
from django.urls import include, path

from apps.home.views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('apps.accounts.urls', namespace='accounts')),
    path('admin/', admin.site.urls),
    path(
        'transactions/',
        include('apps.transactions.urls', namespace='transactions')
    )
]
