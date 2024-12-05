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
    'GetUserResult',
    'AwaitableGetUserResult',
    'get_user',
    'get_user_output',
]

@pulumi.output_type
class GetUserResult:
    """
    A collection of values returned by getUser.
    """
    def __init__(__self__, active=None, administrator=None, email=None, first_name=None, force_sec_auth=None, groups=None, id=None, last_name=None, s3_canonical_user_id=None, sec_auth_active=None):
        if active and not isinstance(active, bool):
            raise TypeError("Expected argument 'active' to be a bool")
        pulumi.set(__self__, "active", active)
        if administrator and not isinstance(administrator, bool):
            raise TypeError("Expected argument 'administrator' to be a bool")
        pulumi.set(__self__, "administrator", administrator)
        if email and not isinstance(email, str):
            raise TypeError("Expected argument 'email' to be a str")
        pulumi.set(__self__, "email", email)
        if first_name and not isinstance(first_name, str):
            raise TypeError("Expected argument 'first_name' to be a str")
        pulumi.set(__self__, "first_name", first_name)
        if force_sec_auth and not isinstance(force_sec_auth, bool):
            raise TypeError("Expected argument 'force_sec_auth' to be a bool")
        pulumi.set(__self__, "force_sec_auth", force_sec_auth)
        if groups and not isinstance(groups, list):
            raise TypeError("Expected argument 'groups' to be a list")
        pulumi.set(__self__, "groups", groups)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_name and not isinstance(last_name, str):
            raise TypeError("Expected argument 'last_name' to be a str")
        pulumi.set(__self__, "last_name", last_name)
        if s3_canonical_user_id and not isinstance(s3_canonical_user_id, str):
            raise TypeError("Expected argument 's3_canonical_user_id' to be a str")
        pulumi.set(__self__, "s3_canonical_user_id", s3_canonical_user_id)
        if sec_auth_active and not isinstance(sec_auth_active, bool):
            raise TypeError("Expected argument 'sec_auth_active' to be a bool")
        pulumi.set(__self__, "sec_auth_active", sec_auth_active)

    @property
    @pulumi.getter
    def active(self) -> bool:
        """
        Indicates if the user is active
        """
        return pulumi.get(self, "active")

    @property
    @pulumi.getter
    def administrator(self) -> bool:
        """
        Indicates if the user has administrative rights. Administrators do not need to be managed in groups, as they automatically have access to all resources associated with the contract.
        """
        return pulumi.get(self, "administrator")

    @property
    @pulumi.getter
    def email(self) -> Optional[str]:
        """
        The e-mail address for the user.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> str:
        """
        The first name for the user.
        """
        return pulumi.get(self, "first_name")

    @property
    @pulumi.getter(name="forceSecAuth")
    def force_sec_auth(self) -> bool:
        """
        Indicates if secure (two-factor) authentication should be forced for the user (true) or not (false).
        """
        return pulumi.get(self, "force_sec_auth")

    @property
    @pulumi.getter
    def groups(self) -> Sequence['outputs.GetUserGroupResult']:
        """
        Shows the id and name of the groups that the user is a member of
        """
        return pulumi.get(self, "groups")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The id of the user.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> str:
        """
        The last name for the user.
        """
        return pulumi.get(self, "last_name")

    @property
    @pulumi.getter(name="s3CanonicalUserId")
    def s3_canonical_user_id(self) -> str:
        """
        Canonical (S3) id of the user for a given identity
        """
        return pulumi.get(self, "s3_canonical_user_id")

    @property
    @pulumi.getter(name="secAuthActive")
    def sec_auth_active(self) -> bool:
        """
        Indicates if secure authentication is active for the user or not
        """
        return pulumi.get(self, "sec_auth_active")


class AwaitableGetUserResult(GetUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserResult(
            active=self.active,
            administrator=self.administrator,
            email=self.email,
            first_name=self.first_name,
            force_sec_auth=self.force_sec_auth,
            groups=self.groups,
            id=self.id,
            last_name=self.last_name,
            s3_canonical_user_id=self.s3_canonical_user_id,
            sec_auth_active=self.sec_auth_active)


def get_user(email: Optional[str] = None,
             id: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUserResult:
    """
    The **User data source** can be used to search for and return existing users.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage

    ### By Email
    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_user(email="example@email.com")
    ```
    <!--End PulumiCodeChooser -->

    ### By Email from Env Variables - Current User
    data "ionoscloud.compute.User" "example" {
    }


    :param str email: Email of an existing user that you want to search for.
    :param str id: ID of the user you want to search for.
           
           Either `email` or `id` can be provided. If no argument is set, the provider will search for the **email that was provided for the configuration**. If none is found, the provider will return an error.
    """
    __args__ = dict()
    __args__['email'] = email
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getUser:getUser', __args__, opts=opts, typ=GetUserResult).value

    return AwaitableGetUserResult(
        active=pulumi.get(__ret__, 'active'),
        administrator=pulumi.get(__ret__, 'administrator'),
        email=pulumi.get(__ret__, 'email'),
        first_name=pulumi.get(__ret__, 'first_name'),
        force_sec_auth=pulumi.get(__ret__, 'force_sec_auth'),
        groups=pulumi.get(__ret__, 'groups'),
        id=pulumi.get(__ret__, 'id'),
        last_name=pulumi.get(__ret__, 'last_name'),
        s3_canonical_user_id=pulumi.get(__ret__, 's3_canonical_user_id'),
        sec_auth_active=pulumi.get(__ret__, 'sec_auth_active'))
def get_user_output(email: Optional[pulumi.Input[Optional[str]]] = None,
                    id: Optional[pulumi.Input[Optional[str]]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUserResult]:
    """
    The **User data source** can be used to search for and return existing users.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage

    ### By Email
    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_user(email="example@email.com")
    ```
    <!--End PulumiCodeChooser -->

    ### By Email from Env Variables - Current User
    data "ionoscloud.compute.User" "example" {
    }


    :param str email: Email of an existing user that you want to search for.
    :param str id: ID of the user you want to search for.
           
           Either `email` or `id` can be provided. If no argument is set, the provider will search for the **email that was provided for the configuration**. If none is found, the provider will return an error.
    """
    __args__ = dict()
    __args__['email'] = email
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:index/getUser:getUser', __args__, opts=opts, typ=GetUserResult)
    return __ret__.apply(lambda __response__: GetUserResult(
        active=pulumi.get(__response__, 'active'),
        administrator=pulumi.get(__response__, 'administrator'),
        email=pulumi.get(__response__, 'email'),
        first_name=pulumi.get(__response__, 'first_name'),
        force_sec_auth=pulumi.get(__response__, 'force_sec_auth'),
        groups=pulumi.get(__response__, 'groups'),
        id=pulumi.get(__response__, 'id'),
        last_name=pulumi.get(__response__, 'last_name'),
        s3_canonical_user_id=pulumi.get(__response__, 's3_canonical_user_id'),
        sec_auth_active=pulumi.get(__response__, 'sec_auth_active')))
