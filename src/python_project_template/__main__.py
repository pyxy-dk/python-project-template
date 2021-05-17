#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Kristian Thy
#
# This file is part of Python Project Template.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""Main entrypoint for the CLI."""

from sys import stderr

from loguru import logger

from python_project_template import ppt

log_format = "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}"


@logger.catch
def main():
    """CLI entrypoint."""
    logger.info("2 + 2 = {sum}", sum=ppt.sum_of_two_integers(2, 2))
    return ppt.quotient_between_two_integers(1, 0)


if __name__ == "__main__":
    logger.add(
        stderr,
        backtrace=True,
        diagnose=True,
        colorize=True,
        format=log_format,
        filter="python_project_template",
        level="INFO",
    )
    logger.add("logs/file_{time}.log", compression="zip", rotation="4 MB", format=log_format)
    main()
