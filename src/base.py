#!/usr/bin/python3
# encoding: utf-8

from util import DEFAULT_SETTINGS
from workflow import Workflow
import sys


class Base(object):
    def __init__(self, args):
        self.args = args.strip()

    def execute(self):
        wf = Workflow(default_settings=DEFAULT_SETTINGS)
        self.wf = wf
        self.log = wf.logger
        sys.exit(wf.run(self.main))

    def main(self, wf):
        pass
