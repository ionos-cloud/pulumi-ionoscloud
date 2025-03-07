# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['NfsShareArgs', 'NfsShare']

@pulumi.input_type
class NfsShareArgs:
    def __init__(__self__, *,
                 client_groups: pulumi.Input[Sequence[pulumi.Input['NfsShareClientGroupArgs']]],
                 cluster_id: pulumi.Input[str],
                 location: pulumi.Input[str],
                 gid: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 quota: Optional[pulumi.Input[int]] = None,
                 uid: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a NfsShare resource.
        :param pulumi.Input[Sequence[pulumi.Input['NfsShareClientGroupArgs']]] client_groups: The groups of clients are the systems connecting to the Network File Storage cluster.
        :param pulumi.Input[str] cluster_id: The ID of the Network File Storage Cluster.
        :param pulumi.Input[str] location: The location of the Network File Storage Cluster. Available locations: 'de/fra, 'de/txl'
        :param pulumi.Input[int] gid: The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
        :param pulumi.Input[str] name: The directory being exported
        :param pulumi.Input[int] quota: The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The
               quota can be disabled using `0`.
        :param pulumi.Input[int] uid: The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
        """
        pulumi.set(__self__, "client_groups", client_groups)
        pulumi.set(__self__, "cluster_id", cluster_id)
        pulumi.set(__self__, "location", location)
        if gid is not None:
            pulumi.set(__self__, "gid", gid)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if quota is not None:
            pulumi.set(__self__, "quota", quota)
        if uid is not None:
            pulumi.set(__self__, "uid", uid)

    @property
    @pulumi.getter(name="clientGroups")
    def client_groups(self) -> pulumi.Input[Sequence[pulumi.Input['NfsShareClientGroupArgs']]]:
        """
        The groups of clients are the systems connecting to the Network File Storage cluster.
        """
        return pulumi.get(self, "client_groups")

    @client_groups.setter
    def client_groups(self, value: pulumi.Input[Sequence[pulumi.Input['NfsShareClientGroupArgs']]]):
        pulumi.set(self, "client_groups", value)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[str]:
        """
        The ID of the Network File Storage Cluster.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        The location of the Network File Storage Cluster. Available locations: 'de/fra, 'de/txl'
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def gid(self) -> Optional[pulumi.Input[int]]:
        """
        The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
        """
        return pulumi.get(self, "gid")

    @gid.setter
    def gid(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "gid", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The directory being exported
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def quota(self) -> Optional[pulumi.Input[int]]:
        """
        The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The
        quota can be disabled using `0`.
        """
        return pulumi.get(self, "quota")

    @quota.setter
    def quota(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "quota", value)

    @property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[int]]:
        """
        The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
        """
        return pulumi.get(self, "uid")

    @uid.setter
    def uid(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "uid", value)


@pulumi.input_type
class _NfsShareState:
    def __init__(__self__, *,
                 client_groups: Optional[pulumi.Input[Sequence[pulumi.Input['NfsShareClientGroupArgs']]]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 gid: Optional[pulumi.Input[int]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nfs_path: Optional[pulumi.Input[str]] = None,
                 quota: Optional[pulumi.Input[int]] = None,
                 uid: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering NfsShare resources.
        :param pulumi.Input[Sequence[pulumi.Input['NfsShareClientGroupArgs']]] client_groups: The groups of clients are the systems connecting to the Network File Storage cluster.
        :param pulumi.Input[str] cluster_id: The ID of the Network File Storage Cluster.
        :param pulumi.Input[int] gid: The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
        :param pulumi.Input[str] location: The location of the Network File Storage Cluster. Available locations: 'de/fra, 'de/txl'
        :param pulumi.Input[str] name: The directory being exported
        :param pulumi.Input[str] nfs_path: Path to the NFS export. The NFS path is the path to the directory being exported.
        :param pulumi.Input[int] quota: The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The
               quota can be disabled using `0`.
        :param pulumi.Input[int] uid: The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
        """
        if client_groups is not None:
            pulumi.set(__self__, "client_groups", client_groups)
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if gid is not None:
            pulumi.set(__self__, "gid", gid)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if nfs_path is not None:
            pulumi.set(__self__, "nfs_path", nfs_path)
        if quota is not None:
            pulumi.set(__self__, "quota", quota)
        if uid is not None:
            pulumi.set(__self__, "uid", uid)

    @property
    @pulumi.getter(name="clientGroups")
    def client_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NfsShareClientGroupArgs']]]]:
        """
        The groups of clients are the systems connecting to the Network File Storage cluster.
        """
        return pulumi.get(self, "client_groups")

    @client_groups.setter
    def client_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NfsShareClientGroupArgs']]]]):
        pulumi.set(self, "client_groups", value)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Network File Storage Cluster.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter
    def gid(self) -> Optional[pulumi.Input[int]]:
        """
        The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
        """
        return pulumi.get(self, "gid")

    @gid.setter
    def gid(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "gid", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the Network File Storage Cluster. Available locations: 'de/fra, 'de/txl'
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The directory being exported
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="nfsPath")
    def nfs_path(self) -> Optional[pulumi.Input[str]]:
        """
        Path to the NFS export. The NFS path is the path to the directory being exported.
        """
        return pulumi.get(self, "nfs_path")

    @nfs_path.setter
    def nfs_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "nfs_path", value)

    @property
    @pulumi.getter
    def quota(self) -> Optional[pulumi.Input[int]]:
        """
        The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The
        quota can be disabled using `0`.
        """
        return pulumi.get(self, "quota")

    @quota.setter
    def quota(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "quota", value)

    @property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[int]]:
        """
        The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
        """
        return pulumi.get(self, "uid")

    @uid.setter
    def uid(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "uid", value)


warnings.warn("""ionoscloud.index/nfsshare.NfsShare has been deprecated in favor of ionoscloud.nfs/share.Share""", DeprecationWarning)


class NfsShare(pulumi.CustomResource):
    warnings.warn("""ionoscloud.index/nfsshare.NfsShare has been deprecated in favor of ionoscloud.nfs/share.Share""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NfsShareClientGroupArgs']]]]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 gid: Optional[pulumi.Input[int]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 quota: Optional[pulumi.Input[int]] = None,
                 uid: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Create a NfsShare resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NfsShareClientGroupArgs']]]] client_groups: The groups of clients are the systems connecting to the Network File Storage cluster.
        :param pulumi.Input[str] cluster_id: The ID of the Network File Storage Cluster.
        :param pulumi.Input[int] gid: The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
        :param pulumi.Input[str] location: The location of the Network File Storage Cluster. Available locations: 'de/fra, 'de/txl'
        :param pulumi.Input[str] name: The directory being exported
        :param pulumi.Input[int] quota: The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The
               quota can be disabled using `0`.
        :param pulumi.Input[int] uid: The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NfsShareArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a NfsShare resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param NfsShareArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NfsShareArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NfsShareClientGroupArgs']]]]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 gid: Optional[pulumi.Input[int]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 quota: Optional[pulumi.Input[int]] = None,
                 uid: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        pulumi.log.warn("""NfsShare is deprecated: ionoscloud.index/nfsshare.NfsShare has been deprecated in favor of ionoscloud.nfs/share.Share""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NfsShareArgs.__new__(NfsShareArgs)

            if client_groups is None and not opts.urn:
                raise TypeError("Missing required property 'client_groups'")
            __props__.__dict__["client_groups"] = client_groups
            if cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_id'")
            __props__.__dict__["cluster_id"] = cluster_id
            __props__.__dict__["gid"] = gid
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["quota"] = quota
            __props__.__dict__["uid"] = uid
            __props__.__dict__["nfs_path"] = None
        super(NfsShare, __self__).__init__(
            'ionoscloud:index/nfsShare:NfsShare',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            client_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NfsShareClientGroupArgs']]]]] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            gid: Optional[pulumi.Input[int]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            nfs_path: Optional[pulumi.Input[str]] = None,
            quota: Optional[pulumi.Input[int]] = None,
            uid: Optional[pulumi.Input[int]] = None) -> 'NfsShare':
        """
        Get an existing NfsShare resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NfsShareClientGroupArgs']]]] client_groups: The groups of clients are the systems connecting to the Network File Storage cluster.
        :param pulumi.Input[str] cluster_id: The ID of the Network File Storage Cluster.
        :param pulumi.Input[int] gid: The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
        :param pulumi.Input[str] location: The location of the Network File Storage Cluster. Available locations: 'de/fra, 'de/txl'
        :param pulumi.Input[str] name: The directory being exported
        :param pulumi.Input[str] nfs_path: Path to the NFS export. The NFS path is the path to the directory being exported.
        :param pulumi.Input[int] quota: The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The
               quota can be disabled using `0`.
        :param pulumi.Input[int] uid: The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NfsShareState.__new__(_NfsShareState)

        __props__.__dict__["client_groups"] = client_groups
        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["gid"] = gid
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["nfs_path"] = nfs_path
        __props__.__dict__["quota"] = quota
        __props__.__dict__["uid"] = uid
        return NfsShare(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clientGroups")
    def client_groups(self) -> pulumi.Output[Sequence['outputs.NfsShareClientGroup']]:
        """
        The groups of clients are the systems connecting to the Network File Storage cluster.
        """
        return pulumi.get(self, "client_groups")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        The ID of the Network File Storage Cluster.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter
    def gid(self) -> pulumi.Output[Optional[int]]:
        """
        The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
        """
        return pulumi.get(self, "gid")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location of the Network File Storage Cluster. Available locations: 'de/fra, 'de/txl'
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The directory being exported
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nfsPath")
    def nfs_path(self) -> pulumi.Output[str]:
        """
        Path to the NFS export. The NFS path is the path to the directory being exported.
        """
        return pulumi.get(self, "nfs_path")

    @property
    @pulumi.getter
    def quota(self) -> pulumi.Output[Optional[int]]:
        """
        The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The
        quota can be disabled using `0`.
        """
        return pulumi.get(self, "quota")

    @property
    @pulumi.getter
    def uid(self) -> pulumi.Output[Optional[int]]:
        """
        The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
        """
        return pulumi.get(self, "uid")

