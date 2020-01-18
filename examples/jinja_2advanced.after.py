# Values.
name = "Monty"
order = [
    {"qty": 1, "name": "Widget"},
    {"qty": 3, "name": "Carpets"}
]

# Our home-grown template language, based on
# Python's string format syntax.
fancy_templ = """
Hello {name},
You ordered:
{{ for item in order }}
* {item[qty]} x {item[name]}
{{ endfor }}
Thank you.
"""


def format_template(template: str, values: dict) -> str:
    """
    Function to process `for` loops in our own simple
    template language. Use for loops as so:
        {{ for item in list }}
        ...
        {{ endfor }}
    """
    loop = ""
    loop_elem = ""
    loop_iter = ""
    in_loop = False
    output = ""
    for line in template.splitlines(keepends=True):
        # Check if starting a loop.
        if line.strip().startswith(r"{{ for"):
            in_loop = True
            # Strip spaces and braces, and parse the `for` statement.
            parsed = line.strip("}{ \t\r\n").lstrip("for").split("in")
            loop_elem = parsed[0].strip()
            loop_iter = parsed[1].strip()
            continue

        # Check if done with a loop.
        if line.strip().startswith(r"{{ endfor }}"):
            # Render the contents of the loop now.
            for x in values[loop_iter]:
                output += loop.format(**{loop_elem: x})
            # Reset and then exit the loop.
            in_loop = False
            loop = ""
            continue

        # Format the current line or load it into a loop.
        if in_loop:
            loop += line
        else:
            output += line.format(**values)

    return output


# Render template with our custom function.
output = format_template(
    fancy_templ,
    {"name": name, "order": order}
)

print(output)
