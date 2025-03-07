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

import types

__config__ = pulumi.Config('ionoscloud')


class _ExportableConfig(types.ModuleType):
    @property
    def contract_number(self) -> Optional[str]:
        return __config__.get('contractNumber')

    @property
    def endpoint(self) -> Optional[str]:
        """
        IonosCloud REST API URL. Usually not necessary to be set, SDKs know internally how to route requests to the API.
        """
        return __config__.get('endpoint')

    @property
    def insecure(self) -> Optional[bool]:
        """
        This field is to be set only for testing purposes. It is not recommended to set this field in production environments.
        """
        return __config__.get_bool('insecure')

    @property
    def password(self) -> Optional[str]:
        """
        IonosCloud password for API operations. If token is provided, token is preferred
        """
        return __config__.get('password')

    @property
    def retries(self) -> Optional[int]:
        return __config__.get_int('retries')

    @property
    def s3_access_key(self) -> Optional[str]:
        """
        Access key for IONOS Object Storage operations.
        """
        return __config__.get('s3AccessKey')

    @property
    def s3_region(self) -> Optional[str]:
        """
        Region for IONOS Object Storage operations.
        """
        return __config__.get('s3Region')

    @property
    def s3_secret_key(self) -> Optional[str]:
        """
        Secret key for IONOS Object Storage operations.
        """
        return __config__.get('s3SecretKey')

    @property
    def token(self) -> Optional[str]:
        """
        IonosCloud bearer token for API operations.
        """
        return __config__.get('token')

    @property
    def username(self) -> Optional[str]:
        """
        IonosCloud username for API operations. If token is provided, token is preferred
        """
        return __config__.get('username')

