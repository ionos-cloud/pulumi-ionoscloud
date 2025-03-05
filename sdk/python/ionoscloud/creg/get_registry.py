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
    'GetRegistryResult',
    'AwaitableGetRegistryResult',
    'get_registry',
    'get_registry_output',
]

@pulumi.output_type
class GetRegistryResult:
    """
    A collection of values returned by getRegistry.
    """
    def __init__(__self__, api_subnet_allow_lists=None, features=None, garbage_collection_schedules=None, hostname=None, id=None, location=None, maintenance_windows=None, name=None, partial_match=None, storage_usages=None):
        if api_subnet_allow_lists and not isinstance(api_subnet_allow_lists, list):
            raise TypeError("Expected argument 'api_subnet_allow_lists' to be a list")
        pulumi.set(__self__, "api_subnet_allow_lists", api_subnet_allow_lists)
        if features and not isinstance(features, list):
            raise TypeError("Expected argument 'features' to be a list")
        pulumi.set(__self__, "features", features)
        if garbage_collection_schedules and not isinstance(garbage_collection_schedules, list):
            raise TypeError("Expected argument 'garbage_collection_schedules' to be a list")
        pulumi.set(__self__, "garbage_collection_schedules", garbage_collection_schedules)
        if hostname and not isinstance(hostname, str):
            raise TypeError("Expected argument 'hostname' to be a str")
        pulumi.set(__self__, "hostname", hostname)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if maintenance_windows and not isinstance(maintenance_windows, list):
            raise TypeError("Expected argument 'maintenance_windows' to be a list")
        pulumi.set(__self__, "maintenance_windows", maintenance_windows)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if partial_match and not isinstance(partial_match, bool):
            raise TypeError("Expected argument 'partial_match' to be a bool")
        pulumi.set(__self__, "partial_match", partial_match)
        if storage_usages and not isinstance(storage_usages, list):
            raise TypeError("Expected argument 'storage_usages' to be a list")
        pulumi.set(__self__, "storage_usages", storage_usages)

    @property
    @pulumi.getter(name="apiSubnetAllowLists")
    def api_subnet_allow_lists(self) -> Sequence[str]:
        """
        The subnet CIDRs that are allowed to connect to the registry.  Specify "a.b.c.d/32" for an individual IP address. __Note__: If this list is empty or not set, there are no restrictions.
        """
        return pulumi.get(self, "api_subnet_allow_lists")

    @property
    @pulumi.getter
    def features(self) -> Sequence['outputs.GetRegistryFeatureResult']:
        return pulumi.get(self, "features")

    @property
    @pulumi.getter(name="garbageCollectionSchedules")
    def garbage_collection_schedules(self) -> Sequence['outputs.GetRegistryGarbageCollectionScheduleResult']:
        return pulumi.get(self, "garbage_collection_schedules")

    @property
    @pulumi.getter
    def hostname(self) -> str:
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Id of the container registry.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(self) -> Sequence['outputs.GetRegistryMaintenanceWindowResult']:
        return pulumi.get(self, "maintenance_windows")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the container registry.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partialMatch")
    def partial_match(self) -> Optional[bool]:
        return pulumi.get(self, "partial_match")

    @property
    @pulumi.getter(name="storageUsages")
    def storage_usages(self) -> Sequence['outputs.GetRegistryStorageUsageResult']:
        return pulumi.get(self, "storage_usages")


class AwaitableGetRegistryResult(GetRegistryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRegistryResult(
            api_subnet_allow_lists=self.api_subnet_allow_lists,
            features=self.features,
            garbage_collection_schedules=self.garbage_collection_schedules,
            hostname=self.hostname,
            id=self.id,
            location=self.location,
            maintenance_windows=self.maintenance_windows,
            name=self.name,
            partial_match=self.partial_match,
            storage_usages=self.storage_usages)


def get_registry(id: Optional[str] = None,
                 location: Optional[str] = None,
                 name: Optional[str] = None,
                 partial_match: Optional[bool] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRegistryResult:
    """
    The **Container Registry data source** can be used to search for and return an existing Container Registry.
    You can provide a string for the name parameter which will be compared with provisioned Container Registry.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search and make sure that your resources have unique names.

    ## Example Usage

    ### By Id
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.creg.get_registry(id="registry_id")
    ```

    ### By Name
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.creg.get_registry(name="container-registry-example")
    ```

    ### By Name with Partial Match
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.creg.get_registry(name="-example",
        partial_match=True)
    ```


    :param str id: ID of the container registry you want to search for.
    :param str name: Name of an existing container registry that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
    :param bool partial_match: Whether partial matching is allowed or not when using name argument. Default value is false.
           
           Either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['location'] = location
    __args__['name'] = name
    __args__['partialMatch'] = partial_match
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:creg/getRegistry:getRegistry', __args__, opts=opts, typ=GetRegistryResult).value

    return AwaitableGetRegistryResult(
        api_subnet_allow_lists=pulumi.get(__ret__, 'api_subnet_allow_lists'),
        features=pulumi.get(__ret__, 'features'),
        garbage_collection_schedules=pulumi.get(__ret__, 'garbage_collection_schedules'),
        hostname=pulumi.get(__ret__, 'hostname'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        maintenance_windows=pulumi.get(__ret__, 'maintenance_windows'),
        name=pulumi.get(__ret__, 'name'),
        partial_match=pulumi.get(__ret__, 'partial_match'),
        storage_usages=pulumi.get(__ret__, 'storage_usages'))
def get_registry_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                        location: Optional[pulumi.Input[Optional[str]]] = None,
                        name: Optional[pulumi.Input[Optional[str]]] = None,
                        partial_match: Optional[pulumi.Input[Optional[bool]]] = None,
                        opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetRegistryResult]:
    """
    The **Container Registry data source** can be used to search for and return an existing Container Registry.
    You can provide a string for the name parameter which will be compared with provisioned Container Registry.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search and make sure that your resources have unique names.

    ## Example Usage

    ### By Id
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.creg.get_registry(id="registry_id")
    ```

    ### By Name
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.creg.get_registry(name="container-registry-example")
    ```

    ### By Name with Partial Match
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.creg.get_registry(name="-example",
        partial_match=True)
    ```


    :param str id: ID of the container registry you want to search for.
    :param str name: Name of an existing container registry that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
    :param bool partial_match: Whether partial matching is allowed or not when using name argument. Default value is false.
           
           Either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['location'] = location
    __args__['name'] = name
    __args__['partialMatch'] = partial_match
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:creg/getRegistry:getRegistry', __args__, opts=opts, typ=GetRegistryResult)
    return __ret__.apply(lambda __response__: GetRegistryResult(
        api_subnet_allow_lists=pulumi.get(__response__, 'api_subnet_allow_lists'),
        features=pulumi.get(__response__, 'features'),
        garbage_collection_schedules=pulumi.get(__response__, 'garbage_collection_schedules'),
        hostname=pulumi.get(__response__, 'hostname'),
        id=pulumi.get(__response__, 'id'),
        location=pulumi.get(__response__, 'location'),
        maintenance_windows=pulumi.get(__response__, 'maintenance_windows'),
        name=pulumi.get(__response__, 'name'),
        partial_match=pulumi.get(__response__, 'partial_match'),
        storage_usages=pulumi.get(__response__, 'storage_usages')))
