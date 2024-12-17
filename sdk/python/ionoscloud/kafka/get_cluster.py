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
    'GetClusterResult',
    'AwaitableGetClusterResult',
    'get_cluster',
    'get_cluster_output',
]

@pulumi.output_type
class GetClusterResult:
    """
    A collection of values returned by getCluster.
    """
    def __init__(__self__, broker_addresses=None, connections=None, id=None, location=None, name=None, partial_match=None, size=None, version=None):
        if broker_addresses and not isinstance(broker_addresses, list):
            raise TypeError("Expected argument 'broker_addresses' to be a list")
        pulumi.set(__self__, "broker_addresses", broker_addresses)
        if connections and not isinstance(connections, list):
            raise TypeError("Expected argument 'connections' to be a list")
        pulumi.set(__self__, "connections", connections)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if partial_match and not isinstance(partial_match, bool):
            raise TypeError("Expected argument 'partial_match' to be a bool")
        pulumi.set(__self__, "partial_match", partial_match)
        if size and not isinstance(size, str):
            raise TypeError("Expected argument 'size' to be a str")
        pulumi.set(__self__, "size", size)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="brokerAddresses")
    def broker_addresses(self) -> Sequence[str]:
        """
        IP address and port of cluster brokers.
        """
        return pulumi.get(self, "broker_addresses")

    @property
    @pulumi.getter
    def connections(self) -> Sequence['outputs.GetClusterConnectionResult']:
        """
        Connection information of the Kafka Cluster. Minimum items: 1, maximum items: 1.
        """
        return pulumi.get(self, "connections")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        UUID of the Kafka Cluster.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the Kafka Cluster.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partialMatch")
    def partial_match(self) -> Optional[bool]:
        return pulumi.get(self, "partial_match")

    @property
    @pulumi.getter
    def size(self) -> str:
        """
        The size of the Kafka Cluster.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        The version of the Kafka Cluster.
        """
        return pulumi.get(self, "version")


class AwaitableGetClusterResult(GetClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterResult(
            broker_addresses=self.broker_addresses,
            connections=self.connections,
            id=self.id,
            location=self.location,
            name=self.name,
            partial_match=self.partial_match,
            size=self.size,
            version=self.version)


def get_cluster(id: Optional[str] = None,
                location: Optional[str] = None,
                name: Optional[str] = None,
                partial_match: Optional[bool] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterResult:
    """
    The **Kafka Cluster data source** can be used to search for and return an existing Kafka Cluster.
    You can provide a string for the name parameter which will be compared with provisioned Kafka Clusters.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage


    :param str id: ID of an existing Kafka Cluster that you want to search for.
    :param str location: The location of the Kafka Cluster. Possible values: `de/fra`, `de/txl`
    :param str name: Name of an existing Kafka Cluster that you want to search for.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['location'] = location
    __args__['name'] = name
    __args__['partialMatch'] = partial_match
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:kafka/getCluster:getCluster', __args__, opts=opts, typ=GetClusterResult).value

    return AwaitableGetClusterResult(
        broker_addresses=pulumi.get(__ret__, 'broker_addresses'),
        connections=pulumi.get(__ret__, 'connections'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        partial_match=pulumi.get(__ret__, 'partial_match'),
        size=pulumi.get(__ret__, 'size'),
        version=pulumi.get(__ret__, 'version'))
def get_cluster_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                       location: Optional[pulumi.Input[str]] = None,
                       name: Optional[pulumi.Input[Optional[str]]] = None,
                       partial_match: Optional[pulumi.Input[Optional[bool]]] = None,
                       opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetClusterResult]:
    """
    The **Kafka Cluster data source** can be used to search for and return an existing Kafka Cluster.
    You can provide a string for the name parameter which will be compared with provisioned Kafka Clusters.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage


    :param str id: ID of an existing Kafka Cluster that you want to search for.
    :param str location: The location of the Kafka Cluster. Possible values: `de/fra`, `de/txl`
    :param str name: Name of an existing Kafka Cluster that you want to search for.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['location'] = location
    __args__['name'] = name
    __args__['partialMatch'] = partial_match
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:kafka/getCluster:getCluster', __args__, opts=opts, typ=GetClusterResult)
    return __ret__.apply(lambda __response__: GetClusterResult(
        broker_addresses=pulumi.get(__response__, 'broker_addresses'),
        connections=pulumi.get(__response__, 'connections'),
        id=pulumi.get(__response__, 'id'),
        location=pulumi.get(__response__, 'location'),
        name=pulumi.get(__response__, 'name'),
        partial_match=pulumi.get(__response__, 'partial_match'),
        size=pulumi.get(__response__, 'size'),
        version=pulumi.get(__response__, 'version')))
