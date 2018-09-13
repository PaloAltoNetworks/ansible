#  Copyright 2016 Palo Alto Networks, Inc
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

__author__ = 'Ivan Bojer'

import json
import os
import xml.etree.ElementTree as ET

from units.modules.utils import AnsibleExitJson, AnsibleFailJson, ModuleTestCase
from ansible.compat.tests.unittest import TestCase

fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures')
fixture_data = {}


def load_fixture(name):
    path = os.path.join(fixture_path, name)

    if path in fixture_data:
        return fixture_data[path]

    # The root of the xml tree.
    root = ET.Element('result')

    # Load the config
    with open('candidate-config-rules.xml', 'r') as fd:
        e = ET.fromstring(fd.read())
        root.append(e)

    fixture_data[path] = root
    return root


class TestPanosModule(ModuleTestCase):
    def execute_module(self):
        return None

    def failed(self):
        return None

    def load_fixtures(self, commands=None, transport='cli'):
        return None
