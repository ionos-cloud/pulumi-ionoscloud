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
    'PipelineLog',
    'PipelineLogDestination',
    'GetPipelineLogResult',
    'GetPipelineLogDestinationResult',
]

@pulumi.output_type
class PipelineLog(dict):
    def __init__(__self__, *,
                 protocol: str,
                 source: str,
                 tag: str,
                 destinations: Optional[Sequence['outputs.PipelineLogDestination']] = None,
                 public: Optional[bool] = None):
        """
        :param str protocol: [string] "Protocol to use as intake. Possible values are: http, tcp."
        :param str source: [string] The source parser to be used.
        :param str tag: [string] The tag is used to distinguish different pipelines. Must be unique amongst the pipeline's array items.
        :param Sequence['PipelineLogDestinationArgs'] destinations: [list] The configuration of the logs datastore, a list that contains elements with the following structure:
        :param bool public: [bool]
        """
        pulumi.set(__self__, "protocol", protocol)
        pulumi.set(__self__, "source", source)
        pulumi.set(__self__, "tag", tag)
        if destinations is not None:
            pulumi.set(__self__, "destinations", destinations)
        if public is not None:
            pulumi.set(__self__, "public", public)

    @property
    @pulumi.getter
    def protocol(self) -> str:
        """
        [string] "Protocol to use as intake. Possible values are: http, tcp."
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter
    def source(self) -> str:
        """
        [string] The source parser to be used.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def tag(self) -> str:
        """
        [string] The tag is used to distinguish different pipelines. Must be unique amongst the pipeline's array items.
        """
        return pulumi.get(self, "tag")

    @property
    @pulumi.getter
    def destinations(self) -> Optional[Sequence['outputs.PipelineLogDestination']]:
        """
        [list] The configuration of the logs datastore, a list that contains elements with the following structure:
        """
        return pulumi.get(self, "destinations")

    @property
    @pulumi.getter
    def public(self) -> Optional[bool]:
        """
        [bool]
        """
        return pulumi.get(self, "public")


@pulumi.output_type
class PipelineLogDestination(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "retentionInDays":
            suggest = "retention_in_days"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PipelineLogDestination. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PipelineLogDestination.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PipelineLogDestination.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 retention_in_days: Optional[int] = None,
                 type: Optional[str] = None):
        """
        :param int retention_in_days: [int] Defines the number of days a log record should be kept in loki. Works with loki destination type only. Can be one of: 7, 14, 30.
        :param str type: [string] The internal output stream to send logs to.
        """
        if retention_in_days is not None:
            pulumi.set(__self__, "retention_in_days", retention_in_days)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> Optional[int]:
        """
        [int] Defines the number of days a log record should be kept in loki. Works with loki destination type only. Can be one of: 7, 14, 30.
        """
        return pulumi.get(self, "retention_in_days")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        [string] The internal output stream to send logs to.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class GetPipelineLogResult(dict):
    def __init__(__self__, *,
                 destinations: Sequence['outputs.GetPipelineLogDestinationResult'],
                 protocol: str,
                 public: bool,
                 source: str,
                 tag: str):
        """
        :param Sequence['GetPipelineLogDestinationArgs'] destinations: [list] The configuration of the logs datastore, a list that contains elements with the following structure:
        :param str protocol: [string] "Protocol to use as intake. Possible values are: http, tcp."
        :param bool public: [bool]
        :param str source: [string] The source parser to be used.
        :param str tag: [string] The tag is used to distinguish different pipelines. Must be unique amongst the pipeline's array items.
        """
        pulumi.set(__self__, "destinations", destinations)
        pulumi.set(__self__, "protocol", protocol)
        pulumi.set(__self__, "public", public)
        pulumi.set(__self__, "source", source)
        pulumi.set(__self__, "tag", tag)

    @property
    @pulumi.getter
    def destinations(self) -> Sequence['outputs.GetPipelineLogDestinationResult']:
        """
        [list] The configuration of the logs datastore, a list that contains elements with the following structure:
        """
        return pulumi.get(self, "destinations")

    @property
    @pulumi.getter
    def protocol(self) -> str:
        """
        [string] "Protocol to use as intake. Possible values are: http, tcp."
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter
    def public(self) -> bool:
        """
        [bool]
        """
        return pulumi.get(self, "public")

    @property
    @pulumi.getter
    def source(self) -> str:
        """
        [string] The source parser to be used.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def tag(self) -> str:
        """
        [string] The tag is used to distinguish different pipelines. Must be unique amongst the pipeline's array items.
        """
        return pulumi.get(self, "tag")


@pulumi.output_type
class GetPipelineLogDestinationResult(dict):
    def __init__(__self__, *,
                 retention_in_days: int,
                 type: str):
        """
        :param int retention_in_days: [int] Defines the number of days a log record should be kept in loki. Works with loki destination type only.
        :param str type: [string] The internal output stream to send logs to.
        """
        pulumi.set(__self__, "retention_in_days", retention_in_days)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> int:
        """
        [int] Defines the number of days a log record should be kept in loki. Works with loki destination type only.
        """
        return pulumi.get(self, "retention_in_days")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        [string] The internal output stream to send logs to.
        """
        return pulumi.get(self, "type")


