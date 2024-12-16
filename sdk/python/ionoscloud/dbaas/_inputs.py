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

__all__ = [
    'InMemoryDBReplicaSetConnectionsArgs',
    'InMemoryDBReplicaSetConnectionsArgsDict',
    'InMemoryDBReplicaSetCredentialsArgs',
    'InMemoryDBReplicaSetCredentialsArgsDict',
    'InMemoryDBReplicaSetCredentialsHashedPasswordArgs',
    'InMemoryDBReplicaSetCredentialsHashedPasswordArgsDict',
    'InMemoryDBReplicaSetMaintenanceWindowArgs',
    'InMemoryDBReplicaSetMaintenanceWindowArgsDict',
    'InMemoryDBReplicaSetResourcesArgs',
    'InMemoryDBReplicaSetResourcesArgsDict',
    'MariaDBClusterConnectionsArgs',
    'MariaDBClusterConnectionsArgsDict',
    'MariaDBClusterCredentialsArgs',
    'MariaDBClusterCredentialsArgsDict',
    'MariaDBClusterMaintenanceWindowArgs',
    'MariaDBClusterMaintenanceWindowArgsDict',
    'MongoClusterBackupArgs',
    'MongoClusterBackupArgsDict',
    'MongoClusterBiConnectorArgs',
    'MongoClusterBiConnectorArgsDict',
    'MongoClusterConnectionsArgs',
    'MongoClusterConnectionsArgsDict',
    'MongoClusterMaintenanceWindowArgs',
    'MongoClusterMaintenanceWindowArgsDict',
    'MongoUserRoleArgs',
    'MongoUserRoleArgsDict',
    'PSQLClusterConnectionPoolerArgs',
    'PSQLClusterConnectionPoolerArgsDict',
    'PSQLClusterConnectionsArgs',
    'PSQLClusterConnectionsArgsDict',
    'PSQLClusterCredentialsArgs',
    'PSQLClusterCredentialsArgsDict',
    'PSQLClusterFromBackupArgs',
    'PSQLClusterFromBackupArgsDict',
    'PSQLClusterMaintenanceWindowArgs',
    'PSQLClusterMaintenanceWindowArgsDict',
    'GetMongoUserRoleArgs',
    'GetMongoUserRoleArgsDict',
]

MYPY = False

if not MYPY:
    class InMemoryDBReplicaSetConnectionsArgsDict(TypedDict):
        cidr: pulumi.Input[str]
        """
        The IP and subnet for your instance. Note the following unavailable IP ranges: 10.233.64.0/18, 10.233.0.0/18, 10.233.114.0/24
        """
        datacenter_id: pulumi.Input[str]
        """
        The datacenter to connect your instance to.
        """
        lan_id: pulumi.Input[str]
        """
        The numeric LAN ID to connect your instance to.
        """
elif False:
    InMemoryDBReplicaSetConnectionsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class InMemoryDBReplicaSetConnectionsArgs:
    def __init__(__self__, *,
                 cidr: pulumi.Input[str],
                 datacenter_id: pulumi.Input[str],
                 lan_id: pulumi.Input[str]):
        """
        :param pulumi.Input[str] cidr: The IP and subnet for your instance. Note the following unavailable IP ranges: 10.233.64.0/18, 10.233.0.0/18, 10.233.114.0/24
        :param pulumi.Input[str] datacenter_id: The datacenter to connect your instance to.
        :param pulumi.Input[str] lan_id: The numeric LAN ID to connect your instance to.
        """
        pulumi.set(__self__, "cidr", cidr)
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        pulumi.set(__self__, "lan_id", lan_id)

    @property
    @pulumi.getter
    def cidr(self) -> pulumi.Input[str]:
        """
        The IP and subnet for your instance. Note the following unavailable IP ranges: 10.233.64.0/18, 10.233.0.0/18, 10.233.114.0/24
        """
        return pulumi.get(self, "cidr")

    @cidr.setter
    def cidr(self, value: pulumi.Input[str]):
        pulumi.set(self, "cidr", value)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> pulumi.Input[str]:
        """
        The datacenter to connect your instance to.
        """
        return pulumi.get(self, "datacenter_id")

    @datacenter_id.setter
    def datacenter_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "datacenter_id", value)

    @property
    @pulumi.getter(name="lanId")
    def lan_id(self) -> pulumi.Input[str]:
        """
        The numeric LAN ID to connect your instance to.
        """
        return pulumi.get(self, "lan_id")

    @lan_id.setter
    def lan_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "lan_id", value)


if not MYPY:
    class InMemoryDBReplicaSetCredentialsArgsDict(TypedDict):
        username: pulumi.Input[str]
        """
        The username for the initial InMemoryDB user. Some system usernames are restricted (e.g. 'admin', 'standby').
        """
        hashed_password: NotRequired[pulumi.Input['InMemoryDBReplicaSetCredentialsHashedPasswordArgsDict']]
        """
        The hashed password for a InMemoryDB user.
        """
        plain_text_password: NotRequired[pulumi.Input[str]]
        """
        The password for a InMemoryDB user.
        """
elif False:
    InMemoryDBReplicaSetCredentialsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class InMemoryDBReplicaSetCredentialsArgs:
    def __init__(__self__, *,
                 username: pulumi.Input[str],
                 hashed_password: Optional[pulumi.Input['InMemoryDBReplicaSetCredentialsHashedPasswordArgs']] = None,
                 plain_text_password: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] username: The username for the initial InMemoryDB user. Some system usernames are restricted (e.g. 'admin', 'standby').
        :param pulumi.Input['InMemoryDBReplicaSetCredentialsHashedPasswordArgs'] hashed_password: The hashed password for a InMemoryDB user.
        :param pulumi.Input[str] plain_text_password: The password for a InMemoryDB user.
        """
        pulumi.set(__self__, "username", username)
        if hashed_password is not None:
            pulumi.set(__self__, "hashed_password", hashed_password)
        if plain_text_password is not None:
            pulumi.set(__self__, "plain_text_password", plain_text_password)

    @property
    @pulumi.getter
    def username(self) -> pulumi.Input[str]:
        """
        The username for the initial InMemoryDB user. Some system usernames are restricted (e.g. 'admin', 'standby').
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: pulumi.Input[str]):
        pulumi.set(self, "username", value)

    @property
    @pulumi.getter(name="hashedPassword")
    def hashed_password(self) -> Optional[pulumi.Input['InMemoryDBReplicaSetCredentialsHashedPasswordArgs']]:
        """
        The hashed password for a InMemoryDB user.
        """
        return pulumi.get(self, "hashed_password")

    @hashed_password.setter
    def hashed_password(self, value: Optional[pulumi.Input['InMemoryDBReplicaSetCredentialsHashedPasswordArgs']]):
        pulumi.set(self, "hashed_password", value)

    @property
    @pulumi.getter(name="plainTextPassword")
    def plain_text_password(self) -> Optional[pulumi.Input[str]]:
        """
        The password for a InMemoryDB user.
        """
        return pulumi.get(self, "plain_text_password")

    @plain_text_password.setter
    def plain_text_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "plain_text_password", value)


if not MYPY:
    class InMemoryDBReplicaSetCredentialsHashedPasswordArgsDict(TypedDict):
        algorithm: pulumi.Input[str]
        hash: pulumi.Input[str]
elif False:
    InMemoryDBReplicaSetCredentialsHashedPasswordArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class InMemoryDBReplicaSetCredentialsHashedPasswordArgs:
    def __init__(__self__, *,
                 algorithm: pulumi.Input[str],
                 hash: pulumi.Input[str]):
        pulumi.set(__self__, "algorithm", algorithm)
        pulumi.set(__self__, "hash", hash)

    @property
    @pulumi.getter
    def algorithm(self) -> pulumi.Input[str]:
        return pulumi.get(self, "algorithm")

    @algorithm.setter
    def algorithm(self, value: pulumi.Input[str]):
        pulumi.set(self, "algorithm", value)

    @property
    @pulumi.getter
    def hash(self) -> pulumi.Input[str]:
        return pulumi.get(self, "hash")

    @hash.setter
    def hash(self, value: pulumi.Input[str]):
        pulumi.set(self, "hash", value)


if not MYPY:
    class InMemoryDBReplicaSetMaintenanceWindowArgsDict(TypedDict):
        day_of_the_week: pulumi.Input[str]
        """
        The name of the week day.
        """
        time: pulumi.Input[str]
        """
        Start of the maintenance window in UTC time.
        """
elif False:
    InMemoryDBReplicaSetMaintenanceWindowArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class InMemoryDBReplicaSetMaintenanceWindowArgs:
    def __init__(__self__, *,
                 day_of_the_week: pulumi.Input[str],
                 time: pulumi.Input[str]):
        """
        :param pulumi.Input[str] day_of_the_week: The name of the week day.
        :param pulumi.Input[str] time: Start of the maintenance window in UTC time.
        """
        pulumi.set(__self__, "day_of_the_week", day_of_the_week)
        pulumi.set(__self__, "time", time)

    @property
    @pulumi.getter(name="dayOfTheWeek")
    def day_of_the_week(self) -> pulumi.Input[str]:
        """
        The name of the week day.
        """
        return pulumi.get(self, "day_of_the_week")

    @day_of_the_week.setter
    def day_of_the_week(self, value: pulumi.Input[str]):
        pulumi.set(self, "day_of_the_week", value)

    @property
    @pulumi.getter
    def time(self) -> pulumi.Input[str]:
        """
        Start of the maintenance window in UTC time.
        """
        return pulumi.get(self, "time")

    @time.setter
    def time(self, value: pulumi.Input[str]):
        pulumi.set(self, "time", value)


if not MYPY:
    class InMemoryDBReplicaSetResourcesArgsDict(TypedDict):
        cores: pulumi.Input[int]
        """
        The number of CPU cores per instance.
        """
        ram: pulumi.Input[int]
        """
        The amount of memory per instance in gigabytes (GB).
        """
        storage: NotRequired[pulumi.Input[int]]
        """
        The size of the storage in GB. The size is derived from the amount of RAM and the persistence mode and is not configurable.
        """
elif False:
    InMemoryDBReplicaSetResourcesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class InMemoryDBReplicaSetResourcesArgs:
    def __init__(__self__, *,
                 cores: pulumi.Input[int],
                 ram: pulumi.Input[int],
                 storage: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[int] cores: The number of CPU cores per instance.
        :param pulumi.Input[int] ram: The amount of memory per instance in gigabytes (GB).
        :param pulumi.Input[int] storage: The size of the storage in GB. The size is derived from the amount of RAM and the persistence mode and is not configurable.
        """
        pulumi.set(__self__, "cores", cores)
        pulumi.set(__self__, "ram", ram)
        if storage is not None:
            pulumi.set(__self__, "storage", storage)

    @property
    @pulumi.getter
    def cores(self) -> pulumi.Input[int]:
        """
        The number of CPU cores per instance.
        """
        return pulumi.get(self, "cores")

    @cores.setter
    def cores(self, value: pulumi.Input[int]):
        pulumi.set(self, "cores", value)

    @property
    @pulumi.getter
    def ram(self) -> pulumi.Input[int]:
        """
        The amount of memory per instance in gigabytes (GB).
        """
        return pulumi.get(self, "ram")

    @ram.setter
    def ram(self, value: pulumi.Input[int]):
        pulumi.set(self, "ram", value)

    @property
    @pulumi.getter
    def storage(self) -> Optional[pulumi.Input[int]]:
        """
        The size of the storage in GB. The size is derived from the amount of RAM and the persistence mode and is not configurable.
        """
        return pulumi.get(self, "storage")

    @storage.setter
    def storage(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "storage", value)


if not MYPY:
    class MariaDBClusterConnectionsArgsDict(TypedDict):
        cidr: pulumi.Input[str]
        """
        The IP and subnet for your cluster.
        """
        datacenter_id: pulumi.Input[str]
        """
        The datacenter to connect your cluster to.
        """
        lan_id: pulumi.Input[str]
        """
        The numeric LAN ID to connect your cluster to.
        """
elif False:
    MariaDBClusterConnectionsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class MariaDBClusterConnectionsArgs:
    def __init__(__self__, *,
                 cidr: pulumi.Input[str],
                 datacenter_id: pulumi.Input[str],
                 lan_id: pulumi.Input[str]):
        """
        :param pulumi.Input[str] cidr: The IP and subnet for your cluster.
        :param pulumi.Input[str] datacenter_id: The datacenter to connect your cluster to.
        :param pulumi.Input[str] lan_id: The numeric LAN ID to connect your cluster to.
        """
        pulumi.set(__self__, "cidr", cidr)
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        pulumi.set(__self__, "lan_id", lan_id)

    @property
    @pulumi.getter
    def cidr(self) -> pulumi.Input[str]:
        """
        The IP and subnet for your cluster.
        """
        return pulumi.get(self, "cidr")

    @cidr.setter
    def cidr(self, value: pulumi.Input[str]):
        pulumi.set(self, "cidr", value)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> pulumi.Input[str]:
        """
        The datacenter to connect your cluster to.
        """
        return pulumi.get(self, "datacenter_id")

    @datacenter_id.setter
    def datacenter_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "datacenter_id", value)

    @property
    @pulumi.getter(name="lanId")
    def lan_id(self) -> pulumi.Input[str]:
        """
        The numeric LAN ID to connect your cluster to.
        """
        return pulumi.get(self, "lan_id")

    @lan_id.setter
    def lan_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "lan_id", value)


if not MYPY:
    class MariaDBClusterCredentialsArgsDict(TypedDict):
        password: pulumi.Input[str]
        """
        The password for a MariaDB user.
        """
        username: pulumi.Input[str]
        """
        The username for the initial MariaDB user. Some system usernames are restricted (e.g 'mariadb', 'admin', 'standby').
        """
elif False:
    MariaDBClusterCredentialsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class MariaDBClusterCredentialsArgs:
    def __init__(__self__, *,
                 password: pulumi.Input[str],
                 username: pulumi.Input[str]):
        """
        :param pulumi.Input[str] password: The password for a MariaDB user.
        :param pulumi.Input[str] username: The username for the initial MariaDB user. Some system usernames are restricted (e.g 'mariadb', 'admin', 'standby').
        """
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        """
        The password for a MariaDB user.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def username(self) -> pulumi.Input[str]:
        """
        The username for the initial MariaDB user. Some system usernames are restricted (e.g 'mariadb', 'admin', 'standby').
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: pulumi.Input[str]):
        pulumi.set(self, "username", value)


if not MYPY:
    class MariaDBClusterMaintenanceWindowArgsDict(TypedDict):
        day_of_the_week: pulumi.Input[str]
        """
        The name of the week day.
        """
        time: pulumi.Input[str]
        """
        Start of the maintenance window in UTC time.
        """
elif False:
    MariaDBClusterMaintenanceWindowArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class MariaDBClusterMaintenanceWindowArgs:
    def __init__(__self__, *,
                 day_of_the_week: pulumi.Input[str],
                 time: pulumi.Input[str]):
        """
        :param pulumi.Input[str] day_of_the_week: The name of the week day.
        :param pulumi.Input[str] time: Start of the maintenance window in UTC time.
        """
        pulumi.set(__self__, "day_of_the_week", day_of_the_week)
        pulumi.set(__self__, "time", time)

    @property
    @pulumi.getter(name="dayOfTheWeek")
    def day_of_the_week(self) -> pulumi.Input[str]:
        """
        The name of the week day.
        """
        return pulumi.get(self, "day_of_the_week")

    @day_of_the_week.setter
    def day_of_the_week(self, value: pulumi.Input[str]):
        pulumi.set(self, "day_of_the_week", value)

    @property
    @pulumi.getter
    def time(self) -> pulumi.Input[str]:
        """
        Start of the maintenance window in UTC time.
        """
        return pulumi.get(self, "time")

    @time.setter
    def time(self, value: pulumi.Input[str]):
        pulumi.set(self, "time", value)


if not MYPY:
    class MongoClusterBackupArgsDict(TypedDict):
        location: NotRequired[pulumi.Input[str]]
        """
        The location where the cluster backups will be stored. If not set, the backup is stored in the nearest location of the cluster. Examples: de, eu-sounth-2, eu-central-2
        """
        point_in_time_window_hours: NotRequired[pulumi.Input[int]]
        """
        Number of hours in the past for which a point-in-time snapshot can be created.
        """
        snapshot_interval_hours: NotRequired[pulumi.Input[int]]
        """
        Number of hours between snapshots.
        """
elif False:
    MongoClusterBackupArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class MongoClusterBackupArgs:
    def __init__(__self__, *,
                 location: Optional[pulumi.Input[str]] = None,
                 point_in_time_window_hours: Optional[pulumi.Input[int]] = None,
                 snapshot_interval_hours: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[str] location: The location where the cluster backups will be stored. If not set, the backup is stored in the nearest location of the cluster. Examples: de, eu-sounth-2, eu-central-2
        :param pulumi.Input[int] point_in_time_window_hours: Number of hours in the past for which a point-in-time snapshot can be created.
        :param pulumi.Input[int] snapshot_interval_hours: Number of hours between snapshots.
        """
        if location is not None:
            pulumi.set(__self__, "location", location)
        if point_in_time_window_hours is not None:
            pulumi.set(__self__, "point_in_time_window_hours", point_in_time_window_hours)
        if snapshot_interval_hours is not None:
            pulumi.set(__self__, "snapshot_interval_hours", snapshot_interval_hours)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location where the cluster backups will be stored. If not set, the backup is stored in the nearest location of the cluster. Examples: de, eu-sounth-2, eu-central-2
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="pointInTimeWindowHours")
    def point_in_time_window_hours(self) -> Optional[pulumi.Input[int]]:
        """
        Number of hours in the past for which a point-in-time snapshot can be created.
        """
        return pulumi.get(self, "point_in_time_window_hours")

    @point_in_time_window_hours.setter
    def point_in_time_window_hours(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "point_in_time_window_hours", value)

    @property
    @pulumi.getter(name="snapshotIntervalHours")
    def snapshot_interval_hours(self) -> Optional[pulumi.Input[int]]:
        """
        Number of hours between snapshots.
        """
        return pulumi.get(self, "snapshot_interval_hours")

    @snapshot_interval_hours.setter
    def snapshot_interval_hours(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "snapshot_interval_hours", value)


if not MYPY:
    class MongoClusterBiConnectorArgsDict(TypedDict):
        enabled: NotRequired[pulumi.Input[bool]]
        """
        Enable or disable the BiConnector.
        """
        host: NotRequired[pulumi.Input[str]]
        """
        The host where this new BI Connector is installed.
        """
        port: NotRequired[pulumi.Input[str]]
        """
        Port number used when connecting to this new BI Connector.
        """
elif False:
    MongoClusterBiConnectorArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class MongoClusterBiConnectorArgs:
    def __init__(__self__, *,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[bool] enabled: Enable or disable the BiConnector.
        :param pulumi.Input[str] host: The host where this new BI Connector is installed.
        :param pulumi.Input[str] port: Port number used when connecting to this new BI Connector.
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if host is not None:
            pulumi.set(__self__, "host", host)
        if port is not None:
            pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable or disable the BiConnector.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[str]]:
        """
        The host where this new BI Connector is installed.
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[str]]:
        """
        Port number used when connecting to this new BI Connector.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "port", value)


if not MYPY:
    class MongoClusterConnectionsArgsDict(TypedDict):
        cidr_lists: pulumi.Input[Sequence[pulumi.Input[str]]]
        """
        The list of IPs and subnet for your cluster. Note the following unavailable IP ranges:10.233.64.0/18, 10.233.0.0/18, 10.233.114.0/24. example: [192.168.1.100/24, 192.168.1.101/24]
        """
        datacenter_id: pulumi.Input[str]
        """
        The datacenter to connect your cluster to.
        """
        lan_id: pulumi.Input[str]
        """
        The LAN to connect your cluster to.
        """
elif False:
    MongoClusterConnectionsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class MongoClusterConnectionsArgs:
    def __init__(__self__, *,
                 cidr_lists: pulumi.Input[Sequence[pulumi.Input[str]]],
                 datacenter_id: pulumi.Input[str],
                 lan_id: pulumi.Input[str]):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] cidr_lists: The list of IPs and subnet for your cluster. Note the following unavailable IP ranges:10.233.64.0/18, 10.233.0.0/18, 10.233.114.0/24. example: [192.168.1.100/24, 192.168.1.101/24]
        :param pulumi.Input[str] datacenter_id: The datacenter to connect your cluster to.
        :param pulumi.Input[str] lan_id: The LAN to connect your cluster to.
        """
        pulumi.set(__self__, "cidr_lists", cidr_lists)
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        pulumi.set(__self__, "lan_id", lan_id)

    @property
    @pulumi.getter(name="cidrLists")
    def cidr_lists(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The list of IPs and subnet for your cluster. Note the following unavailable IP ranges:10.233.64.0/18, 10.233.0.0/18, 10.233.114.0/24. example: [192.168.1.100/24, 192.168.1.101/24]
        """
        return pulumi.get(self, "cidr_lists")

    @cidr_lists.setter
    def cidr_lists(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "cidr_lists", value)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> pulumi.Input[str]:
        """
        The datacenter to connect your cluster to.
        """
        return pulumi.get(self, "datacenter_id")

    @datacenter_id.setter
    def datacenter_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "datacenter_id", value)

    @property
    @pulumi.getter(name="lanId")
    def lan_id(self) -> pulumi.Input[str]:
        """
        The LAN to connect your cluster to.
        """
        return pulumi.get(self, "lan_id")

    @lan_id.setter
    def lan_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "lan_id", value)


if not MYPY:
    class MongoClusterMaintenanceWindowArgsDict(TypedDict):
        day_of_the_week: pulumi.Input[str]
        time: pulumi.Input[str]
elif False:
    MongoClusterMaintenanceWindowArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class MongoClusterMaintenanceWindowArgs:
    def __init__(__self__, *,
                 day_of_the_week: pulumi.Input[str],
                 time: pulumi.Input[str]):
        pulumi.set(__self__, "day_of_the_week", day_of_the_week)
        pulumi.set(__self__, "time", time)

    @property
    @pulumi.getter(name="dayOfTheWeek")
    def day_of_the_week(self) -> pulumi.Input[str]:
        return pulumi.get(self, "day_of_the_week")

    @day_of_the_week.setter
    def day_of_the_week(self, value: pulumi.Input[str]):
        pulumi.set(self, "day_of_the_week", value)

    @property
    @pulumi.getter
    def time(self) -> pulumi.Input[str]:
        return pulumi.get(self, "time")

    @time.setter
    def time(self, value: pulumi.Input[str]):
        pulumi.set(self, "time", value)


if not MYPY:
    class MongoUserRoleArgsDict(TypedDict):
        database: NotRequired[pulumi.Input[str]]
        role: NotRequired[pulumi.Input[str]]
        """
        A list of mongodb user roles. Examples: read, readWrite, readAnyDatabase
        """
elif False:
    MongoUserRoleArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class MongoUserRoleArgs:
    def __init__(__self__, *,
                 database: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] role: A list of mongodb user roles. Examples: read, readWrite, readAnyDatabase
        """
        if database is not None:
            pulumi.set(__self__, "database", database)
        if role is not None:
            pulumi.set(__self__, "role", role)

    @property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        A list of mongodb user roles. Examples: read, readWrite, readAnyDatabase
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)


if not MYPY:
    class PSQLClusterConnectionPoolerArgsDict(TypedDict):
        enabled: pulumi.Input[bool]
        pool_mode: pulumi.Input[str]
        """
        Represents different modes of connection pooling for the connection pooler
        """
elif False:
    PSQLClusterConnectionPoolerArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PSQLClusterConnectionPoolerArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 pool_mode: pulumi.Input[str]):
        """
        :param pulumi.Input[str] pool_mode: Represents different modes of connection pooling for the connection pooler
        """
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "pool_mode", pool_mode)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="poolMode")
    def pool_mode(self) -> pulumi.Input[str]:
        """
        Represents different modes of connection pooling for the connection pooler
        """
        return pulumi.get(self, "pool_mode")

    @pool_mode.setter
    def pool_mode(self, value: pulumi.Input[str]):
        pulumi.set(self, "pool_mode", value)


if not MYPY:
    class PSQLClusterConnectionsArgsDict(TypedDict):
        cidr: pulumi.Input[str]
        """
        The IP and subnet for the database.
                  Note the following unavailable IP ranges:
                  10.233.64.0/18
                  10.233.0.0/18
                  10.233.114.0/24
        """
        datacenter_id: pulumi.Input[str]
        """
        The datacenter to connect your cluster to.
        """
        lan_id: pulumi.Input[str]
        """
        The LAN to connect your cluster to.
        """
elif False:
    PSQLClusterConnectionsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PSQLClusterConnectionsArgs:
    def __init__(__self__, *,
                 cidr: pulumi.Input[str],
                 datacenter_id: pulumi.Input[str],
                 lan_id: pulumi.Input[str]):
        """
        :param pulumi.Input[str] cidr: The IP and subnet for the database.
                         Note the following unavailable IP ranges:
                         10.233.64.0/18
                         10.233.0.0/18
                         10.233.114.0/24
        :param pulumi.Input[str] datacenter_id: The datacenter to connect your cluster to.
        :param pulumi.Input[str] lan_id: The LAN to connect your cluster to.
        """
        pulumi.set(__self__, "cidr", cidr)
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        pulumi.set(__self__, "lan_id", lan_id)

    @property
    @pulumi.getter
    def cidr(self) -> pulumi.Input[str]:
        """
        The IP and subnet for the database.
                  Note the following unavailable IP ranges:
                  10.233.64.0/18
                  10.233.0.0/18
                  10.233.114.0/24
        """
        return pulumi.get(self, "cidr")

    @cidr.setter
    def cidr(self, value: pulumi.Input[str]):
        pulumi.set(self, "cidr", value)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> pulumi.Input[str]:
        """
        The datacenter to connect your cluster to.
        """
        return pulumi.get(self, "datacenter_id")

    @datacenter_id.setter
    def datacenter_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "datacenter_id", value)

    @property
    @pulumi.getter(name="lanId")
    def lan_id(self) -> pulumi.Input[str]:
        """
        The LAN to connect your cluster to.
        """
        return pulumi.get(self, "lan_id")

    @lan_id.setter
    def lan_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "lan_id", value)


if not MYPY:
    class PSQLClusterCredentialsArgsDict(TypedDict):
        password: pulumi.Input[str]
        username: pulumi.Input[str]
        """
        the username for the initial postgres user. some system usernames are restricted (e.g. "postgres", "admin", "standby")
        """
elif False:
    PSQLClusterCredentialsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PSQLClusterCredentialsArgs:
    def __init__(__self__, *,
                 password: pulumi.Input[str],
                 username: pulumi.Input[str]):
        """
        :param pulumi.Input[str] username: the username for the initial postgres user. some system usernames are restricted (e.g. "postgres", "admin", "standby")
        """
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "username", username)

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
        """
        the username for the initial postgres user. some system usernames are restricted (e.g. "postgres", "admin", "standby")
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: pulumi.Input[str]):
        pulumi.set(self, "username", value)


if not MYPY:
    class PSQLClusterFromBackupArgsDict(TypedDict):
        backup_id: pulumi.Input[str]
        """
        The unique ID of the backup you want to restore.
        """
        recovery_target_time: NotRequired[pulumi.Input[str]]
        """
        If this value is supplied as ISO 8601 timestamp, the backup will be replayed up until the given timestamp. If empty, the backup will be applied completely.
        """
elif False:
    PSQLClusterFromBackupArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PSQLClusterFromBackupArgs:
    def __init__(__self__, *,
                 backup_id: pulumi.Input[str],
                 recovery_target_time: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] backup_id: The unique ID of the backup you want to restore.
        :param pulumi.Input[str] recovery_target_time: If this value is supplied as ISO 8601 timestamp, the backup will be replayed up until the given timestamp. If empty, the backup will be applied completely.
        """
        pulumi.set(__self__, "backup_id", backup_id)
        if recovery_target_time is not None:
            pulumi.set(__self__, "recovery_target_time", recovery_target_time)

    @property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> pulumi.Input[str]:
        """
        The unique ID of the backup you want to restore.
        """
        return pulumi.get(self, "backup_id")

    @backup_id.setter
    def backup_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "backup_id", value)

    @property
    @pulumi.getter(name="recoveryTargetTime")
    def recovery_target_time(self) -> Optional[pulumi.Input[str]]:
        """
        If this value is supplied as ISO 8601 timestamp, the backup will be replayed up until the given timestamp. If empty, the backup will be applied completely.
        """
        return pulumi.get(self, "recovery_target_time")

    @recovery_target_time.setter
    def recovery_target_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "recovery_target_time", value)


if not MYPY:
    class PSQLClusterMaintenanceWindowArgsDict(TypedDict):
        day_of_the_week: pulumi.Input[str]
        time: pulumi.Input[str]
elif False:
    PSQLClusterMaintenanceWindowArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PSQLClusterMaintenanceWindowArgs:
    def __init__(__self__, *,
                 day_of_the_week: pulumi.Input[str],
                 time: pulumi.Input[str]):
        pulumi.set(__self__, "day_of_the_week", day_of_the_week)
        pulumi.set(__self__, "time", time)

    @property
    @pulumi.getter(name="dayOfTheWeek")
    def day_of_the_week(self) -> pulumi.Input[str]:
        return pulumi.get(self, "day_of_the_week")

    @day_of_the_week.setter
    def day_of_the_week(self, value: pulumi.Input[str]):
        pulumi.set(self, "day_of_the_week", value)

    @property
    @pulumi.getter
    def time(self) -> pulumi.Input[str]:
        return pulumi.get(self, "time")

    @time.setter
    def time(self, value: pulumi.Input[str]):
        pulumi.set(self, "time", value)


if not MYPY:
    class GetMongoUserRoleArgsDict(TypedDict):
        database: str
        role: str
        """
        A list of mongodb user roles. Examples: read, readWrite, readAnyDatabase
        """
elif False:
    GetMongoUserRoleArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class GetMongoUserRoleArgs:
    def __init__(__self__, *,
                 database: str,
                 role: str):
        """
        :param str role: A list of mongodb user roles. Examples: read, readWrite, readAnyDatabase
        """
        pulumi.set(__self__, "database", database)
        pulumi.set(__self__, "role", role)

    @property
    @pulumi.getter
    def database(self) -> str:
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: str):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter
    def role(self) -> str:
        """
        A list of mongodb user roles. Examples: read, readWrite, readAnyDatabase
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: str):
        pulumi.set(self, "role", value)


