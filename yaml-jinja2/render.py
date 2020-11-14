import argparse
from pathlib import Path

from jinja2 import Template

import helpers

parser = argparse.ArgumentParser(
    description="Render Jinja2 templates based on a YAML model."
)
parser.add_argument("exercise", help="Name of the exercise, e.g. ex1")
args = parser.parse_args()
exercise = args.exercise

j2_template = helpers.load_jinja2_template(f"{exercise}.j2")
yaml_model = helpers.load_yaml_data_model(Path("vars", f"{exercise}.yml"))


def render_config(j2_template: Template, yaml_model: dict) -> str:
    """Renders output based on a YAML data model and a
    Jinja2 template.

    Args:
        j2_template (Template): e.g. templates/ex1.j2
        yaml_data (dict): e.g. vars/ex1.yml

    Returns:
        str
    """
    return j2_template.render(yaml_model)


if __name__ == "__main__":
    output = render_config(j2_template, yaml_model)
    print(output)
