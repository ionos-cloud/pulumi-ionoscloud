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
from ._inputs import *

__all__ = ['VpnWireguardGatewayArgs', 'VpnWireguardGateway']

@pulumi.input_type
class VpnWireguardGatewayArgs:
    def __init__(__self__, *,
                 connections: pulumi.Input[Sequence[pulumi.Input['VpnWireguardGatewayConnectionArgs']]],
                 gateway_ip: pulumi.Input[str],
                 location: pulumi.Input[str],
                 private_key: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 interface_ipv4_cidr: Optional[pulumi.Input[str]] = None,
                 interface_ipv6_cidr: Optional[pulumi.Input[str]] = None,
                 listen_port: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VpnWireguardGateway resource.
        :param pulumi.Input[Sequence[pulumi.Input['VpnWireguardGatewayConnectionArgs']]] connections: [Block] The connection configuration for the WireGuard Gateway. This block supports fields documented below.
        :param pulumi.Input[str] gateway_ip: [String] The IP address of the WireGuard Gateway.
        :param pulumi.Input[str] location: [String] The location of the WireGuard Gateway.
        :param pulumi.Input[str] private_key: [String] The private key for the WireGuard Gateway. To be created with the wg utility.
        :param pulumi.Input[str] description: [String] A description of the WireGuard Gateway.
        :param pulumi.Input[str] interface_ipv4_cidr: [String] The IPv4 CIDR for the WireGuard Gateway interface.
        :param pulumi.Input[str] interface_ipv6_cidr: [String] The IPv6 CIDR for the WireGuard Gateway interface.
        :param pulumi.Input[str] name: [String] The name of the WireGuard Gateway.
        """
        pulumi.set(__self__, "connections", connections)
        pulumi.set(__self__, "gateway_ip", gateway_ip)
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "private_key", private_key)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if interface_ipv4_cidr is not None:
            pulumi.set(__self__, "interface_ipv4_cidr", interface_ipv4_cidr)
        if interface_ipv6_cidr is not None:
            pulumi.set(__self__, "interface_ipv6_cidr", interface_ipv6_cidr)
        if listen_port is not None:
            pulumi.set(__self__, "listen_port", listen_port)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def connections(self) -> pulumi.Input[Sequence[pulumi.Input['VpnWireguardGatewayConnectionArgs']]]:
        """
        [Block] The connection configuration for the WireGuard Gateway. This block supports fields documented below.
        """
        return pulumi.get(self, "connections")

    @connections.setter
    def connections(self, value: pulumi.Input[Sequence[pulumi.Input['VpnWireguardGatewayConnectionArgs']]]):
        pulumi.set(self, "connections", value)

    @property
    @pulumi.getter(name="gatewayIp")
    def gateway_ip(self) -> pulumi.Input[str]:
        """
        [String] The IP address of the WireGuard Gateway.
        """
        return pulumi.get(self, "gateway_ip")

    @gateway_ip.setter
    def gateway_ip(self, value: pulumi.Input[str]):
        pulumi.set(self, "gateway_ip", value)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        [String] The location of the WireGuard Gateway.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Input[str]:
        """
        [String] The private key for the WireGuard Gateway. To be created with the wg utility.
        """
        return pulumi.get(self, "private_key")

    @private_key.setter
    def private_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "private_key", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        [String] A description of the WireGuard Gateway.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="interfaceIpv4Cidr")
    def interface_ipv4_cidr(self) -> Optional[pulumi.Input[str]]:
        """
        [String] The IPv4 CIDR for the WireGuard Gateway interface.
        """
        return pulumi.get(self, "interface_ipv4_cidr")

    @interface_ipv4_cidr.setter
    def interface_ipv4_cidr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "interface_ipv4_cidr", value)

    @property
    @pulumi.getter(name="interfaceIpv6Cidr")
    def interface_ipv6_cidr(self) -> Optional[pulumi.Input[str]]:
        """
        [String] The IPv6 CIDR for the WireGuard Gateway interface.
        """
        return pulumi.get(self, "interface_ipv6_cidr")

    @interface_ipv6_cidr.setter
    def interface_ipv6_cidr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "interface_ipv6_cidr", value)

    @property
    @pulumi.getter(name="listenPort")
    def listen_port(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "listen_port")

    @listen_port.setter
    def listen_port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "listen_port", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [String] The name of the WireGuard Gateway.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _VpnWireguardGatewayState:
    def __init__(__self__, *,
                 connections: Optional[pulumi.Input[Sequence[pulumi.Input['VpnWireguardGatewayConnectionArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 gateway_ip: Optional[pulumi.Input[str]] = None,
                 interface_ipv4_cidr: Optional[pulumi.Input[str]] = None,
                 interface_ipv6_cidr: Optional[pulumi.Input[str]] = None,
                 listen_port: Optional[pulumi.Input[int]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 public_key: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VpnWireguardGateway resources.
        :param pulumi.Input[Sequence[pulumi.Input['VpnWireguardGatewayConnectionArgs']]] connections: [Block] The connection configuration for the WireGuard Gateway. This block supports fields documented below.
        :param pulumi.Input[str] description: [String] A description of the WireGuard Gateway.
        :param pulumi.Input[str] gateway_ip: [String] The IP address of the WireGuard Gateway.
        :param pulumi.Input[str] interface_ipv4_cidr: [String] The IPv4 CIDR for the WireGuard Gateway interface.
        :param pulumi.Input[str] interface_ipv6_cidr: [String] The IPv6 CIDR for the WireGuard Gateway interface.
        :param pulumi.Input[str] location: [String] The location of the WireGuard Gateway.
        :param pulumi.Input[str] name: [String] The name of the WireGuard Gateway.
        :param pulumi.Input[str] private_key: [String] The private key for the WireGuard Gateway. To be created with the wg utility.
        :param pulumi.Input[str] public_key: (Computed)[String] The public key for the WireGuard Gateway.
        :param pulumi.Input[str] status: (Computed)[String] The current status of the WireGuard Gateway.
        """
        if connections is not None:
            pulumi.set(__self__, "connections", connections)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if gateway_ip is not None:
            pulumi.set(__self__, "gateway_ip", gateway_ip)
        if interface_ipv4_cidr is not None:
            pulumi.set(__self__, "interface_ipv4_cidr", interface_ipv4_cidr)
        if interface_ipv6_cidr is not None:
            pulumi.set(__self__, "interface_ipv6_cidr", interface_ipv6_cidr)
        if listen_port is not None:
            pulumi.set(__self__, "listen_port", listen_port)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if private_key is not None:
            pulumi.set(__self__, "private_key", private_key)
        if public_key is not None:
            pulumi.set(__self__, "public_key", public_key)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VpnWireguardGatewayConnectionArgs']]]]:
        """
        [Block] The connection configuration for the WireGuard Gateway. This block supports fields documented below.
        """
        return pulumi.get(self, "connections")

    @connections.setter
    def connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VpnWireguardGatewayConnectionArgs']]]]):
        pulumi.set(self, "connections", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        [String] A description of the WireGuard Gateway.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="gatewayIp")
    def gateway_ip(self) -> Optional[pulumi.Input[str]]:
        """
        [String] The IP address of the WireGuard Gateway.
        """
        return pulumi.get(self, "gateway_ip")

    @gateway_ip.setter
    def gateway_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gateway_ip", value)

    @property
    @pulumi.getter(name="interfaceIpv4Cidr")
    def interface_ipv4_cidr(self) -> Optional[pulumi.Input[str]]:
        """
        [String] The IPv4 CIDR for the WireGuard Gateway interface.
        """
        return pulumi.get(self, "interface_ipv4_cidr")

    @interface_ipv4_cidr.setter
    def interface_ipv4_cidr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "interface_ipv4_cidr", value)

    @property
    @pulumi.getter(name="interfaceIpv6Cidr")
    def interface_ipv6_cidr(self) -> Optional[pulumi.Input[str]]:
        """
        [String] The IPv6 CIDR for the WireGuard Gateway interface.
        """
        return pulumi.get(self, "interface_ipv6_cidr")

    @interface_ipv6_cidr.setter
    def interface_ipv6_cidr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "interface_ipv6_cidr", value)

    @property
    @pulumi.getter(name="listenPort")
    def listen_port(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "listen_port")

    @listen_port.setter
    def listen_port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "listen_port", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        [String] The location of the WireGuard Gateway.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [String] The name of the WireGuard Gateway.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[str]]:
        """
        [String] The private key for the WireGuard Gateway. To be created with the wg utility.
        """
        return pulumi.get(self, "private_key")

    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_key", value)

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[pulumi.Input[str]]:
        """
        (Computed)[String] The public key for the WireGuard Gateway.
        """
        return pulumi.get(self, "public_key")

    @public_key.setter
    def public_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_key", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        (Computed)[String] The current status of the WireGuard Gateway.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class VpnWireguardGateway(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connections: Optional[pulumi.Input[Sequence[pulumi.Input[Union['VpnWireguardGatewayConnectionArgs', 'VpnWireguardGatewayConnectionArgsDict']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 gateway_ip: Optional[pulumi.Input[str]] = None,
                 interface_ipv4_cidr: Optional[pulumi.Input[str]] = None,
                 interface_ipv6_cidr: Optional[pulumi.Input[str]] = None,
                 listen_port: Optional[pulumi.Input[int]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Overview

        The `VpnWireguardGateway` resource manages a WireGuard Gateway within the IONOS Cloud infrastructure.
        This resource facilitates the creation, management, and deletion of WireGuard VPN Gateways, enabling secure connections between your network resources.

        ## Example Usage

        ```python
        import pulumi
        import ionoscloud as ionoscloud

        datacenter_example = ionoscloud.compute.Datacenter("datacenterExample", location="de/fra")
        ipblock_example = ionoscloud.compute.IPBlock("ipblockExample",
            location="de/fra",
            size=1)
        lan_example = ionoscloud.compute.Lan("lanExample", datacenter_id=datacenter_example.id)
        gateway = ionoscloud.VpnWireguardGateway("gateway",
            location="de/fra",
            description="description",
            private_key="private",
            gateway_ip=ipblock_example.ips[0],
            interface_ipv4_cidr="192.168.1.100/24",
            connections=[{
                "datacenter_id": datacenter_example.id,
                "lan_id": lan_example.id,
                "ipv4_cidr": "192.168.1.108/24",
            }])
        ```

        ## Import

        WireGuard Gateways can be imported using their ID:

        ```sh
        $ pulumi import ionoscloud:index/vpnWireguardGateway:VpnWireguardGateway example_gateway location:id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['VpnWireguardGatewayConnectionArgs', 'VpnWireguardGatewayConnectionArgsDict']]]] connections: [Block] The connection configuration for the WireGuard Gateway. This block supports fields documented below.
        :param pulumi.Input[str] description: [String] A description of the WireGuard Gateway.
        :param pulumi.Input[str] gateway_ip: [String] The IP address of the WireGuard Gateway.
        :param pulumi.Input[str] interface_ipv4_cidr: [String] The IPv4 CIDR for the WireGuard Gateway interface.
        :param pulumi.Input[str] interface_ipv6_cidr: [String] The IPv6 CIDR for the WireGuard Gateway interface.
        :param pulumi.Input[str] location: [String] The location of the WireGuard Gateway.
        :param pulumi.Input[str] name: [String] The name of the WireGuard Gateway.
        :param pulumi.Input[str] private_key: [String] The private key for the WireGuard Gateway. To be created with the wg utility.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VpnWireguardGatewayArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Overview

        The `VpnWireguardGateway` resource manages a WireGuard Gateway within the IONOS Cloud infrastructure.
        This resource facilitates the creation, management, and deletion of WireGuard VPN Gateways, enabling secure connections between your network resources.

        ## Example Usage

        ```python
        import pulumi
        import ionoscloud as ionoscloud

        datacenter_example = ionoscloud.compute.Datacenter("datacenterExample", location="de/fra")
        ipblock_example = ionoscloud.compute.IPBlock("ipblockExample",
            location="de/fra",
            size=1)
        lan_example = ionoscloud.compute.Lan("lanExample", datacenter_id=datacenter_example.id)
        gateway = ionoscloud.VpnWireguardGateway("gateway",
            location="de/fra",
            description="description",
            private_key="private",
            gateway_ip=ipblock_example.ips[0],
            interface_ipv4_cidr="192.168.1.100/24",
            connections=[{
                "datacenter_id": datacenter_example.id,
                "lan_id": lan_example.id,
                "ipv4_cidr": "192.168.1.108/24",
            }])
        ```

        ## Import

        WireGuard Gateways can be imported using their ID:

        ```sh
        $ pulumi import ionoscloud:index/vpnWireguardGateway:VpnWireguardGateway example_gateway location:id
        ```

        :param str resource_name: The name of the resource.
        :param VpnWireguardGatewayArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VpnWireguardGatewayArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connections: Optional[pulumi.Input[Sequence[pulumi.Input[Union['VpnWireguardGatewayConnectionArgs', 'VpnWireguardGatewayConnectionArgsDict']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 gateway_ip: Optional[pulumi.Input[str]] = None,
                 interface_ipv4_cidr: Optional[pulumi.Input[str]] = None,
                 interface_ipv6_cidr: Optional[pulumi.Input[str]] = None,
                 listen_port: Optional[pulumi.Input[int]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VpnWireguardGatewayArgs.__new__(VpnWireguardGatewayArgs)

            if connections is None and not opts.urn:
                raise TypeError("Missing required property 'connections'")
            __props__.__dict__["connections"] = connections
            __props__.__dict__["description"] = description
            if gateway_ip is None and not opts.urn:
                raise TypeError("Missing required property 'gateway_ip'")
            __props__.__dict__["gateway_ip"] = gateway_ip
            __props__.__dict__["interface_ipv4_cidr"] = interface_ipv4_cidr
            __props__.__dict__["interface_ipv6_cidr"] = interface_ipv6_cidr
            __props__.__dict__["listen_port"] = listen_port
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if private_key is None and not opts.urn:
                raise TypeError("Missing required property 'private_key'")
            __props__.__dict__["private_key"] = None if private_key is None else pulumi.Output.secret(private_key)
            __props__.__dict__["public_key"] = None
            __props__.__dict__["status"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["privateKey"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(VpnWireguardGateway, __self__).__init__(
            'ionoscloud:index/vpnWireguardGateway:VpnWireguardGateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            connections: Optional[pulumi.Input[Sequence[pulumi.Input[Union['VpnWireguardGatewayConnectionArgs', 'VpnWireguardGatewayConnectionArgsDict']]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            gateway_ip: Optional[pulumi.Input[str]] = None,
            interface_ipv4_cidr: Optional[pulumi.Input[str]] = None,
            interface_ipv6_cidr: Optional[pulumi.Input[str]] = None,
            listen_port: Optional[pulumi.Input[int]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            private_key: Optional[pulumi.Input[str]] = None,
            public_key: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'VpnWireguardGateway':
        """
        Get an existing VpnWireguardGateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['VpnWireguardGatewayConnectionArgs', 'VpnWireguardGatewayConnectionArgsDict']]]] connections: [Block] The connection configuration for the WireGuard Gateway. This block supports fields documented below.
        :param pulumi.Input[str] description: [String] A description of the WireGuard Gateway.
        :param pulumi.Input[str] gateway_ip: [String] The IP address of the WireGuard Gateway.
        :param pulumi.Input[str] interface_ipv4_cidr: [String] The IPv4 CIDR for the WireGuard Gateway interface.
        :param pulumi.Input[str] interface_ipv6_cidr: [String] The IPv6 CIDR for the WireGuard Gateway interface.
        :param pulumi.Input[str] location: [String] The location of the WireGuard Gateway.
        :param pulumi.Input[str] name: [String] The name of the WireGuard Gateway.
        :param pulumi.Input[str] private_key: [String] The private key for the WireGuard Gateway. To be created with the wg utility.
        :param pulumi.Input[str] public_key: (Computed)[String] The public key for the WireGuard Gateway.
        :param pulumi.Input[str] status: (Computed)[String] The current status of the WireGuard Gateway.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VpnWireguardGatewayState.__new__(_VpnWireguardGatewayState)

        __props__.__dict__["connections"] = connections
        __props__.__dict__["description"] = description
        __props__.__dict__["gateway_ip"] = gateway_ip
        __props__.__dict__["interface_ipv4_cidr"] = interface_ipv4_cidr
        __props__.__dict__["interface_ipv6_cidr"] = interface_ipv6_cidr
        __props__.__dict__["listen_port"] = listen_port
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["private_key"] = private_key
        __props__.__dict__["public_key"] = public_key
        __props__.__dict__["status"] = status
        return VpnWireguardGateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def connections(self) -> pulumi.Output[Sequence['outputs.VpnWireguardGatewayConnection']]:
        """
        [Block] The connection configuration for the WireGuard Gateway. This block supports fields documented below.
        """
        return pulumi.get(self, "connections")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        [String] A description of the WireGuard Gateway.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="gatewayIp")
    def gateway_ip(self) -> pulumi.Output[str]:
        """
        [String] The IP address of the WireGuard Gateway.
        """
        return pulumi.get(self, "gateway_ip")

    @property
    @pulumi.getter(name="interfaceIpv4Cidr")
    def interface_ipv4_cidr(self) -> pulumi.Output[Optional[str]]:
        """
        [String] The IPv4 CIDR for the WireGuard Gateway interface.
        """
        return pulumi.get(self, "interface_ipv4_cidr")

    @property
    @pulumi.getter(name="interfaceIpv6Cidr")
    def interface_ipv6_cidr(self) -> pulumi.Output[Optional[str]]:
        """
        [String] The IPv6 CIDR for the WireGuard Gateway interface.
        """
        return pulumi.get(self, "interface_ipv6_cidr")

    @property
    @pulumi.getter(name="listenPort")
    def listen_port(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "listen_port")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        [String] The location of the WireGuard Gateway.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        [String] The name of the WireGuard Gateway.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Output[str]:
        """
        [String] The private key for the WireGuard Gateway. To be created with the wg utility.
        """
        return pulumi.get(self, "private_key")

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> pulumi.Output[str]:
        """
        (Computed)[String] The public key for the WireGuard Gateway.
        """
        return pulumi.get(self, "public_key")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        (Computed)[String] The current status of the WireGuard Gateway.
        """
        return pulumi.get(self, "status")

