from pprint import pprint

import argparse
from yaml import safe_load
from jinja2 import Template

parser = argparse.ArgumentParser(description="Generate config.")
parser.add_argument("yaml_file", type=str, help="YAML file")
parser.add_argument("j2_file", type=str, help="Jinja2 file")


args = parser.parse_args()


with open(args.yaml_file) as fp:
    y = safe_load(fp.read())

with open(args.j2_file) as fp:
    t = Template(fp.read(), trim_blocks=True, lstrip_blocks=True)

print("YAML file".center(80, "*"))
pprint(y)
print()
print("Jinja2 output".center(80, "*"))
print(t.render(y))
