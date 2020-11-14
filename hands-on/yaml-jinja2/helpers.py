from pathlib import Path

from ansible_collections.ansible.netcommon.plugins.filter.ipaddr import ipaddr

from jinja2 import Template, FileSystemLoader, Environment
from yaml import safe_load


def load_jinja2_template(template: str) -> Template:
    """Loads and returns a Jinja2 template

    Args:
        template (str): Name of the Jinja2 template within the templates directory.

    Returns:
        Template: Jinja2 template with trim_blocks and
        l_strickblocks set to True.
    """
    loader = FileSystemLoader("templates")
    env = Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
    env.filters["ipaddr"] = ipaddr
    return env.get_template(template)


def load_yaml_data_model(data: Path) -> dict:
    """Loads a YAML file from a specific file location and returns its
    contents as a dictionary.

    Args:
        data (Path): File location of the YAML data model.
        Starting from the root directory.

    Returns:
        dict
    """
    with open(data) as fp:
        return safe_load(fp)
