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
    'GetWireguardPeerResult',
    'AwaitableGetWireguardPeerResult',
    'get_wireguard_peer',
    'get_wireguard_peer_output',
]

@pulumi.output_type
class GetWireguardPeerResult:
    """
    A collection of values returned by getWireguardPeer.
    """
    def __init__(__self__, allowed_ips=None, description=None, endpoints=None, gateway_id=None, id=None, location=None, name=None, public_key=None, status=None):
        if allowed_ips and not isinstance(allowed_ips, list):
            raise TypeError("Expected argument 'allowed_ips' to be a list")
        pulumi.set(__self__, "allowed_ips", allowed_ips)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if endpoints and not isinstance(endpoints, list):
            raise TypeError("Expected argument 'endpoints' to be a list")
        pulumi.set(__self__, "endpoints", endpoints)
        if gateway_id and not isinstance(gateway_id, str):
            raise TypeError("Expected argument 'gateway_id' to be a str")
        pulumi.set(__self__, "gateway_id", gateway_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if public_key and not isinstance(public_key, str):
            raise TypeError("Expected argument 'public_key' to be a str")
        pulumi.set(__self__, "public_key", public_key)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="allowedIps")
    def allowed_ips(self) -> Sequence[str]:
        """
        The subnet CIDRs that are allowed to connect to the WireGuard Gateway.
        """
        return pulumi.get(self, "allowed_ips")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the WireGuard Peer.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def endpoints(self) -> Sequence['outputs.GetWireguardPeerEndpointResult']:
        """
        The endpoint of the WireGuard Peer.
        """
        return pulumi.get(self, "endpoints")

    @property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> str:
        return pulumi.get(self, "gateway_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The unique ID of the WireGuard Peer.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the WireGuard Peer.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> str:
        """
        WireGuard public key of the connecting peer.
        """
        return pulumi.get(self, "public_key")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The current status of the WireGuard Peer.
        """
        return pulumi.get(self, "status")


class AwaitableGetWireguardPeerResult(GetWireguardPeerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWireguardPeerResult(
            allowed_ips=self.allowed_ips,
            description=self.description,
            endpoints=self.endpoints,
            gateway_id=self.gateway_id,
            id=self.id,
            location=self.location,
            name=self.name,
            public_key=self.public_key,
            status=self.status)


def get_wireguard_peer(gateway_id: Optional[str] = None,
                       id: Optional[str] = None,
                       location: Optional[str] = None,
                       name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWireguardPeerResult:
    """
    The `vpn.WireguardGateway` data source provides information about a specific IonosCloud VPN WireGuard Gateway. You can use this data source to retrieve details of a WireGuard Gateway for use in other resources and configurations.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.vpn.get_wireguard_peer(location="de/fra",
        gateway_id="example-gateway",
        name="example-peer")
    pulumi.export("vpnWireguardPeerPublicKey", example_vpn_wireguard_peer["publicKey"])
    ```


    :param str gateway_id: [String] The ID of the WireGuard Gateway.
    :param str id: [String] The ID of the WireGuard Peer.
    :param str location: [String] The location of the WireGuard Gateway.
    :param str name: [String] The name of the WireGuard Peer.
    """
    __args__ = dict()
    __args__['gatewayId'] = gateway_id
    __args__['id'] = id
    __args__['location'] = location
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:vpn/getWireguardPeer:getWireguardPeer', __args__, opts=opts, typ=GetWireguardPeerResult).value

    return AwaitableGetWireguardPeerResult(
        allowed_ips=pulumi.get(__ret__, 'allowed_ips'),
        description=pulumi.get(__ret__, 'description'),
        endpoints=pulumi.get(__ret__, 'endpoints'),
        gateway_id=pulumi.get(__ret__, 'gateway_id'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        public_key=pulumi.get(__ret__, 'public_key'),
        status=pulumi.get(__ret__, 'status'))
def get_wireguard_peer_output(gateway_id: Optional[pulumi.Input[str]] = None,
                              id: Optional[pulumi.Input[Optional[str]]] = None,
                              location: Optional[pulumi.Input[Optional[str]]] = None,
                              name: Optional[pulumi.Input[Optional[str]]] = None,
                              opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetWireguardPeerResult]:
    """
    The `vpn.WireguardGateway` data source provides information about a specific IonosCloud VPN WireGuard Gateway. You can use this data source to retrieve details of a WireGuard Gateway for use in other resources and configurations.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.vpn.get_wireguard_peer(location="de/fra",
        gateway_id="example-gateway",
        name="example-peer")
    pulumi.export("vpnWireguardPeerPublicKey", example_vpn_wireguard_peer["publicKey"])
    ```


    :param str gateway_id: [String] The ID of the WireGuard Gateway.
    :param str id: [String] The ID of the WireGuard Peer.
    :param str location: [String] The location of the WireGuard Gateway.
    :param str name: [String] The name of the WireGuard Peer.
    """
    __args__ = dict()
    __args__['gatewayId'] = gateway_id
    __args__['id'] = id
    __args__['location'] = location
    __args__['name'] = name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:vpn/getWireguardPeer:getWireguardPeer', __args__, opts=opts, typ=GetWireguardPeerResult)
    return __ret__.apply(lambda __response__: GetWireguardPeerResult(
        allowed_ips=pulumi.get(__response__, 'allowed_ips'),
        description=pulumi.get(__response__, 'description'),
        endpoints=pulumi.get(__response__, 'endpoints'),
        gateway_id=pulumi.get(__response__, 'gateway_id'),
        id=pulumi.get(__response__, 'id'),
        location=pulumi.get(__response__, 'location'),
        name=pulumi.get(__response__, 'name'),
        public_key=pulumi.get(__response__, 'public_key'),
        status=pulumi.get(__response__, 'status')))
