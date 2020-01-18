from jinja2 import Template


# Values.
name = "Monty"
order = [
    {"qty": 1, "name": "Widget"},
    {"qty": 3, "name": "Carpets"}
]

# Jinja template language stynax.
fancy_tmpl = """
Hello {{name}},
You ordered:
{%- for item in order %}
* {{item.qty}} x {{item.name}}
{%- endfor %}
Thank you.
"""

# Render template with Jinja using values.
template = Template(fancy_tmpl)
output = template.render(
    {"name": name, "order": order}
)

print(output)
