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

__all__ = ['ZoneArgs', 'Zone']

@pulumi.input_type
class ZoneArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Zone resource.
        :param pulumi.Input[str] description: [string] The description for the DNS Zone.
        :param pulumi.Input[bool] enabled: [bool] Indicates if the DNS Zone is active or not. Default is `true`.
        :param pulumi.Input[str] name: [string] The name of the DNS Zone.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The description for the DNS Zone.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        [bool] Indicates if the DNS Zone is active or not. Default is `true`.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The name of the DNS Zone.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ZoneState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nameservers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Zone resources.
        :param pulumi.Input[str] description: [string] The description for the DNS Zone.
        :param pulumi.Input[bool] enabled: [bool] Indicates if the DNS Zone is active or not. Default is `true`.
        :param pulumi.Input[str] name: [string] The name of the DNS Zone.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] nameservers: A list of available name servers.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if nameservers is not None:
            pulumi.set(__self__, "nameservers", nameservers)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The description for the DNS Zone.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        [bool] Indicates if the DNS Zone is active or not. Default is `true`.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The name of the DNS Zone.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def nameservers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of available name servers.
        """
        return pulumi.get(self, "nameservers")

    @nameservers.setter
    def nameservers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "nameservers", value)


class Zone(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a **DNS Zone**.

        > ⚠️  Only tokens are accepted for authorization in the **ionoscloud_dns_zone** resource. Please ensure you are using tokens as other methods will not be valid.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ionoscloud as ionoscloud

        example = ionoscloud.dns.Zone("example",
            name="example.com",
            description="description",
            enabled=False)
        ```

        ## Import

        In order to import a DNS Zone, you can define an empty DNS Zone resource in the plan:

        hcl

        resource "ionoscloud_dns_zone" "example" {

        }

        The resource can be imported using the `zone_id`, for example:

        ```sh
        $ pulumi import ionoscloud:dns/zone:Zone examplezone_id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: [string] The description for the DNS Zone.
        :param pulumi.Input[bool] enabled: [bool] Indicates if the DNS Zone is active or not. Default is `true`.
        :param pulumi.Input[str] name: [string] The name of the DNS Zone.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ZoneArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a **DNS Zone**.

        > ⚠️  Only tokens are accepted for authorization in the **ionoscloud_dns_zone** resource. Please ensure you are using tokens as other methods will not be valid.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ionoscloud as ionoscloud

        example = ionoscloud.dns.Zone("example",
            name="example.com",
            description="description",
            enabled=False)
        ```

        ## Import

        In order to import a DNS Zone, you can define an empty DNS Zone resource in the plan:

        hcl

        resource "ionoscloud_dns_zone" "example" {

        }

        The resource can be imported using the `zone_id`, for example:

        ```sh
        $ pulumi import ionoscloud:dns/zone:Zone examplezone_id
        ```

        :param str resource_name: The name of the resource.
        :param ZoneArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ZoneArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ZoneArgs.__new__(ZoneArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["name"] = name
            __props__.__dict__["nameservers"] = None
        super(Zone, __self__).__init__(
            'ionoscloud:dns/zone:Zone',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            nameservers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'Zone':
        """
        Get an existing Zone resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: [string] The description for the DNS Zone.
        :param pulumi.Input[bool] enabled: [bool] Indicates if the DNS Zone is active or not. Default is `true`.
        :param pulumi.Input[str] name: [string] The name of the DNS Zone.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] nameservers: A list of available name servers.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ZoneState.__new__(_ZoneState)

        __props__.__dict__["description"] = description
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["name"] = name
        __props__.__dict__["nameservers"] = nameservers
        return Zone(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        [string] The description for the DNS Zone.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        [bool] Indicates if the DNS Zone is active or not. Default is `true`.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        [string] The name of the DNS Zone.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def nameservers(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of available name servers.
        """
        return pulumi.get(self, "nameservers")

