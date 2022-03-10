from rest_framework import generics

from languages.serializers import LanguageSerializer
from languages.models import Language

# Create your views here.
class LanguagesListCreateView(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class LanguagesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    lookup_field = "language_uuid"
    