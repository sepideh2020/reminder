from django.urls import path

from apps.todo.views import ListCategory, ListTaskCategory, ListTask, AddTask, AddCategory, DetailTask

urlpatterns = [
    path('category_list/', ListCategory.as_view(), name='categorylist'),
    path('task_list/', ListTask.as_view(), name='tasklist'),
    path('<int:pk>/', ListTaskCategory.as_view(), name='list_task_category'),
    path('add_task/', AddTask.as_view(), name='addtask'),
    path('add_category/', AddCategory.as_view(), name='addcategory'),
    path('task_list/<int:pk>/', DetailTask.as_view(), name='taskdetail'),

]
