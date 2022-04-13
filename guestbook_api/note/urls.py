from django.db import router
from rest_framework.routers import DefaultRouter
from .views import NotesViewSet

router = DefaultRouter();
router.register(r'posts',NotesViewSet)
urlpatterns = router.urls
    


