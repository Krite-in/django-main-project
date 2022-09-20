from django.urls import include,path
from django.contrib import admin
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('account/',views.account,name='account'),
     path('tour/',views.tour,name='tour'),
    path('gallery/',views.gallery,name='gallery'),
    
]

    # path('admin/', admin.site.urls),
    # path('',include('index.urls')),
    # path('about/',include('about.urls')),
    # path('account/',include('account.urls')),
    # path('tour/',include('tour.urls')),
    # path('gallery/',include('gallery.urls')),
    # path('account/dashboard/',include('account/dashboard.urls')),
    # path('account/dashboard/<str>/submit',include('account.dashboard/<str>/submiturls')),
