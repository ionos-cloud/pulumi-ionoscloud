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
    'GetK8sNodePoolNodesResult',
    'AwaitableGetK8sNodePoolNodesResult',
    'get_k8s_node_pool_nodes',
    'get_k8s_node_pool_nodes_output',
]

@pulumi.output_type
class GetK8sNodePoolNodesResult:
    """
    A collection of values returned by getK8sNodePoolNodes.
    """
    def __init__(__self__, id=None, k8s_cluster_id=None, node_pool_id=None, nodes=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if k8s_cluster_id and not isinstance(k8s_cluster_id, str):
            raise TypeError("Expected argument 'k8s_cluster_id' to be a str")
        pulumi.set(__self__, "k8s_cluster_id", k8s_cluster_id)
        if node_pool_id and not isinstance(node_pool_id, str):
            raise TypeError("Expected argument 'node_pool_id' to be a str")
        pulumi.set(__self__, "node_pool_id", node_pool_id)
        if nodes and not isinstance(nodes, list):
            raise TypeError("Expected argument 'nodes' to be a list")
        pulumi.set(__self__, "nodes", nodes)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="k8sClusterId")
    def k8s_cluster_id(self) -> str:
        return pulumi.get(self, "k8s_cluster_id")

    @property
    @pulumi.getter(name="nodePoolId")
    def node_pool_id(self) -> str:
        return pulumi.get(self, "node_pool_id")

    @property
    @pulumi.getter
    def nodes(self) -> Sequence['outputs.GetK8sNodePoolNodesNodeResult']:
        return pulumi.get(self, "nodes")


class AwaitableGetK8sNodePoolNodesResult(GetK8sNodePoolNodesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetK8sNodePoolNodesResult(
            id=self.id,
            k8s_cluster_id=self.k8s_cluster_id,
            node_pool_id=self.node_pool_id,
            nodes=self.nodes)


def get_k8s_node_pool_nodes(k8s_cluster_id: Optional[str] = None,
                            node_pool_id: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetK8sNodePoolNodesResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['k8sClusterId'] = k8s_cluster_id
    __args__['nodePoolId'] = node_pool_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getK8sNodePoolNodes:getK8sNodePoolNodes', __args__, opts=opts, typ=GetK8sNodePoolNodesResult).value

    return AwaitableGetK8sNodePoolNodesResult(
        id=pulumi.get(__ret__, 'id'),
        k8s_cluster_id=pulumi.get(__ret__, 'k8s_cluster_id'),
        node_pool_id=pulumi.get(__ret__, 'node_pool_id'),
        nodes=pulumi.get(__ret__, 'nodes'))
def get_k8s_node_pool_nodes_output(k8s_cluster_id: Optional[pulumi.Input[str]] = None,
                                   node_pool_id: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetK8sNodePoolNodesResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['k8sClusterId'] = k8s_cluster_id
    __args__['nodePoolId'] = node_pool_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:index/getK8sNodePoolNodes:getK8sNodePoolNodes', __args__, opts=opts, typ=GetK8sNodePoolNodesResult)
    return __ret__.apply(lambda __response__: GetK8sNodePoolNodesResult(
        id=pulumi.get(__response__, 'id'),
        k8s_cluster_id=pulumi.get(__response__, 'k8s_cluster_id'),
        node_pool_id=pulumi.get(__response__, 'node_pool_id'),
        nodes=pulumi.get(__response__, 'nodes')))
