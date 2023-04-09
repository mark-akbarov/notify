from rest_framework.routers import DefaultRouter
from notify.views.late import LatenessViewSet
from notify.views.remote import RemoteViewSet
from notify.views.timeoff import TimeoffViewSet
from notify.views.warn import WarnViewSet


router = DefaultRouter()
router.register("lateness", LatenessViewSet, "lateness")
router.register("remote", RemoteViewSet, "remote")
router.register("timeoff", TimeoffViewSet, "timeoff")
router.register("warn", WarnViewSet, "warn")

urlpatterns = router.urls