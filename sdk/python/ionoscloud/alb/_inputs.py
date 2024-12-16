# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'BalancerFlowlogArgs',
    'ForwardingRuleHttpRuleArgs',
    'ForwardingRuleHttpRuleConditionArgs',
]

@pulumi.input_type
class BalancerFlowlogArgs:
    def __init__(__self__, *,
                 action: pulumi.Input[str],
                 bucket: pulumi.Input[str],
                 direction: pulumi.Input[str],
                 name: pulumi.Input[str],
                 id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] action: [string] Specifies the action to be taken when the rule is matched. Possible values: ACCEPTED, REJECTED, ALL. Immutable, forces re-creation.
        :param pulumi.Input[str] bucket: [string] Specifies the IONOS Object Storage bucket where the flow log data will be stored. The bucket must exist. Immutable, forces re-creation.
        :param pulumi.Input[str] direction: [string] Specifies the traffic direction pattern. Valid values: INGRESS, EGRESS, BIDIRECTIONAL. Immutable, forces re-creation.
        :param pulumi.Input[str] name: [string] Specifies the name of the flow log.
               
               ⚠️ **Note:**: Removing the `flowlog` forces re-creation of the application load balancer resource.
        :param pulumi.Input[str] id: The resource's unique identifier.
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "bucket", bucket)
        pulumi.set(__self__, "direction", direction)
        pulumi.set(__self__, "name", name)
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Input[str]:
        """
        [string] Specifies the action to be taken when the rule is matched. Possible values: ACCEPTED, REJECTED, ALL. Immutable, forces re-creation.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: pulumi.Input[str]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[str]:
        """
        [string] Specifies the IONOS Object Storage bucket where the flow log data will be stored. The bucket must exist. Immutable, forces re-creation.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter
    def direction(self) -> pulumi.Input[str]:
        """
        [string] Specifies the traffic direction pattern. Valid values: INGRESS, EGRESS, BIDIRECTIONAL. Immutable, forces re-creation.
        """
        return pulumi.get(self, "direction")

    @direction.setter
    def direction(self, value: pulumi.Input[str]):
        pulumi.set(self, "direction", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        [string] Specifies the name of the flow log.

        ⚠️ **Note:**: Removing the `flowlog` forces re-creation of the application load balancer resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource's unique identifier.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)


@pulumi.input_type
class ForwardingRuleHttpRuleArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 type: pulumi.Input[str],
                 conditions: Optional[pulumi.Input[Sequence[pulumi.Input['ForwardingRuleHttpRuleConditionArgs']]]] = None,
                 content_type: Optional[pulumi.Input[str]] = None,
                 drop_query: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 response_message: Optional[pulumi.Input[str]] = None,
                 status_code: Optional[pulumi.Input[int]] = None,
                 target_group: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] name: [string] The unique name of the Application Load Balancer HTTP rule.
        :param pulumi.Input[str] type: [string] Type of the Http Rule condition.
        :param pulumi.Input[Sequence[pulumi.Input['ForwardingRuleHttpRuleConditionArgs']]] conditions: [list] - An array of items in the collection.The action is only performed if each and every condition is met; if no conditions are set, the rule will always be performed.
        :param pulumi.Input[str] content_type: [string] Valid only for STATIC actions.
        :param pulumi.Input[bool] drop_query: [bool] Default is false; valid only for REDIRECT actions.
        :param pulumi.Input[str] location: [string] The location for redirecting; mandatory and valid only for REDIRECT actions.
        :param pulumi.Input[str] response_message: [string] The response message of the request; mandatory for STATIC action.
        :param pulumi.Input[int] status_code: [int] Valid only for REDIRECT and STATIC actions. For REDIRECT actions, default is 301 and possible values are 301, 302, 303, 307, and 308. For STATIC actions, default is 503 and valid range is 200 to 599.
        :param pulumi.Input[str] target_group: [string] The UUID of the target group; mandatory for FORWARD action.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", type)
        if conditions is not None:
            pulumi.set(__self__, "conditions", conditions)
        if content_type is not None:
            pulumi.set(__self__, "content_type", content_type)
        if drop_query is not None:
            pulumi.set(__self__, "drop_query", drop_query)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if response_message is not None:
            pulumi.set(__self__, "response_message", response_message)
        if status_code is not None:
            pulumi.set(__self__, "status_code", status_code)
        if target_group is not None:
            pulumi.set(__self__, "target_group", target_group)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        [string] The unique name of the Application Load Balancer HTTP rule.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        [string] Type of the Http Rule condition.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ForwardingRuleHttpRuleConditionArgs']]]]:
        """
        [list] - An array of items in the collection.The action is only performed if each and every condition is met; if no conditions are set, the rule will always be performed.
        """
        return pulumi.get(self, "conditions")

    @conditions.setter
    def conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ForwardingRuleHttpRuleConditionArgs']]]]):
        pulumi.set(self, "conditions", value)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Valid only for STATIC actions.
        """
        return pulumi.get(self, "content_type")

    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_type", value)

    @property
    @pulumi.getter(name="dropQuery")
    def drop_query(self) -> Optional[pulumi.Input[bool]]:
        """
        [bool] Default is false; valid only for REDIRECT actions.
        """
        return pulumi.get(self, "drop_query")

    @drop_query.setter
    def drop_query(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "drop_query", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The location for redirecting; mandatory and valid only for REDIRECT actions.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="responseMessage")
    def response_message(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The response message of the request; mandatory for STATIC action.
        """
        return pulumi.get(self, "response_message")

    @response_message.setter
    def response_message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "response_message", value)

    @property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> Optional[pulumi.Input[int]]:
        """
        [int] Valid only for REDIRECT and STATIC actions. For REDIRECT actions, default is 301 and possible values are 301, 302, 303, 307, and 308. For STATIC actions, default is 503 and valid range is 200 to 599.
        """
        return pulumi.get(self, "status_code")

    @status_code.setter
    def status_code(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "status_code", value)

    @property
    @pulumi.getter(name="targetGroup")
    def target_group(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The UUID of the target group; mandatory for FORWARD action.
        """
        return pulumi.get(self, "target_group")

    @target_group.setter
    def target_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_group", value)


@pulumi.input_type
class ForwardingRuleHttpRuleConditionArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 condition: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 negate: Optional[pulumi.Input[bool]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] type: [string] Type of the Http Rule condition.
        :param pulumi.Input[str] condition: [string] Matching rule for the HTTP rule condition attribute; mandatory for HEADER, PATH, QUERY, METHOD, HOST, and COOKIE types; must be null when type is SOURCE_IP.
        :param pulumi.Input[str] key: [string] Must be null when type is PATH, METHOD, HOST, or SOURCE_IP. Key can only be set when type is COOKIES, HEADER, or QUERY.
        :param pulumi.Input[bool] negate: [bool] Specifies whether the condition is negated or not; the default is False.
        :param pulumi.Input[str] value: [string] Mandatory for conditions CONTAINS, EQUALS, MATCHES, STARTS_WITH, ENDS_WITH; must be null when condition is EXISTS; should be a valid CIDR if provided and if type is SOURCE_IP.
        """
        pulumi.set(__self__, "type", type)
        if condition is not None:
            pulumi.set(__self__, "condition", condition)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if negate is not None:
            pulumi.set(__self__, "negate", negate)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        [string] Type of the Http Rule condition.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Matching rule for the HTTP rule condition attribute; mandatory for HEADER, PATH, QUERY, METHOD, HOST, and COOKIE types; must be null when type is SOURCE_IP.
        """
        return pulumi.get(self, "condition")

    @condition.setter
    def condition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "condition", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Must be null when type is PATH, METHOD, HOST, or SOURCE_IP. Key can only be set when type is COOKIES, HEADER, or QUERY.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def negate(self) -> Optional[pulumi.Input[bool]]:
        """
        [bool] Specifies whether the condition is negated or not; the default is False.
        """
        return pulumi.get(self, "negate")

    @negate.setter
    def negate(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "negate", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Mandatory for conditions CONTAINS, EQUALS, MATCHES, STARTS_WITH, ENDS_WITH; must be null when condition is EXISTS; should be a valid CIDR if provided and if type is SOURCE_IP.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


