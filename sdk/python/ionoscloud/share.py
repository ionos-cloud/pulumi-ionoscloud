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

__all__ = ['ShareArgs', 'Share']

@pulumi.input_type
class ShareArgs:
    def __init__(__self__, *,
                 group_id: pulumi.Input[str],
                 resource_id: pulumi.Input[str],
                 edit_privilege: Optional[pulumi.Input[bool]] = None,
                 share_privilege: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Share resource.
        :param pulumi.Input[str] group_id: [string] The ID of the specific group containing the resource to update.
        :param pulumi.Input[str] resource_id: [string] The ID of the specific resource to update.
        :param pulumi.Input[bool] edit_privilege: [Boolean] The group has permission to edit privileges on this resource.
        :param pulumi.Input[bool] share_privilege: [Boolean] The group has permission to share this resource.
               
               ⚠️ **Note:** There is a limitation due to which the creation of several shares at the same time leads
               to an error. To avoid this, `parallelism=1` can be used when running `pulumi up` command in order
               to create the resources in a sequential manner. Another solution involves the usage of `depends_on`
               attributes inside the `Share` resource to enforce the sequential creation of the shares.
        """
        pulumi.set(__self__, "group_id", group_id)
        pulumi.set(__self__, "resource_id", resource_id)
        if edit_privilege is not None:
            pulumi.set(__self__, "edit_privilege", edit_privilege)
        if share_privilege is not None:
            pulumi.set(__self__, "share_privilege", share_privilege)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Input[str]:
        """
        [string] The ID of the specific group containing the resource to update.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[str]:
        """
        [string] The ID of the specific resource to update.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter(name="editPrivilege")
    def edit_privilege(self) -> Optional[pulumi.Input[bool]]:
        """
        [Boolean] The group has permission to edit privileges on this resource.
        """
        return pulumi.get(self, "edit_privilege")

    @edit_privilege.setter
    def edit_privilege(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "edit_privilege", value)

    @property
    @pulumi.getter(name="sharePrivilege")
    def share_privilege(self) -> Optional[pulumi.Input[bool]]:
        """
        [Boolean] The group has permission to share this resource.

        ⚠️ **Note:** There is a limitation due to which the creation of several shares at the same time leads
        to an error. To avoid this, `parallelism=1` can be used when running `pulumi up` command in order
        to create the resources in a sequential manner. Another solution involves the usage of `depends_on`
        attributes inside the `Share` resource to enforce the sequential creation of the shares.
        """
        return pulumi.get(self, "share_privilege")

    @share_privilege.setter
    def share_privilege(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "share_privilege", value)


@pulumi.input_type
class _ShareState:
    def __init__(__self__, *,
                 edit_privilege: Optional[pulumi.Input[bool]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 share_privilege: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering Share resources.
        :param pulumi.Input[bool] edit_privilege: [Boolean] The group has permission to edit privileges on this resource.
        :param pulumi.Input[str] group_id: [string] The ID of the specific group containing the resource to update.
        :param pulumi.Input[str] resource_id: [string] The ID of the specific resource to update.
        :param pulumi.Input[bool] share_privilege: [Boolean] The group has permission to share this resource.
               
               ⚠️ **Note:** There is a limitation due to which the creation of several shares at the same time leads
               to an error. To avoid this, `parallelism=1` can be used when running `pulumi up` command in order
               to create the resources in a sequential manner. Another solution involves the usage of `depends_on`
               attributes inside the `Share` resource to enforce the sequential creation of the shares.
        """
        if edit_privilege is not None:
            pulumi.set(__self__, "edit_privilege", edit_privilege)
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)
        if share_privilege is not None:
            pulumi.set(__self__, "share_privilege", share_privilege)

    @property
    @pulumi.getter(name="editPrivilege")
    def edit_privilege(self) -> Optional[pulumi.Input[bool]]:
        """
        [Boolean] The group has permission to edit privileges on this resource.
        """
        return pulumi.get(self, "edit_privilege")

    @edit_privilege.setter
    def edit_privilege(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "edit_privilege", value)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The ID of the specific group containing the resource to update.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The ID of the specific resource to update.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter(name="sharePrivilege")
    def share_privilege(self) -> Optional[pulumi.Input[bool]]:
        """
        [Boolean] The group has permission to share this resource.

        ⚠️ **Note:** There is a limitation due to which the creation of several shares at the same time leads
        to an error. To avoid this, `parallelism=1` can be used when running `pulumi up` command in order
        to create the resources in a sequential manner. Another solution involves the usage of `depends_on`
        attributes inside the `Share` resource to enforce the sequential creation of the shares.
        """
        return pulumi.get(self, "share_privilege")

    @share_privilege.setter
    def share_privilege(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "share_privilege", value)


class Share(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 edit_privilege: Optional[pulumi.Input[bool]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 share_privilege: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Manages **Shares** and list shares permissions granted to the group members for each shared resource.

        ## Example Usage

        ```python
        import pulumi
        import ionoscloud as ionoscloud

        example_datacenter = ionoscloud.compute.Datacenter("exampleDatacenter",
            location="us/las",
            description="Datacenter Description",
            sec_auth_protection=False)
        example_group = ionoscloud.compute.Group("exampleGroup",
            create_datacenter=True,
            create_snapshot=True,
            reserve_ip=True,
            access_activity_log=True,
            create_pcc=True,
            s3_privilege=True,
            create_backup_unit=True,
            create_internet_access=True,
            create_k8s_cluster=True)
        example_share = ionoscloud.Share("exampleShare",
            group_id=example_group.id,
            resource_id=example_datacenter.id,
            edit_privilege=True,
            share_privilege=False)
        ```

        ## Import

        Resource Share can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import ionoscloud:index/share:Share myshare {group uuid}/{resource uuid}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] edit_privilege: [Boolean] The group has permission to edit privileges on this resource.
        :param pulumi.Input[str] group_id: [string] The ID of the specific group containing the resource to update.
        :param pulumi.Input[str] resource_id: [string] The ID of the specific resource to update.
        :param pulumi.Input[bool] share_privilege: [Boolean] The group has permission to share this resource.
               
               ⚠️ **Note:** There is a limitation due to which the creation of several shares at the same time leads
               to an error. To avoid this, `parallelism=1` can be used when running `pulumi up` command in order
               to create the resources in a sequential manner. Another solution involves the usage of `depends_on`
               attributes inside the `Share` resource to enforce the sequential creation of the shares.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ShareArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages **Shares** and list shares permissions granted to the group members for each shared resource.

        ## Example Usage

        ```python
        import pulumi
        import ionoscloud as ionoscloud

        example_datacenter = ionoscloud.compute.Datacenter("exampleDatacenter",
            location="us/las",
            description="Datacenter Description",
            sec_auth_protection=False)
        example_group = ionoscloud.compute.Group("exampleGroup",
            create_datacenter=True,
            create_snapshot=True,
            reserve_ip=True,
            access_activity_log=True,
            create_pcc=True,
            s3_privilege=True,
            create_backup_unit=True,
            create_internet_access=True,
            create_k8s_cluster=True)
        example_share = ionoscloud.Share("exampleShare",
            group_id=example_group.id,
            resource_id=example_datacenter.id,
            edit_privilege=True,
            share_privilege=False)
        ```

        ## Import

        Resource Share can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import ionoscloud:index/share:Share myshare {group uuid}/{resource uuid}
        ```

        :param str resource_name: The name of the resource.
        :param ShareArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ShareArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 edit_privilege: Optional[pulumi.Input[bool]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 share_privilege: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ShareArgs.__new__(ShareArgs)

            __props__.__dict__["edit_privilege"] = edit_privilege
            if group_id is None and not opts.urn:
                raise TypeError("Missing required property 'group_id'")
            __props__.__dict__["group_id"] = group_id
            if resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'resource_id'")
            __props__.__dict__["resource_id"] = resource_id
            __props__.__dict__["share_privilege"] = share_privilege
        super(Share, __self__).__init__(
            'ionoscloud:index/share:Share',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            edit_privilege: Optional[pulumi.Input[bool]] = None,
            group_id: Optional[pulumi.Input[str]] = None,
            resource_id: Optional[pulumi.Input[str]] = None,
            share_privilege: Optional[pulumi.Input[bool]] = None) -> 'Share':
        """
        Get an existing Share resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] edit_privilege: [Boolean] The group has permission to edit privileges on this resource.
        :param pulumi.Input[str] group_id: [string] The ID of the specific group containing the resource to update.
        :param pulumi.Input[str] resource_id: [string] The ID of the specific resource to update.
        :param pulumi.Input[bool] share_privilege: [Boolean] The group has permission to share this resource.
               
               ⚠️ **Note:** There is a limitation due to which the creation of several shares at the same time leads
               to an error. To avoid this, `parallelism=1` can be used when running `pulumi up` command in order
               to create the resources in a sequential manner. Another solution involves the usage of `depends_on`
               attributes inside the `Share` resource to enforce the sequential creation of the shares.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ShareState.__new__(_ShareState)

        __props__.__dict__["edit_privilege"] = edit_privilege
        __props__.__dict__["group_id"] = group_id
        __props__.__dict__["resource_id"] = resource_id
        __props__.__dict__["share_privilege"] = share_privilege
        return Share(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="editPrivilege")
    def edit_privilege(self) -> pulumi.Output[Optional[bool]]:
        """
        [Boolean] The group has permission to edit privileges on this resource.
        """
        return pulumi.get(self, "edit_privilege")

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Output[str]:
        """
        [string] The ID of the specific group containing the resource to update.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[str]:
        """
        [string] The ID of the specific resource to update.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="sharePrivilege")
    def share_privilege(self) -> pulumi.Output[Optional[bool]]:
        """
        [Boolean] The group has permission to share this resource.

        ⚠️ **Note:** There is a limitation due to which the creation of several shares at the same time leads
        to an error. To avoid this, `parallelism=1` can be used when running `pulumi up` command in order
        to create the resources in a sequential manner. Another solution involves the usage of `depends_on`
        attributes inside the `Share` resource to enforce the sequential creation of the shares.
        """
        return pulumi.get(self, "share_privilege")

