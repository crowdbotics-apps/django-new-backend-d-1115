from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    BVVVVViewSet,
    CustomTextViewSet,
    FRFRFRViewSet,
    GffffViewSet,
    GGGGViewSet,
    HomePageViewSet,
    R1ViewSet,
    R2ViewSet,
    R3ViewSet,
    R4ViewSet,
    R6ViewSet,
    TGGGGViewSet,
)

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
    HomePageViewSet,
    CustomTextViewSet,
    AppReportView,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, base_name="signup")
router.register("login", LoginViewSet, base_name="login")
router.register("customtext", CustomTextViewSet)
router.register("homepage", HomePageViewSet)
router.register("r1", R1ViewSet)
router.register("r2", R2ViewSet)
router.register("r3", R3ViewSet)
router.register("r4", R4ViewSet)
router.register("r6", R6ViewSet)
router.register("bvvvv", BVVVVViewSet)
router.register("gggg", GGGGViewSet)
router.register("tgggg", TGGGGViewSet)
router.register("gffff", GffffViewSet)
router.register("frfrfr", FRFRFRViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("report", AppReportView.as_view(), name="app_report"),
]
