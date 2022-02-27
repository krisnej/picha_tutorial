from django.contrib import admin
from django.urls import path

from photos.views import PhotoView
from feedback.views import FeedbackView

urlpatterns = [
    # Examples:
    # url(r'^$', 'picha.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path(r'', PhotoView.as_view(), name="home"),
    path(r'feedback/', FeedbackView.as_view(), name="feedback"),
    path(r'admin/', admin.site.urls),
]
