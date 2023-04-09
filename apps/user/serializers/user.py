from rest_framework import serializers

from user.models.base import User, Position, AssignedDevice
from teams.serializers import ProjectListSerializer


class DayField(serializers.Field):

    def to_representation(self, value):
        if value == 0:
            return "Happy Birthday!!!"
        return "%d day left" % value if value == 1 else "%d days left" % value


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', "image", 'first_name', 'last_name', 'position', 'phone_number', 
                  'telegram', 'birthday', 'work_type', 'project_set', 'employment_type')
        depth = 1
        
    def to_representation(self, instance):
        self.fields['project_set'] = ProjectListSerializer(many=True)
        return super(UserSerializer, self).to_representation(instance)


class UserListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'url', 'first_name', 'last_name', 'position', 'image', 'work_type')
    
    def to_representation(self, instance):
        self.fields['position'] = PositionSerializer(many=True)
        return super(UserListSerializer, self).to_representation(instance)


class BirthdayListSerializer(serializers.HyperlinkedModelSerializer):
    day = DayField()

    class Meta:
        model = User
        fields = ('url', 'id', 'first_name', 'last_name', 'image', 'work_type', 'birthday', 'day')


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', "image", 'first_name', 'last_name', 'position', 'phone_number', 
                  'telegram', 'birthday', 'work_type', 'project_set', 'employment_type', "devices")
        depth = 1
        
    def to_representation(self, instance):
        self.fields['project_set'] = ProjectListSerializer(many=True)
        return super(ProfileSerializer, self).to_representation(instance)


class AssignedDevicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssignedDevice
        fields = '__all__'