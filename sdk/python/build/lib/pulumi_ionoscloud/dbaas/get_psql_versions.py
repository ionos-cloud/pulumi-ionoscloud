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

__all__ = [
    'GetPSQLVersionsResult',
    'AwaitableGetPSQLVersionsResult',
    'get_psql_versions',
    'get_psql_versions_output',
]

@pulumi.output_type
class GetPSQLVersionsResult:
    """
    A collection of values returned by getPSQLVersions.
    """
    def __init__(__self__, cluster_id=None, id=None, postgres_versions=None):
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if postgres_versions and not isinstance(postgres_versions, list):
            raise TypeError("Expected argument 'postgres_versions' to be a list")
        pulumi.set(__self__, "postgres_versions", postgres_versions)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[str]:
        """
        Id of the cluster
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="postgresVersions")
    def postgres_versions(self) -> Sequence[str]:
        """
        list of PostgreSQL versions.
        """
        return pulumi.get(self, "postgres_versions")


class AwaitableGetPSQLVersionsResult(GetPSQLVersionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPSQLVersionsResult(
            cluster_id=self.cluster_id,
            id=self.id,
            postgres_versions=self.postgres_versions)


def get_psql_versions(cluster_id: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPSQLVersionsResult:
    """
    The **DbaaS Postgres Versions data source** can be used to search for and retrieve list of available postgres versions for a specific cluster or for all clusters.

    ## Example Usage

    ### Retrieve list of postgres versions for a specific cluster
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.dbaas.get_psql_versions(cluster_id="cluster_id")
    ```

    ### Retrieve list of postgres versions for all clusters
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.dbaas.get_psql_versions()
    ```


    :param str cluster_id: The unique ID of the cluster.
           
           If `cluster_id` is not provided the data source will return the list of postgres version for all cluster.
    """
    __args__ = dict()
    __args__['clusterId'] = cluster_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:dbaas/getPSQLVersions:getPSQLVersions', __args__, opts=opts, typ=GetPSQLVersionsResult).value

    return AwaitableGetPSQLVersionsResult(
        cluster_id=pulumi.get(__ret__, 'cluster_id'),
        id=pulumi.get(__ret__, 'id'),
        postgres_versions=pulumi.get(__ret__, 'postgres_versions'))
def get_psql_versions_output(cluster_id: Optional[pulumi.Input[Optional[str]]] = None,
                             opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetPSQLVersionsResult]:
    """
    The **DbaaS Postgres Versions data source** can be used to search for and retrieve list of available postgres versions for a specific cluster or for all clusters.

    ## Example Usage

    ### Retrieve list of postgres versions for a specific cluster
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.dbaas.get_psql_versions(cluster_id="cluster_id")
    ```

    ### Retrieve list of postgres versions for all clusters
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.dbaas.get_psql_versions()
    ```


    :param str cluster_id: The unique ID of the cluster.
           
           If `cluster_id` is not provided the data source will return the list of postgres version for all cluster.
    """
    __args__ = dict()
    __args__['clusterId'] = cluster_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:dbaas/getPSQLVersions:getPSQLVersions', __args__, opts=opts, typ=GetPSQLVersionsResult)
    return __ret__.apply(lambda __response__: GetPSQLVersionsResult(
        cluster_id=pulumi.get(__response__, 'cluster_id'),
        id=pulumi.get(__response__, 'id'),
        postgres_versions=pulumi.get(__response__, 'postgres_versions')))
