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
from . import outputs

__all__ = [
    'ClusterConnections',
    'ClusterNfs',
    'ShareClientGroup',
    'ShareClientGroupNfs',
    'GetClusterConnectionResult',
    'GetClusterNfResult',
    'GetShareClientGroupResult',
    'GetShareClientGroupNfResult',
]

@pulumi.output_type
class ClusterConnections(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "datacenterId":
            suggest = "datacenter_id"
        elif key == "ipAddress":
            suggest = "ip_address"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ClusterConnections. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ClusterConnections.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ClusterConnections.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 datacenter_id: str,
                 ip_address: str,
                 lan: str):
        """
        :param str datacenter_id: The datacenter to connect your instance to.
        :param str ip_address: The IP address and subnet for your instance.
        :param str lan: The numeric LAN ID to connect your instance to.
        """
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        pulumi.set(__self__, "ip_address", ip_address)
        pulumi.set(__self__, "lan", lan)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> str:
        """
        The datacenter to connect your instance to.
        """
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> str:
        """
        The IP address and subnet for your instance.
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter
    def lan(self) -> str:
        """
        The numeric LAN ID to connect your instance to.
        """
        return pulumi.get(self, "lan")


@pulumi.output_type
class ClusterNfs(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "minVersion":
            suggest = "min_version"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ClusterNfs. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ClusterNfs.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ClusterNfs.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 min_version: Optional[str] = None):
        """
        :param str min_version: The minimum Network File Storage version
        """
        if min_version is not None:
            pulumi.set(__self__, "min_version", min_version)

    @property
    @pulumi.getter(name="minVersion")
    def min_version(self) -> Optional[str]:
        """
        The minimum Network File Storage version
        """
        return pulumi.get(self, "min_version")


@pulumi.output_type
class ShareClientGroup(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "ipNetworks":
            suggest = "ip_networks"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ShareClientGroup. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ShareClientGroup.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ShareClientGroup.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 hosts: Sequence[str],
                 ip_networks: Sequence[str],
                 description: Optional[str] = None,
                 nfs: Optional['outputs.ShareClientGroupNfs'] = None):
        """
        :param Sequence[str] hosts: A singular host allowed to connect to the share. The host can be specified as IP address and can be either IPv4 or IPv6.
        :param Sequence[str] ip_networks: The allowed host or network to which the export is being shared. The IP address can be either IPv4 or IPv6 and has to be given with CIDR notation.
        :param str description: Optional description for the clients groups.
        """
        pulumi.set(__self__, "hosts", hosts)
        pulumi.set(__self__, "ip_networks", ip_networks)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if nfs is not None:
            pulumi.set(__self__, "nfs", nfs)

    @property
    @pulumi.getter
    def hosts(self) -> Sequence[str]:
        """
        A singular host allowed to connect to the share. The host can be specified as IP address and can be either IPv4 or IPv6.
        """
        return pulumi.get(self, "hosts")

    @property
    @pulumi.getter(name="ipNetworks")
    def ip_networks(self) -> Sequence[str]:
        """
        The allowed host or network to which the export is being shared. The IP address can be either IPv4 or IPv6 and has to be given with CIDR notation.
        """
        return pulumi.get(self, "ip_networks")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Optional description for the clients groups.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def nfs(self) -> Optional['outputs.ShareClientGroupNfs']:
        return pulumi.get(self, "nfs")


@pulumi.output_type
class ShareClientGroupNfs(dict):
    def __init__(__self__, *,
                 squash: Optional[str] = None):
        """
        :param str squash: The squash mode for the export. The squash mode can be: none - No squash mode. no mapping, root-anonymous - Map root user to anonymous uid, all-anonymous - Map all users to anonymous uid.
        """
        if squash is not None:
            pulumi.set(__self__, "squash", squash)

    @property
    @pulumi.getter
    def squash(self) -> Optional[str]:
        """
        The squash mode for the export. The squash mode can be: none - No squash mode. no mapping, root-anonymous - Map root user to anonymous uid, all-anonymous - Map all users to anonymous uid.
        """
        return pulumi.get(self, "squash")


@pulumi.output_type
class GetClusterConnectionResult(dict):
    def __init__(__self__, *,
                 datacenter_id: str,
                 ip_address: str,
                 lan: str):
        """
        :param str datacenter_id: The datacenter ID of the connection.
        :param str ip_address: The IP address of the connection.
        :param str lan: The LAN of the connection.
        """
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        pulumi.set(__self__, "ip_address", ip_address)
        pulumi.set(__self__, "lan", lan)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> str:
        """
        The datacenter ID of the connection.
        """
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> str:
        """
        The IP address of the connection.
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter
    def lan(self) -> str:
        """
        The LAN of the connection.
        """
        return pulumi.get(self, "lan")


@pulumi.output_type
class GetClusterNfResult(dict):
    def __init__(__self__, *,
                 min_version: str):
        """
        :param str min_version: The minimum version of the NFS.
        """
        pulumi.set(__self__, "min_version", min_version)

    @property
    @pulumi.getter(name="minVersion")
    def min_version(self) -> str:
        """
        The minimum version of the NFS.
        """
        return pulumi.get(self, "min_version")


@pulumi.output_type
class GetShareClientGroupResult(dict):
    def __init__(__self__, *,
                 description: str,
                 hosts: Sequence[str],
                 ip_networks: Sequence[str],
                 nfs: Sequence['outputs.GetShareClientGroupNfResult']):
        """
        :param str description: Optional description for the clients groups.
        :param Sequence[str] hosts: A singular host allowed to connect to the share. The host can be specified as IP address and can be either IPv4 or IPv6.
        :param Sequence[str] ip_networks: The allowed host or network to which the export is being shared. The IP address can be either IPv4 or IPv6 and has to be given with CIDR notation.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "hosts", hosts)
        pulumi.set(__self__, "ip_networks", ip_networks)
        pulumi.set(__self__, "nfs", nfs)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Optional description for the clients groups.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def hosts(self) -> Sequence[str]:
        """
        A singular host allowed to connect to the share. The host can be specified as IP address and can be either IPv4 or IPv6.
        """
        return pulumi.get(self, "hosts")

    @property
    @pulumi.getter(name="ipNetworks")
    def ip_networks(self) -> Sequence[str]:
        """
        The allowed host or network to which the export is being shared. The IP address can be either IPv4 or IPv6 and has to be given with CIDR notation.
        """
        return pulumi.get(self, "ip_networks")

    @property
    @pulumi.getter
    def nfs(self) -> Sequence['outputs.GetShareClientGroupNfResult']:
        return pulumi.get(self, "nfs")


@pulumi.output_type
class GetShareClientGroupNfResult(dict):
    def __init__(__self__, *,
                 squash: str):
        """
        :param str squash: The squash mode for the export. The squash mode can be: none - No squash mode. no mapping, root-anonymous - Map root user to anonymous uid, all-anonymous - Map all users to anonymous uid.
        """
        pulumi.set(__self__, "squash", squash)

    @property
    @pulumi.getter
    def squash(self) -> str:
        """
        The squash mode for the export. The squash mode can be: none - No squash mode. no mapping, root-anonymous - Map root user to anonymous uid, all-anonymous - Map all users to anonymous uid.
        """
        return pulumi.get(self, "squash")


