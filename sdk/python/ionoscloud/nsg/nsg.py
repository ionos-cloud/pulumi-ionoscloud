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

__all__ = ['NsgArgs', 'Nsg']

@pulumi.input_type
class NsgArgs:
    def __init__(__self__, *,
                 datacenter_id: pulumi.Input[str],
                 description: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Nsg resource.
        :param pulumi.Input[str] datacenter_id: [string] The ID of a Virtual Data Center.
        :param pulumi.Input[str] description: [string] Description for the Network Security Group.
        :param pulumi.Input[str] name: [string] The name of the Network Security Group.
        """
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> pulumi.Input[str]:
        """
        [string] The ID of a Virtual Data Center.
        """
        return pulumi.get(self, "datacenter_id")

    @datacenter_id.setter
    def datacenter_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "datacenter_id", value)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        [string] Description for the Network Security Group.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The name of the Network Security Group.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _NsgState:
    def __init__(__self__, *,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rule_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Nsg resources.
        :param pulumi.Input[str] datacenter_id: [string] The ID of a Virtual Data Center.
        :param pulumi.Input[str] description: [string] Description for the Network Security Group.
        :param pulumi.Input[str] name: [string] The name of the Network Security Group.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] rule_ids: List of Firewall Rules that are part of the Network Security Group
        """
        if datacenter_id is not None:
            pulumi.set(__self__, "datacenter_id", datacenter_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if rule_ids is not None:
            pulumi.set(__self__, "rule_ids", rule_ids)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The ID of a Virtual Data Center.
        """
        return pulumi.get(self, "datacenter_id")

    @datacenter_id.setter
    def datacenter_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datacenter_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Description for the Network Security Group.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The name of the Network Security Group.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="ruleIds")
    def rule_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of Firewall Rules that are part of the Network Security Group
        """
        return pulumi.get(self, "rule_ids")

    @rule_ids.setter
    def rule_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "rule_ids", value)


class Nsg(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a **Network Security Group** on IonosCloud.

        ## Example Usage

        ```python
        import pulumi
        import ionoscloud as ionoscloud

        example = ionoscloud.compute.Datacenter("example",
            name="Datacenter NSG Example",
            location="de/txl")
        example_nsg = ionoscloud.nsg.Nsg("example",
            name="Example NSG",
            description="Example NSG Description",
            datacenter_id=example.id)
        ```

        ## Import

        Resource Server can be imported using the `resource id` and the `datacenter id`, e.g.

        ```sh
        $ pulumi import ionoscloud:nsg/nsg:Nsg mynsg datacenter uuid/nsg uuid
        ```

        Or by using an `import` block. Here is an example that allows you to import the default created nsg into terraform.

        hcl

        resource "ionoscloud_datacenter" "example" {

          name            = "Datacenter NSG Example"

          location        = "de/txl"

        }

        import {

          to = ionoscloud_nsg.imported

          id = "datacenter uuid/default nsg uuid"

        }

        resource "ionoscloud_nsg" "imported_default" {  # Imported here

          datacenter_id     = ionoscloud_datacenter.example.id

        }

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] datacenter_id: [string] The ID of a Virtual Data Center.
        :param pulumi.Input[str] description: [string] Description for the Network Security Group.
        :param pulumi.Input[str] name: [string] The name of the Network Security Group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NsgArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a **Network Security Group** on IonosCloud.

        ## Example Usage

        ```python
        import pulumi
        import ionoscloud as ionoscloud

        example = ionoscloud.compute.Datacenter("example",
            name="Datacenter NSG Example",
            location="de/txl")
        example_nsg = ionoscloud.nsg.Nsg("example",
            name="Example NSG",
            description="Example NSG Description",
            datacenter_id=example.id)
        ```

        ## Import

        Resource Server can be imported using the `resource id` and the `datacenter id`, e.g.

        ```sh
        $ pulumi import ionoscloud:nsg/nsg:Nsg mynsg datacenter uuid/nsg uuid
        ```

        Or by using an `import` block. Here is an example that allows you to import the default created nsg into terraform.

        hcl

        resource "ionoscloud_datacenter" "example" {

          name            = "Datacenter NSG Example"

          location        = "de/txl"

        }

        import {

          to = ionoscloud_nsg.imported

          id = "datacenter uuid/default nsg uuid"

        }

        resource "ionoscloud_nsg" "imported_default" {  # Imported here

          datacenter_id     = ionoscloud_datacenter.example.id

        }

        :param str resource_name: The name of the resource.
        :param NsgArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NsgArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NsgArgs.__new__(NsgArgs)

            if datacenter_id is None and not opts.urn:
                raise TypeError("Missing required property 'datacenter_id'")
            __props__.__dict__["datacenter_id"] = datacenter_id
            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["rule_ids"] = None
        super(Nsg, __self__).__init__(
            'ionoscloud:nsg/nsg:Nsg',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            datacenter_id: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            rule_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'Nsg':
        """
        Get an existing Nsg resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] datacenter_id: [string] The ID of a Virtual Data Center.
        :param pulumi.Input[str] description: [string] Description for the Network Security Group.
        :param pulumi.Input[str] name: [string] The name of the Network Security Group.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] rule_ids: List of Firewall Rules that are part of the Network Security Group
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NsgState.__new__(_NsgState)

        __props__.__dict__["datacenter_id"] = datacenter_id
        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["rule_ids"] = rule_ids
        return Nsg(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> pulumi.Output[str]:
        """
        [string] The ID of a Virtual Data Center.
        """
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        [string] Description for the Network Security Group.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        [string] The name of the Network Security Group.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="ruleIds")
    def rule_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        List of Firewall Rules that are part of the Network Security Group
        """
        return pulumi.get(self, "rule_ids")

