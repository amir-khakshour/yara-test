from rest_framework import serializers

from misc_api.utils import PhoneValidator
from misc_api.models import UserPurchaseHistory


class UserPurchaseHistorySerializer(serializers.ModelSerializer):
    def validate(self, data):
        PhoneValidator()(data['phone_number'])  # check by django validator not by re.match
        return data

    class Meta:
        model = UserPurchaseHistory
        fields = '__all__'  # for the sake of simplicity :)

