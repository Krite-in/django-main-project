from django.urls import include,path
from django.contrib import admin
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('',views.about,name='about'),
    path('',views.account,name='account'),
    path('',views.tour,name='tour'),
    path('',views.gallery,name='gallery'),
    
]

    # path('admin/', admin.site.urls),
    # path('',include('index.urls')),
    # path('about/',include('about.urls')),
    # path('account/',include('account.urls')),
    # path('tour/',include('tour.urls')),
    # path('gallery/',include('gallery.urls')),
    # path('account/dashboard/',include('account/dashboard.urls')),
    # path('account/dashboard/<str>/submit',include('account.dashboard/<str>/submiturls')),
