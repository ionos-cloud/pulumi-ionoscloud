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

__all__ = [
    'GetMariadbClusterResult',
    'AwaitableGetMariadbClusterResult',
    'get_mariadb_cluster',
    'get_mariadb_cluster_output',
]

@pulumi.output_type
class GetMariadbClusterResult:
    """
    A collection of values returned by getMariadbCluster.
    """
    def __init__(__self__, connections=None, cores=None, display_name=None, dns_name=None, id=None, instances=None, location=None, maintenance_windows=None, mariadb_version=None, ram=None, storage_size=None):
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
        if mariadb_version and not isinstance(mariadb_version, str):
            raise TypeError("Expected argument 'mariadb_version' to be a str")
        pulumi.set(__self__, "mariadb_version", mariadb_version)
        if ram and not isinstance(ram, int):
            raise TypeError("Expected argument 'ram' to be a int")
        pulumi.set(__self__, "ram", ram)
        if storage_size and not isinstance(storage_size, int):
            raise TypeError("Expected argument 'storage_size' to be a int")
        pulumi.set(__self__, "storage_size", storage_size)

    @property
    @pulumi.getter
    def connections(self) -> Sequence['outputs.GetMariadbClusterConnectionResult']:
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
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def instances(self) -> int:
        return pulumi.get(self, "instances")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(self) -> Sequence['outputs.GetMariadbClusterMaintenanceWindowResult']:
        return pulumi.get(self, "maintenance_windows")

    @property
    @pulumi.getter(name="mariadbVersion")
    def mariadb_version(self) -> str:
        return pulumi.get(self, "mariadb_version")

    @property
    @pulumi.getter
    def ram(self) -> int:
        return pulumi.get(self, "ram")

    @property
    @pulumi.getter(name="storageSize")
    def storage_size(self) -> int:
        return pulumi.get(self, "storage_size")


class AwaitableGetMariadbClusterResult(GetMariadbClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMariadbClusterResult(
            connections=self.connections,
            cores=self.cores,
            display_name=self.display_name,
            dns_name=self.dns_name,
            id=self.id,
            instances=self.instances,
            location=self.location,
            maintenance_windows=self.maintenance_windows,
            mariadb_version=self.mariadb_version,
            ram=self.ram,
            storage_size=self.storage_size)


def get_mariadb_cluster(display_name: Optional[str] = None,
                        id: Optional[str] = None,
                        location: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMariadbClusterResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['displayName'] = display_name
    __args__['id'] = id
    __args__['location'] = location
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getMariadbCluster:getMariadbCluster', __args__, opts=opts, typ=GetMariadbClusterResult).value

    return AwaitableGetMariadbClusterResult(
        connections=pulumi.get(__ret__, 'connections'),
        cores=pulumi.get(__ret__, 'cores'),
        display_name=pulumi.get(__ret__, 'display_name'),
        dns_name=pulumi.get(__ret__, 'dns_name'),
        id=pulumi.get(__ret__, 'id'),
        instances=pulumi.get(__ret__, 'instances'),
        location=pulumi.get(__ret__, 'location'),
        maintenance_windows=pulumi.get(__ret__, 'maintenance_windows'),
        mariadb_version=pulumi.get(__ret__, 'mariadb_version'),
        ram=pulumi.get(__ret__, 'ram'),
        storage_size=pulumi.get(__ret__, 'storage_size'))


@_utilities.lift_output_func(get_mariadb_cluster)
def get_mariadb_cluster_output(display_name: Optional[pulumi.Input[Optional[str]]] = None,
                               id: Optional[pulumi.Input[Optional[str]]] = None,
                               location: Optional[pulumi.Input[Optional[str]]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMariadbClusterResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
