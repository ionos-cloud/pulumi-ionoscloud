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

__all__ = [
    'GetK8sClusterResult',
    'AwaitableGetK8sClusterResult',
    'get_k8s_cluster',
    'get_k8s_cluster_output',
]

@pulumi.output_type
class GetK8sClusterResult:
    """
    A collection of values returned by getK8sCluster.
    """
    def __init__(__self__, api_subnet_allow_lists=None, available_upgrade_versions=None, ca_crt=None, configs=None, id=None, k8s_version=None, kube_config=None, location=None, maintenance_windows=None, name=None, nat_gateway_ip=None, node_pools=None, node_subnet=None, public=None, s3_buckets=None, server=None, state=None, user_tokens=None, viable_node_pool_versions=None):
        if api_subnet_allow_lists and not isinstance(api_subnet_allow_lists, list):
            raise TypeError("Expected argument 'api_subnet_allow_lists' to be a list")
        pulumi.set(__self__, "api_subnet_allow_lists", api_subnet_allow_lists)
        if available_upgrade_versions and not isinstance(available_upgrade_versions, list):
            raise TypeError("Expected argument 'available_upgrade_versions' to be a list")
        pulumi.set(__self__, "available_upgrade_versions", available_upgrade_versions)
        if ca_crt and not isinstance(ca_crt, str):
            raise TypeError("Expected argument 'ca_crt' to be a str")
        pulumi.set(__self__, "ca_crt", ca_crt)
        if configs and not isinstance(configs, list):
            raise TypeError("Expected argument 'configs' to be a list")
        pulumi.set(__self__, "configs", configs)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if k8s_version and not isinstance(k8s_version, str):
            raise TypeError("Expected argument 'k8s_version' to be a str")
        pulumi.set(__self__, "k8s_version", k8s_version)
        if kube_config and not isinstance(kube_config, str):
            raise TypeError("Expected argument 'kube_config' to be a str")
        pulumi.set(__self__, "kube_config", kube_config)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if maintenance_windows and not isinstance(maintenance_windows, list):
            raise TypeError("Expected argument 'maintenance_windows' to be a list")
        pulumi.set(__self__, "maintenance_windows", maintenance_windows)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if nat_gateway_ip and not isinstance(nat_gateway_ip, str):
            raise TypeError("Expected argument 'nat_gateway_ip' to be a str")
        pulumi.set(__self__, "nat_gateway_ip", nat_gateway_ip)
        if node_pools and not isinstance(node_pools, list):
            raise TypeError("Expected argument 'node_pools' to be a list")
        pulumi.set(__self__, "node_pools", node_pools)
        if node_subnet and not isinstance(node_subnet, str):
            raise TypeError("Expected argument 'node_subnet' to be a str")
        pulumi.set(__self__, "node_subnet", node_subnet)
        if public and not isinstance(public, bool):
            raise TypeError("Expected argument 'public' to be a bool")
        pulumi.set(__self__, "public", public)
        if s3_buckets and not isinstance(s3_buckets, list):
            raise TypeError("Expected argument 's3_buckets' to be a list")
        pulumi.set(__self__, "s3_buckets", s3_buckets)
        if server and not isinstance(server, str):
            raise TypeError("Expected argument 'server' to be a str")
        pulumi.set(__self__, "server", server)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if user_tokens and not isinstance(user_tokens, dict):
            raise TypeError("Expected argument 'user_tokens' to be a dict")
        pulumi.set(__self__, "user_tokens", user_tokens)
        if viable_node_pool_versions and not isinstance(viable_node_pool_versions, list):
            raise TypeError("Expected argument 'viable_node_pool_versions' to be a list")
        pulumi.set(__self__, "viable_node_pool_versions", viable_node_pool_versions)

    @property
    @pulumi.getter(name="apiSubnetAllowLists")
    def api_subnet_allow_lists(self) -> Sequence[str]:
        """
        access to the K8s API server is restricted to these CIDRs
        """
        return pulumi.get(self, "api_subnet_allow_lists")

    @property
    @pulumi.getter(name="availableUpgradeVersions")
    def available_upgrade_versions(self) -> Sequence[str]:
        """
        A list of available versions for upgrading the cluster
        """
        return pulumi.get(self, "available_upgrade_versions")

    @property
    @pulumi.getter(name="caCrt")
    def ca_crt(self) -> str:
        """
        base64 decoded cluster certificate authority data (provided as an attribute for direct use)
        """
        return pulumi.get(self, "ca_crt")

    @property
    @pulumi.getter
    def configs(self) -> Sequence['outputs.GetK8sClusterConfigResult']:
        """
        structured kubernetes config consisting of a list with 1 item with the following fields:
        * api_version - Kubernetes API Version
        * kind - "Config"
        * current-context - string
        * clusters - list of
        * name - name of cluster
        * cluster - map of
        * certificate-authority-data - **base64 decoded** cluster CA data
        * server -  server address in the form `https://host:port`
        * contexts - list of
        * name - context name
        * context - map of
        * cluster - cluster name
        * user - cluster user
        * users - list of
        * name - user name
        * user - map of
        * token - user token used for authentication
        """
        return pulumi.get(self, "configs")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        id of the cluster
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="k8sVersion")
    def k8s_version(self) -> str:
        """
        Kubernetes version
        """
        return pulumi.get(self, "k8s_version")

    @property
    @pulumi.getter(name="kubeConfig")
    def kube_config(self) -> str:
        """
        Kubernetes configuration
        """
        return pulumi.get(self, "kube_config")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        this attribute is mandatory if the cluster is private.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(self) -> Sequence['outputs.GetK8sClusterMaintenanceWindowResult']:
        """
        A maintenance window comprise of a day of the week and a time for maintenance to be allowed
        """
        return pulumi.get(self, "maintenance_windows")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        name of the cluster
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="natGatewayIp")
    def nat_gateway_ip(self) -> str:
        """
        the NAT gateway IP of the cluster if the cluster is private.
        """
        return pulumi.get(self, "nat_gateway_ip")

    @property
    @pulumi.getter(name="nodePools")
    def node_pools(self) -> Sequence[str]:
        """
        list of the IDs of the node pools in this cluster
        """
        return pulumi.get(self, "node_pools")

    @property
    @pulumi.getter(name="nodeSubnet")
    def node_subnet(self) -> str:
        """
        the node subnet of the cluster, if the cluster is private.
        """
        return pulumi.get(self, "node_subnet")

    @property
    @pulumi.getter
    def public(self) -> bool:
        """
        indicates if the cluster is public or private.
        """
        return pulumi.get(self, "public")

    @property
    @pulumi.getter(name="s3Buckets")
    def s3_buckets(self) -> Sequence['outputs.GetK8sClusterS3BucketResult']:
        """
        list of IONOS Object Storage bucket configured for K8s usage
        """
        return pulumi.get(self, "s3_buckets")

    @property
    @pulumi.getter
    def server(self) -> str:
        """
        cluster server (same as `config[0].clusters[0].cluster.server` but provided as an attribute for ease of use)
        """
        return pulumi.get(self, "server")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        one of "AVAILABLE",
        "INACTIVE",
        "BUSY",
        "DEPLOYING",
        "ACTIVE",
        "FAILED",
        "SUSPENDED",
        "FAILED_SUSPENDED",
        "UPDATING",
        "FAILED_UPDATING",
        "DESTROYING",
        "FAILED_DESTROYING",
        "TERMINATED"
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="userTokens")
    def user_tokens(self) -> Mapping[str, str]:
        """
        a convenience map to be search the token of a specific user
        - key - is the user name
        - value - is the token
        """
        return pulumi.get(self, "user_tokens")

    @property
    @pulumi.getter(name="viableNodePoolVersions")
    def viable_node_pool_versions(self) -> Sequence[str]:
        """
        A list of versions that may be used for node pools under this cluster
        """
        return pulumi.get(self, "viable_node_pool_versions")


class AwaitableGetK8sClusterResult(GetK8sClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetK8sClusterResult(
            api_subnet_allow_lists=self.api_subnet_allow_lists,
            available_upgrade_versions=self.available_upgrade_versions,
            ca_crt=self.ca_crt,
            configs=self.configs,
            id=self.id,
            k8s_version=self.k8s_version,
            kube_config=self.kube_config,
            location=self.location,
            maintenance_windows=self.maintenance_windows,
            name=self.name,
            nat_gateway_ip=self.nat_gateway_ip,
            node_pools=self.node_pools,
            node_subnet=self.node_subnet,
            public=self.public,
            s3_buckets=self.s3_buckets,
            server=self.server,
            state=self.state,
            user_tokens=self.user_tokens,
            viable_node_pool_versions=self.viable_node_pool_versions)


def get_k8s_cluster(id: Optional[str] = None,
                    name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetK8sClusterResult:
    """
    The **k8s Cluster data source** can be used to search for and return existing k8s clusters.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage

    ### By Name
    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_k8s_cluster(name="K8s Cluster Example")
    ```
    <!--End PulumiCodeChooser -->


    :param str id: ID of the cluster you want to search for.
           
           Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
    :param str name: Name of an existing cluster that you want to search for.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getK8sCluster:getK8sCluster', __args__, opts=opts, typ=GetK8sClusterResult).value

    return AwaitableGetK8sClusterResult(
        api_subnet_allow_lists=pulumi.get(__ret__, 'api_subnet_allow_lists'),
        available_upgrade_versions=pulumi.get(__ret__, 'available_upgrade_versions'),
        ca_crt=pulumi.get(__ret__, 'ca_crt'),
        configs=pulumi.get(__ret__, 'configs'),
        id=pulumi.get(__ret__, 'id'),
        k8s_version=pulumi.get(__ret__, 'k8s_version'),
        kube_config=pulumi.get(__ret__, 'kube_config'),
        location=pulumi.get(__ret__, 'location'),
        maintenance_windows=pulumi.get(__ret__, 'maintenance_windows'),
        name=pulumi.get(__ret__, 'name'),
        nat_gateway_ip=pulumi.get(__ret__, 'nat_gateway_ip'),
        node_pools=pulumi.get(__ret__, 'node_pools'),
        node_subnet=pulumi.get(__ret__, 'node_subnet'),
        public=pulumi.get(__ret__, 'public'),
        s3_buckets=pulumi.get(__ret__, 's3_buckets'),
        server=pulumi.get(__ret__, 'server'),
        state=pulumi.get(__ret__, 'state'),
        user_tokens=pulumi.get(__ret__, 'user_tokens'),
        viable_node_pool_versions=pulumi.get(__ret__, 'viable_node_pool_versions'))
def get_k8s_cluster_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                           name: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetK8sClusterResult]:
    """
    The **k8s Cluster data source** can be used to search for and return existing k8s clusters.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage

    ### By Name
    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_k8s_cluster(name="K8s Cluster Example")
    ```
    <!--End PulumiCodeChooser -->


    :param str id: ID of the cluster you want to search for.
           
           Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
    :param str name: Name of an existing cluster that you want to search for.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:index/getK8sCluster:getK8sCluster', __args__, opts=opts, typ=GetK8sClusterResult)
    return __ret__.apply(lambda __response__: GetK8sClusterResult(
        api_subnet_allow_lists=pulumi.get(__response__, 'api_subnet_allow_lists'),
        available_upgrade_versions=pulumi.get(__response__, 'available_upgrade_versions'),
        ca_crt=pulumi.get(__response__, 'ca_crt'),
        configs=pulumi.get(__response__, 'configs'),
        id=pulumi.get(__response__, 'id'),
        k8s_version=pulumi.get(__response__, 'k8s_version'),
        kube_config=pulumi.get(__response__, 'kube_config'),
        location=pulumi.get(__response__, 'location'),
        maintenance_windows=pulumi.get(__response__, 'maintenance_windows'),
        name=pulumi.get(__response__, 'name'),
        nat_gateway_ip=pulumi.get(__response__, 'nat_gateway_ip'),
        node_pools=pulumi.get(__response__, 'node_pools'),
        node_subnet=pulumi.get(__response__, 'node_subnet'),
        public=pulumi.get(__response__, 'public'),
        s3_buckets=pulumi.get(__response__, 's3_buckets'),
        server=pulumi.get(__response__, 'server'),
        state=pulumi.get(__response__, 'state'),
        user_tokens=pulumi.get(__response__, 'user_tokens'),
        viable_node_pool_versions=pulumi.get(__response__, 'viable_node_pool_versions')))
