from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    # Get all lots belonging to user
    # ex: api/lots/user/<username>
    path('user/<str:username>', views.get_lots, name='get-lots'),

    # Get a lot given an id
    # ex: api/lots/<id>
    path('<int:id>', views.get_lot, name='get-lot'),

    # Update existing build
    # ex: api/lots/<id>/edit
    path('<int:id>/edit', views.update_lot, name='update-lot'),

    # Delete existing lot
    # ex: api/lots/<id>/delete
    path('<int:id>/delete', views.delete_lot, name='delete-lot'),

    # Post a new build
    # ex: api/lots/new
    path('new', views.new_lot, name='new-lot'),
]