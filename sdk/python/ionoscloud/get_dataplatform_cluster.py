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
    'GetDataplatformClusterResult',
    'AwaitableGetDataplatformClusterResult',
    'get_dataplatform_cluster',
    'get_dataplatform_cluster_output',
]

@pulumi.output_type
class GetDataplatformClusterResult:
    """
    A collection of values returned by getDataplatformCluster.
    """
    def __init__(__self__, ca_crt=None, configs=None, datacenter_id=None, id=None, kube_config=None, lans=None, maintenance_windows=None, name=None, partial_match=None, server=None, user_tokens=None, version=None):
        if ca_crt and not isinstance(ca_crt, str):
            raise TypeError("Expected argument 'ca_crt' to be a str")
        pulumi.set(__self__, "ca_crt", ca_crt)
        if configs and not isinstance(configs, list):
            raise TypeError("Expected argument 'configs' to be a list")
        pulumi.set(__self__, "configs", configs)
        if datacenter_id and not isinstance(datacenter_id, str):
            raise TypeError("Expected argument 'datacenter_id' to be a str")
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kube_config and not isinstance(kube_config, str):
            raise TypeError("Expected argument 'kube_config' to be a str")
        pulumi.set(__self__, "kube_config", kube_config)
        if lans and not isinstance(lans, list):
            raise TypeError("Expected argument 'lans' to be a list")
        pulumi.set(__self__, "lans", lans)
        if maintenance_windows and not isinstance(maintenance_windows, list):
            raise TypeError("Expected argument 'maintenance_windows' to be a list")
        pulumi.set(__self__, "maintenance_windows", maintenance_windows)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if partial_match and not isinstance(partial_match, bool):
            raise TypeError("Expected argument 'partial_match' to be a bool")
        pulumi.set(__self__, "partial_match", partial_match)
        if server and not isinstance(server, str):
            raise TypeError("Expected argument 'server' to be a str")
        pulumi.set(__self__, "server", server)
        if user_tokens and not isinstance(user_tokens, dict):
            raise TypeError("Expected argument 'user_tokens' to be a dict")
        pulumi.set(__self__, "user_tokens", user_tokens)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="caCrt")
    def ca_crt(self) -> str:
        """
        base64 decoded cluster certificate authority data (provided as an attribute for direct use)
        """
        return pulumi.get(self, "ca_crt")

    @property
    @pulumi.getter
    def configs(self) -> Sequence['outputs.GetDataplatformClusterConfigResult']:
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
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> str:
        """
        The UUID of the virtual data center (VDC) in which the cluster is provisioned.
        """
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The UUID of the cluster.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="kubeConfig")
    def kube_config(self) -> str:
        """
        Kubernetes configuration
        """
        return pulumi.get(self, "kube_config")

    @property
    @pulumi.getter
    def lans(self) -> Sequence['outputs.GetDataplatformClusterLanResult']:
        """
        A list of LANs you want this node pool to be part of
        """
        return pulumi.get(self, "lans")

    @property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(self) -> Sequence['outputs.GetDataplatformClusterMaintenanceWindowResult']:
        """
        Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
        """
        return pulumi.get(self, "maintenance_windows")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of your cluster.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partialMatch")
    def partial_match(self) -> Optional[bool]:
        return pulumi.get(self, "partial_match")

    @property
    @pulumi.getter
    def server(self) -> str:
        """
        cluster server (same as `config[0].clusters[0].cluster.server` but provided as an attribute for ease of use)
        """
        return pulumi.get(self, "server")

    @property
    @pulumi.getter(name="userTokens")
    def user_tokens(self) -> Mapping[str, str]:
        """
        a convenience map to be search the token of a specific user
        * key - is the user name
        * value - is the token
        """
        return pulumi.get(self, "user_tokens")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        The version of the Data Platform.
        """
        return pulumi.get(self, "version")


class AwaitableGetDataplatformClusterResult(GetDataplatformClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDataplatformClusterResult(
            ca_crt=self.ca_crt,
            configs=self.configs,
            datacenter_id=self.datacenter_id,
            id=self.id,
            kube_config=self.kube_config,
            lans=self.lans,
            maintenance_windows=self.maintenance_windows,
            name=self.name,
            partial_match=self.partial_match,
            server=self.server,
            user_tokens=self.user_tokens,
            version=self.version)


def get_dataplatform_cluster(id: Optional[str] = None,
                             name: Optional[str] = None,
                             partial_match: Optional[bool] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDataplatformClusterResult:
    """
    The **Dataplatform Cluster Data Source** can be used to search for and return an existing Dataplatform Cluster.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search and make sure that your resources have unique names.

    ## Example Usage

    ### By Name

    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_dataplatform_cluster(name="Dataplatform_Cluster_Example")
    ```

    ### By Name with Partial Match

    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_dataplatform_cluster(name="_Example",
        partial_match=True)
    ```


    :param str id: ID of the cluster you want to search for.
    :param str name: Name of an existing cluster that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
    :param bool partial_match: Whether partial matching is allowed or not when using name argument. Default value is false.
           
           Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['partialMatch'] = partial_match
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getDataplatformCluster:getDataplatformCluster', __args__, opts=opts, typ=GetDataplatformClusterResult).value

    return AwaitableGetDataplatformClusterResult(
        ca_crt=pulumi.get(__ret__, 'ca_crt'),
        configs=pulumi.get(__ret__, 'configs'),
        datacenter_id=pulumi.get(__ret__, 'datacenter_id'),
        id=pulumi.get(__ret__, 'id'),
        kube_config=pulumi.get(__ret__, 'kube_config'),
        lans=pulumi.get(__ret__, 'lans'),
        maintenance_windows=pulumi.get(__ret__, 'maintenance_windows'),
        name=pulumi.get(__ret__, 'name'),
        partial_match=pulumi.get(__ret__, 'partial_match'),
        server=pulumi.get(__ret__, 'server'),
        user_tokens=pulumi.get(__ret__, 'user_tokens'),
        version=pulumi.get(__ret__, 'version'))
def get_dataplatform_cluster_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                                    name: Optional[pulumi.Input[Optional[str]]] = None,
                                    partial_match: Optional[pulumi.Input[Optional[bool]]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDataplatformClusterResult]:
    """
    The **Dataplatform Cluster Data Source** can be used to search for and return an existing Dataplatform Cluster.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search and make sure that your resources have unique names.

    ## Example Usage

    ### By Name

    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_dataplatform_cluster(name="Dataplatform_Cluster_Example")
    ```

    ### By Name with Partial Match

    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_dataplatform_cluster(name="_Example",
        partial_match=True)
    ```


    :param str id: ID of the cluster you want to search for.
    :param str name: Name of an existing cluster that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
    :param bool partial_match: Whether partial matching is allowed or not when using name argument. Default value is false.
           
           Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['partialMatch'] = partial_match
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:index/getDataplatformCluster:getDataplatformCluster', __args__, opts=opts, typ=GetDataplatformClusterResult)
    return __ret__.apply(lambda __response__: GetDataplatformClusterResult(
        ca_crt=pulumi.get(__response__, 'ca_crt'),
        configs=pulumi.get(__response__, 'configs'),
        datacenter_id=pulumi.get(__response__, 'datacenter_id'),
        id=pulumi.get(__response__, 'id'),
        kube_config=pulumi.get(__response__, 'kube_config'),
        lans=pulumi.get(__response__, 'lans'),
        maintenance_windows=pulumi.get(__response__, 'maintenance_windows'),
        name=pulumi.get(__response__, 'name'),
        partial_match=pulumi.get(__response__, 'partial_match'),
        server=pulumi.get(__response__, 'server'),
        user_tokens=pulumi.get(__response__, 'user_tokens'),
        version=pulumi.get(__response__, 'version')))
