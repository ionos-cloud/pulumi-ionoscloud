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
    'GetAccessKeyResult',
    'AwaitableGetAccessKeyResult',
    'get_access_key',
    'get_access_key_output',
]

@pulumi.output_type
class GetAccessKeyResult:
    """
    A collection of values returned by getAccessKey.
    """
    def __init__(__self__, accesskey=None, canonical_user_id=None, contract_user_id=None, description=None, id=None):
        if accesskey and not isinstance(accesskey, str):
            raise TypeError("Expected argument 'accesskey' to be a str")
        pulumi.set(__self__, "accesskey", accesskey)
        if canonical_user_id and not isinstance(canonical_user_id, str):
            raise TypeError("Expected argument 'canonical_user_id' to be a str")
        pulumi.set(__self__, "canonical_user_id", canonical_user_id)
        if contract_user_id and not isinstance(contract_user_id, str):
            raise TypeError("Expected argument 'contract_user_id' to be a str")
        pulumi.set(__self__, "contract_user_id", contract_user_id)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def accesskey(self) -> str:
        """
        Access key metadata is a string of 92 characters.
        """
        return pulumi.get(self, "accesskey")

    @property
    @pulumi.getter(name="canonicalUserId")
    def canonical_user_id(self) -> str:
        """
        The canonical user ID which is valid for user-owned buckets.
        """
        return pulumi.get(self, "canonical_user_id")

    @property
    @pulumi.getter(name="contractUserId")
    def contract_user_id(self) -> str:
        """
        The contract user ID which is valid for contract-owned buckets
        """
        return pulumi.get(self, "contract_user_id")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the Access key.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID (UUID) of the AccessKey.
        """
        return pulumi.get(self, "id")


class AwaitableGetAccessKeyResult(GetAccessKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccessKeyResult(
            accesskey=self.accesskey,
            canonical_user_id=self.canonical_user_id,
            contract_user_id=self.contract_user_id,
            description=self.description,
            id=self.id)


def get_access_key(accesskey: Optional[str] = None,
                   description: Optional[str] = None,
                   id: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccessKeyResult:
    """
    The **Object Storage Accesskey data source** can be used to search for and return an existing Object Storage Accesskeys.

    ## Example Usage

    ### By ID
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.objectstorage.get_access_key(id="accesskey_id")
    ```


    :param str accesskey: Access key metadata is a string of 92 characters.
    :param str description: Description of the Access key.
    :param str id: Id of an existing object storage accesskey that you want to search for.
    """
    __args__ = dict()
    __args__['accesskey'] = accesskey
    __args__['description'] = description
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:objectstorage/getAccessKey:getAccessKey', __args__, opts=opts, typ=GetAccessKeyResult).value

    return AwaitableGetAccessKeyResult(
        accesskey=pulumi.get(__ret__, 'accesskey'),
        canonical_user_id=pulumi.get(__ret__, 'canonical_user_id'),
        contract_user_id=pulumi.get(__ret__, 'contract_user_id'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'))
def get_access_key_output(accesskey: Optional[pulumi.Input[Optional[str]]] = None,
                          description: Optional[pulumi.Input[Optional[str]]] = None,
                          id: Optional[pulumi.Input[Optional[str]]] = None,
                          opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetAccessKeyResult]:
    """
    The **Object Storage Accesskey data source** can be used to search for and return an existing Object Storage Accesskeys.

    ## Example Usage

    ### By ID
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.objectstorage.get_access_key(id="accesskey_id")
    ```


    :param str accesskey: Access key metadata is a string of 92 characters.
    :param str description: Description of the Access key.
    :param str id: Id of an existing object storage accesskey that you want to search for.
    """
    __args__ = dict()
    __args__['accesskey'] = accesskey
    __args__['description'] = description
    __args__['id'] = id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:objectstorage/getAccessKey:getAccessKey', __args__, opts=opts, typ=GetAccessKeyResult)
    return __ret__.apply(lambda __response__: GetAccessKeyResult(
        accesskey=pulumi.get(__response__, 'accesskey'),
        canonical_user_id=pulumi.get(__response__, 'canonical_user_id'),
        contract_user_id=pulumi.get(__response__, 'contract_user_id'),
        description=pulumi.get(__response__, 'description'),
        id=pulumi.get(__response__, 'id')))
