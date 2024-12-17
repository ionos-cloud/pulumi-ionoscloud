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

__all__ = [
    'GetS3KeyResult',
    'AwaitableGetS3KeyResult',
    'get_s3_key',
    'get_s3_key_output',
]

@pulumi.output_type
class GetS3KeyResult:
    """
    A collection of values returned by getS3Key.
    """
    def __init__(__self__, active=None, id=None, secret_key=None, user_id=None):
        if active and not isinstance(active, bool):
            raise TypeError("Expected argument 'active' to be a bool")
        pulumi.set(__self__, "active", active)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if secret_key and not isinstance(secret_key, str):
            raise TypeError("Expected argument 'secret_key' to be a str")
        pulumi.set(__self__, "secret_key", secret_key)
        if user_id and not isinstance(user_id, str):
            raise TypeError("Expected argument 'user_id' to be a str")
        pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter
    def active(self) -> Optional[bool]:
        """
        The state of the IONOS Object Storage key
        """
        return pulumi.get(self, "active")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The id of the IONOS Object Storage key
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="secretKey")
    def secret_key(self) -> str:
        """
        (Computed)The IONOS Object Storage Secret key.
        """
        return pulumi.get(self, "secret_key")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> str:
        """
        The ID of the user that owns the key
        """
        return pulumi.get(self, "user_id")


class AwaitableGetS3KeyResult(GetS3KeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetS3KeyResult(
            active=self.active,
            id=self.id,
            secret_key=self.secret_key,
            user_id=self.user_id)


def get_s3_key(active: Optional[bool] = None,
               id: Optional[str] = None,
               user_id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetS3KeyResult:
    """
    The **IONOS Object Storage key data source** can be used to search for and return an existing IONOS Object Storage key.
    You can provide a string id which will be compared with provisioned IONOS Object Storage keys.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.


    :param bool active: The state of the IONOS Object Storage key
    :param str id: ID of the IONOS Object Storage key you want to search for.
    :param str user_id: [string] The UUID of the user owning the IONOS Object Storage Key.
    """
    __args__ = dict()
    __args__['active'] = active
    __args__['id'] = id
    __args__['userId'] = user_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getS3Key:getS3Key', __args__, opts=opts, typ=GetS3KeyResult).value

    return AwaitableGetS3KeyResult(
        active=pulumi.get(__ret__, 'active'),
        id=pulumi.get(__ret__, 'id'),
        secret_key=pulumi.get(__ret__, 'secret_key'),
        user_id=pulumi.get(__ret__, 'user_id'))
def get_s3_key_output(active: Optional[pulumi.Input[Optional[bool]]] = None,
                      id: Optional[pulumi.Input[Optional[str]]] = None,
                      user_id: Optional[pulumi.Input[str]] = None,
                      opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetS3KeyResult]:
    """
    The **IONOS Object Storage key data source** can be used to search for and return an existing IONOS Object Storage key.
    You can provide a string id which will be compared with provisioned IONOS Object Storage keys.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.


    :param bool active: The state of the IONOS Object Storage key
    :param str id: ID of the IONOS Object Storage key you want to search for.
    :param str user_id: [string] The UUID of the user owning the IONOS Object Storage Key.
    """
    __args__ = dict()
    __args__['active'] = active
    __args__['id'] = id
    __args__['userId'] = user_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:index/getS3Key:getS3Key', __args__, opts=opts, typ=GetS3KeyResult)
    return __ret__.apply(lambda __response__: GetS3KeyResult(
        active=pulumi.get(__response__, 'active'),
        id=pulumi.get(__response__, 'id'),
        secret_key=pulumi.get(__response__, 'secret_key'),
        user_id=pulumi.get(__response__, 'user_id')))
