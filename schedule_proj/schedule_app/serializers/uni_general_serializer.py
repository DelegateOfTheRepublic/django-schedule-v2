from rest_framework import serializers
from schedule_app.models import Link, LinkPlatform, StudyGroup, Template, Role, Person, Folder
from schedule_app.utils import default_platform_icon_path

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class LinkPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkPlatform
        fields = '__all__'

class LinkSerializer(serializers.ModelSerializer):
    person_id = serializers.PrimaryKeyRelatedField(source='person', queryset=Person.objects.all(), write_only=True)
    person = serializers.CharField(read_only=True)
    study_group_id = serializers.PrimaryKeyRelatedField(source='study_group', queryset=StudyGroup.objects.all(), write_only=True)
    study_group = serializers.CharField(read_only=True)
    platform_id = serializers.PrimaryKeyRelatedField(source='platform', queryset=LinkPlatform.objects.all(), write_only=True)
    platform = serializers.CharField(read_only=True)

    class Meta:
        model = Link
        fields = '__all__'

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = '__all__'

class TemplateSerializer(serializers.ModelSerializer):
    folder_id = serializers.PrimaryKeyRelatedField(source='folder', queryset=Folder.objects.all(), write_only=True)
    folder = serializers.CharField(read_only=True)

    class Meta:
        model = Template
        fields = '__all__'