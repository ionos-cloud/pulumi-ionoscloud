# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'RegistryFeatures',
    'RegistryGarbageCollectionSchedule',
    'RegistryStorageUsage',
    'RegistryTokenCredential',
    'RegistryTokenScope',
]

@pulumi.output_type
class RegistryFeatures(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "vulnerabilityScanning":
            suggest = "vulnerability_scanning"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RegistryFeatures. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RegistryFeatures.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RegistryFeatures.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 vulnerability_scanning: Optional[bool] = None):
        """
        :param bool vulnerability_scanning: [bool] Enables or disables the Vulnerability Scanning feature for the Container Registry. To disable this feature, set the attribute to false when creating the CR resource.
               
               > **⚠ WARNING** `Container Registry Vulnerability Scanning` is a paid feature which is enabled by default, and cannot be turned off after activation. To disable this feature for a Container Registry, ensure `vulnerability_scanning` is set to false on resource creation.
        """
        if vulnerability_scanning is not None:
            pulumi.set(__self__, "vulnerability_scanning", vulnerability_scanning)

    @property
    @pulumi.getter(name="vulnerabilityScanning")
    def vulnerability_scanning(self) -> Optional[bool]:
        """
        [bool] Enables or disables the Vulnerability Scanning feature for the Container Registry. To disable this feature, set the attribute to false when creating the CR resource.

        > **⚠ WARNING** `Container Registry Vulnerability Scanning` is a paid feature which is enabled by default, and cannot be turned off after activation. To disable this feature for a Container Registry, ensure `vulnerability_scanning` is set to false on resource creation.
        """
        return pulumi.get(self, "vulnerability_scanning")


@pulumi.output_type
class RegistryGarbageCollectionSchedule(dict):
    def __init__(__self__, *,
                 days: Sequence[str],
                 time: str):
        """
        :param Sequence[str] days: [list] Elements of list must have one of the values: `Saturday`, `Sunday`, `Monday`, `Tuesday`,  `Wednesday`,  `Thursday`,  `Friday`
        :param str time: [string]
        """
        pulumi.set(__self__, "days", days)
        pulumi.set(__self__, "time", time)

    @property
    @pulumi.getter
    def days(self) -> Sequence[str]:
        """
        [list] Elements of list must have one of the values: `Saturday`, `Sunday`, `Monday`, `Tuesday`,  `Wednesday`,  `Thursday`,  `Friday`
        """
        return pulumi.get(self, "days")

    @property
    @pulumi.getter
    def time(self) -> str:
        """
        [string]
        """
        return pulumi.get(self, "time")


@pulumi.output_type
class RegistryStorageUsage(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "updatedAt":
            suggest = "updated_at"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RegistryStorageUsage. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RegistryStorageUsage.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RegistryStorageUsage.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 bytes: Optional[int] = None,
                 updated_at: Optional[str] = None):
        if bytes is not None:
            pulumi.set(__self__, "bytes", bytes)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter
    def bytes(self) -> Optional[int]:
        return pulumi.get(self, "bytes")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[str]:
        return pulumi.get(self, "updated_at")


@pulumi.output_type
class RegistryTokenCredential(dict):
    def __init__(__self__, *,
                 password: str,
                 username: str):
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def password(self) -> str:
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def username(self) -> str:
        return pulumi.get(self, "username")


@pulumi.output_type
class RegistryTokenScope(dict):
    def __init__(__self__, *,
                 actions: Sequence[str],
                 name: str,
                 type: str):
        """
        :param Sequence[str] actions: [string] Example: ["pull", "push", "delete"]
        :param str name: [string]
        :param str type: [string]
        """
        pulumi.set(__self__, "actions", actions)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def actions(self) -> Sequence[str]:
        """
        [string] Example: ["pull", "push", "delete"]
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        [string]
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        [string]
        """
        return pulumi.get(self, "type")


