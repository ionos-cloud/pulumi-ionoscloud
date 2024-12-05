# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetResourceResult',
    'AwaitableGetResourceResult',
    'get_resource',
    'get_resource_output',
]

@pulumi.output_type
class GetResourceResult:
    """
    A collection of values returned by getResource.
    """
    def __init__(__self__, id=None, resource_id=None, resource_type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if resource_id and not isinstance(resource_id, str):
            raise TypeError("Expected argument 'resource_id' to be a str")
        pulumi.set(__self__, "resource_id", resource_id)
        if resource_type and not isinstance(resource_type, str):
            raise TypeError("Expected argument 'resource_type' to be a str")
        pulumi.set(__self__, "resource_type", resource_type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[str]:
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[str]:
        return pulumi.get(self, "resource_type")


class AwaitableGetResourceResult(GetResourceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResourceResult(
            id=self.id,
            resource_id=self.resource_id,
            resource_type=self.resource_type)


def get_resource(resource_id: Optional[str] = None,
                 resource_type: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResourceResult:
    """
    The **Resource data source** can be used to search for and return any existing IonosCloud resource and optionally their group associations.
    You can provide a string for the resource type (datacenter,image,snapshot,ipblock) and/or resource id parameters which will be queries against available resources.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage

    ### By Type
    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_resource(resource_type="datacenter")
    ```
    <!--End PulumiCodeChooser -->


    :param str resource_id: The ID of the specific resource to retrieve information about.
    :param str resource_type: The specific type of resources to retrieve information about.
    """
    __args__ = dict()
    __args__['resourceId'] = resource_id
    __args__['resourceType'] = resource_type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getResource:getResource', __args__, opts=opts, typ=GetResourceResult).value

    return AwaitableGetResourceResult(
        id=pulumi.get(__ret__, 'id'),
        resource_id=pulumi.get(__ret__, 'resource_id'),
        resource_type=pulumi.get(__ret__, 'resource_type'))


@_utilities.lift_output_func(get_resource)
def get_resource_output(resource_id: Optional[pulumi.Input[Optional[str]]] = None,
                        resource_type: Optional[pulumi.Input[Optional[str]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetResourceResult]:
    """
    The **Resource data source** can be used to search for and return any existing IonosCloud resource and optionally their group associations.
    You can provide a string for the resource type (datacenter,image,snapshot,ipblock) and/or resource id parameters which will be queries against available resources.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage

    ### By Type
    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_resource(resource_type="datacenter")
    ```
    <!--End PulumiCodeChooser -->


    :param str resource_id: The ID of the specific resource to retrieve information about.
    :param str resource_type: The specific type of resources to retrieve information about.
    """
    ...
