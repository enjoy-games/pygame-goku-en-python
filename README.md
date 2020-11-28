# pygame-goku-en-python

## Introduction

I developed this mini game originally in 2007 when I started learning python. You can still find the original code in branch `2007_old_original_code`.

The orphan branch `development` contains up-to-date code with my current python knowledge.

#### Game controls

- Input device: Keyboard
  - Movement: arrow keys (up, left, down, right)
  - Attack / Kamehameha: space bar


## Versioning

This project follows semantic versioning.

Given a version number MAJOR.MINOR.PATCH, increment the:

- MAJOR version when incompatible API changes are made
- MINOR version when functionality in a backwards compatible manner is added
- PATCH version when backwards compatible bug fixes are made

See https://semver.org for more information


## No master/main branch

There is no `master/main` branch due to the fact that the name doesn't have any semantic meaning in relation to the state of the code.
Although some people use `master/main` as "code in production", it seems a rather inappropriate use, considering the fact that a branch pointer moves after each new commit.

The code is only in production after it has being deployed. After years of extensive experience in the software industry, it becomes clear that there are too many cases where a deploy has to be postponed and the `master/main` ~~branch~~ pointer is not reflecting production code anymore.

Following best practices it seems optimal not to deploy a git branch, but a git tag, which is also a pointer to a commit and doesn't move as the purpose of a git tag lies upon the fact that it remains still.
