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

__all__ = ['BackupUnitArgs', 'BackupUnit']

@pulumi.input_type
class BackupUnitArgs:
    def __init__(__self__, *,
                 email: pulumi.Input[str],
                 password: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a BackupUnit resource.
        :param pulumi.Input[str] email: The e-mail address you want assigned to the backup unit.
        :param pulumi.Input[str] password: The password you want assigned to the backup unit.
        :param pulumi.Input[str] name: Alphanumeric name you want assigned to the backup unit.
        """
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "password", password)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def email(self) -> pulumi.Input[str]:
        """
        The e-mail address you want assigned to the backup unit.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: pulumi.Input[str]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        """
        The password you want assigned to the backup unit.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Alphanumeric name you want assigned to the backup unit.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _BackupUnitState:
    def __init__(__self__, *,
                 email: Optional[pulumi.Input[str]] = None,
                 login: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering BackupUnit resources.
        :param pulumi.Input[str] email: The e-mail address you want assigned to the backup unit.
        :param pulumi.Input[str] login: The login associated with the backup unit. Derived from the contract number
        :param pulumi.Input[str] name: Alphanumeric name you want assigned to the backup unit.
        :param pulumi.Input[str] password: The password you want assigned to the backup unit.
        """
        if email is not None:
            pulumi.set(__self__, "email", email)
        if login is not None:
            pulumi.set(__self__, "login", login)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if password is not None:
            pulumi.set(__self__, "password", password)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        The e-mail address you want assigned to the backup unit.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter
    def login(self) -> Optional[pulumi.Input[str]]:
        """
        The login associated with the backup unit. Derived from the contract number
        """
        return pulumi.get(self, "login")

    @login.setter
    def login(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "login", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Alphanumeric name you want assigned to the backup unit.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        The password you want assigned to the backup unit.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)


class BackupUnit(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a BackupUnit resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] email: The e-mail address you want assigned to the backup unit.
        :param pulumi.Input[str] name: Alphanumeric name you want assigned to the backup unit.
        :param pulumi.Input[str] password: The password you want assigned to the backup unit.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BackupUnitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a BackupUnit resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param BackupUnitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BackupUnitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BackupUnitArgs.__new__(BackupUnitArgs)

            if email is None and not opts.urn:
                raise TypeError("Missing required property 'email'")
            __props__.__dict__["email"] = email
            __props__.__dict__["name"] = name
            if password is None and not opts.urn:
                raise TypeError("Missing required property 'password'")
            __props__.__dict__["password"] = None if password is None else pulumi.Output.secret(password)
            __props__.__dict__["login"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["password"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(BackupUnit, __self__).__init__(
            'ionoscloud:compute/backupUnit:BackupUnit',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            email: Optional[pulumi.Input[str]] = None,
            login: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            password: Optional[pulumi.Input[str]] = None) -> 'BackupUnit':
        """
        Get an existing BackupUnit resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] email: The e-mail address you want assigned to the backup unit.
        :param pulumi.Input[str] login: The login associated with the backup unit. Derived from the contract number
        :param pulumi.Input[str] name: Alphanumeric name you want assigned to the backup unit.
        :param pulumi.Input[str] password: The password you want assigned to the backup unit.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BackupUnitState.__new__(_BackupUnitState)

        __props__.__dict__["email"] = email
        __props__.__dict__["login"] = login
        __props__.__dict__["name"] = name
        __props__.__dict__["password"] = password
        return BackupUnit(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[str]:
        """
        The e-mail address you want assigned to the backup unit.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def login(self) -> pulumi.Output[str]:
        """
        The login associated with the backup unit. Derived from the contract number
        """
        return pulumi.get(self, "login")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Alphanumeric name you want assigned to the backup unit.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[str]:
        """
        The password you want assigned to the backup unit.
        """
        return pulumi.get(self, "password")

