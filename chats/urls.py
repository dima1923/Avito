from .views import UserView,ChatView,MessageView
from rest_framework import routers
from django.urls import path

"""router = routers.DefaultRouter()
router.register('users/add', UserView)
router.register('chats', ChatView)
router.register('messages', MessageView)


urlpatterns = router.urls"""

urlpatterns = [
    path('users/add', UserView.as_view({'post':'create'})),
    path('users/', UserView.as_view({'get':'list'})),
    path('chats/add', ChatView.as_view({'post':'create'})),
    path('chats/', ChatView.as_view({'get':'list'})),
    path('chats/get', ChatView.as_view({'post':'show_chats'})),
    path('messages/',MessageView.as_view({'get':'list'})),
    path('messages/add', MessageView.as_view({'post':'create'})),
    path('messages/get', MessageView.as_view({'post':'show_message'}))
]
