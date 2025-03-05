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

__all__ = ['PSQLDatabaseArgs', 'PSQLDatabase']

@pulumi.input_type
class PSQLDatabaseArgs:
    def __init__(__self__, *,
                 cluster_id: pulumi.Input[str],
                 owner: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PSQLDatabase resource.
        :param pulumi.Input[str] cluster_id: [string] The unique ID of the cluster.
        :param pulumi.Input[str] owner: [string] The owner of the database.
        :param pulumi.Input[str] name: [string] The name of the database.
        """
        pulumi.set(__self__, "cluster_id", cluster_id)
        pulumi.set(__self__, "owner", owner)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[str]:
        """
        [string] The unique ID of the cluster.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Input[str]:
        """
        [string] The owner of the database.
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: pulumi.Input[str]):
        pulumi.set(self, "owner", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The name of the database.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _PSQLDatabaseState:
    def __init__(__self__, *,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering PSQLDatabase resources.
        :param pulumi.Input[str] cluster_id: [string] The unique ID of the cluster.
        :param pulumi.Input[str] name: [string] The name of the database.
        :param pulumi.Input[str] owner: [string] The owner of the database.
        """
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if owner is not None:
            pulumi.set(__self__, "owner", owner)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The unique ID of the cluster.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The name of the database.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The owner of the database.
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner", value)


class PSQLDatabase(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a **DbaaS PgSql Database**.

        ## Example Usage

        Create a `PgSQL` cluster as presented in the documentation for the cluster, then define a database resource
        and link it with the previously created cluster:

        ```python
        import pulumi
        import ionoscloud as ionoscloud

        example_pg_database = ionoscloud.dbaas.PSQLDatabase("example_pg_database",
            cluster_id=example["id"],
            name="exampledatabase",
            owner="exampleuser")
        ```

        ## Import

        In order to import a PgSql database, you can define an empty database resource in the plan:

        hcl

        resource "ionoscloud_pg_database" "example" {

        }

        The resource can be imported using the `clusterId` and the `name`, for example:

        ```sh
        $ pulumi import ionoscloud:dbaas/pSQLDatabase:PSQLDatabase example clusterid/name
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: [string] The unique ID of the cluster.
        :param pulumi.Input[str] name: [string] The name of the database.
        :param pulumi.Input[str] owner: [string] The owner of the database.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PSQLDatabaseArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a **DbaaS PgSql Database**.

        ## Example Usage

        Create a `PgSQL` cluster as presented in the documentation for the cluster, then define a database resource
        and link it with the previously created cluster:

        ```python
        import pulumi
        import ionoscloud as ionoscloud

        example_pg_database = ionoscloud.dbaas.PSQLDatabase("example_pg_database",
            cluster_id=example["id"],
            name="exampledatabase",
            owner="exampleuser")
        ```

        ## Import

        In order to import a PgSql database, you can define an empty database resource in the plan:

        hcl

        resource "ionoscloud_pg_database" "example" {

        }

        The resource can be imported using the `clusterId` and the `name`, for example:

        ```sh
        $ pulumi import ionoscloud:dbaas/pSQLDatabase:PSQLDatabase example clusterid/name
        ```

        :param str resource_name: The name of the resource.
        :param PSQLDatabaseArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PSQLDatabaseArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PSQLDatabaseArgs.__new__(PSQLDatabaseArgs)

            if cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_id'")
            __props__.__dict__["cluster_id"] = cluster_id
            __props__.__dict__["name"] = name
            if owner is None and not opts.urn:
                raise TypeError("Missing required property 'owner'")
            __props__.__dict__["owner"] = owner
        super(PSQLDatabase, __self__).__init__(
            'ionoscloud:dbaas/pSQLDatabase:PSQLDatabase',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            owner: Optional[pulumi.Input[str]] = None) -> 'PSQLDatabase':
        """
        Get an existing PSQLDatabase resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: [string] The unique ID of the cluster.
        :param pulumi.Input[str] name: [string] The name of the database.
        :param pulumi.Input[str] owner: [string] The owner of the database.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PSQLDatabaseState.__new__(_PSQLDatabaseState)

        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["name"] = name
        __props__.__dict__["owner"] = owner
        return PSQLDatabase(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        [string] The unique ID of the cluster.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        [string] The name of the database.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output[str]:
        """
        [string] The owner of the database.
        """
        return pulumi.get(self, "owner")

