# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import


helps['nonazurevm'] = """
    type: group
    short-summary: Commands to manage Non azure vms.
"""

helps['nonazurevm list'] = """
    type: command
    short-summary: List Non azure vms.
"""

helps['nonazurevm delete'] = """
    type: command
    short-summary: Delete a Non azure vm.
"""

helps['nonazurevm show'] = """
    type: command
    short-summary: Show details of a Non azure vm.
"""
