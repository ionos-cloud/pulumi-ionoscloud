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
from . import outputs

__all__ = [
    'GetPgClusterResult',
    'AwaitableGetPgClusterResult',
    'get_pg_cluster',
    'get_pg_cluster_output',
]

@pulumi.output_type
class GetPgClusterResult:
    """
    A collection of values returned by getPgCluster.
    """
    def __init__(__self__, backup_location=None, connection_poolers=None, connections=None, cores=None, display_name=None, dns_name=None, from_backups=None, id=None, instances=None, location=None, maintenance_windows=None, postgres_version=None, ram=None, storage_size=None, storage_type=None, synchronization_mode=None):
        if backup_location and not isinstance(backup_location, str):
            raise TypeError("Expected argument 'backup_location' to be a str")
        pulumi.set(__self__, "backup_location", backup_location)
        if connection_poolers and not isinstance(connection_poolers, list):
            raise TypeError("Expected argument 'connection_poolers' to be a list")
        pulumi.set(__self__, "connection_poolers", connection_poolers)
        if connections and not isinstance(connections, list):
            raise TypeError("Expected argument 'connections' to be a list")
        pulumi.set(__self__, "connections", connections)
        if cores and not isinstance(cores, int):
            raise TypeError("Expected argument 'cores' to be a int")
        pulumi.set(__self__, "cores", cores)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if dns_name and not isinstance(dns_name, str):
            raise TypeError("Expected argument 'dns_name' to be a str")
        pulumi.set(__self__, "dns_name", dns_name)
        if from_backups and not isinstance(from_backups, list):
            raise TypeError("Expected argument 'from_backups' to be a list")
        pulumi.set(__self__, "from_backups", from_backups)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instances and not isinstance(instances, int):
            raise TypeError("Expected argument 'instances' to be a int")
        pulumi.set(__self__, "instances", instances)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if maintenance_windows and not isinstance(maintenance_windows, list):
            raise TypeError("Expected argument 'maintenance_windows' to be a list")
        pulumi.set(__self__, "maintenance_windows", maintenance_windows)
        if postgres_version and not isinstance(postgres_version, str):
            raise TypeError("Expected argument 'postgres_version' to be a str")
        pulumi.set(__self__, "postgres_version", postgres_version)
        if ram and not isinstance(ram, int):
            raise TypeError("Expected argument 'ram' to be a int")
        pulumi.set(__self__, "ram", ram)
        if storage_size and not isinstance(storage_size, int):
            raise TypeError("Expected argument 'storage_size' to be a int")
        pulumi.set(__self__, "storage_size", storage_size)
        if storage_type and not isinstance(storage_type, str):
            raise TypeError("Expected argument 'storage_type' to be a str")
        pulumi.set(__self__, "storage_type", storage_type)
        if synchronization_mode and not isinstance(synchronization_mode, str):
            raise TypeError("Expected argument 'synchronization_mode' to be a str")
        pulumi.set(__self__, "synchronization_mode", synchronization_mode)

    @property
    @pulumi.getter(name="backupLocation")
    def backup_location(self) -> str:
        return pulumi.get(self, "backup_location")

    @property
    @pulumi.getter(name="connectionPoolers")
    def connection_poolers(self) -> Sequence['outputs.GetPgClusterConnectionPoolerResult']:
        return pulumi.get(self, "connection_poolers")

    @property
    @pulumi.getter
    def connections(self) -> Sequence['outputs.GetPgClusterConnectionResult']:
        return pulumi.get(self, "connections")

    @property
    @pulumi.getter
    def cores(self) -> int:
        return pulumi.get(self, "cores")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> str:
        return pulumi.get(self, "dns_name")

    @property
    @pulumi.getter(name="fromBackups")
    def from_backups(self) -> Sequence['outputs.GetPgClusterFromBackupResult']:
        return pulumi.get(self, "from_backups")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def instances(self) -> int:
        return pulumi.get(self, "instances")

    @property
    @pulumi.getter
    def location(self) -> str:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(self) -> Sequence['outputs.GetPgClusterMaintenanceWindowResult']:
        return pulumi.get(self, "maintenance_windows")

    @property
    @pulumi.getter(name="postgresVersion")
    def postgres_version(self) -> str:
        return pulumi.get(self, "postgres_version")

    @property
    @pulumi.getter
    def ram(self) -> int:
        return pulumi.get(self, "ram")

    @property
    @pulumi.getter(name="storageSize")
    def storage_size(self) -> int:
        return pulumi.get(self, "storage_size")

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> str:
        return pulumi.get(self, "storage_type")

    @property
    @pulumi.getter(name="synchronizationMode")
    def synchronization_mode(self) -> str:
        return pulumi.get(self, "synchronization_mode")


class AwaitableGetPgClusterResult(GetPgClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPgClusterResult(
            backup_location=self.backup_location,
            connection_poolers=self.connection_poolers,
            connections=self.connections,
            cores=self.cores,
            display_name=self.display_name,
            dns_name=self.dns_name,
            from_backups=self.from_backups,
            id=self.id,
            instances=self.instances,
            location=self.location,
            maintenance_windows=self.maintenance_windows,
            postgres_version=self.postgres_version,
            ram=self.ram,
            storage_size=self.storage_size,
            storage_type=self.storage_type,
            synchronization_mode=self.synchronization_mode)


def get_pg_cluster(display_name: Optional[str] = None,
                   id: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPgClusterResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['displayName'] = display_name
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getPgCluster:getPgCluster', __args__, opts=opts, typ=GetPgClusterResult).value

    return AwaitableGetPgClusterResult(
        backup_location=pulumi.get(__ret__, 'backup_location'),
        connection_poolers=pulumi.get(__ret__, 'connection_poolers'),
        connections=pulumi.get(__ret__, 'connections'),
        cores=pulumi.get(__ret__, 'cores'),
        display_name=pulumi.get(__ret__, 'display_name'),
        dns_name=pulumi.get(__ret__, 'dns_name'),
        from_backups=pulumi.get(__ret__, 'from_backups'),
        id=pulumi.get(__ret__, 'id'),
        instances=pulumi.get(__ret__, 'instances'),
        location=pulumi.get(__ret__, 'location'),
        maintenance_windows=pulumi.get(__ret__, 'maintenance_windows'),
        postgres_version=pulumi.get(__ret__, 'postgres_version'),
        ram=pulumi.get(__ret__, 'ram'),
        storage_size=pulumi.get(__ret__, 'storage_size'),
        storage_type=pulumi.get(__ret__, 'storage_type'),
        synchronization_mode=pulumi.get(__ret__, 'synchronization_mode'))
def get_pg_cluster_output(display_name: Optional[pulumi.Input[Optional[str]]] = None,
                          id: Optional[pulumi.Input[Optional[str]]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPgClusterResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['displayName'] = display_name
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:index/getPgCluster:getPgCluster', __args__, opts=opts, typ=GetPgClusterResult)
    return __ret__.apply(lambda __response__: GetPgClusterResult(
        backup_location=pulumi.get(__response__, 'backup_location'),
        connection_poolers=pulumi.get(__response__, 'connection_poolers'),
        connections=pulumi.get(__response__, 'connections'),
        cores=pulumi.get(__response__, 'cores'),
        display_name=pulumi.get(__response__, 'display_name'),
        dns_name=pulumi.get(__response__, 'dns_name'),
        from_backups=pulumi.get(__response__, 'from_backups'),
        id=pulumi.get(__response__, 'id'),
        instances=pulumi.get(__response__, 'instances'),
        location=pulumi.get(__response__, 'location'),
        maintenance_windows=pulumi.get(__response__, 'maintenance_windows'),
        postgres_version=pulumi.get(__response__, 'postgres_version'),
        ram=pulumi.get(__response__, 'ram'),
        storage_size=pulumi.get(__response__, 'storage_size'),
        storage_type=pulumi.get(__response__, 'storage_type'),
        synchronization_mode=pulumi.get(__response__, 'synchronization_mode')))
