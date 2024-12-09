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
    'GetMongoUserResult',
    'AwaitableGetMongoUserResult',
    'get_mongo_user',
    'get_mongo_user_output',
]

@pulumi.output_type
class GetMongoUserResult:
    """
    A collection of values returned by getMongoUser.
    """
    def __init__(__self__, cluster_id=None, database=None, id=None, roles=None, username=None):
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if database and not isinstance(database, str):
            raise TypeError("Expected argument 'database' to be a str")
        pulumi.set(__self__, "database", database)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if roles and not isinstance(roles, list):
            raise TypeError("Expected argument 'roles' to be a list")
        pulumi.set(__self__, "roles", roles)
        if username and not isinstance(username, str):
            raise TypeError("Expected argument 'username' to be a str")
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter
    def database(self) -> str:
        return pulumi.get(self, "database")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def roles(self) -> Sequence['outputs.GetMongoUserRoleResult']:
        return pulumi.get(self, "roles")

    @property
    @pulumi.getter
    def username(self) -> str:
        return pulumi.get(self, "username")


class AwaitableGetMongoUserResult(GetMongoUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMongoUserResult(
            cluster_id=self.cluster_id,
            database=self.database,
            id=self.id,
            roles=self.roles,
            username=self.username)


def get_mongo_user(cluster_id: Optional[str] = None,
                   database: Optional[str] = None,
                   id: Optional[str] = None,
                   roles: Optional[Sequence[Union['GetMongoUserRoleArgs', 'GetMongoUserRoleArgsDict']]] = None,
                   username: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMongoUserResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['clusterId'] = cluster_id
    __args__['database'] = database
    __args__['id'] = id
    __args__['roles'] = roles
    __args__['username'] = username
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getMongoUser:getMongoUser', __args__, opts=opts, typ=GetMongoUserResult).value

    return AwaitableGetMongoUserResult(
        cluster_id=pulumi.get(__ret__, 'cluster_id'),
        database=pulumi.get(__ret__, 'database'),
        id=pulumi.get(__ret__, 'id'),
        roles=pulumi.get(__ret__, 'roles'),
        username=pulumi.get(__ret__, 'username'))
def get_mongo_user_output(cluster_id: Optional[pulumi.Input[str]] = None,
                          database: Optional[pulumi.Input[Optional[str]]] = None,
                          id: Optional[pulumi.Input[Optional[str]]] = None,
                          roles: Optional[pulumi.Input[Optional[Sequence[Union['GetMongoUserRoleArgs', 'GetMongoUserRoleArgsDict']]]]] = None,
                          username: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMongoUserResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['clusterId'] = cluster_id
    __args__['database'] = database
    __args__['id'] = id
    __args__['roles'] = roles
    __args__['username'] = username
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:index/getMongoUser:getMongoUser', __args__, opts=opts, typ=GetMongoUserResult)
    return __ret__.apply(lambda __response__: GetMongoUserResult(
        cluster_id=pulumi.get(__response__, 'cluster_id'),
        database=pulumi.get(__response__, 'database'),
        id=pulumi.get(__response__, 'id'),
        roles=pulumi.get(__response__, 'roles'),
        username=pulumi.get(__response__, 'username')))
