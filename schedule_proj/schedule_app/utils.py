

def create_user_data_path(person, filename: str) -> str:
    return f'users_data/{person.user.email}/{filename}'

def templates(template, filename: str) -> str:
    return f'templates/{template.title}' if template.folder_name else f'templates/{template.folder_name}/{template.title}'