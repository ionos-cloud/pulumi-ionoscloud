# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['UserArgs', 'User']

@pulumi.input_type
class UserArgs:
    def __init__(__self__, *,
                 email: pulumi.Input[str],
                 first_name: pulumi.Input[str],
                 last_name: pulumi.Input[str],
                 password: pulumi.Input[str],
                 active: Optional[pulumi.Input[bool]] = None,
                 administrator: Optional[pulumi.Input[bool]] = None,
                 force_sec_auth: Optional[pulumi.Input[bool]] = None,
                 group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a User resource.
        :param pulumi.Input[str] email: [string] An e-mail address for the user.
        :param pulumi.Input[str] first_name: [string] A first name for the user.
        :param pulumi.Input[str] last_name: [string] A last name for the user.
        :param pulumi.Input[str] password: [string] A password for the user.
        :param pulumi.Input[bool] active: [Boolean] Indicates if the user is active
        :param pulumi.Input[bool] administrator: [Boolean] Indicates if the user has administrative rights. Administrators do not need to be managed in groups, as they automatically have access to all resources associated with the contract.
        :param pulumi.Input[bool] force_sec_auth: [Boolean] Indicates if secure (two-factor) authentication should be forced for the user (true) or not (false).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] group_ids: [Set] The groups that this user will be a member of
               
               **NOTE:** Group_ids field cannot be used at the same time with user_ids field in group resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
        """
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "first_name", first_name)
        pulumi.set(__self__, "last_name", last_name)
        pulumi.set(__self__, "password", password)
        if active is not None:
            pulumi.set(__self__, "active", active)
        if administrator is not None:
            pulumi.set(__self__, "administrator", administrator)
        if force_sec_auth is not None:
            pulumi.set(__self__, "force_sec_auth", force_sec_auth)
        if group_ids is not None:
            pulumi.set(__self__, "group_ids", group_ids)

    @property
    @pulumi.getter
    def email(self) -> pulumi.Input[str]:
        """
        [string] An e-mail address for the user.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: pulumi.Input[str]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> pulumi.Input[str]:
        """
        [string] A first name for the user.
        """
        return pulumi.get(self, "first_name")

    @first_name.setter
    def first_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "first_name", value)

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> pulumi.Input[str]:
        """
        [string] A last name for the user.
        """
        return pulumi.get(self, "last_name")

    @last_name.setter
    def last_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "last_name", value)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        """
        [string] A password for the user.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def active(self) -> Optional[pulumi.Input[bool]]:
        """
        [Boolean] Indicates if the user is active
        """
        return pulumi.get(self, "active")

    @active.setter
    def active(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "active", value)

    @property
    @pulumi.getter
    def administrator(self) -> Optional[pulumi.Input[bool]]:
        """
        [Boolean] Indicates if the user has administrative rights. Administrators do not need to be managed in groups, as they automatically have access to all resources associated with the contract.
        """
        return pulumi.get(self, "administrator")

    @administrator.setter
    def administrator(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "administrator", value)

    @property
    @pulumi.getter(name="forceSecAuth")
    def force_sec_auth(self) -> Optional[pulumi.Input[bool]]:
        """
        [Boolean] Indicates if secure (two-factor) authentication should be forced for the user (true) or not (false).
        """
        return pulumi.get(self, "force_sec_auth")

    @force_sec_auth.setter
    def force_sec_auth(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force_sec_auth", value)

    @property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        [Set] The groups that this user will be a member of

        **NOTE:** Group_ids field cannot be used at the same time with user_ids field in group resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
        """
        return pulumi.get(self, "group_ids")

    @group_ids.setter
    def group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "group_ids", value)


@pulumi.input_type
class _UserState:
    def __init__(__self__, *,
                 active: Optional[pulumi.Input[bool]] = None,
                 administrator: Optional[pulumi.Input[bool]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 first_name: Optional[pulumi.Input[str]] = None,
                 force_sec_auth: Optional[pulumi.Input[bool]] = None,
                 group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 last_name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 s3_canonical_user_id: Optional[pulumi.Input[str]] = None,
                 sec_auth_active: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering User resources.
        :param pulumi.Input[bool] active: [Boolean] Indicates if the user is active
        :param pulumi.Input[bool] administrator: [Boolean] Indicates if the user has administrative rights. Administrators do not need to be managed in groups, as they automatically have access to all resources associated with the contract.
        :param pulumi.Input[str] email: [string] An e-mail address for the user.
        :param pulumi.Input[str] first_name: [string] A first name for the user.
        :param pulumi.Input[bool] force_sec_auth: [Boolean] Indicates if secure (two-factor) authentication should be forced for the user (true) or not (false).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] group_ids: [Set] The groups that this user will be a member of
               
               **NOTE:** Group_ids field cannot be used at the same time with user_ids field in group resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
        :param pulumi.Input[str] last_name: [string] A last name for the user.
        :param pulumi.Input[str] password: [string] A password for the user.
        :param pulumi.Input[str] s3_canonical_user_id: Canonical (IONOS Object Storage) id of the user for a given identity
        :param pulumi.Input[bool] sec_auth_active: [Boolean] Indicates if secure authentication is active for the user or not. *it can not be used in create requests - can be used in update*
        """
        if active is not None:
            pulumi.set(__self__, "active", active)
        if administrator is not None:
            pulumi.set(__self__, "administrator", administrator)
        if email is not None:
            pulumi.set(__self__, "email", email)
        if first_name is not None:
            pulumi.set(__self__, "first_name", first_name)
        if force_sec_auth is not None:
            pulumi.set(__self__, "force_sec_auth", force_sec_auth)
        if group_ids is not None:
            pulumi.set(__self__, "group_ids", group_ids)
        if last_name is not None:
            pulumi.set(__self__, "last_name", last_name)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if s3_canonical_user_id is not None:
            pulumi.set(__self__, "s3_canonical_user_id", s3_canonical_user_id)
        if sec_auth_active is not None:
            pulumi.set(__self__, "sec_auth_active", sec_auth_active)

    @property
    @pulumi.getter
    def active(self) -> Optional[pulumi.Input[bool]]:
        """
        [Boolean] Indicates if the user is active
        """
        return pulumi.get(self, "active")

    @active.setter
    def active(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "active", value)

    @property
    @pulumi.getter
    def administrator(self) -> Optional[pulumi.Input[bool]]:
        """
        [Boolean] Indicates if the user has administrative rights. Administrators do not need to be managed in groups, as they automatically have access to all resources associated with the contract.
        """
        return pulumi.get(self, "administrator")

    @administrator.setter
    def administrator(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "administrator", value)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        [string] An e-mail address for the user.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] A first name for the user.
        """
        return pulumi.get(self, "first_name")

    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "first_name", value)

    @property
    @pulumi.getter(name="forceSecAuth")
    def force_sec_auth(self) -> Optional[pulumi.Input[bool]]:
        """
        [Boolean] Indicates if secure (two-factor) authentication should be forced for the user (true) or not (false).
        """
        return pulumi.get(self, "force_sec_auth")

    @force_sec_auth.setter
    def force_sec_auth(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force_sec_auth", value)

    @property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        [Set] The groups that this user will be a member of

        **NOTE:** Group_ids field cannot be used at the same time with user_ids field in group resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
        """
        return pulumi.get(self, "group_ids")

    @group_ids.setter
    def group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "group_ids", value)

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] A last name for the user.
        """
        return pulumi.get(self, "last_name")

    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_name", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        [string] A password for the user.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="s3CanonicalUserId")
    def s3_canonical_user_id(self) -> Optional[pulumi.Input[str]]:
        """
        Canonical (IONOS Object Storage) id of the user for a given identity
        """
        return pulumi.get(self, "s3_canonical_user_id")

    @s3_canonical_user_id.setter
    def s3_canonical_user_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "s3_canonical_user_id", value)

    @property
    @pulumi.getter(name="secAuthActive")
    def sec_auth_active(self) -> Optional[pulumi.Input[bool]]:
        """
        [Boolean] Indicates if secure authentication is active for the user or not. *it can not be used in create requests - can be used in update*
        """
        return pulumi.get(self, "sec_auth_active")

    @sec_auth_active.setter
    def sec_auth_active(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "sec_auth_active", value)


class User(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active: Optional[pulumi.Input[bool]] = None,
                 administrator: Optional[pulumi.Input[bool]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 first_name: Optional[pulumi.Input[str]] = None,
                 force_sec_auth: Optional[pulumi.Input[bool]] = None,
                 group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 last_name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages **Users** and list users and groups associated with that user.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ionoscloud as ionoscloud
        import pulumi_random as random

        group1 = ionoscloud.compute.Group("group1",
            create_datacenter=True,
            create_snapshot=True,
            reserve_ip=True,
            access_activity_log=False,
            create_k8s_cluster=True)
        group2 = ionoscloud.compute.Group("group2",
            create_datacenter=True,
            create_snapshot=True,
            reserve_ip=True,
            access_activity_log=False,
            create_k8s_cluster=True)
        group3 = ionoscloud.compute.Group("group3",
            create_datacenter=True,
            create_snapshot=True,
            reserve_ip=True,
            access_activity_log=False)
        user_password = random.RandomPassword("userPassword",
            length=16,
            special=True,
            override_special="!#$%&*()-_=+[]{}<>:?")
        example = ionoscloud.compute.User("example",
            first_name="example",
            last_name="example",
            email="unique@email.com",
            password=user_password.result,
            administrator=False,
            force_sec_auth=False,
            active=True,
            group_ids=[
                group1.id,
                group2.id,
                group3.id,
            ])
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        Resource User can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import ionoscloud:compute/user:User myuser {user uuid}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] active: [Boolean] Indicates if the user is active
        :param pulumi.Input[bool] administrator: [Boolean] Indicates if the user has administrative rights. Administrators do not need to be managed in groups, as they automatically have access to all resources associated with the contract.
        :param pulumi.Input[str] email: [string] An e-mail address for the user.
        :param pulumi.Input[str] first_name: [string] A first name for the user.
        :param pulumi.Input[bool] force_sec_auth: [Boolean] Indicates if secure (two-factor) authentication should be forced for the user (true) or not (false).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] group_ids: [Set] The groups that this user will be a member of
               
               **NOTE:** Group_ids field cannot be used at the same time with user_ids field in group resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
        :param pulumi.Input[str] last_name: [string] A last name for the user.
        :param pulumi.Input[str] password: [string] A password for the user.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages **Users** and list users and groups associated with that user.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ionoscloud as ionoscloud
        import pulumi_random as random

        group1 = ionoscloud.compute.Group("group1",
            create_datacenter=True,
            create_snapshot=True,
            reserve_ip=True,
            access_activity_log=False,
            create_k8s_cluster=True)
        group2 = ionoscloud.compute.Group("group2",
            create_datacenter=True,
            create_snapshot=True,
            reserve_ip=True,
            access_activity_log=False,
            create_k8s_cluster=True)
        group3 = ionoscloud.compute.Group("group3",
            create_datacenter=True,
            create_snapshot=True,
            reserve_ip=True,
            access_activity_log=False)
        user_password = random.RandomPassword("userPassword",
            length=16,
            special=True,
            override_special="!#$%&*()-_=+[]{}<>:?")
        example = ionoscloud.compute.User("example",
            first_name="example",
            last_name="example",
            email="unique@email.com",
            password=user_password.result,
            administrator=False,
            force_sec_auth=False,
            active=True,
            group_ids=[
                group1.id,
                group2.id,
                group3.id,
            ])
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        Resource User can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import ionoscloud:compute/user:User myuser {user uuid}
        ```

        :param str resource_name: The name of the resource.
        :param UserArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active: Optional[pulumi.Input[bool]] = None,
                 administrator: Optional[pulumi.Input[bool]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 first_name: Optional[pulumi.Input[str]] = None,
                 force_sec_auth: Optional[pulumi.Input[bool]] = None,
                 group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 last_name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserArgs.__new__(UserArgs)

            __props__.__dict__["active"] = active
            __props__.__dict__["administrator"] = administrator
            if email is None and not opts.urn:
                raise TypeError("Missing required property 'email'")
            __props__.__dict__["email"] = email
            if first_name is None and not opts.urn:
                raise TypeError("Missing required property 'first_name'")
            __props__.__dict__["first_name"] = first_name
            __props__.__dict__["force_sec_auth"] = force_sec_auth
            __props__.__dict__["group_ids"] = group_ids
            if last_name is None and not opts.urn:
                raise TypeError("Missing required property 'last_name'")
            __props__.__dict__["last_name"] = last_name
            if password is None and not opts.urn:
                raise TypeError("Missing required property 'password'")
            __props__.__dict__["password"] = None if password is None else pulumi.Output.secret(password)
            __props__.__dict__["s3_canonical_user_id"] = None
            __props__.__dict__["sec_auth_active"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["password"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(User, __self__).__init__(
            'ionoscloud:compute/user:User',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            active: Optional[pulumi.Input[bool]] = None,
            administrator: Optional[pulumi.Input[bool]] = None,
            email: Optional[pulumi.Input[str]] = None,
            first_name: Optional[pulumi.Input[str]] = None,
            force_sec_auth: Optional[pulumi.Input[bool]] = None,
            group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            last_name: Optional[pulumi.Input[str]] = None,
            password: Optional[pulumi.Input[str]] = None,
            s3_canonical_user_id: Optional[pulumi.Input[str]] = None,
            sec_auth_active: Optional[pulumi.Input[bool]] = None) -> 'User':
        """
        Get an existing User resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] active: [Boolean] Indicates if the user is active
        :param pulumi.Input[bool] administrator: [Boolean] Indicates if the user has administrative rights. Administrators do not need to be managed in groups, as they automatically have access to all resources associated with the contract.
        :param pulumi.Input[str] email: [string] An e-mail address for the user.
        :param pulumi.Input[str] first_name: [string] A first name for the user.
        :param pulumi.Input[bool] force_sec_auth: [Boolean] Indicates if secure (two-factor) authentication should be forced for the user (true) or not (false).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] group_ids: [Set] The groups that this user will be a member of
               
               **NOTE:** Group_ids field cannot be used at the same time with user_ids field in group resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
        :param pulumi.Input[str] last_name: [string] A last name for the user.
        :param pulumi.Input[str] password: [string] A password for the user.
        :param pulumi.Input[str] s3_canonical_user_id: Canonical (IONOS Object Storage) id of the user for a given identity
        :param pulumi.Input[bool] sec_auth_active: [Boolean] Indicates if secure authentication is active for the user or not. *it can not be used in create requests - can be used in update*
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UserState.__new__(_UserState)

        __props__.__dict__["active"] = active
        __props__.__dict__["administrator"] = administrator
        __props__.__dict__["email"] = email
        __props__.__dict__["first_name"] = first_name
        __props__.__dict__["force_sec_auth"] = force_sec_auth
        __props__.__dict__["group_ids"] = group_ids
        __props__.__dict__["last_name"] = last_name
        __props__.__dict__["password"] = password
        __props__.__dict__["s3_canonical_user_id"] = s3_canonical_user_id
        __props__.__dict__["sec_auth_active"] = sec_auth_active
        return User(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def active(self) -> pulumi.Output[Optional[bool]]:
        """
        [Boolean] Indicates if the user is active
        """
        return pulumi.get(self, "active")

    @property
    @pulumi.getter
    def administrator(self) -> pulumi.Output[Optional[bool]]:
        """
        [Boolean] Indicates if the user has administrative rights. Administrators do not need to be managed in groups, as they automatically have access to all resources associated with the contract.
        """
        return pulumi.get(self, "administrator")

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[str]:
        """
        [string] An e-mail address for the user.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> pulumi.Output[str]:
        """
        [string] A first name for the user.
        """
        return pulumi.get(self, "first_name")

    @property
    @pulumi.getter(name="forceSecAuth")
    def force_sec_auth(self) -> pulumi.Output[Optional[bool]]:
        """
        [Boolean] Indicates if secure (two-factor) authentication should be forced for the user (true) or not (false).
        """
        return pulumi.get(self, "force_sec_auth")

    @property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        [Set] The groups that this user will be a member of

        **NOTE:** Group_ids field cannot be used at the same time with user_ids field in group resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
        """
        return pulumi.get(self, "group_ids")

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> pulumi.Output[str]:
        """
        [string] A last name for the user.
        """
        return pulumi.get(self, "last_name")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[str]:
        """
        [string] A password for the user.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="s3CanonicalUserId")
    def s3_canonical_user_id(self) -> pulumi.Output[str]:
        """
        Canonical (IONOS Object Storage) id of the user for a given identity
        """
        return pulumi.get(self, "s3_canonical_user_id")

    @property
    @pulumi.getter(name="secAuthActive")
    def sec_auth_active(self) -> pulumi.Output[bool]:
        """
        [Boolean] Indicates if secure authentication is active for the user or not. *it can not be used in create requests - can be used in update*
        """
        return pulumi.get(self, "sec_auth_active")

