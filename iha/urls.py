from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListIHAView.as_view(), name="list-iha"),
    path("add/", views.AddIHAView.as_view(), name="add-iha"),
    path("update/<int:id>/", views.UpdateIHAView.as_view(), name="update-iha"),
    path("delete/<int:id>/", views.DeleteIHAView.as_view(), name="delete-iha"),

    path("all/", views.IHADataView.as_view(), name="all-iha-data"),
    path("user-actions/", views.UserActionsListView.as_view(), name="user-actions-list"),
    path("user-actions-data/", views.UserActionsDataView.as_view(), name="user-actions-data"),
]
