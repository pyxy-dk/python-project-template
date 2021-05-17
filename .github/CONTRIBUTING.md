# Contributing to python-project-template

Hi! :wave: Thank you for considering to contribute to this project.

> Please read the [Code of Conduct][CoC] for this project before going ahead.

## Development environment setup

* Assumes you have `pipenv` installed and in your path.

```bash
pipenv install --dev
```

*Et voilà!* :wink:

## Contributions

Contributions are accepted as pull requests to the `python-project-template`
repository in the spirit of the maxim:

> *If there's no pull request, then it hasn't happened.*

Inspired by [Microsoft's branching guide](https://docs.microsoft.com/en-us/azure/devops/repos/git/git-branching-guidance),
 `python-project-template`'s branching strategy follows these principles:

* Use feature branches, preferably short-lived, for all new features and
  bug fixes.
* Merge feature branches into the main branch using pull requests.
* Keep a high quality, up-to-date main branch.

### Use short-lived feature branches for all changes

Features and bug fixes are developed in feature branches based off the main
branch. Even small fixes and changes should have their own feature branch.
Git branches are inexpensive to create and maintain.

Branches should be named by convention:

* `features/feature-name`
* `bugfix/bug-name-or-ref`

The feature name or bug name should be meaningful. Branches should be
short-lived so as not to diverge unduly from other development.

### Tests are an integral part of all changes

"All" is only a slight exaggeration. As a general rule, changes to the main
code are accompanied by corresponding updates to the tests.

In particular, tests are the primary way to demonstrate new/changed
functionality. Explicit documentation is also great, almost as great as
tests.

### Submitting and reviewing pull requests

The author submits their changes as a pull request in the GitHub user
interface.

The reviewer(s) run the test suite and read the changes to the code base.
Comment exchanges and commits ensue until all issues are resolved as either:

* fixed,
* punted to the backlog as a new work item for later, or
* explicitly abandoned as "won't fix".

Once the reviewer(s) indicate their acceptance of the PR, they will
complete the PR by merging it.

Reviewers in general should diligently commit to reviewing PRs as soon as
possible so as not to delay further work.
