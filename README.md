Pure Python Equivalents
=======================

This project exists to show code snippets and examples for how to replace
common 3rd-party packages with "pure" Python code using only the standard
library. This in no way is meant to speak ill of any packages listed here - it
is to provide learning and reference for common Python idioms.

This project is inspired by
[You might not need jQuery](http://youmightnotneedjquery.com/) which I've found
to be a great resource for re-learning JavaScript.


Contributing
------------

Contributions are welcome! This is intended to be a collaborative effort, and
will hopefully become a rich resource of code snippets.

To contribute, create three files in the `examples/` directory:
* `name.md` - where the first line of the file is the title. Provide any
  additional reference info, links, instruction, etc. here. To maintain
  consistency, please follow the format used by other examples as so:
  ```markdown
  Package Name
  ============

  Level 2 heading
  ---------------

  [Link](http://example.com)
  List:
  * Bullet 1
  * Bullet 2
  ```
* `name.before.py` - the "before" code using the 3rd-party package.
* `name.after.py` - the "after" code using only built-in Python functionality.

As this is a reference site, please follow these coding guidelines to make the
examples as digestible as possible:
* Include docstrings on each class and function.
* Use comments liberally to annotate even basic concepts.
* Keep line lengths around 40-60 characters so that both snippets easily fit
  side-by-side.
* Run your code through `flake8` or `pylint` before committing to ensure it
  adheres to [PEP-8](https://www.python.org/dev/peps/pep-0008/) style and does
  not contain errors.


Building
--------

First create a virtual environment:

```
$ python -m venv ~/env/purepython
```

Activate the environment:

Mac/Linux

```
$ source ~/env/purepython/bin/activate
```

Windows (PowerShell)

```
PS> ~\env\purepython\Scripts\Activate.ps1
```

Install the requirements:

```
(purepython)$ pip install -r requirements.txt
```

Now, build the site:

```
(purepython)$ python render.py
```
