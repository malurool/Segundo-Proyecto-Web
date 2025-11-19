from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import GameViewSet, RegisterView

router = DefaultRouter()
router.register(r'games', GameViewSet)

urlpatterns = router.urls + [
    path('register/', RegisterView.as_view()),
]
