#!/usr/bin/env python
# Copyright (C) 2024 xiangchen96
# This software may be modified and distributed under the terms
# of the MIT license. See the LICENSE file for details.

from lib.core.packages import Package


class Deb(Package):
    """Deb analysis package."""

    def prepare(self):
        self.args = [self.target] + self.args
        self.target = "dpkg -i"
