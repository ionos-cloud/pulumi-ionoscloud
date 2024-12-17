# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities
from . import outputs

__all__ = [
    'GetNatGatewayRuleResult',
    'AwaitableGetNatGatewayRuleResult',
    'get_nat_gateway_rule',
    'get_nat_gateway_rule_output',
]

@pulumi.output_type
class GetNatGatewayRuleResult:
    """
    A collection of values returned by getNatGatewayRule.
    """
    def __init__(__self__, datacenter_id=None, id=None, name=None, natgateway_id=None, protocol=None, public_ip=None, source_subnet=None, target_port_ranges=None, target_subnet=None, type=None):
        if datacenter_id and not isinstance(datacenter_id, str):
            raise TypeError("Expected argument 'datacenter_id' to be a str")
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if natgateway_id and not isinstance(natgateway_id, str):
            raise TypeError("Expected argument 'natgateway_id' to be a str")
        pulumi.set(__self__, "natgateway_id", natgateway_id)
        if protocol and not isinstance(protocol, str):
            raise TypeError("Expected argument 'protocol' to be a str")
        pulumi.set(__self__, "protocol", protocol)
        if public_ip and not isinstance(public_ip, str):
            raise TypeError("Expected argument 'public_ip' to be a str")
        pulumi.set(__self__, "public_ip", public_ip)
        if source_subnet and not isinstance(source_subnet, str):
            raise TypeError("Expected argument 'source_subnet' to be a str")
        pulumi.set(__self__, "source_subnet", source_subnet)
        if target_port_ranges and not isinstance(target_port_ranges, list):
            raise TypeError("Expected argument 'target_port_ranges' to be a list")
        pulumi.set(__self__, "target_port_ranges", target_port_ranges)
        if target_subnet and not isinstance(target_subnet, str):
            raise TypeError("Expected argument 'target_subnet' to be a str")
        pulumi.set(__self__, "target_subnet", target_subnet)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> str:
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Id of the NAT gateway rule
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of the NAT gateway rule
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="natgatewayId")
    def natgateway_id(self) -> str:
        return pulumi.get(self, "natgateway_id")

    @property
    @pulumi.getter
    def protocol(self) -> str:
        """
        Protocol of the NAT gateway rule. Defaults to ALL. If protocol is 'ICMP' then targetPortRange start and end cannot be set.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> str:
        """
        Public IP address of the NAT gateway rule. Specifies the address used for masking outgoing packets source address field. Should be one of the customer reserved IP address already configured on the NAT gateway resource
        """
        return pulumi.get(self, "public_ip")

    @property
    @pulumi.getter(name="sourceSubnet")
    def source_subnet(self) -> str:
        """
        Source subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets source IP address.
        """
        return pulumi.get(self, "source_subnet")

    @property
    @pulumi.getter(name="targetPortRanges")
    def target_port_ranges(self) -> Sequence['outputs.GetNatGatewayRuleTargetPortRangeResult']:
        """
        Target port range of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on destination port. If none is provided, rule will match any port
        """
        return pulumi.get(self, "target_port_ranges")

    @property
    @pulumi.getter(name="targetSubnet")
    def target_subnet(self) -> str:
        """
        Target or destination subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets destination IP address. If none is provided, rule will match any address.
        """
        return pulumi.get(self, "target_subnet")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        ype of the NAT gateway rule.
        """
        return pulumi.get(self, "type")


class AwaitableGetNatGatewayRuleResult(GetNatGatewayRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNatGatewayRuleResult(
            datacenter_id=self.datacenter_id,
            id=self.id,
            name=self.name,
            natgateway_id=self.natgateway_id,
            protocol=self.protocol,
            public_ip=self.public_ip,
            source_subnet=self.source_subnet,
            target_port_ranges=self.target_port_ranges,
            target_subnet=self.target_subnet,
            type=self.type)


def get_nat_gateway_rule(datacenter_id: Optional[str] = None,
                         id: Optional[str] = None,
                         name: Optional[str] = None,
                         natgateway_id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNatGatewayRuleResult:
    """
    The **NAT Gateway Rule data source** can be used to search for and return existing NAT Gateway Rules.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage


    :param str datacenter_id: Datacenter's UUID.
    :param str id: ID of the NAT gateway rule you want to search for.
           
           Both `datacenter_id` and `natgateway_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
    :param str name: Name of an existing NAT gateway rule that you want to search for.
    :param str natgateway_id: Nat Gateway's UUID.
    """
    __args__ = dict()
    __args__['datacenterId'] = datacenter_id
    __args__['id'] = id
    __args__['name'] = name
    __args__['natgatewayId'] = natgateway_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:compute/getNatGatewayRule:getNatGatewayRule', __args__, opts=opts, typ=GetNatGatewayRuleResult).value

    return AwaitableGetNatGatewayRuleResult(
        datacenter_id=pulumi.get(__ret__, 'datacenter_id'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        natgateway_id=pulumi.get(__ret__, 'natgateway_id'),
        protocol=pulumi.get(__ret__, 'protocol'),
        public_ip=pulumi.get(__ret__, 'public_ip'),
        source_subnet=pulumi.get(__ret__, 'source_subnet'),
        target_port_ranges=pulumi.get(__ret__, 'target_port_ranges'),
        target_subnet=pulumi.get(__ret__, 'target_subnet'),
        type=pulumi.get(__ret__, 'type'))
def get_nat_gateway_rule_output(datacenter_id: Optional[pulumi.Input[str]] = None,
                                id: Optional[pulumi.Input[Optional[str]]] = None,
                                name: Optional[pulumi.Input[Optional[str]]] = None,
                                natgateway_id: Optional[pulumi.Input[str]] = None,
                                opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetNatGatewayRuleResult]:
    """
    The **NAT Gateway Rule data source** can be used to search for and return existing NAT Gateway Rules.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage


    :param str datacenter_id: Datacenter's UUID.
    :param str id: ID of the NAT gateway rule you want to search for.
           
           Both `datacenter_id` and `natgateway_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
    :param str name: Name of an existing NAT gateway rule that you want to search for.
    :param str natgateway_id: Nat Gateway's UUID.
    """
    __args__ = dict()
    __args__['datacenterId'] = datacenter_id
    __args__['id'] = id
    __args__['name'] = name
    __args__['natgatewayId'] = natgateway_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:compute/getNatGatewayRule:getNatGatewayRule', __args__, opts=opts, typ=GetNatGatewayRuleResult)
    return __ret__.apply(lambda __response__: GetNatGatewayRuleResult(
        datacenter_id=pulumi.get(__response__, 'datacenter_id'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        natgateway_id=pulumi.get(__response__, 'natgateway_id'),
        protocol=pulumi.get(__response__, 'protocol'),
        public_ip=pulumi.get(__response__, 'public_ip'),
        source_subnet=pulumi.get(__response__, 'source_subnet'),
        target_port_ranges=pulumi.get(__response__, 'target_port_ranges'),
        target_subnet=pulumi.get(__response__, 'target_subnet'),
        type=pulumi.get(__response__, 'type')))
