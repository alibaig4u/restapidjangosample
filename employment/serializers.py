from rest_framework import serializers
from employment.models import Employee


class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    address = serializers.CharField(style={'base_template': 'textarea.html'})
    phone_number = serializers.CharField(max_length=100)
    txId = serializers.CharField(max_length=100)


    class Meta:
        model = Employee
        fields = ['id', 'user_name', 'address', 'phone_number', 'txId']

    def create(self, validated_data):
        """
        Create and return a new `Employee` instance, given the validated data.
        """
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Employee` instance, given the validated data.
        """
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.address = validated_data.get('address', instance.address)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.txId = validated_data.get('txId', instance.txId)
        instance.save()
        return instance