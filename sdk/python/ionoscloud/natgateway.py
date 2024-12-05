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

__all__ = ['NatgatewayArgs', 'Natgateway']

@pulumi.input_type
class NatgatewayArgs:
    def __init__(__self__, *,
                 datacenter_id: pulumi.Input[str],
                 lans: pulumi.Input[Sequence[pulumi.Input['NatgatewayLanArgs']]],
                 public_ips: pulumi.Input[Sequence[pulumi.Input[str]]],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Natgateway resource.
        :param pulumi.Input[str] datacenter_id: [string] A Datacenter's UUID.
        :param pulumi.Input[Sequence[pulumi.Input['NatgatewayLanArgs']]] lans: [list] A list of Local Area Networks the node pool should be part of.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] public_ips: [list]Collection of public IP addresses of the NAT gateway. Should be customer reserved IP addresses in that location.
        :param pulumi.Input[str] name: [string] Name of the NAT gateway.
        """
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        pulumi.set(__self__, "lans", lans)
        pulumi.set(__self__, "public_ips", public_ips)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> pulumi.Input[str]:
        """
        [string] A Datacenter's UUID.
        """
        return pulumi.get(self, "datacenter_id")

    @datacenter_id.setter
    def datacenter_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "datacenter_id", value)

    @property
    @pulumi.getter
    def lans(self) -> pulumi.Input[Sequence[pulumi.Input['NatgatewayLanArgs']]]:
        """
        [list] A list of Local Area Networks the node pool should be part of.
        """
        return pulumi.get(self, "lans")

    @lans.setter
    def lans(self, value: pulumi.Input[Sequence[pulumi.Input['NatgatewayLanArgs']]]):
        pulumi.set(self, "lans", value)

    @property
    @pulumi.getter(name="publicIps")
    def public_ips(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        [list]Collection of public IP addresses of the NAT gateway. Should be customer reserved IP addresses in that location.
        """
        return pulumi.get(self, "public_ips")

    @public_ips.setter
    def public_ips(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "public_ips", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Name of the NAT gateway.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _NatgatewayState:
    def __init__(__self__, *,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 lans: Optional[pulumi.Input[Sequence[pulumi.Input['NatgatewayLanArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 public_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Natgateway resources.
        :param pulumi.Input[str] datacenter_id: [string] A Datacenter's UUID.
        :param pulumi.Input[Sequence[pulumi.Input['NatgatewayLanArgs']]] lans: [list] A list of Local Area Networks the node pool should be part of.
        :param pulumi.Input[str] name: [string] Name of the NAT gateway.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] public_ips: [list]Collection of public IP addresses of the NAT gateway. Should be customer reserved IP addresses in that location.
        """
        if datacenter_id is not None:
            pulumi.set(__self__, "datacenter_id", datacenter_id)
        if lans is not None:
            pulumi.set(__self__, "lans", lans)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if public_ips is not None:
            pulumi.set(__self__, "public_ips", public_ips)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> Optional[pulumi.Input[str]]:
        """
        [string] A Datacenter's UUID.
        """
        return pulumi.get(self, "datacenter_id")

    @datacenter_id.setter
    def datacenter_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datacenter_id", value)

    @property
    @pulumi.getter
    def lans(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NatgatewayLanArgs']]]]:
        """
        [list] A list of Local Area Networks the node pool should be part of.
        """
        return pulumi.get(self, "lans")

    @lans.setter
    def lans(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NatgatewayLanArgs']]]]):
        pulumi.set(self, "lans", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Name of the NAT gateway.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="publicIps")
    def public_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        [list]Collection of public IP addresses of the NAT gateway. Should be customer reserved IP addresses in that location.
        """
        return pulumi.get(self, "public_ips")

    @public_ips.setter
    def public_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "public_ips", value)


class Natgateway(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 lans: Optional[pulumi.Input[Sequence[pulumi.Input[Union['NatgatewayLanArgs', 'NatgatewayLanArgsDict']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 public_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Manages a **Nat Gateway** on IonosCloud.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ionoscloud as ionoscloud

        example_datacenter = ionoscloud.compute.Datacenter("exampleDatacenter",
            location="us/las",
            description="Datacenter Description",
            sec_auth_protection=False)
        example_ip_block = ionoscloud.compute.IPBlock("exampleIPBlock",
            location="us/las",
            size=2)
        example_lan = ionoscloud.compute.Lan("exampleLan",
            datacenter_id=example_datacenter.id,
            public=True)
        example_natgateway = ionoscloud.Natgateway("exampleNatgateway",
            datacenter_id=example_datacenter.id,
            public_ips=[
                example_ip_block.ips[0],
                example_ip_block.ips[1],
            ],
            lans=[ionoscloud.NatgatewayLanArgs(
                id=example_lan.id,
                gateway_ips=["10.11.2.5"],
            )])
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        A Nat Gateway resource can be imported using its `resource id` and the `datacenter id`, e.g.

        ```sh
        $ pulumi import ionoscloud:index/natgateway:Natgateway my_natgateway {datacenter uuid}/{nat gateway uuid}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] datacenter_id: [string] A Datacenter's UUID.
        :param pulumi.Input[Sequence[pulumi.Input[Union['NatgatewayLanArgs', 'NatgatewayLanArgsDict']]]] lans: [list] A list of Local Area Networks the node pool should be part of.
        :param pulumi.Input[str] name: [string] Name of the NAT gateway.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] public_ips: [list]Collection of public IP addresses of the NAT gateway. Should be customer reserved IP addresses in that location.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NatgatewayArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a **Nat Gateway** on IonosCloud.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ionoscloud as ionoscloud

        example_datacenter = ionoscloud.compute.Datacenter("exampleDatacenter",
            location="us/las",
            description="Datacenter Description",
            sec_auth_protection=False)
        example_ip_block = ionoscloud.compute.IPBlock("exampleIPBlock",
            location="us/las",
            size=2)
        example_lan = ionoscloud.compute.Lan("exampleLan",
            datacenter_id=example_datacenter.id,
            public=True)
        example_natgateway = ionoscloud.Natgateway("exampleNatgateway",
            datacenter_id=example_datacenter.id,
            public_ips=[
                example_ip_block.ips[0],
                example_ip_block.ips[1],
            ],
            lans=[ionoscloud.NatgatewayLanArgs(
                id=example_lan.id,
                gateway_ips=["10.11.2.5"],
            )])
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        A Nat Gateway resource can be imported using its `resource id` and the `datacenter id`, e.g.

        ```sh
        $ pulumi import ionoscloud:index/natgateway:Natgateway my_natgateway {datacenter uuid}/{nat gateway uuid}
        ```

        :param str resource_name: The name of the resource.
        :param NatgatewayArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NatgatewayArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 lans: Optional[pulumi.Input[Sequence[pulumi.Input[Union['NatgatewayLanArgs', 'NatgatewayLanArgsDict']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 public_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NatgatewayArgs.__new__(NatgatewayArgs)

            if datacenter_id is None and not opts.urn:
                raise TypeError("Missing required property 'datacenter_id'")
            __props__.__dict__["datacenter_id"] = datacenter_id
            if lans is None and not opts.urn:
                raise TypeError("Missing required property 'lans'")
            __props__.__dict__["lans"] = lans
            __props__.__dict__["name"] = name
            if public_ips is None and not opts.urn:
                raise TypeError("Missing required property 'public_ips'")
            __props__.__dict__["public_ips"] = public_ips
        super(Natgateway, __self__).__init__(
            'ionoscloud:index/natgateway:Natgateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            datacenter_id: Optional[pulumi.Input[str]] = None,
            lans: Optional[pulumi.Input[Sequence[pulumi.Input[Union['NatgatewayLanArgs', 'NatgatewayLanArgsDict']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            public_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'Natgateway':
        """
        Get an existing Natgateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] datacenter_id: [string] A Datacenter's UUID.
        :param pulumi.Input[Sequence[pulumi.Input[Union['NatgatewayLanArgs', 'NatgatewayLanArgsDict']]]] lans: [list] A list of Local Area Networks the node pool should be part of.
        :param pulumi.Input[str] name: [string] Name of the NAT gateway.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] public_ips: [list]Collection of public IP addresses of the NAT gateway. Should be customer reserved IP addresses in that location.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NatgatewayState.__new__(_NatgatewayState)

        __props__.__dict__["datacenter_id"] = datacenter_id
        __props__.__dict__["lans"] = lans
        __props__.__dict__["name"] = name
        __props__.__dict__["public_ips"] = public_ips
        return Natgateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> pulumi.Output[str]:
        """
        [string] A Datacenter's UUID.
        """
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter
    def lans(self) -> pulumi.Output[Sequence['outputs.NatgatewayLan']]:
        """
        [list] A list of Local Area Networks the node pool should be part of.
        """
        return pulumi.get(self, "lans")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        [string] Name of the NAT gateway.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="publicIps")
    def public_ips(self) -> pulumi.Output[Sequence[str]]:
        """
        [list]Collection of public IP addresses of the NAT gateway. Should be customer reserved IP addresses in that location.
        """
        return pulumi.get(self, "public_ips")

