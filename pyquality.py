#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import logging
import subprocess
import coloredlogs
import verboselogs


def run(command, chdir, action, silent=True, shell=True):
    errors = 0
    logger = logging.getLogger(__name__)
    logger.debug('\nRunning %s' % action)

    logger.debug('    %s' % command)
    process = subprocess.Popen(
        command,
        cwd=chdir,
        shell=True,
        bufsize=0,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    output = ''
    output, _ = process.communicate()

    if not silent:
        logger.notice(output.decode('utf-8'))

    if process.returncode == 0:
        logger.success('    %s OK' % action)
    else:
        if type(output) is bytes:
            output = output.decode("utf-8", "replace")
        logger.warn('\n'.join(output.splitlines()))
        logger.critical('    %s FAILED' % action)
        errors += 1
    return errors


def main():
    # Set logs
    verboselogs.install()
    logger = logging.getLogger(__name__)
    os.environ['COLOREDLOGS_LOG_FORMAT'] = '%(message)s'
    coloredlogs.install(level='DEBUG', logger=logger)
 
    # Set by arguments
    chdir = sys.argv[1]
    report = False if '--no-report' in sys.argv else True
    flake8 = False if '--no-flake8' in sys.argv else True
    unittest = False if '--no-unittest' in sys.argv else True
    pylint = False if '--no-pylint' in sys.argv else True
    mi = False if '--no-mi' in sys.argv else True
    cc = False if '--no-cc' in sys.argv else True

    # Run quality commands
    errors = 0
    if unittest:
        errors += run(
            command='coverage run -m --omit=*tests* unittest',
            chdir=chdir,
            action="Unit tests",
            silent=False if report else True
        )
    if report:
        errors += run(
            command='coverage report -m',
            chdir=chdir,
            action="Coverage report",
            silent=False
        )
    if flake8:
        errors += run(
            command='flake8 --ignore=E501 .',
            chdir=chdir,
            action="Code sniffer"
        )
    if pylint:
        errors += run(
            command='pylint --ignore=tests -r y %s' % chdir.split('/')[-1],
            chdir='/'.join(chdir.split('/')[:-1]),
            action="Python linter",
            silent=False if report else True
        )
    if mi:
        errors += run(
            command="radon mi -i tests -s .",
            chdir=chdir,
            action="Verify project maintainability",
            silent=False if report else True
        )
    if cc:
        errors += run(
            command="xenon --max-absolute B --max-modules A --max-average A .",
            chdir=chdir,
            action="Verify project cyclomatic complexity"
        )

    sys.exit(0 if not errors else 1)
