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
from .. import _utilities

__all__ = ['PSQLUserArgs', 'PSQLUser']

@pulumi.input_type
class PSQLUserArgs:
    def __init__(__self__, *,
                 cluster_id: pulumi.Input[str],
                 password: pulumi.Input[str],
                 username: pulumi.Input[str]):
        """
        The set of arguments for constructing a PSQLUser resource.
        """
        pulumi.set(__self__, "cluster_id", cluster_id)
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def username(self) -> pulumi.Input[str]:
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: pulumi.Input[str]):
        pulumi.set(self, "username", value)


@pulumi.input_type
class _PSQLUserState:
    def __init__(__self__, *,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 is_system_user: Optional[pulumi.Input[bool]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering PSQLUser resources.
        :param pulumi.Input[bool] is_system_user: Describes whether this user is a system user or not. A system user cannot be updated or deleted.
        """
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if is_system_user is not None:
            pulumi.set(__self__, "is_system_user", is_system_user)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="isSystemUser")
    def is_system_user(self) -> Optional[pulumi.Input[bool]]:
        """
        Describes whether this user is a system user or not. A system user cannot be updated or deleted.
        """
        return pulumi.get(self, "is_system_user")

    @is_system_user.setter
    def is_system_user(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_system_user", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


class PSQLUser(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a PSQLUser resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PSQLUserArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a PSQLUser resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param PSQLUserArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PSQLUserArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PSQLUserArgs.__new__(PSQLUserArgs)

            if cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_id'")
            __props__.__dict__["cluster_id"] = cluster_id
            if password is None and not opts.urn:
                raise TypeError("Missing required property 'password'")
            __props__.__dict__["password"] = None if password is None else pulumi.Output.secret(password)
            if username is None and not opts.urn:
                raise TypeError("Missing required property 'username'")
            __props__.__dict__["username"] = username
            __props__.__dict__["is_system_user"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="ionoscloud:index/pgUser:PgUser")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["password"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(PSQLUser, __self__).__init__(
            'ionoscloud:dbaas/pSQLUser:PSQLUser',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            is_system_user: Optional[pulumi.Input[bool]] = None,
            password: Optional[pulumi.Input[str]] = None,
            username: Optional[pulumi.Input[str]] = None) -> 'PSQLUser':
        """
        Get an existing PSQLUser resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] is_system_user: Describes whether this user is a system user or not. A system user cannot be updated or deleted.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PSQLUserState.__new__(_PSQLUserState)

        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["is_system_user"] = is_system_user
        __props__.__dict__["password"] = password
        __props__.__dict__["username"] = username
        return PSQLUser(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="isSystemUser")
    def is_system_user(self) -> pulumi.Output[bool]:
        """
        Describes whether this user is a system user or not. A system user cannot be updated or deleted.
        """
        return pulumi.get(self, "is_system_user")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[str]:
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[str]:
        return pulumi.get(self, "username")

