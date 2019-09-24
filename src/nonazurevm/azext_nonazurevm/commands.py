# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azext_nonazurevm._client_factory import cf_nonazurevm


def load_command_table(self, _):

    nonazurevm_sdk = CliCommandType(
        operations_tmpl='azext_nonazurevm.vendored_sdks.operations#MachinesOperations.{}',
        client_factory=cf_nonazurevm)


    with self.command_group('nonazurevm', nonazurevm_sdk, client_factory=cf_nonazurevm) as g:
        g.custom_command('delete', 'delete_nonazurevm')
        g.custom_command('list', 'list_nonazurevm')
        g.custom_command('show', 'show_nonazurevm')

    with self.command_group('nonazurevm', is_preview=True):
        pass

