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

__all__ = ['S3KeyArgs', 'S3Key']

@pulumi.input_type
class S3KeyArgs:
    def __init__(__self__, *,
                 user_id: pulumi.Input[str],
                 active: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a S3Key resource.
        :param pulumi.Input[str] user_id: [string] The UUID of the user owning the IONOS Object Storage Key.
        :param pulumi.Input[bool] active: [boolean] Whether the IONOS Object Storage is active / enabled or not - Please keep in mind this is only required on create. Default value in true
        """
        pulumi.set(__self__, "user_id", user_id)
        if active is not None:
            pulumi.set(__self__, "active", active)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Input[str]:
        """
        [string] The UUID of the user owning the IONOS Object Storage Key.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_id", value)

    @property
    @pulumi.getter
    def active(self) -> Optional[pulumi.Input[bool]]:
        """
        [boolean] Whether the IONOS Object Storage is active / enabled or not - Please keep in mind this is only required on create. Default value in true
        """
        return pulumi.get(self, "active")

    @active.setter
    def active(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "active", value)


@pulumi.input_type
class _S3KeyState:
    def __init__(__self__, *,
                 active: Optional[pulumi.Input[bool]] = None,
                 secret_key: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering S3Key resources.
        :param pulumi.Input[bool] active: [boolean] Whether the IONOS Object Storage is active / enabled or not - Please keep in mind this is only required on create. Default value in true
        :param pulumi.Input[str] secret_key: The IONOS Object Storage Secret key.
        :param pulumi.Input[str] user_id: [string] The UUID of the user owning the IONOS Object Storage Key.
        """
        if active is not None:
            pulumi.set(__self__, "active", active)
        if secret_key is not None:
            pulumi.set(__self__, "secret_key", secret_key)
        if user_id is not None:
            pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter
    def active(self) -> Optional[pulumi.Input[bool]]:
        """
        [boolean] Whether the IONOS Object Storage is active / enabled or not - Please keep in mind this is only required on create. Default value in true
        """
        return pulumi.get(self, "active")

    @active.setter
    def active(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "active", value)

    @property
    @pulumi.getter(name="secretKey")
    def secret_key(self) -> Optional[pulumi.Input[str]]:
        """
        The IONOS Object Storage Secret key.
        """
        return pulumi.get(self, "secret_key")

    @secret_key.setter
    def secret_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_key", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The UUID of the user owning the IONOS Object Storage Key.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_id", value)


class S3Key(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active: Optional[pulumi.Input[bool]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages an **IONOS Object Storage Key** on IonosCloud.

        ## Example Usage

        ```python
        import pulumi
        import ionoscloud as ionoscloud

        example = ionoscloud.compute.User("example",
            first_name="example",
            last_name="example",
            email="unique@email.com",
            password="abc123-321CBA",
            administrator=False,
            force_sec_auth=False)
        example_s3_key = ionoscloud.compute.S3Key("example",
            user_id=example.id,
            active=True)
        ```

        ## Import

        An IONOS Object Storage Unit resource can be imported using its user id as well as its `resource id`, e.g.

        ```sh
        $ pulumi import ionoscloud:compute/s3Key:S3Key demo userid/s3Keyid
        ```

        This can be helpful when you want to import IONOS Object Storage Keys which you have already created manually or using other means, outside of terraform.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] active: [boolean] Whether the IONOS Object Storage is active / enabled or not - Please keep in mind this is only required on create. Default value in true
        :param pulumi.Input[str] user_id: [string] The UUID of the user owning the IONOS Object Storage Key.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: S3KeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an **IONOS Object Storage Key** on IonosCloud.

        ## Example Usage

        ```python
        import pulumi
        import ionoscloud as ionoscloud

        example = ionoscloud.compute.User("example",
            first_name="example",
            last_name="example",
            email="unique@email.com",
            password="abc123-321CBA",
            administrator=False,
            force_sec_auth=False)
        example_s3_key = ionoscloud.compute.S3Key("example",
            user_id=example.id,
            active=True)
        ```

        ## Import

        An IONOS Object Storage Unit resource can be imported using its user id as well as its `resource id`, e.g.

        ```sh
        $ pulumi import ionoscloud:compute/s3Key:S3Key demo userid/s3Keyid
        ```

        This can be helpful when you want to import IONOS Object Storage Keys which you have already created manually or using other means, outside of terraform.

        :param str resource_name: The name of the resource.
        :param S3KeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(S3KeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active: Optional[pulumi.Input[bool]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = S3KeyArgs.__new__(S3KeyArgs)

            __props__.__dict__["active"] = active
            if user_id is None and not opts.urn:
                raise TypeError("Missing required property 'user_id'")
            __props__.__dict__["user_id"] = user_id
            __props__.__dict__["secret_key"] = None
        super(S3Key, __self__).__init__(
            'ionoscloud:compute/s3Key:S3Key',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            active: Optional[pulumi.Input[bool]] = None,
            secret_key: Optional[pulumi.Input[str]] = None,
            user_id: Optional[pulumi.Input[str]] = None) -> 'S3Key':
        """
        Get an existing S3Key resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] active: [boolean] Whether the IONOS Object Storage is active / enabled or not - Please keep in mind this is only required on create. Default value in true
        :param pulumi.Input[str] secret_key: The IONOS Object Storage Secret key.
        :param pulumi.Input[str] user_id: [string] The UUID of the user owning the IONOS Object Storage Key.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _S3KeyState.__new__(_S3KeyState)

        __props__.__dict__["active"] = active
        __props__.__dict__["secret_key"] = secret_key
        __props__.__dict__["user_id"] = user_id
        return S3Key(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def active(self) -> pulumi.Output[Optional[bool]]:
        """
        [boolean] Whether the IONOS Object Storage is active / enabled or not - Please keep in mind this is only required on create. Default value in true
        """
        return pulumi.get(self, "active")

    @property
    @pulumi.getter(name="secretKey")
    def secret_key(self) -> pulumi.Output[str]:
        """
        The IONOS Object Storage Secret key.
        """
        return pulumi.get(self, "secret_key")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[str]:
        """
        [string] The UUID of the user owning the IONOS Object Storage Key.
        """
        return pulumi.get(self, "user_id")

