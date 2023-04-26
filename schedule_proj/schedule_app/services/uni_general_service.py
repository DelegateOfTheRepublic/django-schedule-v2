from typing import Dict, Iterable, List
from django.http import QueryDict
from schedule_app.models import Link, Template, Folder, Role, LinkPlatform, Subject, StudyGroup

class RoleService:
    def get_all(self) -> Iterable[Role]:
        return Role.objects.all()

class FolderService:
    def get_all(self) -> Iterable[Folder]:
        return Folder.objects.all()

    def create_folder(self, validate_data: Dict) -> Folder:
        return Folder.objects.create(**validate_data)

    def update_folder(self, instance: Folder, validate_data: Dict) -> int:
        return Folder.objects.filter(pk=instance.pk).update(**validate_data)

class LinkPlatformService:
    def get_all(self) -> Iterable[LinkPlatform]:
        return LinkPlatform.objects.all()

    def get_one(self, pk: int) -> LinkPlatform | None:
        return LinkPlatform.objects.filter(pk=pk).first()

    def create_link_plt(self, validate_data: Dict) -> LinkPlatform | None:
        short_name: str = validate_data.get('short_name', None)

        if short_name is None:
            validate_data['short_name'] = validate_data['name'].lower()

        return LinkPlatform.objects.create(**validate_data)

    def update_link_plt(self, instance: LinkPlatform, validate_data: Dict) -> int:
        return LinkPlatform.objects.filter(pk=instance.pk).update(**validate_data)

class LinkService:
    def get_all(self) -> Iterable[Link]:
        return Link.objects.all()

    def get_one(self, pk:int) -> Link | None:
        return Link.objects.filter(pk=pk).first()

    def create_link(self, validate_data: Dict) -> Link | None:
        return Link.objects.create(**validate_data)

    def update_link(self, instance: Link, validate_data: Dict) -> int:
        return Link.objects.filter(pk=instance.pk).update(**validate_data)

class TemplateService:
    def get_all(self) -> Iterable[Template]:
        return Template.objects.all()

    def get_one(self, pk:int) -> Template | None:
        return Template.objects.filter(pk=pk).first()

    def create_template(self, validate_data: Dict) -> Template | None:
        return Template.objects.create(**validate_data)

    def update_template(self, instance: Template, validate_data: Dict) -> int:
        return Template.objects.filter(pk=instance.pk).update(**validate_data)