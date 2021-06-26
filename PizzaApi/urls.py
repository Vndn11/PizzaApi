from django.urls import path
from . import views
# from .views import CreatePizza
urlpatterns = [
    path('',views.PizzaList),
    path('create',views.CreatePizza),
    path('size/<str:size_id>',views.PizzaList_Size),
    path('type/<str:type_id>',views.PizzaList_Type),
    path('edit/<str:pizza_id>',views.UpdatePizza),
    path('delete/<str:pizza_id>',views.DeletePizza),

    
]