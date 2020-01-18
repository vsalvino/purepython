Jinja Templates (Simple)
========================

[Jinja2](https://pypi.org/project/Jinja2/) is an amazing template renderer. It
is capable of generating huge complicated web pages, system configuration files,
or just about anything else you throw at it. It is also endlessly customizable
via plugins and extensions.

However, if you just need to render a simple template, such as an email or
a config file, you could easily do that using Python's built-in string
formatting functionality.

In either case, you would probably want to read the templates from a file,
and write the outputs to another file using Python's `open()` command.
