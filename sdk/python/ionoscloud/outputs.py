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
    'GetMariadbBackupsBackupResult',
    'GetMariadbBackupsBackupBaseBackupResult',
]

@pulumi.output_type
class GetMariadbBackupsBackupResult(dict):
    def __init__(__self__, *,
                 base_backups: Sequence['outputs.GetMariadbBackupsBackupBaseBackupResult'],
                 cluster_id: str,
                 earliest_recovery_target_time: str,
                 size: int):
        """
        :param Sequence['GetMariadbBackupsBackupBaseBackupArgs'] base_backups: The list of backups for the specified cluster
        :param str cluster_id: [string] The unique ID of the cluster.
        :param str earliest_recovery_target_time: The oldest available timestamp to which you can restore.
        :param int size: The size of the backup in Mebibytes (MiB). This is the size of the binary backup file that was stored
        """
        pulumi.set(__self__, "base_backups", base_backups)
        pulumi.set(__self__, "cluster_id", cluster_id)
        pulumi.set(__self__, "earliest_recovery_target_time", earliest_recovery_target_time)
        pulumi.set(__self__, "size", size)

    @property
    @pulumi.getter(name="baseBackups")
    def base_backups(self) -> Sequence['outputs.GetMariadbBackupsBackupBaseBackupResult']:
        """
        The list of backups for the specified cluster
        """
        return pulumi.get(self, "base_backups")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        """
        [string] The unique ID of the cluster.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="earliestRecoveryTargetTime")
    def earliest_recovery_target_time(self) -> str:
        """
        The oldest available timestamp to which you can restore.
        """
        return pulumi.get(self, "earliest_recovery_target_time")

    @property
    @pulumi.getter
    def size(self) -> int:
        """
        The size of the backup in Mebibytes (MiB). This is the size of the binary backup file that was stored
        """
        return pulumi.get(self, "size")


@pulumi.output_type
class GetMariadbBackupsBackupBaseBackupResult(dict):
    def __init__(__self__, *,
                 created: str,
                 size: int):
        """
        :param str created: The ISO 8601 creation timestamp
        :param int size: The size of the backup in Mebibytes (MiB). This is the size of the binary backup file that was stored
        """
        pulumi.set(__self__, "created", created)
        pulumi.set(__self__, "size", size)

    @property
    @pulumi.getter
    def created(self) -> str:
        """
        The ISO 8601 creation timestamp
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter
    def size(self) -> int:
        """
        The size of the backup in Mebibytes (MiB). This is the size of the binary backup file that was stored
        """
        return pulumi.get(self, "size")


