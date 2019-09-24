# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer)

TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class NonazurevmScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_nonazurevm')
    @AllowLargeResponse(size_kb=3072)
    def test_nonazurevm(self, resource_group):
        self.kwargs.update({
            'name': 'fv-az461lw7ph_e2etest',
            'rg': 'hybridrptest',
        })
        count = len(self.cmd('nonazurevm list').get_output_in_json())
        self.cmd('az nonazurevm show --resource-group {rg} --name {name}', checks=[
            self.check('name', '{name}'),
            self.check('resourceGroup', '{rg}'),
        ])
        self.cmd('nonazurevm delete -g {rg} -n {name}')
        final_count = len(self.cmd('nonazurevm list').get_output_in_json())
        self.assertTrue(final_count, count - 1)
