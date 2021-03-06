from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.fields import CharField

from agricultores.models import Department, District, Region, Supply, Advertisement, LinkedTo, Publish, Order


class RelatedFieldAlternative(serializers.PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = kwargs.pop('serializer', None)
        if self.serializer is not None and not issubclass(self.serializer, serializers.Serializer):
            raise TypeError('"serializer" is not a valid serializer class')

        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False if self.serializer else True

    def to_representation(self, instance):
        if self.serializer:
            return self.serializer(instance, context=self.context).data
        return super().to_representation(instance)


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']


class DistrictSerializer(serializers.ModelSerializer):
    region = RegionSerializer()
    department = DepartmentSerializer()

    class Meta:
        model = District
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    district = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'phone_number',
            'email',
            'first_name',
            'last_name',
            'profile_picture_URL',
            'RUC',
            'DNI',
            'district',
            'latitude',
            'longitude',
            'is_advertiser',
            'role',
            'is_verified',
            'password'
        ]
        extra_kwargs = {
            'number_of_credits': {'read_only': True}
        }

    def create(self, validated_data):
        user = get_user_model().objects.create(
            phone_number=validated_data['phone_number'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            DNI=validated_data['DNI'],
            RUC=validated_data['RUC'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def get_district(self, obj):
        if obj.district is None:
            return ""
        return obj.district.name + ', ' + obj.district.region.name + ' (' + obj.district.department.name + ')'


class SuppliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply
        fields = '__all__'


class AdvertisementSerializer(serializers.ModelSerializer):
    region = RegionSerializer()
    department = DepartmentSerializer()
    district = DistrictSerializer()
    class Meta:
        model = Advertisement
        fields = '__all__'


class AdressedToSerializer(serializers.ModelSerializer):
    advertisement = AdvertisementSerializer()
    supply = SuppliesSerializer()
    class Meta:
        model = LinkedTo
        fields = '__all__'


class PublishSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    supplies = RelatedFieldAlternative(queryset=Supply.objects.all(), serializer=SuppliesSerializer)
    user_phone_number = serializers.SerializerMethodField()

    class Meta:
        model = Publish
        fields = '__all__'

    def get_user_phone_number(self, obj):
        return obj.user.phone_number.as_e164


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    supplies = RelatedFieldAlternative(queryset=Supply.objects.all(), serializer=SuppliesSerializer)
    user_phone_number = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_user_phone_number(self, obj):
        return obj.user.phone_number.as_e164
