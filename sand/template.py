from jinja2 import Environment, FileSystemLoader


def get_environment(templates_dir):
    return Environment(loader=FileSystemLoader(templates_dir))
