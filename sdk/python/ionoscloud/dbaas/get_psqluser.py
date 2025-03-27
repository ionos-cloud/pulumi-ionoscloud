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
    'GetPSQLUserResult',
    'AwaitableGetPSQLUserResult',
    'get_psqluser',
    'get_psqluser_output',
]

@pulumi.output_type
class GetPSQLUserResult:
    """
    A collection of values returned by getPSQLUser.
    """
    def __init__(__self__, cluster_id=None, id=None, is_system_user=None, username=None):
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_system_user and not isinstance(is_system_user, bool):
            raise TypeError("Expected argument 'is_system_user' to be a bool")
        pulumi.set(__self__, "is_system_user", is_system_user)
        if username and not isinstance(username, str):
            raise TypeError("Expected argument 'username' to be a str")
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        [string] The id of the user.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isSystemUser")
    def is_system_user(self) -> bool:
        """
        [bool] Describes whether this user is a system user or not. A system user cannot be updated or deleted.
        """
        return pulumi.get(self, "is_system_user")

    @property
    @pulumi.getter
    def username(self) -> str:
        return pulumi.get(self, "username")


class AwaitableGetPSQLUserResult(GetPSQLUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPSQLUserResult(
            cluster_id=self.cluster_id,
            id=self.id,
            is_system_user=self.is_system_user,
            username=self.username)


def get_psqluser(cluster_id: Optional[str] = None,
                 username: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPSQLUserResult:
    """
    The **PgSql User data source** can be used to search for and return an existing PgSql user.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.dbaas.get_psqluser(cluster_id="cluster_id",
        username="username")
    ```


    :param str cluster_id: [string] The ID of the cluster.
    :param str username: [string] Name of an existing user that you want to search for.
    """
    __args__ = dict()
    __args__['clusterId'] = cluster_id
    __args__['username'] = username
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:dbaas/getPSQLUser:getPSQLUser', __args__, opts=opts, typ=GetPSQLUserResult).value

    return AwaitableGetPSQLUserResult(
        cluster_id=pulumi.get(__ret__, 'cluster_id'),
        id=pulumi.get(__ret__, 'id'),
        is_system_user=pulumi.get(__ret__, 'is_system_user'),
        username=pulumi.get(__ret__, 'username'))
def get_psqluser_output(cluster_id: Optional[pulumi.Input[str]] = None,
                        username: Optional[pulumi.Input[str]] = None,
                        opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetPSQLUserResult]:
    """
    The **PgSql User data source** can be used to search for and return an existing PgSql user.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.dbaas.get_psqluser(cluster_id="cluster_id",
        username="username")
    ```


    :param str cluster_id: [string] The ID of the cluster.
    :param str username: [string] Name of an existing user that you want to search for.
    """
    __args__ = dict()
    __args__['clusterId'] = cluster_id
    __args__['username'] = username
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:dbaas/getPSQLUser:getPSQLUser', __args__, opts=opts, typ=GetPSQLUserResult)
    return __ret__.apply(lambda __response__: GetPSQLUserResult(
        cluster_id=pulumi.get(__response__, 'cluster_id'),
        id=pulumi.get(__response__, 'id'),
        is_system_user=pulumi.get(__response__, 'is_system_user'),
        username=pulumi.get(__response__, 'username')))
