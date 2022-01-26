from django.contrib import admin
from django.urls import include,path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('photo/in/',views.photoin),
    path('dummy/',views.dummy),
    path('photo/out/',views.photoout),
    path('phototest/',views.phototest),
    path('',views.homepage),
    path('crowd/syokuji/',views.syokuji),
    path('crowd/kyukei/',views.kyukei),
    path('crowd/pc/',views.pc),
    path('ai/',views.ai),
    path('menu/green/',views.menu_green),
    path('menu/ikuta/',views.menu_ikuta),
    path('api/',views.api),
    path('resultprocessing/',include('resultprocessing.urls'))
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
