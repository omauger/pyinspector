# pyinspector

Pipeline to run quality tools on python projet :
* unittest
* coverage report
* flake8
* pylint
* radon for maintainability report
* xenon for cyclomatic complexity

## Install

```
pip install pyinspector
```

## Usage
```
pyinspector <project_path> <options_not_required>
```
<project_path> need to be explicit path. Don't use '.'

You can use options :
* `--no-report`: to not print results and not coverage report
* `--no-unittest`: to not run unittest
* `--no-flake8`: to not run flake8
* `--no-pylint`: to not run pylint
* `--no-mi`: to not inspect maintainability
* `--no-cc`: to not inspect cyclomatic complexity

