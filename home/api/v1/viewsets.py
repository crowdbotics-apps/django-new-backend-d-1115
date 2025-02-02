from rest_framework import viewsets
import json
from .serializers import (
    BVVVVSerializer,
    CustomTextSerializer,
    FRFRFRSerializer,
    GffffSerializer,
    GGGGSerializer,
    HomePageSerializer,
    R1Serializer,
    R2Serializer,
    R3Serializer,
    R4Serializer,
    R6Serializer,
    TGGGGSerializer,
)

from django import apps
from django.core.management import call_command
from .permissions import CrowboticsExclusive

from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from home.api.v1.serializers import (
    SignupSerializer,
    CustomTextSerializer,
    HomePageSerializer,
    UserSerializer,
)
from home.models import (
    BVVVV,
    CustomText,
    FRFRFR,
    Gffff,
    GGGG,
    HomePage,
    R1,
    R2,
    R3,
    R4,
    R6,
    TGGGG,
)


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})


class CustomTextViewSet(ModelViewSet):
    serializer_class = CustomTextSerializer
    queryset = CustomText.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = [IsAdminUser]
    http_method_names = ["get", "put", "patch"]


class HomePageViewSet(ModelViewSet):
    serializer_class = HomePageSerializer
    queryset = HomePage.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = [IsAdminUser]
    http_method_names = ["get", "put", "patch"]


class AppReportView(APIView):
    """
    DO NOT REMOVE THIS CODE SNIPPET, YOUR DASHBOARD MAY NOT REFLECT THE CORRECT
    RESOURCES IN YOUR APP.
    """

    permission_classes = [CrowboticsExclusive]

    def _get_models(self):
        project_models = apps.apps.get_models(
            include_auto_created=True, include_swapped=True
        )
        parsed_data = [
            str(model).split(".")[-1].replace("'", "").strip(">")
            for model in project_models
        ]
        return parsed_data

    def _get_urls(self):
        parsed_data = json.loads(call_command("show_urls", format="json"))
        return parsed_data

    def get(self, request):
        return Response(
            {"models": self._get_models(), "urls": self._get_urls()},
            status=status.HTTP_200_OK,
        )


class R1ViewSet(viewsets.ModelViewSet):
    serializer_class = R1Serializer
    queryset = R1.objects.all()


class R2ViewSet(viewsets.ModelViewSet):
    serializer_class = R2Serializer
    queryset = R2.objects.all()


class R3ViewSet(viewsets.ModelViewSet):
    serializer_class = R3Serializer
    queryset = R3.objects.all()


class R4ViewSet(viewsets.ModelViewSet):
    serializer_class = R4Serializer
    queryset = R4.objects.all()


class R6ViewSet(viewsets.ModelViewSet):
    serializer_class = R6Serializer
    queryset = R6.objects.all()


class BVVVVViewSet(viewsets.ModelViewSet):
    serializer_class = BVVVVSerializer
    queryset = BVVVV.objects.all()


class GGGGViewSet(viewsets.ModelViewSet):
    serializer_class = GGGGSerializer
    queryset = GGGG.objects.all()


class TGGGGViewSet(viewsets.ModelViewSet):
    serializer_class = TGGGGSerializer
    queryset = TGGGG.objects.all()


class GffffViewSet(viewsets.ModelViewSet):
    serializer_class = GffffSerializer
    queryset = Gffff.objects.all()


class FRFRFRViewSet(viewsets.ModelViewSet):
    serializer_class = FRFRFRSerializer
    queryset = FRFRFR.objects.all()
