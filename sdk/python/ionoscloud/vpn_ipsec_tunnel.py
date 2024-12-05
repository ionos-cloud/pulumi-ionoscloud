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
from . import outputs
from ._inputs import *

__all__ = ['VpnIpsecTunnelArgs', 'VpnIpsecTunnel']

@pulumi.input_type
class VpnIpsecTunnelArgs:
    def __init__(__self__, *,
                 auth: pulumi.Input['VpnIpsecTunnelAuthArgs'],
                 cloud_network_cidrs: pulumi.Input[Sequence[pulumi.Input[str]]],
                 esps: pulumi.Input[Sequence[pulumi.Input['VpnIpsecTunnelEspArgs']]],
                 gateway_id: pulumi.Input[str],
                 ike: pulumi.Input['VpnIpsecTunnelIkeArgs'],
                 location: pulumi.Input[str],
                 peer_network_cidrs: pulumi.Input[Sequence[pulumi.Input[str]]],
                 remote_host: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VpnIpsecTunnel resource.
        :param pulumi.Input['VpnIpsecTunnelAuthArgs'] auth: [string] Properties with all data needed to define IPSec Authentication. Minimum items: 1. Maximum
               items: 1.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cloud_network_cidrs: [list] The network CIDRs on the "Left" side that are allowed to connect to the IPSec
               tunnel, i.e. the CIDRs within your IONOS Cloud LAN. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1.
               Maximum items: 20.
        :param pulumi.Input[Sequence[pulumi.Input['VpnIpsecTunnelEspArgs']]] esps: [list] Settings for the IPSec SA (ESP) phase. Minimum items: 1. Maximum items: 1.
        :param pulumi.Input[str] gateway_id: [string] The ID of the IPSec Gateway that the tunnel belongs to.
        :param pulumi.Input['VpnIpsecTunnelIkeArgs'] ike: [list] Settings for the initial security exchange phase. Minimum items: 1. Maximum items: 1.
        :param pulumi.Input[str] location: [string] The location of the IPSec Gateway Tunnel. Supported locations: de/fra, de/txl, es/vit,
               gb/lhr, us/ewr, us/las, us/mci, fr/par
        :param pulumi.Input[Sequence[pulumi.Input[str]]] peer_network_cidrs: [list] The network CIDRs on the "Right" side that are allowed to connect to the IPSec
               tunnel. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1. Maximum items: 20.
        :param pulumi.Input[str] remote_host: [string] The remote peer host fully qualified domain name or public IPV4 IP to connect to.
        :param pulumi.Input[str] description: [string] The human-readable description of your IPSec Gateway Tunnel.
        :param pulumi.Input[str] name: [string] The name of the IPSec Gateway Tunnel.
        """
        pulumi.set(__self__, "auth", auth)
        pulumi.set(__self__, "cloud_network_cidrs", cloud_network_cidrs)
        pulumi.set(__self__, "esps", esps)
        pulumi.set(__self__, "gateway_id", gateway_id)
        pulumi.set(__self__, "ike", ike)
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "peer_network_cidrs", peer_network_cidrs)
        pulumi.set(__self__, "remote_host", remote_host)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def auth(self) -> pulumi.Input['VpnIpsecTunnelAuthArgs']:
        """
        [string] Properties with all data needed to define IPSec Authentication. Minimum items: 1. Maximum
        items: 1.
        """
        return pulumi.get(self, "auth")

    @auth.setter
    def auth(self, value: pulumi.Input['VpnIpsecTunnelAuthArgs']):
        pulumi.set(self, "auth", value)

    @property
    @pulumi.getter(name="cloudNetworkCidrs")
    def cloud_network_cidrs(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        [list] The network CIDRs on the "Left" side that are allowed to connect to the IPSec
        tunnel, i.e. the CIDRs within your IONOS Cloud LAN. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1.
        Maximum items: 20.
        """
        return pulumi.get(self, "cloud_network_cidrs")

    @cloud_network_cidrs.setter
    def cloud_network_cidrs(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "cloud_network_cidrs", value)

    @property
    @pulumi.getter
    def esps(self) -> pulumi.Input[Sequence[pulumi.Input['VpnIpsecTunnelEspArgs']]]:
        """
        [list] Settings for the IPSec SA (ESP) phase. Minimum items: 1. Maximum items: 1.
        """
        return pulumi.get(self, "esps")

    @esps.setter
    def esps(self, value: pulumi.Input[Sequence[pulumi.Input['VpnIpsecTunnelEspArgs']]]):
        pulumi.set(self, "esps", value)

    @property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> pulumi.Input[str]:
        """
        [string] The ID of the IPSec Gateway that the tunnel belongs to.
        """
        return pulumi.get(self, "gateway_id")

    @gateway_id.setter
    def gateway_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "gateway_id", value)

    @property
    @pulumi.getter
    def ike(self) -> pulumi.Input['VpnIpsecTunnelIkeArgs']:
        """
        [list] Settings for the initial security exchange phase. Minimum items: 1. Maximum items: 1.
        """
        return pulumi.get(self, "ike")

    @ike.setter
    def ike(self, value: pulumi.Input['VpnIpsecTunnelIkeArgs']):
        pulumi.set(self, "ike", value)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        [string] The location of the IPSec Gateway Tunnel. Supported locations: de/fra, de/txl, es/vit,
        gb/lhr, us/ewr, us/las, us/mci, fr/par
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="peerNetworkCidrs")
    def peer_network_cidrs(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        [list] The network CIDRs on the "Right" side that are allowed to connect to the IPSec
        tunnel. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1. Maximum items: 20.
        """
        return pulumi.get(self, "peer_network_cidrs")

    @peer_network_cidrs.setter
    def peer_network_cidrs(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "peer_network_cidrs", value)

    @property
    @pulumi.getter(name="remoteHost")
    def remote_host(self) -> pulumi.Input[str]:
        """
        [string] The remote peer host fully qualified domain name or public IPV4 IP to connect to.
        """
        return pulumi.get(self, "remote_host")

    @remote_host.setter
    def remote_host(self, value: pulumi.Input[str]):
        pulumi.set(self, "remote_host", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The human-readable description of your IPSec Gateway Tunnel.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The name of the IPSec Gateway Tunnel.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _VpnIpsecTunnelState:
    def __init__(__self__, *,
                 auth: Optional[pulumi.Input['VpnIpsecTunnelAuthArgs']] = None,
                 cloud_network_cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 esps: Optional[pulumi.Input[Sequence[pulumi.Input['VpnIpsecTunnelEspArgs']]]] = None,
                 gateway_id: Optional[pulumi.Input[str]] = None,
                 ike: Optional[pulumi.Input['VpnIpsecTunnelIkeArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 peer_network_cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 remote_host: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VpnIpsecTunnel resources.
        :param pulumi.Input['VpnIpsecTunnelAuthArgs'] auth: [string] Properties with all data needed to define IPSec Authentication. Minimum items: 1. Maximum
               items: 1.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cloud_network_cidrs: [list] The network CIDRs on the "Left" side that are allowed to connect to the IPSec
               tunnel, i.e. the CIDRs within your IONOS Cloud LAN. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1.
               Maximum items: 20.
        :param pulumi.Input[str] description: [string] The human-readable description of your IPSec Gateway Tunnel.
        :param pulumi.Input[Sequence[pulumi.Input['VpnIpsecTunnelEspArgs']]] esps: [list] Settings for the IPSec SA (ESP) phase. Minimum items: 1. Maximum items: 1.
        :param pulumi.Input[str] gateway_id: [string] The ID of the IPSec Gateway that the tunnel belongs to.
        :param pulumi.Input['VpnIpsecTunnelIkeArgs'] ike: [list] Settings for the initial security exchange phase. Minimum items: 1. Maximum items: 1.
        :param pulumi.Input[str] location: [string] The location of the IPSec Gateway Tunnel. Supported locations: de/fra, de/txl, es/vit,
               gb/lhr, us/ewr, us/las, us/mci, fr/par
        :param pulumi.Input[str] name: [string] The name of the IPSec Gateway Tunnel.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] peer_network_cidrs: [list] The network CIDRs on the "Right" side that are allowed to connect to the IPSec
               tunnel. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1. Maximum items: 20.
        :param pulumi.Input[str] remote_host: [string] The remote peer host fully qualified domain name or public IPV4 IP to connect to.
        """
        if auth is not None:
            pulumi.set(__self__, "auth", auth)
        if cloud_network_cidrs is not None:
            pulumi.set(__self__, "cloud_network_cidrs", cloud_network_cidrs)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if esps is not None:
            pulumi.set(__self__, "esps", esps)
        if gateway_id is not None:
            pulumi.set(__self__, "gateway_id", gateway_id)
        if ike is not None:
            pulumi.set(__self__, "ike", ike)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if peer_network_cidrs is not None:
            pulumi.set(__self__, "peer_network_cidrs", peer_network_cidrs)
        if remote_host is not None:
            pulumi.set(__self__, "remote_host", remote_host)

    @property
    @pulumi.getter
    def auth(self) -> Optional[pulumi.Input['VpnIpsecTunnelAuthArgs']]:
        """
        [string] Properties with all data needed to define IPSec Authentication. Minimum items: 1. Maximum
        items: 1.
        """
        return pulumi.get(self, "auth")

    @auth.setter
    def auth(self, value: Optional[pulumi.Input['VpnIpsecTunnelAuthArgs']]):
        pulumi.set(self, "auth", value)

    @property
    @pulumi.getter(name="cloudNetworkCidrs")
    def cloud_network_cidrs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        [list] The network CIDRs on the "Left" side that are allowed to connect to the IPSec
        tunnel, i.e. the CIDRs within your IONOS Cloud LAN. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1.
        Maximum items: 20.
        """
        return pulumi.get(self, "cloud_network_cidrs")

    @cloud_network_cidrs.setter
    def cloud_network_cidrs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "cloud_network_cidrs", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The human-readable description of your IPSec Gateway Tunnel.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def esps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VpnIpsecTunnelEspArgs']]]]:
        """
        [list] Settings for the IPSec SA (ESP) phase. Minimum items: 1. Maximum items: 1.
        """
        return pulumi.get(self, "esps")

    @esps.setter
    def esps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VpnIpsecTunnelEspArgs']]]]):
        pulumi.set(self, "esps", value)

    @property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The ID of the IPSec Gateway that the tunnel belongs to.
        """
        return pulumi.get(self, "gateway_id")

    @gateway_id.setter
    def gateway_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gateway_id", value)

    @property
    @pulumi.getter
    def ike(self) -> Optional[pulumi.Input['VpnIpsecTunnelIkeArgs']]:
        """
        [list] Settings for the initial security exchange phase. Minimum items: 1. Maximum items: 1.
        """
        return pulumi.get(self, "ike")

    @ike.setter
    def ike(self, value: Optional[pulumi.Input['VpnIpsecTunnelIkeArgs']]):
        pulumi.set(self, "ike", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The location of the IPSec Gateway Tunnel. Supported locations: de/fra, de/txl, es/vit,
        gb/lhr, us/ewr, us/las, us/mci, fr/par
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The name of the IPSec Gateway Tunnel.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="peerNetworkCidrs")
    def peer_network_cidrs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        [list] The network CIDRs on the "Right" side that are allowed to connect to the IPSec
        tunnel. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1. Maximum items: 20.
        """
        return pulumi.get(self, "peer_network_cidrs")

    @peer_network_cidrs.setter
    def peer_network_cidrs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "peer_network_cidrs", value)

    @property
    @pulumi.getter(name="remoteHost")
    def remote_host(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The remote peer host fully qualified domain name or public IPV4 IP to connect to.
        """
        return pulumi.get(self, "remote_host")

    @remote_host.setter
    def remote_host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remote_host", value)


class VpnIpsecTunnel(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth: Optional[pulumi.Input[Union['VpnIpsecTunnelAuthArgs', 'VpnIpsecTunnelAuthArgsDict']]] = None,
                 cloud_network_cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 esps: Optional[pulumi.Input[Sequence[pulumi.Input[Union['VpnIpsecTunnelEspArgs', 'VpnIpsecTunnelEspArgsDict']]]]] = None,
                 gateway_id: Optional[pulumi.Input[str]] = None,
                 ike: Optional[pulumi.Input[Union['VpnIpsecTunnelIkeArgs', 'VpnIpsecTunnelIkeArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 peer_network_cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 remote_host: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An IPSec Gateway Tunnel resource manages the creation, management, and deletion of VPN IPSec Gateway Tunnels within the
        IONOS Cloud infrastructure. This resource facilitates the creation of VPN IPSec Gateway Tunnels, enabling secure
        connections between your network resources.

        ## Usage example

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ionoscloud as ionoscloud

        # Basic example
        test_datacenter = ionoscloud.compute.Datacenter("testDatacenter", location="de/fra")
        test_lan = ionoscloud.compute.Lan("testLan",
            public=False,
            datacenter_id=test_datacenter.id)
        test_ipblock = ionoscloud.compute.IPBlock("testIpblock",
            location="de/fra",
            size=1)
        example_vpn_ipsec_gateway = ionoscloud.VpnIpsecGateway("exampleVpnIpsecGateway",
            location="de/fra",
            gateway_ip=test_ipblock.ips[0],
            version="IKEv2",
            description="This gateway connects site A to VDC X.",
            connections=[ionoscloud.VpnIpsecGatewayConnectionArgs(
                datacenter_id=test_datacenter.id,
                lan_id=test_lan.id,
                ipv4_cidr="192.168.100.10/24",
            )])
        example_vpn_ipsec_tunnel = ionoscloud.VpnIpsecTunnel("exampleVpnIpsecTunnel",
            location="de/fra",
            gateway_id=example_vpn_ipsec_gateway.id,
            remote_host="vpn.mycompany.com",
            description="Allows local subnet X to connect to virtual network Y.",
            auth=ionoscloud.VpnIpsecTunnelAuthArgs(
                method="PSK",
                psk_key="X2wosbaw74M8hQGbK3jCCaEusR6CCFRa",
            ),
            ike=ionoscloud.VpnIpsecTunnelIkeArgs(
                diffie_hellman_group="16-MODP4096",
                encryption_algorithm="AES256",
                integrity_algorithm="SHA256",
                lifetime=86400,
            ),
            esps=[ionoscloud.VpnIpsecTunnelEspArgs(
                diffie_hellman_group="16-MODP4096",
                encryption_algorithm="AES256",
                integrity_algorithm="SHA256",
                lifetime=3600,
            )],
            cloud_network_cidrs=["0.0.0.0/0"],
            peer_network_cidrs=["1.2.3.4/32"])
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        The resource can be imported using the `location`, `gateway_id` and `tunnel_id`, for example:

        ```sh
        $ pulumi import ionoscloud:index/vpnIpsecTunnel:VpnIpsecTunnel example {location}:{gateway_id}:{tunnel_id}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['VpnIpsecTunnelAuthArgs', 'VpnIpsecTunnelAuthArgsDict']] auth: [string] Properties with all data needed to define IPSec Authentication. Minimum items: 1. Maximum
               items: 1.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cloud_network_cidrs: [list] The network CIDRs on the "Left" side that are allowed to connect to the IPSec
               tunnel, i.e. the CIDRs within your IONOS Cloud LAN. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1.
               Maximum items: 20.
        :param pulumi.Input[str] description: [string] The human-readable description of your IPSec Gateway Tunnel.
        :param pulumi.Input[Sequence[pulumi.Input[Union['VpnIpsecTunnelEspArgs', 'VpnIpsecTunnelEspArgsDict']]]] esps: [list] Settings for the IPSec SA (ESP) phase. Minimum items: 1. Maximum items: 1.
        :param pulumi.Input[str] gateway_id: [string] The ID of the IPSec Gateway that the tunnel belongs to.
        :param pulumi.Input[Union['VpnIpsecTunnelIkeArgs', 'VpnIpsecTunnelIkeArgsDict']] ike: [list] Settings for the initial security exchange phase. Minimum items: 1. Maximum items: 1.
        :param pulumi.Input[str] location: [string] The location of the IPSec Gateway Tunnel. Supported locations: de/fra, de/txl, es/vit,
               gb/lhr, us/ewr, us/las, us/mci, fr/par
        :param pulumi.Input[str] name: [string] The name of the IPSec Gateway Tunnel.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] peer_network_cidrs: [list] The network CIDRs on the "Right" side that are allowed to connect to the IPSec
               tunnel. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1. Maximum items: 20.
        :param pulumi.Input[str] remote_host: [string] The remote peer host fully qualified domain name or public IPV4 IP to connect to.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VpnIpsecTunnelArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An IPSec Gateway Tunnel resource manages the creation, management, and deletion of VPN IPSec Gateway Tunnels within the
        IONOS Cloud infrastructure. This resource facilitates the creation of VPN IPSec Gateway Tunnels, enabling secure
        connections between your network resources.

        ## Usage example

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ionoscloud as ionoscloud

        # Basic example
        test_datacenter = ionoscloud.compute.Datacenter("testDatacenter", location="de/fra")
        test_lan = ionoscloud.compute.Lan("testLan",
            public=False,
            datacenter_id=test_datacenter.id)
        test_ipblock = ionoscloud.compute.IPBlock("testIpblock",
            location="de/fra",
            size=1)
        example_vpn_ipsec_gateway = ionoscloud.VpnIpsecGateway("exampleVpnIpsecGateway",
            location="de/fra",
            gateway_ip=test_ipblock.ips[0],
            version="IKEv2",
            description="This gateway connects site A to VDC X.",
            connections=[ionoscloud.VpnIpsecGatewayConnectionArgs(
                datacenter_id=test_datacenter.id,
                lan_id=test_lan.id,
                ipv4_cidr="192.168.100.10/24",
            )])
        example_vpn_ipsec_tunnel = ionoscloud.VpnIpsecTunnel("exampleVpnIpsecTunnel",
            location="de/fra",
            gateway_id=example_vpn_ipsec_gateway.id,
            remote_host="vpn.mycompany.com",
            description="Allows local subnet X to connect to virtual network Y.",
            auth=ionoscloud.VpnIpsecTunnelAuthArgs(
                method="PSK",
                psk_key="X2wosbaw74M8hQGbK3jCCaEusR6CCFRa",
            ),
            ike=ionoscloud.VpnIpsecTunnelIkeArgs(
                diffie_hellman_group="16-MODP4096",
                encryption_algorithm="AES256",
                integrity_algorithm="SHA256",
                lifetime=86400,
            ),
            esps=[ionoscloud.VpnIpsecTunnelEspArgs(
                diffie_hellman_group="16-MODP4096",
                encryption_algorithm="AES256",
                integrity_algorithm="SHA256",
                lifetime=3600,
            )],
            cloud_network_cidrs=["0.0.0.0/0"],
            peer_network_cidrs=["1.2.3.4/32"])
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        The resource can be imported using the `location`, `gateway_id` and `tunnel_id`, for example:

        ```sh
        $ pulumi import ionoscloud:index/vpnIpsecTunnel:VpnIpsecTunnel example {location}:{gateway_id}:{tunnel_id}
        ```

        :param str resource_name: The name of the resource.
        :param VpnIpsecTunnelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VpnIpsecTunnelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth: Optional[pulumi.Input[Union['VpnIpsecTunnelAuthArgs', 'VpnIpsecTunnelAuthArgsDict']]] = None,
                 cloud_network_cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 esps: Optional[pulumi.Input[Sequence[pulumi.Input[Union['VpnIpsecTunnelEspArgs', 'VpnIpsecTunnelEspArgsDict']]]]] = None,
                 gateway_id: Optional[pulumi.Input[str]] = None,
                 ike: Optional[pulumi.Input[Union['VpnIpsecTunnelIkeArgs', 'VpnIpsecTunnelIkeArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 peer_network_cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 remote_host: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VpnIpsecTunnelArgs.__new__(VpnIpsecTunnelArgs)

            if auth is None and not opts.urn:
                raise TypeError("Missing required property 'auth'")
            __props__.__dict__["auth"] = auth
            if cloud_network_cidrs is None and not opts.urn:
                raise TypeError("Missing required property 'cloud_network_cidrs'")
            __props__.__dict__["cloud_network_cidrs"] = cloud_network_cidrs
            __props__.__dict__["description"] = description
            if esps is None and not opts.urn:
                raise TypeError("Missing required property 'esps'")
            __props__.__dict__["esps"] = esps
            if gateway_id is None and not opts.urn:
                raise TypeError("Missing required property 'gateway_id'")
            __props__.__dict__["gateway_id"] = gateway_id
            if ike is None and not opts.urn:
                raise TypeError("Missing required property 'ike'")
            __props__.__dict__["ike"] = ike
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if peer_network_cidrs is None and not opts.urn:
                raise TypeError("Missing required property 'peer_network_cidrs'")
            __props__.__dict__["peer_network_cidrs"] = peer_network_cidrs
            if remote_host is None and not opts.urn:
                raise TypeError("Missing required property 'remote_host'")
            __props__.__dict__["remote_host"] = remote_host
        super(VpnIpsecTunnel, __self__).__init__(
            'ionoscloud:index/vpnIpsecTunnel:VpnIpsecTunnel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            auth: Optional[pulumi.Input[Union['VpnIpsecTunnelAuthArgs', 'VpnIpsecTunnelAuthArgsDict']]] = None,
            cloud_network_cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            esps: Optional[pulumi.Input[Sequence[pulumi.Input[Union['VpnIpsecTunnelEspArgs', 'VpnIpsecTunnelEspArgsDict']]]]] = None,
            gateway_id: Optional[pulumi.Input[str]] = None,
            ike: Optional[pulumi.Input[Union['VpnIpsecTunnelIkeArgs', 'VpnIpsecTunnelIkeArgsDict']]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            peer_network_cidrs: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            remote_host: Optional[pulumi.Input[str]] = None) -> 'VpnIpsecTunnel':
        """
        Get an existing VpnIpsecTunnel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['VpnIpsecTunnelAuthArgs', 'VpnIpsecTunnelAuthArgsDict']] auth: [string] Properties with all data needed to define IPSec Authentication. Minimum items: 1. Maximum
               items: 1.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cloud_network_cidrs: [list] The network CIDRs on the "Left" side that are allowed to connect to the IPSec
               tunnel, i.e. the CIDRs within your IONOS Cloud LAN. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1.
               Maximum items: 20.
        :param pulumi.Input[str] description: [string] The human-readable description of your IPSec Gateway Tunnel.
        :param pulumi.Input[Sequence[pulumi.Input[Union['VpnIpsecTunnelEspArgs', 'VpnIpsecTunnelEspArgsDict']]]] esps: [list] Settings for the IPSec SA (ESP) phase. Minimum items: 1. Maximum items: 1.
        :param pulumi.Input[str] gateway_id: [string] The ID of the IPSec Gateway that the tunnel belongs to.
        :param pulumi.Input[Union['VpnIpsecTunnelIkeArgs', 'VpnIpsecTunnelIkeArgsDict']] ike: [list] Settings for the initial security exchange phase. Minimum items: 1. Maximum items: 1.
        :param pulumi.Input[str] location: [string] The location of the IPSec Gateway Tunnel. Supported locations: de/fra, de/txl, es/vit,
               gb/lhr, us/ewr, us/las, us/mci, fr/par
        :param pulumi.Input[str] name: [string] The name of the IPSec Gateway Tunnel.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] peer_network_cidrs: [list] The network CIDRs on the "Right" side that are allowed to connect to the IPSec
               tunnel. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1. Maximum items: 20.
        :param pulumi.Input[str] remote_host: [string] The remote peer host fully qualified domain name or public IPV4 IP to connect to.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VpnIpsecTunnelState.__new__(_VpnIpsecTunnelState)

        __props__.__dict__["auth"] = auth
        __props__.__dict__["cloud_network_cidrs"] = cloud_network_cidrs
        __props__.__dict__["description"] = description
        __props__.__dict__["esps"] = esps
        __props__.__dict__["gateway_id"] = gateway_id
        __props__.__dict__["ike"] = ike
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["peer_network_cidrs"] = peer_network_cidrs
        __props__.__dict__["remote_host"] = remote_host
        return VpnIpsecTunnel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def auth(self) -> pulumi.Output['outputs.VpnIpsecTunnelAuth']:
        """
        [string] Properties with all data needed to define IPSec Authentication. Minimum items: 1. Maximum
        items: 1.
        """
        return pulumi.get(self, "auth")

    @property
    @pulumi.getter(name="cloudNetworkCidrs")
    def cloud_network_cidrs(self) -> pulumi.Output[Sequence[str]]:
        """
        [list] The network CIDRs on the "Left" side that are allowed to connect to the IPSec
        tunnel, i.e. the CIDRs within your IONOS Cloud LAN. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1.
        Maximum items: 20.
        """
        return pulumi.get(self, "cloud_network_cidrs")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        [string] The human-readable description of your IPSec Gateway Tunnel.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def esps(self) -> pulumi.Output[Sequence['outputs.VpnIpsecTunnelEsp']]:
        """
        [list] Settings for the IPSec SA (ESP) phase. Minimum items: 1. Maximum items: 1.
        """
        return pulumi.get(self, "esps")

    @property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> pulumi.Output[str]:
        """
        [string] The ID of the IPSec Gateway that the tunnel belongs to.
        """
        return pulumi.get(self, "gateway_id")

    @property
    @pulumi.getter
    def ike(self) -> pulumi.Output['outputs.VpnIpsecTunnelIke']:
        """
        [list] Settings for the initial security exchange phase. Minimum items: 1. Maximum items: 1.
        """
        return pulumi.get(self, "ike")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        [string] The location of the IPSec Gateway Tunnel. Supported locations: de/fra, de/txl, es/vit,
        gb/lhr, us/ewr, us/las, us/mci, fr/par
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        [string] The name of the IPSec Gateway Tunnel.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="peerNetworkCidrs")
    def peer_network_cidrs(self) -> pulumi.Output[Sequence[str]]:
        """
        [list] The network CIDRs on the "Right" side that are allowed to connect to the IPSec
        tunnel. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1. Maximum items: 20.
        """
        return pulumi.get(self, "peer_network_cidrs")

    @property
    @pulumi.getter(name="remoteHost")
    def remote_host(self) -> pulumi.Output[str]:
        """
        [string] The remote peer host fully qualified domain name or public IPV4 IP to connect to.
        """
        return pulumi.get(self, "remote_host")

