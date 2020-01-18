# Values.
name = "Monty"
num = 4

# Python string format syntax.
simple_tmpl = """
Hello {name},
Your magic number is {num}.
"""

# Render template with Python string formatter.
output = simple_tmpl.format(name=name, num=num)

print(output)
