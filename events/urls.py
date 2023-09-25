from django.urls import path

from .views import (
    EventCreateView,
    EventListView,
    EventUpdateView,
    EventDetailView,
    EventDeleteView,
    UpdateEventStatusView,
    CompleteEventList,
    search_event,
    create_event,
)

urlpatterns = [
    path('event-create/', EventCreateView.as_view(), name='event-create'),
    path('event-list/', EventListView.as_view(), name='event-list'),
    path('event/<int:pk>/edit/', EventUpdateView.as_view(), name='event-edit'),
    path('detail/<int:pk>', EventDetailView.as_view(), name='event-detail'),
    path('delete/<int:pk>', EventDeleteView.as_view(), name='event-delete'),
    path('update-status/<int:pk>/event/', UpdateEventStatusView.as_view(), name='update-event-status'),
    path('complete-event/', CompleteEventList.as_view(), name='complete-event'),
    path('search_event/', search_event, name='search-event'),
    path('create/', create_event, name='create'),
]