from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

admin.site.site_title = 'Casting'
admin.site.site_header = 'Casting' + ' administration'
admin.site.index_title = 'Administration'

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', include('casting.urls')),

    # admin
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('_adm1n_/', admin.site.urls),

    # translate
    path('_translation_/', include('rosetta.urls')),
)
