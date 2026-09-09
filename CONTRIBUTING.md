# How to contribute

sandpit is an internal development and testing repo not intended for public consumption, but if you fancy making a contribution, knock yourself out.

## Coding conventions

  * This is open source software. We endeavour to make the code as transparent as possible.
  * We use and recommend Visual Studio Code for development and testing. The VSCode workflow
  provided is intended to work on MacOS, Linux and Windows (with PowerShell>=5.1).
  * We document the code in accordance with [Sphinx](https://www.sphinx-doc.org/en/master/) (>=8.2) docstring conventions.
  * We use [pylint](https://pypi.org/project/pylint/) (>=3.3) for code analysis.
  * We use [bandit](https://pypi.org/project/bandit/) (>=1.8) for security vulnerability analysis.
  * We use [black](https://pypi.org/project/black/) (>=25.0) for code formatting and ask that you do the same.

## Testing

We use Python's pytest (>=8.4) framework for local unit testing, complemented by the GitHub Actions automated build and testing workflow.

Please write pytest examples for new code you create and add them to the /tests folder following the naming convention test_*.py.

## Submitting changes

Please send a [GitHub Pull Request to sandpit](https://github.com/semuadmin/sandpit/pulls) with a clear list of what you've done (read more about [pull requests](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/about-pull-requests)). Please follow our coding conventions (below) and make sure all of your commits are atomic (one feature per commit).

Always write a clear log message for your commits. One-line messages are fine for small changes, but bigger changes should look like this:

    $ git commit -m "A brief summary of the commit
    > 
    > A paragraph describing what changed and its impact."

Thanks,

semuadmin
