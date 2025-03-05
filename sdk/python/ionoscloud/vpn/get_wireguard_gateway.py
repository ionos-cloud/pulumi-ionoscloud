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
    'GetWireguardGatewayResult',
    'AwaitableGetWireguardGatewayResult',
    'get_wireguard_gateway',
    'get_wireguard_gateway_output',
]

@pulumi.output_type
class GetWireguardGatewayResult:
    """
    A collection of values returned by getWireguardGateway.
    """
    def __init__(__self__, connections=None, description=None, gateway_ip=None, id=None, interface_ipv4_cidr=None, interface_ipv6_cidr=None, listen_port=None, location=None, maintenance_windows=None, name=None, public_key=None, status=None, tier=None):
        if connections and not isinstance(connections, list):
            raise TypeError("Expected argument 'connections' to be a list")
        pulumi.set(__self__, "connections", connections)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if gateway_ip and not isinstance(gateway_ip, str):
            raise TypeError("Expected argument 'gateway_ip' to be a str")
        pulumi.set(__self__, "gateway_ip", gateway_ip)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if interface_ipv4_cidr and not isinstance(interface_ipv4_cidr, str):
            raise TypeError("Expected argument 'interface_ipv4_cidr' to be a str")
        pulumi.set(__self__, "interface_ipv4_cidr", interface_ipv4_cidr)
        if interface_ipv6_cidr and not isinstance(interface_ipv6_cidr, str):
            raise TypeError("Expected argument 'interface_ipv6_cidr' to be a str")
        pulumi.set(__self__, "interface_ipv6_cidr", interface_ipv6_cidr)
        if listen_port and not isinstance(listen_port, int):
            raise TypeError("Expected argument 'listen_port' to be a int")
        pulumi.set(__self__, "listen_port", listen_port)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if maintenance_windows and not isinstance(maintenance_windows, list):
            raise TypeError("Expected argument 'maintenance_windows' to be a list")
        pulumi.set(__self__, "maintenance_windows", maintenance_windows)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if public_key and not isinstance(public_key, str):
            raise TypeError("Expected argument 'public_key' to be a str")
        pulumi.set(__self__, "public_key", public_key)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tier and not isinstance(tier, str):
            raise TypeError("Expected argument 'tier' to be a str")
        pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def connections(self) -> Sequence['outputs.GetWireguardGatewayConnectionResult']:
        """
        A list of connection configurations for the WireGuard Gateway. Each `connections` block contains:
        """
        return pulumi.get(self, "connections")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the WireGuard Gateway.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="gatewayIp")
    def gateway_ip(self) -> str:
        """
        The IP address of the WireGuard Gateway.
        """
        return pulumi.get(self, "gateway_ip")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="interfaceIpv4Cidr")
    def interface_ipv4_cidr(self) -> str:
        """
        The IPv4 CIDR for the WireGuard Gateway interface.
        """
        return pulumi.get(self, "interface_ipv4_cidr")

    @property
    @pulumi.getter(name="interfaceIpv6Cidr")
    def interface_ipv6_cidr(self) -> str:
        """
        The IPv6 CIDR for the WireGuard Gateway interface.
        """
        return pulumi.get(self, "interface_ipv6_cidr")

    @property
    @pulumi.getter(name="listenPort")
    def listen_port(self) -> int:
        return pulumi.get(self, "listen_port")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(self) -> Sequence['outputs.GetWireguardGatewayMaintenanceWindowResult']:
        """
        A weekly 4 hour-long window, during which maintenance might occur.
        """
        return pulumi.get(self, "maintenance_windows")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> str:
        """
        The public key for the WireGuard Gateway.
        """
        return pulumi.get(self, "public_key")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The current status of the WireGuard Gateway.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tier(self) -> str:
        """
        Gateway performance options.
        """
        return pulumi.get(self, "tier")


class AwaitableGetWireguardGatewayResult(GetWireguardGatewayResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWireguardGatewayResult(
            connections=self.connections,
            description=self.description,
            gateway_ip=self.gateway_ip,
            id=self.id,
            interface_ipv4_cidr=self.interface_ipv4_cidr,
            interface_ipv6_cidr=self.interface_ipv6_cidr,
            listen_port=self.listen_port,
            location=self.location,
            maintenance_windows=self.maintenance_windows,
            name=self.name,
            public_key=self.public_key,
            status=self.status,
            tier=self.tier)


def get_wireguard_gateway(description: Optional[str] = None,
                          id: Optional[str] = None,
                          location: Optional[str] = None,
                          name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWireguardGatewayResult:
    """
    The `vpn.WireguardGateway` data source provides information about a specific IonosCloud VPN WireGuard Gateway. You can use this data source to retrieve details of a WireGuard Gateway for use in other resources and configurations.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.vpn.get_wireguard_gateway(location="de/fra",
        name="example-gateway")
    pulumi.export("vpnWireguardGatewayPublicKey", example_vpn_wireguard_gateway["publicKey"])
    ```


    :param str description: The description of the WireGuard Gateway.
    :param str id: [String] The ID of the WireGuard Gateway.
    :param str location: [String] The location of the WireGuard Gateway.
    :param str name: [String] The name of the WireGuard Gateway.
    """
    __args__ = dict()
    __args__['description'] = description
    __args__['id'] = id
    __args__['location'] = location
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:vpn/getWireguardGateway:getWireguardGateway', __args__, opts=opts, typ=GetWireguardGatewayResult).value

    return AwaitableGetWireguardGatewayResult(
        connections=pulumi.get(__ret__, 'connections'),
        description=pulumi.get(__ret__, 'description'),
        gateway_ip=pulumi.get(__ret__, 'gateway_ip'),
        id=pulumi.get(__ret__, 'id'),
        interface_ipv4_cidr=pulumi.get(__ret__, 'interface_ipv4_cidr'),
        interface_ipv6_cidr=pulumi.get(__ret__, 'interface_ipv6_cidr'),
        listen_port=pulumi.get(__ret__, 'listen_port'),
        location=pulumi.get(__ret__, 'location'),
        maintenance_windows=pulumi.get(__ret__, 'maintenance_windows'),
        name=pulumi.get(__ret__, 'name'),
        public_key=pulumi.get(__ret__, 'public_key'),
        status=pulumi.get(__ret__, 'status'),
        tier=pulumi.get(__ret__, 'tier'))
def get_wireguard_gateway_output(description: Optional[pulumi.Input[Optional[str]]] = None,
                                 id: Optional[pulumi.Input[Optional[str]]] = None,
                                 location: Optional[pulumi.Input[Optional[str]]] = None,
                                 name: Optional[pulumi.Input[Optional[str]]] = None,
                                 opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetWireguardGatewayResult]:
    """
    The `vpn.WireguardGateway` data source provides information about a specific IonosCloud VPN WireGuard Gateway. You can use this data source to retrieve details of a WireGuard Gateway for use in other resources and configurations.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.vpn.get_wireguard_gateway(location="de/fra",
        name="example-gateway")
    pulumi.export("vpnWireguardGatewayPublicKey", example_vpn_wireguard_gateway["publicKey"])
    ```


    :param str description: The description of the WireGuard Gateway.
    :param str id: [String] The ID of the WireGuard Gateway.
    :param str location: [String] The location of the WireGuard Gateway.
    :param str name: [String] The name of the WireGuard Gateway.
    """
    __args__ = dict()
    __args__['description'] = description
    __args__['id'] = id
    __args__['location'] = location
    __args__['name'] = name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:vpn/getWireguardGateway:getWireguardGateway', __args__, opts=opts, typ=GetWireguardGatewayResult)
    return __ret__.apply(lambda __response__: GetWireguardGatewayResult(
        connections=pulumi.get(__response__, 'connections'),
        description=pulumi.get(__response__, 'description'),
        gateway_ip=pulumi.get(__response__, 'gateway_ip'),
        id=pulumi.get(__response__, 'id'),
        interface_ipv4_cidr=pulumi.get(__response__, 'interface_ipv4_cidr'),
        interface_ipv6_cidr=pulumi.get(__response__, 'interface_ipv6_cidr'),
        listen_port=pulumi.get(__response__, 'listen_port'),
        location=pulumi.get(__response__, 'location'),
        maintenance_windows=pulumi.get(__response__, 'maintenance_windows'),
        name=pulumi.get(__response__, 'name'),
        public_key=pulumi.get(__response__, 'public_key'),
        status=pulumi.get(__response__, 'status'),
        tier=pulumi.get(__response__, 'tier')))
