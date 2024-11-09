from rest_framework.routers import DefaultRouter
from .views import AppViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'apps', AppViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = router.urls
