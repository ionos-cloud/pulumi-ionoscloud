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

__all__ = [
    'GetK8sClustersResult',
    'AwaitableGetK8sClustersResult',
    'get_k8s_clusters',
    'get_k8s_clusters_output',
]

@pulumi.output_type
class GetK8sClustersResult:
    """
    A collection of values returned by getK8sClusters.
    """
    def __init__(__self__, clusters=None, entries=None, filters=None, id=None):
        if clusters and not isinstance(clusters, list):
            raise TypeError("Expected argument 'clusters' to be a list")
        pulumi.set(__self__, "clusters", clusters)
        if entries and not isinstance(entries, int):
            raise TypeError("Expected argument 'entries' to be a int")
        pulumi.set(__self__, "entries", entries)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def clusters(self) -> Sequence['outputs.GetK8sClustersClusterResult']:
        return pulumi.get(self, "clusters")

    @property
    @pulumi.getter
    def entries(self) -> int:
        return pulumi.get(self, "entries")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetK8sClustersFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")


class AwaitableGetK8sClustersResult(GetK8sClustersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetK8sClustersResult(
            clusters=self.clusters,
            entries=self.entries,
            filters=self.filters,
            id=self.id)


def get_k8s_clusters(filters: Optional[Sequence[Union['GetK8sClustersFilterArgs', 'GetK8sClustersFilterArgsDict']]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetK8sClustersResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['filters'] = filters
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getK8sClusters:getK8sClusters', __args__, opts=opts, typ=GetK8sClustersResult).value

    return AwaitableGetK8sClustersResult(
        clusters=pulumi.get(__ret__, 'clusters'),
        entries=pulumi.get(__ret__, 'entries'),
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'))
def get_k8s_clusters_output(filters: Optional[pulumi.Input[Optional[Sequence[Union['GetK8sClustersFilterArgs', 'GetK8sClustersFilterArgsDict']]]]] = None,
                            opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetK8sClustersResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['filters'] = filters
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:index/getK8sClusters:getK8sClusters', __args__, opts=opts, typ=GetK8sClustersResult)
    return __ret__.apply(lambda __response__: GetK8sClustersResult(
        clusters=pulumi.get(__response__, 'clusters'),
        entries=pulumi.get(__response__, 'entries'),
        filters=pulumi.get(__response__, 'filters'),
        id=pulumi.get(__response__, 'id')))
