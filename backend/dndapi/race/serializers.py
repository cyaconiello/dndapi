from rest_framework import serializers

from race.models import Race

class RaceBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = [
            "race_uuid",
            "name",
            "size",
            "speed",
        ]
        
class RaceFullSerializer(RaceBaseSerializer):
    racial_ability_score_increase = serializers.SerializerMethodField(read_only=True)

    class Meta(RaceBaseSerializer.Meta):
        model = Race
        fields =  RaceBaseSerializer.Meta.fields + ['description', 'racial_ability_score_increase']

    def get_racial_ability_score_increase(self, obj: Race):
        data = {
            "strength": obj.strength_ability_increase,
            "dexterity": obj.dexterity_ability_increase,
            "constitution": obj.constitution_ability_increase,
            "intellegince": obj.intellegince_ability_increase,
            "wisdom": obj.wisdom_ability_increase,
            "charisma": obj.charisma_ability_increase,
        }
        return data
