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
from . import _utilities
from . import outputs

__all__ = [
    'GetNicResult',
    'AwaitableGetNicResult',
    'get_nic',
    'get_nic_output',
]

@pulumi.output_type
class GetNicResult:
    """
    A collection of values returned by getNic.
    """
    def __init__(__self__, datacenter_id=None, device_number=None, dhcp=None, dhcpv6=None, firewall_active=None, firewall_type=None, flowlogs=None, id=None, ips=None, ipv6_cidr_block=None, ipv6_ips=None, lan=None, mac=None, name=None, pci_slot=None, server_id=None):
        if datacenter_id and not isinstance(datacenter_id, str):
            raise TypeError("Expected argument 'datacenter_id' to be a str")
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        if device_number and not isinstance(device_number, int):
            raise TypeError("Expected argument 'device_number' to be a int")
        pulumi.set(__self__, "device_number", device_number)
        if dhcp and not isinstance(dhcp, bool):
            raise TypeError("Expected argument 'dhcp' to be a bool")
        pulumi.set(__self__, "dhcp", dhcp)
        if dhcpv6 and not isinstance(dhcpv6, bool):
            raise TypeError("Expected argument 'dhcpv6' to be a bool")
        pulumi.set(__self__, "dhcpv6", dhcpv6)
        if firewall_active and not isinstance(firewall_active, bool):
            raise TypeError("Expected argument 'firewall_active' to be a bool")
        pulumi.set(__self__, "firewall_active", firewall_active)
        if firewall_type and not isinstance(firewall_type, str):
            raise TypeError("Expected argument 'firewall_type' to be a str")
        pulumi.set(__self__, "firewall_type", firewall_type)
        if flowlogs and not isinstance(flowlogs, list):
            raise TypeError("Expected argument 'flowlogs' to be a list")
        pulumi.set(__self__, "flowlogs", flowlogs)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ips and not isinstance(ips, list):
            raise TypeError("Expected argument 'ips' to be a list")
        pulumi.set(__self__, "ips", ips)
        if ipv6_cidr_block and not isinstance(ipv6_cidr_block, str):
            raise TypeError("Expected argument 'ipv6_cidr_block' to be a str")
        pulumi.set(__self__, "ipv6_cidr_block", ipv6_cidr_block)
        if ipv6_ips and not isinstance(ipv6_ips, list):
            raise TypeError("Expected argument 'ipv6_ips' to be a list")
        pulumi.set(__self__, "ipv6_ips", ipv6_ips)
        if lan and not isinstance(lan, int):
            raise TypeError("Expected argument 'lan' to be a int")
        pulumi.set(__self__, "lan", lan)
        if mac and not isinstance(mac, str):
            raise TypeError("Expected argument 'mac' to be a str")
        pulumi.set(__self__, "mac", mac)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if pci_slot and not isinstance(pci_slot, int):
            raise TypeError("Expected argument 'pci_slot' to be a int")
        pulumi.set(__self__, "pci_slot", pci_slot)
        if server_id and not isinstance(server_id, str):
            raise TypeError("Expected argument 'server_id' to be a str")
        pulumi.set(__self__, "server_id", server_id)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> str:
        """
        The ID of a Virtual Data Center.
        """
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter(name="deviceNumber")
    def device_number(self) -> int:
        """
        The Logical Unit Number (LUN) of the storage volume. Null if this NIC was created from CloudAPI and no DCD changes were done on the Datacenter.
        """
        return pulumi.get(self, "device_number")

    @property
    @pulumi.getter
    def dhcp(self) -> Optional[bool]:
        """
        Indicates if the NIC should get an IP address using DHCP (true) or not (false).
        """
        return pulumi.get(self, "dhcp")

    @property
    @pulumi.getter
    def dhcpv6(self) -> Optional[bool]:
        return pulumi.get(self, "dhcpv6")

    @property
    @pulumi.getter(name="firewallActive")
    def firewall_active(self) -> Optional[bool]:
        """
        If this resource is set to true and is nested under a server resource firewall, with open SSH port, resource must be nested under the NIC.
        """
        return pulumi.get(self, "firewall_active")

    @property
    @pulumi.getter(name="firewallType")
    def firewall_type(self) -> str:
        """
        The type of firewall rules that will be allowed on the NIC. If it is not specified it will take the default value INGRESS
        """
        return pulumi.get(self, "firewall_type")

    @property
    @pulumi.getter
    def flowlogs(self) -> Sequence['outputs.GetNicFlowlogResult']:
        """
        Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
        """
        return pulumi.get(self, "flowlogs")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The id of the NIC.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ips(self) -> Sequence[str]:
        """
        Collection of IP addresses assigned to a nic. Explicitly assigned public IPs need to come from reserved IP blocks, Passing value null or empty array will assign an IP address automatically.
        """
        return pulumi.get(self, "ips")

    @property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> str:
        return pulumi.get(self, "ipv6_cidr_block")

    @property
    @pulumi.getter(name="ipv6Ips")
    def ipv6_ips(self) -> Sequence[str]:
        return pulumi.get(self, "ipv6_ips")

    @property
    @pulumi.getter
    def lan(self) -> Optional[int]:
        """
        The LAN ID the NIC will sit on.
        """
        return pulumi.get(self, "lan")

    @property
    @pulumi.getter
    def mac(self) -> str:
        """
        The MAC address of the NIC.
        """
        return pulumi.get(self, "mac")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Specifies the name of the flow log.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="pciSlot")
    def pci_slot(self) -> int:
        """
        The PCI slot number of the Nic.
        """
        return pulumi.get(self, "pci_slot")

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> str:
        """
        The ID of a server.
        """
        return pulumi.get(self, "server_id")


class AwaitableGetNicResult(GetNicResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNicResult(
            datacenter_id=self.datacenter_id,
            device_number=self.device_number,
            dhcp=self.dhcp,
            dhcpv6=self.dhcpv6,
            firewall_active=self.firewall_active,
            firewall_type=self.firewall_type,
            flowlogs=self.flowlogs,
            id=self.id,
            ips=self.ips,
            ipv6_cidr_block=self.ipv6_cidr_block,
            ipv6_ips=self.ipv6_ips,
            lan=self.lan,
            mac=self.mac,
            name=self.name,
            pci_slot=self.pci_slot,
            server_id=self.server_id)


def get_nic(datacenter_id: Optional[str] = None,
            dhcp: Optional[bool] = None,
            dhcpv6: Optional[bool] = None,
            firewall_active: Optional[bool] = None,
            firewall_type: Optional[str] = None,
            id: Optional[str] = None,
            ips: Optional[Sequence[str]] = None,
            ipv6_cidr_block: Optional[str] = None,
            ipv6_ips: Optional[Sequence[str]] = None,
            lan: Optional[int] = None,
            name: Optional[str] = None,
            server_id: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNicResult:
    """
    The **Nic data source** can be used to search for and return existing nics.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage


    :param str datacenter_id: [string] The ID of a Virtual Data Center.
    :param bool dhcp: Indicates if the NIC should get an IP address using DHCP (true) or not (false).
    :param bool firewall_active: If this resource is set to true and is nested under a server resource firewall, with open SSH port, resource must be nested under the NIC.
    :param str firewall_type: The type of firewall rules that will be allowed on the NIC. If it is not specified it will take the default value INGRESS
    :param str id: ID of the nic you want to search for.
           
           `datacenter_id` and either `name` or `id` must be provided.
           If none, are provided, the datasource will return an error.
    :param Sequence[str] ips: Collection of IP addresses assigned to a nic. Explicitly assigned public IPs need to come from reserved IP blocks, Passing value null or empty array will assign an IP address automatically.
    :param int lan: The LAN ID the NIC will sit on.
    :param str name: [string] The name of the LAN.
    :param str server_id: [string] The ID of a server.
    """
    __args__ = dict()
    __args__['datacenterId'] = datacenter_id
    __args__['dhcp'] = dhcp
    __args__['dhcpv6'] = dhcpv6
    __args__['firewallActive'] = firewall_active
    __args__['firewallType'] = firewall_type
    __args__['id'] = id
    __args__['ips'] = ips
    __args__['ipv6CidrBlock'] = ipv6_cidr_block
    __args__['ipv6Ips'] = ipv6_ips
    __args__['lan'] = lan
    __args__['name'] = name
    __args__['serverId'] = server_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getNic:getNic', __args__, opts=opts, typ=GetNicResult).value

    return AwaitableGetNicResult(
        datacenter_id=pulumi.get(__ret__, 'datacenter_id'),
        device_number=pulumi.get(__ret__, 'device_number'),
        dhcp=pulumi.get(__ret__, 'dhcp'),
        dhcpv6=pulumi.get(__ret__, 'dhcpv6'),
        firewall_active=pulumi.get(__ret__, 'firewall_active'),
        firewall_type=pulumi.get(__ret__, 'firewall_type'),
        flowlogs=pulumi.get(__ret__, 'flowlogs'),
        id=pulumi.get(__ret__, 'id'),
        ips=pulumi.get(__ret__, 'ips'),
        ipv6_cidr_block=pulumi.get(__ret__, 'ipv6_cidr_block'),
        ipv6_ips=pulumi.get(__ret__, 'ipv6_ips'),
        lan=pulumi.get(__ret__, 'lan'),
        mac=pulumi.get(__ret__, 'mac'),
        name=pulumi.get(__ret__, 'name'),
        pci_slot=pulumi.get(__ret__, 'pci_slot'),
        server_id=pulumi.get(__ret__, 'server_id'))
def get_nic_output(datacenter_id: Optional[pulumi.Input[str]] = None,
                   dhcp: Optional[pulumi.Input[Optional[bool]]] = None,
                   dhcpv6: Optional[pulumi.Input[Optional[bool]]] = None,
                   firewall_active: Optional[pulumi.Input[Optional[bool]]] = None,
                   firewall_type: Optional[pulumi.Input[Optional[str]]] = None,
                   id: Optional[pulumi.Input[Optional[str]]] = None,
                   ips: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                   ipv6_cidr_block: Optional[pulumi.Input[Optional[str]]] = None,
                   ipv6_ips: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                   lan: Optional[pulumi.Input[Optional[int]]] = None,
                   name: Optional[pulumi.Input[Optional[str]]] = None,
                   server_id: Optional[pulumi.Input[str]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNicResult]:
    """
    The **Nic data source** can be used to search for and return existing nics.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage


    :param str datacenter_id: [string] The ID of a Virtual Data Center.
    :param bool dhcp: Indicates if the NIC should get an IP address using DHCP (true) or not (false).
    :param bool firewall_active: If this resource is set to true and is nested under a server resource firewall, with open SSH port, resource must be nested under the NIC.
    :param str firewall_type: The type of firewall rules that will be allowed on the NIC. If it is not specified it will take the default value INGRESS
    :param str id: ID of the nic you want to search for.
           
           `datacenter_id` and either `name` or `id` must be provided.
           If none, are provided, the datasource will return an error.
    :param Sequence[str] ips: Collection of IP addresses assigned to a nic. Explicitly assigned public IPs need to come from reserved IP blocks, Passing value null or empty array will assign an IP address automatically.
    :param int lan: The LAN ID the NIC will sit on.
    :param str name: [string] The name of the LAN.
    :param str server_id: [string] The ID of a server.
    """
    __args__ = dict()
    __args__['datacenterId'] = datacenter_id
    __args__['dhcp'] = dhcp
    __args__['dhcpv6'] = dhcpv6
    __args__['firewallActive'] = firewall_active
    __args__['firewallType'] = firewall_type
    __args__['id'] = id
    __args__['ips'] = ips
    __args__['ipv6CidrBlock'] = ipv6_cidr_block
    __args__['ipv6Ips'] = ipv6_ips
    __args__['lan'] = lan
    __args__['name'] = name
    __args__['serverId'] = server_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:index/getNic:getNic', __args__, opts=opts, typ=GetNicResult)
    return __ret__.apply(lambda __response__: GetNicResult(
        datacenter_id=pulumi.get(__response__, 'datacenter_id'),
        device_number=pulumi.get(__response__, 'device_number'),
        dhcp=pulumi.get(__response__, 'dhcp'),
        dhcpv6=pulumi.get(__response__, 'dhcpv6'),
        firewall_active=pulumi.get(__response__, 'firewall_active'),
        firewall_type=pulumi.get(__response__, 'firewall_type'),
        flowlogs=pulumi.get(__response__, 'flowlogs'),
        id=pulumi.get(__response__, 'id'),
        ips=pulumi.get(__response__, 'ips'),
        ipv6_cidr_block=pulumi.get(__response__, 'ipv6_cidr_block'),
        ipv6_ips=pulumi.get(__response__, 'ipv6_ips'),
        lan=pulumi.get(__response__, 'lan'),
        mac=pulumi.get(__response__, 'mac'),
        name=pulumi.get(__response__, 'name'),
        pci_slot=pulumi.get(__response__, 'pci_slot'),
        server_id=pulumi.get(__response__, 'server_id')))
