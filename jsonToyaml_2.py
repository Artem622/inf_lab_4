import json
from ruamel.yaml import YAML

out_file = 'table1.yaml'
in_file = 'table.json'

yaml = YAML(typ="safe")
yaml.default_flow_style = False
with open(in_file, "r", encoding = 'UTF-8' ) as i:
    data = json.load(i)
with open(out_file, "w", encoding = 'UTF-8' ) as o:
    yaml.dump(data, o)
