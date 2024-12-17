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
from ._inputs import *

__all__ = ['RegistryArgs', 'Registry']

@pulumi.input_type
class RegistryArgs:
    def __init__(__self__, *,
                 location: pulumi.Input[str],
                 api_subnet_allow_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 features: Optional[pulumi.Input['RegistryFeaturesArgs']] = None,
                 garbage_collection_schedule: Optional[pulumi.Input['RegistryGarbageCollectionScheduleArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Registry resource.
        :param pulumi.Input[str] location: [string] Immutable, update forces re-creation of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] api_subnet_allow_lists: [list] The subnet CIDRs that are allowed to connect to the registry.  Specify "a.b.c.d/32" for an individual IP address. __Note__: If this list is empty or not set, there are no restrictions.
        :param pulumi.Input['RegistryFeaturesArgs'] features: [Map]
        :param pulumi.Input['RegistryGarbageCollectionScheduleArgs'] garbage_collection_schedule: [Map]
        :param pulumi.Input[str] name: The name of the container registry. Immutable, update forces re-creation of the resource.
        """
        pulumi.set(__self__, "location", location)
        if api_subnet_allow_lists is not None:
            pulumi.set(__self__, "api_subnet_allow_lists", api_subnet_allow_lists)
        if features is not None:
            pulumi.set(__self__, "features", features)
        if garbage_collection_schedule is not None:
            pulumi.set(__self__, "garbage_collection_schedule", garbage_collection_schedule)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        [string] Immutable, update forces re-creation of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="apiSubnetAllowLists")
    def api_subnet_allow_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        [list] The subnet CIDRs that are allowed to connect to the registry.  Specify "a.b.c.d/32" for an individual IP address. __Note__: If this list is empty or not set, there are no restrictions.
        """
        return pulumi.get(self, "api_subnet_allow_lists")

    @api_subnet_allow_lists.setter
    def api_subnet_allow_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "api_subnet_allow_lists", value)

    @property
    @pulumi.getter
    def features(self) -> Optional[pulumi.Input['RegistryFeaturesArgs']]:
        """
        [Map]
        """
        return pulumi.get(self, "features")

    @features.setter
    def features(self, value: Optional[pulumi.Input['RegistryFeaturesArgs']]):
        pulumi.set(self, "features", value)

    @property
    @pulumi.getter(name="garbageCollectionSchedule")
    def garbage_collection_schedule(self) -> Optional[pulumi.Input['RegistryGarbageCollectionScheduleArgs']]:
        """
        [Map]
        """
        return pulumi.get(self, "garbage_collection_schedule")

    @garbage_collection_schedule.setter
    def garbage_collection_schedule(self, value: Optional[pulumi.Input['RegistryGarbageCollectionScheduleArgs']]):
        pulumi.set(self, "garbage_collection_schedule", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the container registry. Immutable, update forces re-creation of the resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _RegistryState:
    def __init__(__self__, *,
                 api_subnet_allow_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 features: Optional[pulumi.Input['RegistryFeaturesArgs']] = None,
                 garbage_collection_schedule: Optional[pulumi.Input['RegistryGarbageCollectionScheduleArgs']] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 storage_usages: Optional[pulumi.Input[Sequence[pulumi.Input['RegistryStorageUsageArgs']]]] = None):
        """
        Input properties used for looking up and filtering Registry resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] api_subnet_allow_lists: [list] The subnet CIDRs that are allowed to connect to the registry.  Specify "a.b.c.d/32" for an individual IP address. __Note__: If this list is empty or not set, there are no restrictions.
        :param pulumi.Input['RegistryFeaturesArgs'] features: [Map]
        :param pulumi.Input['RegistryGarbageCollectionScheduleArgs'] garbage_collection_schedule: [Map]
        :param pulumi.Input[str] location: [string] Immutable, update forces re-creation of the resource.
        :param pulumi.Input[str] name: The name of the container registry. Immutable, update forces re-creation of the resource.
        """
        if api_subnet_allow_lists is not None:
            pulumi.set(__self__, "api_subnet_allow_lists", api_subnet_allow_lists)
        if features is not None:
            pulumi.set(__self__, "features", features)
        if garbage_collection_schedule is not None:
            pulumi.set(__self__, "garbage_collection_schedule", garbage_collection_schedule)
        if hostname is not None:
            pulumi.set(__self__, "hostname", hostname)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if storage_usages is not None:
            pulumi.set(__self__, "storage_usages", storage_usages)

    @property
    @pulumi.getter(name="apiSubnetAllowLists")
    def api_subnet_allow_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        [list] The subnet CIDRs that are allowed to connect to the registry.  Specify "a.b.c.d/32" for an individual IP address. __Note__: If this list is empty or not set, there are no restrictions.
        """
        return pulumi.get(self, "api_subnet_allow_lists")

    @api_subnet_allow_lists.setter
    def api_subnet_allow_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "api_subnet_allow_lists", value)

    @property
    @pulumi.getter
    def features(self) -> Optional[pulumi.Input['RegistryFeaturesArgs']]:
        """
        [Map]
        """
        return pulumi.get(self, "features")

    @features.setter
    def features(self, value: Optional[pulumi.Input['RegistryFeaturesArgs']]):
        pulumi.set(self, "features", value)

    @property
    @pulumi.getter(name="garbageCollectionSchedule")
    def garbage_collection_schedule(self) -> Optional[pulumi.Input['RegistryGarbageCollectionScheduleArgs']]:
        """
        [Map]
        """
        return pulumi.get(self, "garbage_collection_schedule")

    @garbage_collection_schedule.setter
    def garbage_collection_schedule(self, value: Optional[pulumi.Input['RegistryGarbageCollectionScheduleArgs']]):
        pulumi.set(self, "garbage_collection_schedule", value)

    @property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Immutable, update forces re-creation of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the container registry. Immutable, update forces re-creation of the resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="storageUsages")
    def storage_usages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RegistryStorageUsageArgs']]]]:
        return pulumi.get(self, "storage_usages")

    @storage_usages.setter
    def storage_usages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RegistryStorageUsageArgs']]]]):
        pulumi.set(self, "storage_usages", value)


class Registry(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_subnet_allow_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 features: Optional[pulumi.Input[Union['RegistryFeaturesArgs', 'RegistryFeaturesArgsDict']]] = None,
                 garbage_collection_schedule: Optional[pulumi.Input[Union['RegistryGarbageCollectionScheduleArgs', 'RegistryGarbageCollectionScheduleArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages an **Container Registry** on IonosCloud.

        ## Example Usage

        ```python
        import pulumi
        import ionoscloud as ionoscloud

        example = ionoscloud.creg.Registry("example",
            api_subnet_allow_lists=["1.2.3.4/32"],
            garbage_collection_schedule={
                "days": [
                    "Monday",
                    "Tuesday",
                ],
                "time": "05:19:00+00:00",
            },
            location="de/fra")
        ```

        ## Import

        Resource Container Registry can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import ionoscloud:creg/registry:Registry mycr {container_registry uuid}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] api_subnet_allow_lists: [list] The subnet CIDRs that are allowed to connect to the registry.  Specify "a.b.c.d/32" for an individual IP address. __Note__: If this list is empty or not set, there are no restrictions.
        :param pulumi.Input[Union['RegistryFeaturesArgs', 'RegistryFeaturesArgsDict']] features: [Map]
        :param pulumi.Input[Union['RegistryGarbageCollectionScheduleArgs', 'RegistryGarbageCollectionScheduleArgsDict']] garbage_collection_schedule: [Map]
        :param pulumi.Input[str] location: [string] Immutable, update forces re-creation of the resource.
        :param pulumi.Input[str] name: The name of the container registry. Immutable, update forces re-creation of the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RegistryArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an **Container Registry** on IonosCloud.

        ## Example Usage

        ```python
        import pulumi
        import ionoscloud as ionoscloud

        example = ionoscloud.creg.Registry("example",
            api_subnet_allow_lists=["1.2.3.4/32"],
            garbage_collection_schedule={
                "days": [
                    "Monday",
                    "Tuesday",
                ],
                "time": "05:19:00+00:00",
            },
            location="de/fra")
        ```

        ## Import

        Resource Container Registry can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import ionoscloud:creg/registry:Registry mycr {container_registry uuid}
        ```

        :param str resource_name: The name of the resource.
        :param RegistryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RegistryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_subnet_allow_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 features: Optional[pulumi.Input[Union['RegistryFeaturesArgs', 'RegistryFeaturesArgsDict']]] = None,
                 garbage_collection_schedule: Optional[pulumi.Input[Union['RegistryGarbageCollectionScheduleArgs', 'RegistryGarbageCollectionScheduleArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RegistryArgs.__new__(RegistryArgs)

            __props__.__dict__["api_subnet_allow_lists"] = api_subnet_allow_lists
            __props__.__dict__["features"] = features
            __props__.__dict__["garbage_collection_schedule"] = garbage_collection_schedule
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["hostname"] = None
            __props__.__dict__["storage_usages"] = None
        super(Registry, __self__).__init__(
            'ionoscloud:creg/registry:Registry',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_subnet_allow_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            features: Optional[pulumi.Input[Union['RegistryFeaturesArgs', 'RegistryFeaturesArgsDict']]] = None,
            garbage_collection_schedule: Optional[pulumi.Input[Union['RegistryGarbageCollectionScheduleArgs', 'RegistryGarbageCollectionScheduleArgsDict']]] = None,
            hostname: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            storage_usages: Optional[pulumi.Input[Sequence[pulumi.Input[Union['RegistryStorageUsageArgs', 'RegistryStorageUsageArgsDict']]]]] = None) -> 'Registry':
        """
        Get an existing Registry resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] api_subnet_allow_lists: [list] The subnet CIDRs that are allowed to connect to the registry.  Specify "a.b.c.d/32" for an individual IP address. __Note__: If this list is empty or not set, there are no restrictions.
        :param pulumi.Input[Union['RegistryFeaturesArgs', 'RegistryFeaturesArgsDict']] features: [Map]
        :param pulumi.Input[Union['RegistryGarbageCollectionScheduleArgs', 'RegistryGarbageCollectionScheduleArgsDict']] garbage_collection_schedule: [Map]
        :param pulumi.Input[str] location: [string] Immutable, update forces re-creation of the resource.
        :param pulumi.Input[str] name: The name of the container registry. Immutable, update forces re-creation of the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RegistryState.__new__(_RegistryState)

        __props__.__dict__["api_subnet_allow_lists"] = api_subnet_allow_lists
        __props__.__dict__["features"] = features
        __props__.__dict__["garbage_collection_schedule"] = garbage_collection_schedule
        __props__.__dict__["hostname"] = hostname
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["storage_usages"] = storage_usages
        return Registry(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiSubnetAllowLists")
    def api_subnet_allow_lists(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        [list] The subnet CIDRs that are allowed to connect to the registry.  Specify "a.b.c.d/32" for an individual IP address. __Note__: If this list is empty or not set, there are no restrictions.
        """
        return pulumi.get(self, "api_subnet_allow_lists")

    @property
    @pulumi.getter
    def features(self) -> pulumi.Output['outputs.RegistryFeatures']:
        """
        [Map]
        """
        return pulumi.get(self, "features")

    @property
    @pulumi.getter(name="garbageCollectionSchedule")
    def garbage_collection_schedule(self) -> pulumi.Output['outputs.RegistryGarbageCollectionSchedule']:
        """
        [Map]
        """
        return pulumi.get(self, "garbage_collection_schedule")

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Output[str]:
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        [string] Immutable, update forces re-creation of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the container registry. Immutable, update forces re-creation of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="storageUsages")
    def storage_usages(self) -> pulumi.Output[Sequence['outputs.RegistryStorageUsage']]:
        return pulumi.get(self, "storage_usages")

