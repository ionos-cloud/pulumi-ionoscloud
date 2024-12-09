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

contractNumber: Optional[str]

endpoint: Optional[str]
"""
IonosCloud REST API URL. Usually not necessary to be set, SDKs know internally how to route requests to the API.
"""

password: Optional[str]
"""
IonosCloud password for API operations. If token is provided, token is preferred
"""

retries: Optional[int]

s3AccessKey: Optional[str]
"""
Access key for IONOS Object Storage operations.
"""

s3Region: Optional[str]
"""
Region for IONOS Object Storage operations.
"""

s3SecretKey: Optional[str]
"""
Secret key for IONOS Object Storage operations.
"""

token: Optional[str]
"""
IonosCloud bearer token for API operations.
"""

username: Optional[str]
"""
IonosCloud username for API operations. If token is provided, token is preferred
"""

