
def default_platform_icon_path(link_platform, filename: str) -> str:
    return f'platform_icons/{link_platform.short_name.lower()}.svg'

def create_user_data_path(person, filename: str) -> str:
    return f'users_data/{person.user.email}/{filename}'

def templates(template, filename: str) -> str:
    return f'templates/{filename}' if not template.folder else f'templates/{template.folder.name}/{filename}'