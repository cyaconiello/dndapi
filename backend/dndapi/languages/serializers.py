from rest_framework import serializers

from languages.models import Language

class LanguageSerializer(serializers.ModelSerializer):
    # print(Language.objects.all().first().language_uuid)
    class Meta:
        model = Language
        fields = [
            'language_uuid',
            'name',
            'description'
        ]