# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
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
from . import _utilities

__all__ = [
    'GetFirewallResult',
    'AwaitableGetFirewallResult',
    'get_firewall',
    'get_firewall_output',
]

@pulumi.output_type
class GetFirewallResult:
    """
    A collection of values returned by getFirewall.
    """
    def __init__(__self__, datacenter_id=None, icmp_code=None, icmp_type=None, id=None, name=None, nic_id=None, port_range_end=None, port_range_start=None, protocol=None, server_id=None, source_ip=None, source_mac=None, target_ip=None, type=None):
        if datacenter_id and not isinstance(datacenter_id, str):
            raise TypeError("Expected argument 'datacenter_id' to be a str")
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        if icmp_code and not isinstance(icmp_code, str):
            raise TypeError("Expected argument 'icmp_code' to be a str")
        pulumi.set(__self__, "icmp_code", icmp_code)
        if icmp_type and not isinstance(icmp_type, str):
            raise TypeError("Expected argument 'icmp_type' to be a str")
        pulumi.set(__self__, "icmp_type", icmp_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if nic_id and not isinstance(nic_id, str):
            raise TypeError("Expected argument 'nic_id' to be a str")
        pulumi.set(__self__, "nic_id", nic_id)
        if port_range_end and not isinstance(port_range_end, int):
            raise TypeError("Expected argument 'port_range_end' to be a int")
        pulumi.set(__self__, "port_range_end", port_range_end)
        if port_range_start and not isinstance(port_range_start, int):
            raise TypeError("Expected argument 'port_range_start' to be a int")
        pulumi.set(__self__, "port_range_start", port_range_start)
        if protocol and not isinstance(protocol, str):
            raise TypeError("Expected argument 'protocol' to be a str")
        pulumi.set(__self__, "protocol", protocol)
        if server_id and not isinstance(server_id, str):
            raise TypeError("Expected argument 'server_id' to be a str")
        pulumi.set(__self__, "server_id", server_id)
        if source_ip and not isinstance(source_ip, str):
            raise TypeError("Expected argument 'source_ip' to be a str")
        pulumi.set(__self__, "source_ip", source_ip)
        if source_mac and not isinstance(source_mac, str):
            raise TypeError("Expected argument 'source_mac' to be a str")
        pulumi.set(__self__, "source_mac", source_mac)
        if target_ip and not isinstance(target_ip, str):
            raise TypeError("Expected argument 'target_ip' to be a str")
        pulumi.set(__self__, "target_ip", target_ip)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> str:
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter(name="icmpCode")
    def icmp_code(self) -> str:
        """
        Defines the allowed code (from 0 to 254) if protocol ICMP is chosen.
        """
        return pulumi.get(self, "icmp_code")

    @property
    @pulumi.getter(name="icmpType")
    def icmp_type(self) -> str:
        """
        Defines the allowed type (from 0 to 254) if the protocol ICMP is chosen.
        """
        return pulumi.get(self, "icmp_type")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The id of the firewall rule.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the firewall rule.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nicId")
    def nic_id(self) -> str:
        return pulumi.get(self, "nic_id")

    @property
    @pulumi.getter(name="portRangeEnd")
    def port_range_end(self) -> int:
        """
        Defines the end range of the allowed port (from 1 to 65534) if the protocol TCP or UDP is chosen.
        """
        return pulumi.get(self, "port_range_end")

    @property
    @pulumi.getter(name="portRangeStart")
    def port_range_start(self) -> int:
        """
        Defines the start range of the allowed port (from 1 to 65534) if protocol TCP or UDP is chosen.
        """
        return pulumi.get(self, "port_range_start")

    @property
    @pulumi.getter
    def protocol(self) -> str:
        """
        The protocol for the rule: TCP, UDP, ICMP, ANY. This property is immutable.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> str:
        return pulumi.get(self, "server_id")

    @property
    @pulumi.getter(name="sourceIp")
    def source_ip(self) -> str:
        """
        Only traffic originating from the respective IPv4 address is allowed.
        """
        return pulumi.get(self, "source_ip")

    @property
    @pulumi.getter(name="sourceMac")
    def source_mac(self) -> str:
        """
        Only traffic originating from the respective MAC address is allowed.
        """
        return pulumi.get(self, "source_mac")

    @property
    @pulumi.getter(name="targetIp")
    def target_ip(self) -> str:
        """
        Only traffic directed to the respective IP address of the NIC is allowed.
        """
        return pulumi.get(self, "target_ip")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")


class AwaitableGetFirewallResult(GetFirewallResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFirewallResult(
            datacenter_id=self.datacenter_id,
            icmp_code=self.icmp_code,
            icmp_type=self.icmp_type,
            id=self.id,
            name=self.name,
            nic_id=self.nic_id,
            port_range_end=self.port_range_end,
            port_range_start=self.port_range_start,
            protocol=self.protocol,
            server_id=self.server_id,
            source_ip=self.source_ip,
            source_mac=self.source_mac,
            target_ip=self.target_ip,
            type=self.type)


def get_firewall(datacenter_id: Optional[str] = None,
                 id: Optional[str] = None,
                 name: Optional[str] = None,
                 nic_id: Optional[str] = None,
                 server_id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFirewallResult:
    """
    The **Firewall data source** can be used to search for and return an existing FirewallRules.
    You can provide a string for either id or name parameters which will be compared with provisioned Firewall Rules.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage


    :param str datacenter_id: The Virtual Data Center ID.
    :param str id: ID of the firewall rule you want to search for.
    :param str name: Name of an existing firewall rule that you want to search for.
    :param str nic_id: The NIC ID.
           
           Either `name` or   `id` must be provided. If none, or both are provided, the datasource will return an error.
    :param str server_id: The Server ID.
    """
    __args__ = dict()
    __args__['datacenterId'] = datacenter_id
    __args__['id'] = id
    __args__['name'] = name
    __args__['nicId'] = nic_id
    __args__['serverId'] = server_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getFirewall:getFirewall', __args__, opts=opts, typ=GetFirewallResult).value

    return AwaitableGetFirewallResult(
        datacenter_id=pulumi.get(__ret__, 'datacenter_id'),
        icmp_code=pulumi.get(__ret__, 'icmp_code'),
        icmp_type=pulumi.get(__ret__, 'icmp_type'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        nic_id=pulumi.get(__ret__, 'nic_id'),
        port_range_end=pulumi.get(__ret__, 'port_range_end'),
        port_range_start=pulumi.get(__ret__, 'port_range_start'),
        protocol=pulumi.get(__ret__, 'protocol'),
        server_id=pulumi.get(__ret__, 'server_id'),
        source_ip=pulumi.get(__ret__, 'source_ip'),
        source_mac=pulumi.get(__ret__, 'source_mac'),
        target_ip=pulumi.get(__ret__, 'target_ip'),
        type=pulumi.get(__ret__, 'type'))
def get_firewall_output(datacenter_id: Optional[pulumi.Input[str]] = None,
                        id: Optional[pulumi.Input[Optional[str]]] = None,
                        name: Optional[pulumi.Input[Optional[str]]] = None,
                        nic_id: Optional[pulumi.Input[str]] = None,
                        server_id: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFirewallResult]:
    """
    The **Firewall data source** can be used to search for and return an existing FirewallRules.
    You can provide a string for either id or name parameters which will be compared with provisioned Firewall Rules.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage


    :param str datacenter_id: The Virtual Data Center ID.
    :param str id: ID of the firewall rule you want to search for.
    :param str name: Name of an existing firewall rule that you want to search for.
    :param str nic_id: The NIC ID.
           
           Either `name` or   `id` must be provided. If none, or both are provided, the datasource will return an error.
    :param str server_id: The Server ID.
    """
    __args__ = dict()
    __args__['datacenterId'] = datacenter_id
    __args__['id'] = id
    __args__['name'] = name
    __args__['nicId'] = nic_id
    __args__['serverId'] = server_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:index/getFirewall:getFirewall', __args__, opts=opts, typ=GetFirewallResult)
    return __ret__.apply(lambda __response__: GetFirewallResult(
        datacenter_id=pulumi.get(__response__, 'datacenter_id'),
        icmp_code=pulumi.get(__response__, 'icmp_code'),
        icmp_type=pulumi.get(__response__, 'icmp_type'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        nic_id=pulumi.get(__response__, 'nic_id'),
        port_range_end=pulumi.get(__response__, 'port_range_end'),
        port_range_start=pulumi.get(__response__, 'port_range_start'),
        protocol=pulumi.get(__response__, 'protocol'),
        server_id=pulumi.get(__response__, 'server_id'),
        source_ip=pulumi.get(__response__, 'source_ip'),
        source_mac=pulumi.get(__response__, 'source_mac'),
        target_ip=pulumi.get(__response__, 'target_ip'),
        type=pulumi.get(__response__, 'type')))
