from django.contrib import admin
from django.urls import path, include
from firstapp import views
from service import views as serviceViews
from record import views as recordViews
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', TemplateView.as_view(template_name="home.html")),
    path('info/<int:info_id>', serviceViews.info),
    path('record/<int:record_id>', recordViews.record),
    path('account/', include('account.urls'))
]

handler404 = views.page_not_found_view

