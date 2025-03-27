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
from ._inputs import *

__all__ = ['CorsConfigurationArgs', 'CorsConfiguration']

@pulumi.input_type
class CorsConfigurationArgs:
    def __init__(__self__, *,
                 bucket: pulumi.Input[str],
                 cors_rules: Optional[pulumi.Input[Sequence[pulumi.Input['CorsConfigurationCorsRuleArgs']]]] = None):
        """
        The set of arguments for constructing a CorsConfiguration resource.
        :param pulumi.Input[str] bucket: [string] The name of the bucket where the object will be stored.
        :param pulumi.Input[Sequence[pulumi.Input['CorsConfigurationCorsRuleArgs']]] cors_rules: [block] A block of cors_rule as defined below.
        """
        pulumi.set(__self__, "bucket", bucket)
        if cors_rules is not None:
            pulumi.set(__self__, "cors_rules", cors_rules)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[str]:
        """
        [string] The name of the bucket where the object will be stored.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter(name="corsRules")
    def cors_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CorsConfigurationCorsRuleArgs']]]]:
        """
        [block] A block of cors_rule as defined below.
        """
        return pulumi.get(self, "cors_rules")

    @cors_rules.setter
    def cors_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CorsConfigurationCorsRuleArgs']]]]):
        pulumi.set(self, "cors_rules", value)


@pulumi.input_type
class _CorsConfigurationState:
    def __init__(__self__, *,
                 bucket: Optional[pulumi.Input[str]] = None,
                 cors_rules: Optional[pulumi.Input[Sequence[pulumi.Input['CorsConfigurationCorsRuleArgs']]]] = None):
        """
        Input properties used for looking up and filtering CorsConfiguration resources.
        :param pulumi.Input[str] bucket: [string] The name of the bucket where the object will be stored.
        :param pulumi.Input[Sequence[pulumi.Input['CorsConfigurationCorsRuleArgs']]] cors_rules: [block] A block of cors_rule as defined below.
        """
        if bucket is not None:
            pulumi.set(__self__, "bucket", bucket)
        if cors_rules is not None:
            pulumi.set(__self__, "cors_rules", cors_rules)

    @property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The name of the bucket where the object will be stored.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter(name="corsRules")
    def cors_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CorsConfigurationCorsRuleArgs']]]]:
        """
        [block] A block of cors_rule as defined below.
        """
        return pulumi.get(self, "cors_rules")

    @cors_rules.setter
    def cors_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CorsConfigurationCorsRuleArgs']]]]):
        pulumi.set(self, "cors_rules", value)


class CorsConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 cors_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union['CorsConfigurationCorsRuleArgs', 'CorsConfigurationCorsRuleArgsDict']]]]] = None,
                 __props__=None):
        """
        Manages Object Lock Configuration for Buckets on IonosCloud.

        ## Example Usage

        ```python
        import pulumi
        import ionoscloud as ionoscloud

        example = ionoscloud.objectstorage.Bucket("example", name="example")
        test = ionoscloud.objectstorage.CorsConfiguration("test",
            bucket=example.name,
            cors_rules=[{
                "allowed_headers": ["*"],
                "allowed_methods": [
                    "PUT",
                    "POST",
                ],
                "allowed_origins": ["https://s3-website-test.hashicorp.com"],
                "expose_headers": ["ETag"],
                "max_age_seconds": 3000,
                "id": 1234,
            }])
        ```

        ## Import

        IONOS Object Storage Bucket cors configuration can be imported using the `bucket` name.

        ```sh
        $ pulumi import ionoscloud:objectstorage/corsConfiguration:CorsConfiguration example example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: [string] The name of the bucket where the object will be stored.
        :param pulumi.Input[Sequence[pulumi.Input[Union['CorsConfigurationCorsRuleArgs', 'CorsConfigurationCorsRuleArgsDict']]]] cors_rules: [block] A block of cors_rule as defined below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CorsConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages Object Lock Configuration for Buckets on IonosCloud.

        ## Example Usage

        ```python
        import pulumi
        import ionoscloud as ionoscloud

        example = ionoscloud.objectstorage.Bucket("example", name="example")
        test = ionoscloud.objectstorage.CorsConfiguration("test",
            bucket=example.name,
            cors_rules=[{
                "allowed_headers": ["*"],
                "allowed_methods": [
                    "PUT",
                    "POST",
                ],
                "allowed_origins": ["https://s3-website-test.hashicorp.com"],
                "expose_headers": ["ETag"],
                "max_age_seconds": 3000,
                "id": 1234,
            }])
        ```

        ## Import

        IONOS Object Storage Bucket cors configuration can be imported using the `bucket` name.

        ```sh
        $ pulumi import ionoscloud:objectstorage/corsConfiguration:CorsConfiguration example example
        ```

        :param str resource_name: The name of the resource.
        :param CorsConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CorsConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 cors_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union['CorsConfigurationCorsRuleArgs', 'CorsConfigurationCorsRuleArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CorsConfigurationArgs.__new__(CorsConfigurationArgs)

            if bucket is None and not opts.urn:
                raise TypeError("Missing required property 'bucket'")
            __props__.__dict__["bucket"] = bucket
            __props__.__dict__["cors_rules"] = cors_rules
        super(CorsConfiguration, __self__).__init__(
            'ionoscloud:objectstorage/corsConfiguration:CorsConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bucket: Optional[pulumi.Input[str]] = None,
            cors_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union['CorsConfigurationCorsRuleArgs', 'CorsConfigurationCorsRuleArgsDict']]]]] = None) -> 'CorsConfiguration':
        """
        Get an existing CorsConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: [string] The name of the bucket where the object will be stored.
        :param pulumi.Input[Sequence[pulumi.Input[Union['CorsConfigurationCorsRuleArgs', 'CorsConfigurationCorsRuleArgsDict']]]] cors_rules: [block] A block of cors_rule as defined below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CorsConfigurationState.__new__(_CorsConfigurationState)

        __props__.__dict__["bucket"] = bucket
        __props__.__dict__["cors_rules"] = cors_rules
        return CorsConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[str]:
        """
        [string] The name of the bucket where the object will be stored.
        """
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter(name="corsRules")
    def cors_rules(self) -> pulumi.Output[Optional[Sequence['outputs.CorsConfigurationCorsRule']]]:
        """
        [block] A block of cors_rule as defined below.
        """
        return pulumi.get(self, "cors_rules")

