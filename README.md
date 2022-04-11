# Python Project Template

This is a comprehensive repo template for a Python &geq;3.7 project. Read
through the list of [features](#-1-features) and prune as desired - at
least one of the LICENSE files has to go :wink: and `pyproject.toml`
then edited accordingly. If you don't go for the AGPL, you should also
modify the copyright blurb in the source files.

[![License: CC0-1.0][license-badge-img-cc0]][license-badge-href-cc0]

**This template repository itself is licensed under the Creative Commons
“No Rights Reserved” CC0 1.0 Universal Public Domain Dedication.**

## Table of Contents

1. [Features](#-1-features)
1. [TODO](#-2-todo)
1. [Project Layout](#%EF%B8%8F-3-project-layout)
1. [Getting Started](#-4-getting-started)
1. [Creating a New Release](#-5-creating-a-new-release)
1. [Handy Developer References](#-6-handy-developer-references)
1. [A Selection of Badges](#-7-a-selection-of-badges)

---

## ✨ 1: Features

* Project setup with [flit] for building and distributing as a PyPi package.
* GitHub workflows for CI (lint, test, coverage) and building a release
  with a Windows executable.
* Community files (code of conduct, contributing, support etc.) that will
  integrate nicely with GitHub as well.
* [EditorConfig] support.
* Standardized commit messages plus changelog/release notes workflow,
  courtesy of [commitizen].
* Linting with [flake8] and friends, code formatting with [black][black-badge-href]
  and static analysis with [mypy] - both as linter scripts and git
  [pre-commit][pre-commit-badge-href] hooks.
* Speaking of git, there's a comprehensive `.gitignore` file.
* Easy logging with [loguru].
* Integration with [pre-commit.ci][pre-commit-ci] for auto-fixing pull requests.
* Integration with [pyup.io](https://pyup.io) for automated dependency updates.
* Pytest setup with [codecov.io](https://codecov.io) integration.

## 👷 2: TODO

* [[#1](https://github.com/pyxy-dk/python-project-template/issues/1)]
  Move [mypy] configuration into `pyproject.toml`
  [once the functionality has stabilised](https://github.com/python/mypy/issues/5205#issuecomment-832779057).
* [[#2](https://github.com/pyxy-dk/python-project-template/issues/2)] Ensure
  [pipx](https://pipxproject.github.io/pipx/) compatibility by setting up
  [flit entrypoints](https://flit.readthedocs.io/en/latest/pyproject_toml.html#scripts-section).
* [[#3](https://github.com/pyxy-dk/python-project-template/issues/3)] Set up [tox].
* [[#4](https://github.com/pyxy-dk/python-project-template/issues/4)] Add sample
  GitHub workflow step to upload package to [PyPi].

## 🗺️ 3: Project Layout

```text
python-project-template
│
├── .github
│   ├── workflows
│   │   ├── build.yml               ← CI workflow
│   │   └── release.yml             ← Release workflow for Windows .exe
│   │
│   ├── CODE_OF_CONDUCT.md          ← Code of Conduct
│   ├── CONTRIBUTING.md             ← Instructions for contributing
│   ├── FUNDING.yml                 ← GitHub funding integration
│   ├── SECURITY.md                 ← How to submit bug reports
│   └── SUPPORT.md                  ← How to get support
│
├── dist
│   ├── python_project_template.cfg ← Config file to include in release
│   └── README.txt                  ← Readme file to include in release
│
├── img
│   └── python-project-template.ico ← Icon for Windows .exe
│
├── release-notes
│   └── v0.0.1.md                   ← Release notes per version
│
├── scripts
│   └── lint.py                     ← Cleans up your code
│
├── src
│   └── python_project_template
│       ├── __init__.py             ← Module definition
│       ├── __main__.py             ← Package entrypoint
│       └── ppt.py                  ← Actual application code
│
├── tests
│   └── test_ppt.py                 ← A simple test
│
├── .editorconfig                   ← Editor settings
├── .flake8                         ← Linter settings
├── .gitignore                      ← List of ignored files
├── .markdownlint.json              ← Markdown lint settings
├── .pre-commit-config.yaml         ← Git pre-commit hooks
├── .pyup.yml                       ← PyUp.io settings
├── CHANGELOG.md                    ← Changelog
├── LICENSE                         ← Actual license for this repo
├── LICENSE.AGPLv3.md               ← AGPLv3 license template
├── LICENSE.MIT.md                  ← MIT license template
├── Pipfile                         ← Dependencies and scripts
├── pyproject.toml                  ← Project metadata and settings
├── README.md                       ← This file
└── version.yml                     ← File info for Windows .exe
```

Note that `Pipfile.lock` is not included but should be committed once generated.

## 🎬 4: Getting Started

* Create a new repo on GitHub using this repo as a template. ([HOWTO])
* Make sure to turn off git `autocrlf`:\
  `git config core.autocrlf false`
* To make the various integrations work you need to sign up with the
  different services (pyup.io, readthedocs, pre-commit.ci etc.) of
  course. Most of these have a free tier for open source projects.
* Make it your own project. Search and replace the following strings
  with your project/repo/real name as applicable:\
  `python-project-template`\
  `python_project_template`\
  `Python Project Template`\
  `Kristian Thy`\
  `PyXY`\
  `pyxy.dk`
* Initialize a virtualenv and install dependencies:\
  `$ pipenv update --dev`
* If you want to publish to [PyPi] at some point, remember to fill in
  your `~/.pypirc` as per [these instructions][antonz].
* Start the `pipenv shell` and:
  * Install the package locally using one of:\
    `flit install --symlink` (*nix, privileged Windows accounts)\
    `flit install --pth-file` (Windows, if the above doesn't work)
  * Install Git hooks:\
    `pre-commit install --hook-type pre-commit --hook-type commit-msg`

## 📦 5: Creating a New Release

1. Commit the code to be released as a new version using `cz commit`.
1. Push and verify that the CI build completed without errors.
1. Commit a new Markdown file in `./release-notes/` named after the new version's
   number, e.g. `./release-notes/v1.2.3.md`. The text in this file will be displayed
   as release notes on GitHub.
1. Run `cz bump`, which will
    1. Tag the latest commit with the new version name, e.g. `1.2.3`.
    1. Update `CHANGELOG.md`.
    1. Update the version number in `src/python_project_template/__init__.py`.
    1. Update the version number in `pyproject.toml`

Do not change the `0.0.0.0` in `version.yml` - it will be autofilled by the
release workflow.

## 📜 6: Handy Developer References

* [pytest - good integration practices](https://docs.pytest.org/en/6.2.x/goodpractices.html)
* [Python packaging pitfalls](https://blog.ionelmc.ro/2014/06/25/python-packaging-pitfalls/)
* [Python 3 Type Hints Cheat Sheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)

## 🥇 7: A Selection of Badges

Not all of these work or even make sense for this template, but they may serve
as inspiration for which scout marks you want to display for your own project.

[![Code style: black][black-badge-img]][black-badge-href]
[![Conventional commits][conventional-commits-badge-img]][conventional-commits-badge-href]
[![pre-commit][pre-commit-badge-img]][pre-commit-badge-href]
[![Updates][pyup-badge-img]][pyup-badge-href]

![Build status][github-actions-build-badge-img]
![Release status][github-actions-release-badge-img]
[![Code coverage][codecov-badge-img]][codecov-badge-href]
[![Maintainability rating][sonarcloud-badge-img]][sonarcloud-badge-href]

![Pipenv - Python version][pipenv-badge-img]
[![PyPI - Python version][pypi-badge-img-pyv]][pypi-badge-href]
[![PyPI - Implementation][pypi-badge-img-impl]][pypi-badge-href]
[![PyPI - Wheel][pypi-badge-img-whl]][pypi-badge-href]

[![Latest GitHub release][release-badge-img]][release-badge-href]
![License][license-badge-img]

---

[antonz]: https://antonz.org/python-packaging/
[black-badge-href]: https://github.com/psf/black
[black-badge-img]: https://img.shields.io/badge/code%20style-black-000000.svg
[codecov-badge-href]: https://codecov.io/gh/pyxy-dk/python-project-template
[codecov-badge-img]: https://codecov.io/gh/pyxy-dk/python-project-template/branch/main/graph/badge.svg
[commitizen]: https://commitizen-tools.github.io/commitizen/
[conventional-commits-badge-href]: https://www.conventionalcommits.org/en/v1.0.0/
[conventional-commits-badge-img]: https://img.shields.io/badge/conventional%20commits-1.0.0-blue.svg
[EditorConfig]: https://editorconfig.org/
[flake8]: https://flake8.pycqa.org/
[flit]: https://pypi.org/project/flit/
[github-actions-build-badge-img]: https://github.com/pyxy-dk/python-project-template/workflows/build/badge.svg
[github-actions-release-badge-img]: https://github.com/pyxy-dk/python-project-template/workflows/release/badge.svg
[HOWTO]: https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template
[license-badge-img]: https://img.shields.io/github/license/pyxy-dk/python-project-template
[license-badge-href-cc0]: http://creativecommons.org/publicdomain/zero/1.0/
[license-badge-img-cc0]: https://licensebuttons.net/l/zero/1.0/88x31.png
[loguru]: https://github.com/Delgan/loguru
[mypy]: https://mypy.readthedocs.io/en/latest/config_file.html#the-mypy-configuration-file
[pipenv-badge-img]: https://img.shields.io/github/pipenv/locked/python-version/pyxy-dk/python-project-template
[pre-commit-badge-href]: https://github.com/pre-commit/pre-commit
[pre-commit-badge-img]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[pre-commit-ci]: https://pre-commit.ci/
[PyPi]: https://pypi.org/
[pypi-badge-href]: https://pypi.org/project/python-project-template/
[pypi-badge-img-impl]: https://img.shields.io/pypi/implementation/python-project-template
[pypi-badge-img-pyv]: https://img.shields.io/pypi/pyversions/python-project-template
[pypi-badge-img-whl]: https://img.shields.io/pypi/wheel/python-project-template
[pyup-badge-href]: https://pyup.io/repos/github/pyxy-dk/python-project-template/
[pyup-badge-img]: https://pyup.io/repos/github/pyxy-dk/python-project-template/shield.svg
[release-badge-img]: https://img.shields.io/github/v/release/pyxy-dk/python-project-template?sort=semver
[release-badge-href]: https://github.com/pyxy-dk/python-project-template/releases
[sonarcloud-badge-href]: https://sonarcloud.io/dashboard?id=kthy_python-project-template
[sonarcloud-badge-img]: https://sonarcloud.io/api/project_badges/measure?project=kthy_python-project-template&metric=sqale_rating
[tox]: https://tox.readthedocs.io/en/latest/
