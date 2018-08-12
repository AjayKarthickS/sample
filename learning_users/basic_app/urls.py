from django.conf.urls import url
from basic_app import views

#TEMPLATE URLs
app_name = 'basic_app'

urlpatterns = [
    url(r'^base/$',views.base,name='base'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]
