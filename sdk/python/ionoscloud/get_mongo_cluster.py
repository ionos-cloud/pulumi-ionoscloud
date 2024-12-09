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
    'GetMongoClusterResult',
    'AwaitableGetMongoClusterResult',
    'get_mongo_cluster',
    'get_mongo_cluster_output',
]

@pulumi.output_type
class GetMongoClusterResult:
    """
    A collection of values returned by getMongoCluster.
    """
    def __init__(__self__, backups=None, bi_connectors=None, connection_string=None, connections=None, cores=None, display_name=None, edition=None, id=None, instances=None, location=None, maintenance_windows=None, mongodb_version=None, ram=None, shards=None, storage_size=None, storage_type=None, template_id=None, type=None):
        if backups and not isinstance(backups, list):
            raise TypeError("Expected argument 'backups' to be a list")
        pulumi.set(__self__, "backups", backups)
        if bi_connectors and not isinstance(bi_connectors, list):
            raise TypeError("Expected argument 'bi_connectors' to be a list")
        pulumi.set(__self__, "bi_connectors", bi_connectors)
        if connection_string and not isinstance(connection_string, str):
            raise TypeError("Expected argument 'connection_string' to be a str")
        pulumi.set(__self__, "connection_string", connection_string)
        if connections and not isinstance(connections, list):
            raise TypeError("Expected argument 'connections' to be a list")
        pulumi.set(__self__, "connections", connections)
        if cores and not isinstance(cores, int):
            raise TypeError("Expected argument 'cores' to be a int")
        pulumi.set(__self__, "cores", cores)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if edition and not isinstance(edition, str):
            raise TypeError("Expected argument 'edition' to be a str")
        pulumi.set(__self__, "edition", edition)
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
        if mongodb_version and not isinstance(mongodb_version, str):
            raise TypeError("Expected argument 'mongodb_version' to be a str")
        pulumi.set(__self__, "mongodb_version", mongodb_version)
        if ram and not isinstance(ram, int):
            raise TypeError("Expected argument 'ram' to be a int")
        pulumi.set(__self__, "ram", ram)
        if shards and not isinstance(shards, int):
            raise TypeError("Expected argument 'shards' to be a int")
        pulumi.set(__self__, "shards", shards)
        if storage_size and not isinstance(storage_size, int):
            raise TypeError("Expected argument 'storage_size' to be a int")
        pulumi.set(__self__, "storage_size", storage_size)
        if storage_type and not isinstance(storage_type, str):
            raise TypeError("Expected argument 'storage_type' to be a str")
        pulumi.set(__self__, "storage_type", storage_type)
        if template_id and not isinstance(template_id, str):
            raise TypeError("Expected argument 'template_id' to be a str")
        pulumi.set(__self__, "template_id", template_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def backups(self) -> Sequence['outputs.GetMongoClusterBackupResult']:
        return pulumi.get(self, "backups")

    @property
    @pulumi.getter(name="biConnectors")
    def bi_connectors(self) -> Sequence['outputs.GetMongoClusterBiConnectorResult']:
        return pulumi.get(self, "bi_connectors")

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> str:
        return pulumi.get(self, "connection_string")

    @property
    @pulumi.getter
    def connections(self) -> Sequence['outputs.GetMongoClusterConnectionResult']:
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
    @pulumi.getter
    def edition(self) -> str:
        return pulumi.get(self, "edition")

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
    def maintenance_windows(self) -> Sequence['outputs.GetMongoClusterMaintenanceWindowResult']:
        return pulumi.get(self, "maintenance_windows")

    @property
    @pulumi.getter(name="mongodbVersion")
    def mongodb_version(self) -> str:
        return pulumi.get(self, "mongodb_version")

    @property
    @pulumi.getter
    def ram(self) -> int:
        return pulumi.get(self, "ram")

    @property
    @pulumi.getter
    def shards(self) -> int:
        return pulumi.get(self, "shards")

    @property
    @pulumi.getter(name="storageSize")
    def storage_size(self) -> int:
        return pulumi.get(self, "storage_size")

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> str:
        return pulumi.get(self, "storage_type")

    @property
    @pulumi.getter(name="templateId")
    def template_id(self) -> str:
        return pulumi.get(self, "template_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")


class AwaitableGetMongoClusterResult(GetMongoClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMongoClusterResult(
            backups=self.backups,
            bi_connectors=self.bi_connectors,
            connection_string=self.connection_string,
            connections=self.connections,
            cores=self.cores,
            display_name=self.display_name,
            edition=self.edition,
            id=self.id,
            instances=self.instances,
            location=self.location,
            maintenance_windows=self.maintenance_windows,
            mongodb_version=self.mongodb_version,
            ram=self.ram,
            shards=self.shards,
            storage_size=self.storage_size,
            storage_type=self.storage_type,
            template_id=self.template_id,
            type=self.type)


def get_mongo_cluster(display_name: Optional[str] = None,
                      id: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMongoClusterResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['displayName'] = display_name
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getMongoCluster:getMongoCluster', __args__, opts=opts, typ=GetMongoClusterResult).value

    return AwaitableGetMongoClusterResult(
        backups=pulumi.get(__ret__, 'backups'),
        bi_connectors=pulumi.get(__ret__, 'bi_connectors'),
        connection_string=pulumi.get(__ret__, 'connection_string'),
        connections=pulumi.get(__ret__, 'connections'),
        cores=pulumi.get(__ret__, 'cores'),
        display_name=pulumi.get(__ret__, 'display_name'),
        edition=pulumi.get(__ret__, 'edition'),
        id=pulumi.get(__ret__, 'id'),
        instances=pulumi.get(__ret__, 'instances'),
        location=pulumi.get(__ret__, 'location'),
        maintenance_windows=pulumi.get(__ret__, 'maintenance_windows'),
        mongodb_version=pulumi.get(__ret__, 'mongodb_version'),
        ram=pulumi.get(__ret__, 'ram'),
        shards=pulumi.get(__ret__, 'shards'),
        storage_size=pulumi.get(__ret__, 'storage_size'),
        storage_type=pulumi.get(__ret__, 'storage_type'),
        template_id=pulumi.get(__ret__, 'template_id'),
        type=pulumi.get(__ret__, 'type'))
def get_mongo_cluster_output(display_name: Optional[pulumi.Input[Optional[str]]] = None,
                             id: Optional[pulumi.Input[Optional[str]]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMongoClusterResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['displayName'] = display_name
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:index/getMongoCluster:getMongoCluster', __args__, opts=opts, typ=GetMongoClusterResult)
    return __ret__.apply(lambda __response__: GetMongoClusterResult(
        backups=pulumi.get(__response__, 'backups'),
        bi_connectors=pulumi.get(__response__, 'bi_connectors'),
        connection_string=pulumi.get(__response__, 'connection_string'),
        connections=pulumi.get(__response__, 'connections'),
        cores=pulumi.get(__response__, 'cores'),
        display_name=pulumi.get(__response__, 'display_name'),
        edition=pulumi.get(__response__, 'edition'),
        id=pulumi.get(__response__, 'id'),
        instances=pulumi.get(__response__, 'instances'),
        location=pulumi.get(__response__, 'location'),
        maintenance_windows=pulumi.get(__response__, 'maintenance_windows'),
        mongodb_version=pulumi.get(__response__, 'mongodb_version'),
        ram=pulumi.get(__response__, 'ram'),
        shards=pulumi.get(__response__, 'shards'),
        storage_size=pulumi.get(__response__, 'storage_size'),
        storage_type=pulumi.get(__response__, 'storage_type'),
        template_id=pulumi.get(__response__, 'template_id'),
        type=pulumi.get(__response__, 'type')))
