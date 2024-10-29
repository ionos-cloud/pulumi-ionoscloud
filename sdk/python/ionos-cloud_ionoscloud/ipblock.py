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

__all__ = ['IpblockArgs', 'Ipblock']

@pulumi.input_type
class IpblockArgs:
    def __init__(__self__, *,
                 location: pulumi.Input[str],
                 size: pulumi.Input[int],
                 ip_consumers: Optional[pulumi.Input[Sequence[pulumi.Input['IpblockIpConsumerArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Ipblock resource.
        :param pulumi.Input[str] location: [string] The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
        :param pulumi.Input[int] size: [integer] The number of IP addresses to reserve for this block.
        :param pulumi.Input[Sequence[pulumi.Input['IpblockIpConsumerArgs']]] ip_consumers: Read-Only attribute. Lists consumption detail of an individual ip
        :param pulumi.Input[str] name: [string] The name of Ip Block
        """
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "size", size)
        if ip_consumers is not None:
            pulumi.set(__self__, "ip_consumers", ip_consumers)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        [string] The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def size(self) -> pulumi.Input[int]:
        """
        [integer] The number of IP addresses to reserve for this block.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: pulumi.Input[int]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter(name="ipConsumers")
    def ip_consumers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IpblockIpConsumerArgs']]]]:
        """
        Read-Only attribute. Lists consumption detail of an individual ip
        """
        return pulumi.get(self, "ip_consumers")

    @ip_consumers.setter
    def ip_consumers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IpblockIpConsumerArgs']]]]):
        pulumi.set(self, "ip_consumers", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The name of Ip Block
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _IpblockState:
    def __init__(__self__, *,
                 ip_consumers: Optional[pulumi.Input[Sequence[pulumi.Input['IpblockIpConsumerArgs']]]] = None,
                 ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Ipblock resources.
        :param pulumi.Input[Sequence[pulumi.Input['IpblockIpConsumerArgs']]] ip_consumers: Read-Only attribute. Lists consumption detail of an individual ip
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ips: [integer] The list of IP addresses associated with this block.
        :param pulumi.Input[str] location: [string] The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
        :param pulumi.Input[str] name: [string] The name of Ip Block
        :param pulumi.Input[int] size: [integer] The number of IP addresses to reserve for this block.
        """
        if ip_consumers is not None:
            pulumi.set(__self__, "ip_consumers", ip_consumers)
        if ips is not None:
            pulumi.set(__self__, "ips", ips)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if size is not None:
            pulumi.set(__self__, "size", size)

    @property
    @pulumi.getter(name="ipConsumers")
    def ip_consumers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IpblockIpConsumerArgs']]]]:
        """
        Read-Only attribute. Lists consumption detail of an individual ip
        """
        return pulumi.get(self, "ip_consumers")

    @ip_consumers.setter
    def ip_consumers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IpblockIpConsumerArgs']]]]):
        pulumi.set(self, "ip_consumers", value)

    @property
    @pulumi.getter
    def ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        [integer] The list of IP addresses associated with this block.
        """
        return pulumi.get(self, "ips")

    @ips.setter
    def ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ips", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The name of Ip Block
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[int]]:
        """
        [integer] The number of IP addresses to reserve for this block.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "size", value)


class Ipblock(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ip_consumers: Optional[pulumi.Input[Sequence[pulumi.Input[Union['IpblockIpConsumerArgs', 'IpblockIpConsumerArgsDict']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Manages **IP Blocks** on IonosCloud. IP Blocks contain reserved public IP addresses that can be assigned servers or other resources.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ionos-cloud_ionoscloud as ionoscloud

        example = ionoscloud.Ipblock("example",
            location="us/las",
            size=1)
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        Resource Ipblock can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import ionoscloud:index/ipblock:Ipblock myipblock {ipblock uuid}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['IpblockIpConsumerArgs', 'IpblockIpConsumerArgsDict']]]] ip_consumers: Read-Only attribute. Lists consumption detail of an individual ip
        :param pulumi.Input[str] location: [string] The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
        :param pulumi.Input[str] name: [string] The name of Ip Block
        :param pulumi.Input[int] size: [integer] The number of IP addresses to reserve for this block.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IpblockArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages **IP Blocks** on IonosCloud. IP Blocks contain reserved public IP addresses that can be assigned servers or other resources.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ionos-cloud_ionoscloud as ionoscloud

        example = ionoscloud.Ipblock("example",
            location="us/las",
            size=1)
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        Resource Ipblock can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import ionoscloud:index/ipblock:Ipblock myipblock {ipblock uuid}
        ```

        :param str resource_name: The name of the resource.
        :param IpblockArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IpblockArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ip_consumers: Optional[pulumi.Input[Sequence[pulumi.Input[Union['IpblockIpConsumerArgs', 'IpblockIpConsumerArgsDict']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IpblockArgs.__new__(IpblockArgs)

            __props__.__dict__["ip_consumers"] = ip_consumers
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if size is None and not opts.urn:
                raise TypeError("Missing required property 'size'")
            __props__.__dict__["size"] = size
            __props__.__dict__["ips"] = None
        super(Ipblock, __self__).__init__(
            'ionoscloud:index/ipblock:Ipblock',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            ip_consumers: Optional[pulumi.Input[Sequence[pulumi.Input[Union['IpblockIpConsumerArgs', 'IpblockIpConsumerArgsDict']]]]] = None,
            ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            size: Optional[pulumi.Input[int]] = None) -> 'Ipblock':
        """
        Get an existing Ipblock resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['IpblockIpConsumerArgs', 'IpblockIpConsumerArgsDict']]]] ip_consumers: Read-Only attribute. Lists consumption detail of an individual ip
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ips: [integer] The list of IP addresses associated with this block.
        :param pulumi.Input[str] location: [string] The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
        :param pulumi.Input[str] name: [string] The name of Ip Block
        :param pulumi.Input[int] size: [integer] The number of IP addresses to reserve for this block.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IpblockState.__new__(_IpblockState)

        __props__.__dict__["ip_consumers"] = ip_consumers
        __props__.__dict__["ips"] = ips
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["size"] = size
        return Ipblock(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="ipConsumers")
    def ip_consumers(self) -> pulumi.Output[Sequence['outputs.IpblockIpConsumer']]:
        """
        Read-Only attribute. Lists consumption detail of an individual ip
        """
        return pulumi.get(self, "ip_consumers")

    @property
    @pulumi.getter
    def ips(self) -> pulumi.Output[Sequence[str]]:
        """
        [integer] The list of IP addresses associated with this block.
        """
        return pulumi.get(self, "ips")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        [string] The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        [string] The name of Ip Block
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[int]:
        """
        [integer] The number of IP addresses to reserve for this block.
        """
        return pulumi.get(self, "size")

