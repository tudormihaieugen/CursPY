from django.contrib import admin
from django.urls import path, include

from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
)

urlpatterns = [
    path('', post_list, name='list'),
    path('create/', post_create),
    path('<slug:slug>/', post_detail, name='detail'),
    path('<slug:slug>/edit/', post_update, name='update'),
    path('<slug:slug>/delete/', post_delete),
]
