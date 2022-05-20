from math import perm
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
# from .views import snippet_list,snippet_detail

#for @apiview
# urlpatterns = [
#     path('snippets/',views.snippet_list),
#     path('snippets/<int:pk>/',views.snippet_detail),
# ]

#for apiview class
urlpatterns = [
    path('snippets/',views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view())#,
    # path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]