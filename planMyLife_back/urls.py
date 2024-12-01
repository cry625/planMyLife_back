from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 事件接口
    path('events/add', views.add_event, name='add_event'),
    path('events', views.get_events, name='get_events'),
    path('events/<int:event_id>', views.get_event, name='get_event'),
    path('events/<int:event_id>/update', views.update_event, name='update_event'),
    path('events/<int:event_id>/delete', views.delete_event, name='delete_event'),
]
