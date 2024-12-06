# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetShareResult',
    'AwaitableGetShareResult',
    'get_share',
    'get_share_output',
]

@pulumi.output_type
class GetShareResult:
    """
    A collection of values returned by getShare.
    """
    def __init__(__self__, edit_privilege=None, group_id=None, id=None, resource_id=None, share_privilege=None):
        if edit_privilege and not isinstance(edit_privilege, bool):
            raise TypeError("Expected argument 'edit_privilege' to be a bool")
        pulumi.set(__self__, "edit_privilege", edit_privilege)
        if group_id and not isinstance(group_id, str):
            raise TypeError("Expected argument 'group_id' to be a str")
        pulumi.set(__self__, "group_id", group_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if resource_id and not isinstance(resource_id, str):
            raise TypeError("Expected argument 'resource_id' to be a str")
        pulumi.set(__self__, "resource_id", resource_id)
        if share_privilege and not isinstance(share_privilege, bool):
            raise TypeError("Expected argument 'share_privilege' to be a bool")
        pulumi.set(__self__, "share_privilege", share_privilege)

    @property
    @pulumi.getter(name="editPrivilege")
    def edit_privilege(self) -> Optional[bool]:
        """
        The flag that specifies if the group has permission to edit privileges on this resource.
        """
        return pulumi.get(self, "edit_privilege")

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> str:
        """
        The ID of the specific group containing the resource to update.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The id of the share resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> str:
        """
        The ID of the specific resource to update.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="sharePrivilege")
    def share_privilege(self) -> Optional[bool]:
        """
        The group has permission to share this resource.
        """
        return pulumi.get(self, "share_privilege")


class AwaitableGetShareResult(GetShareResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetShareResult(
            edit_privilege=self.edit_privilege,
            group_id=self.group_id,
            id=self.id,
            resource_id=self.resource_id,
            share_privilege=self.share_privilege)


def get_share(edit_privilege: Optional[bool] = None,
              group_id: Optional[str] = None,
              id: Optional[str] = None,
              resource_id: Optional[str] = None,
              share_privilege: Optional[bool] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetShareResult:
    """
    The **Share data source** can be used to search for and return an existing share object.
    You need to provide the group_id and resource_id to get the group resources for the shared resource.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.


    :param bool edit_privilege: The flag that specifies if the group has permission to edit privileges on this resource.
    :param str group_id: The ID of the specific group containing the resource to update.
    :param str id: The uuid of the share object
           
           
           `id`, `resource_id` and `group_id` must be provided. If any of them are missing, the datasource will return an error.
    :param str resource_id: The ID of the specific resource to update.
    :param bool share_privilege: The group has permission to share this resource.
    """
    __args__ = dict()
    __args__['editPrivilege'] = edit_privilege
    __args__['groupId'] = group_id
    __args__['id'] = id
    __args__['resourceId'] = resource_id
    __args__['sharePrivilege'] = share_privilege
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getShare:getShare', __args__, opts=opts, typ=GetShareResult).value

    return AwaitableGetShareResult(
        edit_privilege=pulumi.get(__ret__, 'edit_privilege'),
        group_id=pulumi.get(__ret__, 'group_id'),
        id=pulumi.get(__ret__, 'id'),
        resource_id=pulumi.get(__ret__, 'resource_id'),
        share_privilege=pulumi.get(__ret__, 'share_privilege'))


@_utilities.lift_output_func(get_share)
def get_share_output(edit_privilege: Optional[pulumi.Input[Optional[bool]]] = None,
                     group_id: Optional[pulumi.Input[str]] = None,
                     id: Optional[pulumi.Input[str]] = None,
                     resource_id: Optional[pulumi.Input[str]] = None,
                     share_privilege: Optional[pulumi.Input[Optional[bool]]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetShareResult]:
    """
    The **Share data source** can be used to search for and return an existing share object.
    You need to provide the group_id and resource_id to get the group resources for the shared resource.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.


    :param bool edit_privilege: The flag that specifies if the group has permission to edit privileges on this resource.
    :param str group_id: The ID of the specific group containing the resource to update.
    :param str id: The uuid of the share object
           
           
           `id`, `resource_id` and `group_id` must be provided. If any of them are missing, the datasource will return an error.
    :param str resource_id: The ID of the specific resource to update.
    :param bool share_privilege: The group has permission to share this resource.
    """
    ...
