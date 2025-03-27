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

__all__ = [
    'ObjectStorageAccesskeyTimeouts',
    'GetObjectStorageRegionCapabilityResult',
]

@pulumi.output_type
class ObjectStorageAccesskeyTimeouts(dict):
    def __init__(__self__, *,
                 create: Optional[str] = None,
                 delete: Optional[str] = None,
                 read: Optional[str] = None):
        """
        :param str create: [string] Time to wait for the bucket to be created. Default is `10m`.
        :param str delete: [string] Time to wait for the bucket to be deleted. Default is `10m`.
        :param str read: A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Read operations occur during any refresh or planning operation when refresh is enabled.
        """
        if create is not None:
            pulumi.set(__self__, "create", create)
        if delete is not None:
            pulumi.set(__self__, "delete", delete)
        if read is not None:
            pulumi.set(__self__, "read", read)

    @property
    @pulumi.getter
    def create(self) -> Optional[str]:
        """
        [string] Time to wait for the bucket to be created. Default is `10m`.
        """
        return pulumi.get(self, "create")

    @property
    @pulumi.getter
    def delete(self) -> Optional[str]:
        """
        [string] Time to wait for the bucket to be deleted. Default is `10m`.
        """
        return pulumi.get(self, "delete")

    @property
    @pulumi.getter
    def read(self) -> Optional[str]:
        """
        A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Read operations occur during any refresh or planning operation when refresh is enabled.
        """
        return pulumi.get(self, "read")


@pulumi.output_type
class GetObjectStorageRegionCapabilityResult(dict):
    def __init__(__self__, *,
                 iam: bool,
                 s3select: bool):
        """
        :param bool iam: Indicates if IAM policy based access is supported
        :param bool s3select: Indicates if S3 Select is supported
        """
        pulumi.set(__self__, "iam", iam)
        pulumi.set(__self__, "s3select", s3select)

    @property
    @pulumi.getter
    def iam(self) -> bool:
        """
        Indicates if IAM policy based access is supported
        """
        return pulumi.get(self, "iam")

    @property
    @pulumi.getter
    def s3select(self) -> bool:
        """
        Indicates if S3 Select is supported
        """
        return pulumi.get(self, "s3select")


