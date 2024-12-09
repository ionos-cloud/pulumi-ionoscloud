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

__all__ = [
    'GetLocationResult',
    'AwaitableGetLocationResult',
    'get_location',
    'get_location_output',
]

@pulumi.output_type
class GetLocationResult:
    """
    A collection of values returned by getLocation.
    """
    def __init__(__self__, cpu_architectures=None, feature=None, id=None, image_aliases=None, name=None):
        if cpu_architectures and not isinstance(cpu_architectures, list):
            raise TypeError("Expected argument 'cpu_architectures' to be a list")
        pulumi.set(__self__, "cpu_architectures", cpu_architectures)
        if feature and not isinstance(feature, str):
            raise TypeError("Expected argument 'feature' to be a str")
        pulumi.set(__self__, "feature", feature)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image_aliases and not isinstance(image_aliases, list):
            raise TypeError("Expected argument 'image_aliases' to be a list")
        pulumi.set(__self__, "image_aliases", image_aliases)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="cpuArchitectures")
    def cpu_architectures(self) -> Sequence['outputs.GetLocationCpuArchitectureResult']:
        """
        Array of features and CPU families available in a location
        """
        return pulumi.get(self, "cpu_architectures")

    @property
    @pulumi.getter
    def feature(self) -> Optional[str]:
        return pulumi.get(self, "feature")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="imageAliases")
    def image_aliases(self) -> Sequence[str]:
        """
        List of image aliases available for the location
        """
        return pulumi.get(self, "image_aliases")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")


class AwaitableGetLocationResult(GetLocationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLocationResult(
            cpu_architectures=self.cpu_architectures,
            feature=self.feature,
            id=self.id,
            image_aliases=self.image_aliases,
            name=self.name)


def get_location(feature: Optional[str] = None,
                 name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLocationResult:
    """
    The **Location data source** can be used to search for and return an existing location which can then be used elsewhere in the configuration.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_location(feature="SSD",
        name="karlsruhe")
    ```


    :param str feature: A desired feature that the location must be able to provide.
    :param str name: Name of the location to search for.
    """
    __args__ = dict()
    __args__['feature'] = feature
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getLocation:getLocation', __args__, opts=opts, typ=GetLocationResult).value

    return AwaitableGetLocationResult(
        cpu_architectures=pulumi.get(__ret__, 'cpu_architectures'),
        feature=pulumi.get(__ret__, 'feature'),
        id=pulumi.get(__ret__, 'id'),
        image_aliases=pulumi.get(__ret__, 'image_aliases'),
        name=pulumi.get(__ret__, 'name'))
def get_location_output(feature: Optional[pulumi.Input[Optional[str]]] = None,
                        name: Optional[pulumi.Input[Optional[str]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLocationResult]:
    """
    The **Location data source** can be used to search for and return an existing location which can then be used elsewhere in the configuration.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_location(feature="SSD",
        name="karlsruhe")
    ```


    :param str feature: A desired feature that the location must be able to provide.
    :param str name: Name of the location to search for.
    """
    __args__ = dict()
    __args__['feature'] = feature
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:index/getLocation:getLocation', __args__, opts=opts, typ=GetLocationResult)
    return __ret__.apply(lambda __response__: GetLocationResult(
        cpu_architectures=pulumi.get(__response__, 'cpu_architectures'),
        feature=pulumi.get(__response__, 'feature'),
        id=pulumi.get(__response__, 'id'),
        image_aliases=pulumi.get(__response__, 'image_aliases'),
        name=pulumi.get(__response__, 'name')))
