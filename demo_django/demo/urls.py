from django.conf.urls import url

from demo_django.demo.views import DemoView

app_name = "demo"
urlpatterns = [
    url(r'^$', DemoView.as_view()),
]
