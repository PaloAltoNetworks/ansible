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

from __future__ import (absolute_import, division)
__metaclass__ = type

from ansible.compat.tests.unittest import TestCase
from ansible.compat.tests.mock import call, create_autospec, patch, mock_open
from ansible.module_utils.basic import AnsibleModule
from ansible.modules.network.panos import panos_query_rules
from units.modules.utils import set_module_args
from .panos_module import TestPanosModule


class TestPanosQueryRulesModule(TestPanosModule):

    module = panos_query_rules

    def setUp(self):
        super(TestPanosModule, self).setUp()

    def tearDown(self):
        super(TestPanosModule, self).tearDown()

    def test_panos_query_rules(self):
        set_module_args(dict(banner='login', text='test\nbanner\nstring',
                             transport='cli'))
        commands = ['banner login', 'test', 'banner', 'string', 'EOF']
        self.execute_module(changed=True, commands=commands)

    # def test_panos_query_rules(self):
    #     module = TestPanosModule()
    #
    #     # Setup
    #     mod_cls = create_autospec(AnsibleModule)
    #     mod = mod_cls.return_value
    #     mod.params = dict(
    #         url="https://www.google.com",
    #         dest="/tmp/firstmod.txt"
    #     )
    #
    #     # Exercise
    #     module.execute_module()

