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


class CustomRule(Model):
    """Defines contents of a web application rule.

    All required parameters must be populated in order to send to Azure.

    :param name: Describes the name of the rule.
    :type name: str
    :param priority: Required. Describes priority of the rule. Rules with a
     lower value will be evaluated before rules with a higher value.
    :type priority: int
    :param enabled_state: Describes if the custom rule is in enabled or
     disabled state. Defaults to Enabled if not specified. Possible values
     include: 'Disabled', 'Enabled'
    :type enabled_state: str or
     ~azure.mgmt.frontdoor.models.CustomRuleEnabledState
    :param rule_type: Required. Describes type of rule. Possible values
     include: 'MatchRule', 'RateLimitRule'
    :type rule_type: str or ~azure.mgmt.frontdoor.models.RuleType
    :param rate_limit_duration_in_minutes: Time window for resetting the rate
     limit count. Default is 1 minute.
    :type rate_limit_duration_in_minutes: int
    :param rate_limit_threshold: Number of allowed requests per client within
     the time window.
    :type rate_limit_threshold: int
    :param match_conditions: Required. List of match conditions.
    :type match_conditions: list[~azure.mgmt.frontdoor.models.MatchCondition]
    :param action: Required. Describes what action to be applied when rule
     matches. Possible values include: 'Allow', 'Block', 'Log', 'Redirect'
    :type action: str or ~azure.mgmt.frontdoor.models.ActionType
    """

    _validation = {
        'name': {'max_length': 128},
        'priority': {'required': True},
        'rule_type': {'required': True},
        'rate_limit_duration_in_minutes': {'maximum': 5, 'minimum': 0},
        'rate_limit_threshold': {'minimum': 0},
        'match_conditions': {'required': True},
        'action': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'priority': {'key': 'priority', 'type': 'int'},
        'enabled_state': {'key': 'enabledState', 'type': 'str'},
        'rule_type': {'key': 'ruleType', 'type': 'str'},
        'rate_limit_duration_in_minutes': {'key': 'rateLimitDurationInMinutes', 'type': 'int'},
        'rate_limit_threshold': {'key': 'rateLimitThreshold', 'type': 'int'},
        'match_conditions': {'key': 'matchConditions', 'type': '[MatchCondition]'},
        'action': {'key': 'action', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CustomRule, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.priority = kwargs.get('priority', None)
        self.enabled_state = kwargs.get('enabled_state', None)
        self.rule_type = kwargs.get('rule_type', None)
        self.rate_limit_duration_in_minutes = kwargs.get('rate_limit_duration_in_minutes', None)
        self.rate_limit_threshold = kwargs.get('rate_limit_threshold', None)
        self.match_conditions = kwargs.get('match_conditions', None)
        self.action = kwargs.get('action', None)
