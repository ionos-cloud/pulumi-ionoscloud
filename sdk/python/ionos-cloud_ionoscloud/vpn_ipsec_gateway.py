# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['VpnIpsecGatewayArgs', 'VpnIpsecGateway']

@pulumi.input_type
class VpnIpsecGatewayArgs:
    def __init__(__self__, *,
                 connections: pulumi.Input[Sequence[pulumi.Input['VpnIpsecGatewayConnectionArgs']]],
                 gateway_ip: pulumi.Input[str],
                 location: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VpnIpsecGateway resource.
        :param pulumi.Input[Sequence[pulumi.Input['VpnIpsecGatewayConnectionArgs']]] connections: [list] The network connection for your gateway. **Note**: all connections must belong to the
               same datacenter. Minimum items: 1. Maximum items: 10.
        :param pulumi.Input[str] gateway_ip: [string] Public IP address to be assigned to the gateway. Note: This must be an IP address in
               the same datacenter as the connections.
        :param pulumi.Input[str] location: [string] The location of the IPSec Gateway. Supported locations: de/fra, de/txl, es/vit,
               gb/lhr, us/ewr, us/las, us/mci, fr/par
        :param pulumi.Input[str] description: [string] The human-readable description of the IPSec Gateway.
        :param pulumi.Input[str] name: [string] The name of the IPSec Gateway.
        :param pulumi.Input[str] version: [string] The IKE version that is permitted for the VPN tunnels. Default: `IKEv2`. Possible
               values: `IKEv2`.
        """
        pulumi.set(__self__, "connections", connections)
        pulumi.set(__self__, "gateway_ip", gateway_ip)
        pulumi.set(__self__, "location", location)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def connections(self) -> pulumi.Input[Sequence[pulumi.Input['VpnIpsecGatewayConnectionArgs']]]:
        """
        [list] The network connection for your gateway. **Note**: all connections must belong to the
        same datacenter. Minimum items: 1. Maximum items: 10.
        """
        return pulumi.get(self, "connections")

    @connections.setter
    def connections(self, value: pulumi.Input[Sequence[pulumi.Input['VpnIpsecGatewayConnectionArgs']]]):
        pulumi.set(self, "connections", value)

    @property
    @pulumi.getter(name="gatewayIp")
    def gateway_ip(self) -> pulumi.Input[str]:
        """
        [string] Public IP address to be assigned to the gateway. Note: This must be an IP address in
        the same datacenter as the connections.
        """
        return pulumi.get(self, "gateway_ip")

    @gateway_ip.setter
    def gateway_ip(self, value: pulumi.Input[str]):
        pulumi.set(self, "gateway_ip", value)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        [string] The location of the IPSec Gateway. Supported locations: de/fra, de/txl, es/vit,
        gb/lhr, us/ewr, us/las, us/mci, fr/par
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The human-readable description of the IPSec Gateway.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The name of the IPSec Gateway.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The IKE version that is permitted for the VPN tunnels. Default: `IKEv2`. Possible
        values: `IKEv2`.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


@pulumi.input_type
class _VpnIpsecGatewayState:
    def __init__(__self__, *,
                 connections: Optional[pulumi.Input[Sequence[pulumi.Input['VpnIpsecGatewayConnectionArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 gateway_ip: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VpnIpsecGateway resources.
        :param pulumi.Input[Sequence[pulumi.Input['VpnIpsecGatewayConnectionArgs']]] connections: [list] The network connection for your gateway. **Note**: all connections must belong to the
               same datacenter. Minimum items: 1. Maximum items: 10.
        :param pulumi.Input[str] description: [string] The human-readable description of the IPSec Gateway.
        :param pulumi.Input[str] gateway_ip: [string] Public IP address to be assigned to the gateway. Note: This must be an IP address in
               the same datacenter as the connections.
        :param pulumi.Input[str] location: [string] The location of the IPSec Gateway. Supported locations: de/fra, de/txl, es/vit,
               gb/lhr, us/ewr, us/las, us/mci, fr/par
        :param pulumi.Input[str] name: [string] The name of the IPSec Gateway.
        :param pulumi.Input[str] version: [string] The IKE version that is permitted for the VPN tunnels. Default: `IKEv2`. Possible
               values: `IKEv2`.
        """
        if connections is not None:
            pulumi.set(__self__, "connections", connections)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if gateway_ip is not None:
            pulumi.set(__self__, "gateway_ip", gateway_ip)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VpnIpsecGatewayConnectionArgs']]]]:
        """
        [list] The network connection for your gateway. **Note**: all connections must belong to the
        same datacenter. Minimum items: 1. Maximum items: 10.
        """
        return pulumi.get(self, "connections")

    @connections.setter
    def connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VpnIpsecGatewayConnectionArgs']]]]):
        pulumi.set(self, "connections", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The human-readable description of the IPSec Gateway.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="gatewayIp")
    def gateway_ip(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Public IP address to be assigned to the gateway. Note: This must be an IP address in
        the same datacenter as the connections.
        """
        return pulumi.get(self, "gateway_ip")

    @gateway_ip.setter
    def gateway_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gateway_ip", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The location of the IPSec Gateway. Supported locations: de/fra, de/txl, es/vit,
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
        [string] The name of the IPSec Gateway.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The IKE version that is permitted for the VPN tunnels. Default: `IKEv2`. Possible
        values: `IKEv2`.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class VpnIpsecGateway(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnIpsecGatewayConnectionArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 gateway_ip: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An IPSec Gateway resource manages the creation, management, and deletion of VPN IPSec Gateways within the IONOS Cloud
        infrastructure. This resource facilitates the creation of VPN IPSec Gateways, enabling secure connections between your
        network resources.

        ## Usage example

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ionos-cloud_ionoscloud as ionoscloud

        # Basic example
        test_datacenter = ionoscloud.compute.Datacenter("testDatacenter", location="de/fra")
        test_lan = ionoscloud.compute.Lan("testLan",
            public=False,
            datacenter_id=test_datacenter.id)
        test_ipblock = ionoscloud.compute.IPBlock("testIpblock",
            location="de/fra",
            size=1)
        example = ionoscloud.VpnIpsecGateway("example",
            location="de/fra",
            gateway_ip=test_ipblock.ips[0],
            version="IKEv2",
            description="This gateway connects site A to VDC X.",
            connections=[ionoscloud.VpnIpsecGatewayConnectionArgs(
                datacenter_id=test_datacenter.id,
                lan_id=test_lan.id,
                ipv4_cidr="192.168.100.10/24",
            )])
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        The resource can be imported using the `location` and `gateway_id`, for example:

        ```sh
        $ pulumi import ionoscloud:index/vpnIpsecGateway:VpnIpsecGateway example {location}:{gateway_id}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnIpsecGatewayConnectionArgs']]]] connections: [list] The network connection for your gateway. **Note**: all connections must belong to the
               same datacenter. Minimum items: 1. Maximum items: 10.
        :param pulumi.Input[str] description: [string] The human-readable description of the IPSec Gateway.
        :param pulumi.Input[str] gateway_ip: [string] Public IP address to be assigned to the gateway. Note: This must be an IP address in
               the same datacenter as the connections.
        :param pulumi.Input[str] location: [string] The location of the IPSec Gateway. Supported locations: de/fra, de/txl, es/vit,
               gb/lhr, us/ewr, us/las, us/mci, fr/par
        :param pulumi.Input[str] name: [string] The name of the IPSec Gateway.
        :param pulumi.Input[str] version: [string] The IKE version that is permitted for the VPN tunnels. Default: `IKEv2`. Possible
               values: `IKEv2`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VpnIpsecGatewayArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An IPSec Gateway resource manages the creation, management, and deletion of VPN IPSec Gateways within the IONOS Cloud
        infrastructure. This resource facilitates the creation of VPN IPSec Gateways, enabling secure connections between your
        network resources.

        ## Usage example

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ionos-cloud_ionoscloud as ionoscloud

        # Basic example
        test_datacenter = ionoscloud.compute.Datacenter("testDatacenter", location="de/fra")
        test_lan = ionoscloud.compute.Lan("testLan",
            public=False,
            datacenter_id=test_datacenter.id)
        test_ipblock = ionoscloud.compute.IPBlock("testIpblock",
            location="de/fra",
            size=1)
        example = ionoscloud.VpnIpsecGateway("example",
            location="de/fra",
            gateway_ip=test_ipblock.ips[0],
            version="IKEv2",
            description="This gateway connects site A to VDC X.",
            connections=[ionoscloud.VpnIpsecGatewayConnectionArgs(
                datacenter_id=test_datacenter.id,
                lan_id=test_lan.id,
                ipv4_cidr="192.168.100.10/24",
            )])
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        The resource can be imported using the `location` and `gateway_id`, for example:

        ```sh
        $ pulumi import ionoscloud:index/vpnIpsecGateway:VpnIpsecGateway example {location}:{gateway_id}
        ```

        :param str resource_name: The name of the resource.
        :param VpnIpsecGatewayArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VpnIpsecGatewayArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnIpsecGatewayConnectionArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 gateway_ip: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VpnIpsecGatewayArgs.__new__(VpnIpsecGatewayArgs)

            if connections is None and not opts.urn:
                raise TypeError("Missing required property 'connections'")
            __props__.__dict__["connections"] = connections
            __props__.__dict__["description"] = description
            if gateway_ip is None and not opts.urn:
                raise TypeError("Missing required property 'gateway_ip'")
            __props__.__dict__["gateway_ip"] = gateway_ip
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["version"] = version
        super(VpnIpsecGateway, __self__).__init__(
            'ionoscloud:index/vpnIpsecGateway:VpnIpsecGateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            connections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnIpsecGatewayConnectionArgs']]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            gateway_ip: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[str]] = None) -> 'VpnIpsecGateway':
        """
        Get an existing VpnIpsecGateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnIpsecGatewayConnectionArgs']]]] connections: [list] The network connection for your gateway. **Note**: all connections must belong to the
               same datacenter. Minimum items: 1. Maximum items: 10.
        :param pulumi.Input[str] description: [string] The human-readable description of the IPSec Gateway.
        :param pulumi.Input[str] gateway_ip: [string] Public IP address to be assigned to the gateway. Note: This must be an IP address in
               the same datacenter as the connections.
        :param pulumi.Input[str] location: [string] The location of the IPSec Gateway. Supported locations: de/fra, de/txl, es/vit,
               gb/lhr, us/ewr, us/las, us/mci, fr/par
        :param pulumi.Input[str] name: [string] The name of the IPSec Gateway.
        :param pulumi.Input[str] version: [string] The IKE version that is permitted for the VPN tunnels. Default: `IKEv2`. Possible
               values: `IKEv2`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VpnIpsecGatewayState.__new__(_VpnIpsecGatewayState)

        __props__.__dict__["connections"] = connections
        __props__.__dict__["description"] = description
        __props__.__dict__["gateway_ip"] = gateway_ip
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["version"] = version
        return VpnIpsecGateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def connections(self) -> pulumi.Output[Sequence['outputs.VpnIpsecGatewayConnection']]:
        """
        [list] The network connection for your gateway. **Note**: all connections must belong to the
        same datacenter. Minimum items: 1. Maximum items: 10.
        """
        return pulumi.get(self, "connections")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        [string] The human-readable description of the IPSec Gateway.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="gatewayIp")
    def gateway_ip(self) -> pulumi.Output[str]:
        """
        [string] Public IP address to be assigned to the gateway. Note: This must be an IP address in
        the same datacenter as the connections.
        """
        return pulumi.get(self, "gateway_ip")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        [string] The location of the IPSec Gateway. Supported locations: de/fra, de/txl, es/vit,
        gb/lhr, us/ewr, us/las, us/mci, fr/par
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        [string] The name of the IPSec Gateway.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[str]]:
        """
        [string] The IKE version that is permitted for the VPN tunnels. Default: `IKEv2`. Possible
        values: `IKEv2`.
        """
        return pulumi.get(self, "version")

