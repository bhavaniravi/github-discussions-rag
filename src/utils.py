def get_project_name_from_github_url(url: str) -> str:
    return url.split("/")[-1]


def get_project_owner_from_github_url(url: str) -> str:
    return url.split("/")[-2]
