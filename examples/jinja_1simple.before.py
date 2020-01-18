from jinja2 import Template


# Values.
name = "Monty"
num = 4

# Jinja template language syntax.
simple_tmpl = """
Hello {{name}},
Your magic number is {{num}}.
"""

# Render template with Jinja using values.
template = Template(simple_tmpl)
output = template.render(name=name, num=num)

print(output)
