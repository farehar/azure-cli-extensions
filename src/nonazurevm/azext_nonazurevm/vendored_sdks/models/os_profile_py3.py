# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class OSProfile(Model):
    """Specifies the operating system settings for the hybrid machine.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar computer_name: Specifies the host OS name of the hybrid machine.
    :vartype computer_name: str
    """

    _validation = {
        'computer_name': {'readonly': True},
    }

    _attribute_map = {
        'computer_name': {'key': 'computerName', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(OSProfile, self).__init__(**kwargs)
        self.computer_name = None
