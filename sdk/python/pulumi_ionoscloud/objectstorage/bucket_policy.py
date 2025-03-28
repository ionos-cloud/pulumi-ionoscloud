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

__all__ = ['BucketPolicyArgs', 'BucketPolicy']

@pulumi.input_type
class BucketPolicyArgs:
    def __init__(__self__, *,
                 bucket: pulumi.Input[str],
                 policy: pulumi.Input[str]):
        """
        The set of arguments for constructing a BucketPolicy resource.
        :param pulumi.Input[str] bucket: [string] The name of the bucket where the object will be stored.
        :param pulumi.Input[str] policy: [string] The policy document. This is a JSON formatted string.
        """
        pulumi.set(__self__, "bucket", bucket)
        pulumi.set(__self__, "policy", policy)

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
    @pulumi.getter
    def policy(self) -> pulumi.Input[str]:
        """
        [string] The policy document. This is a JSON formatted string.
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy", value)


@pulumi.input_type
class _BucketPolicyState:
    def __init__(__self__, *,
                 bucket: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering BucketPolicy resources.
        :param pulumi.Input[str] bucket: [string] The name of the bucket where the object will be stored.
        :param pulumi.Input[str] policy: [string] The policy document. This is a JSON formatted string.
        """
        if bucket is not None:
            pulumi.set(__self__, "bucket", bucket)
        if policy is not None:
            pulumi.set(__self__, "policy", policy)

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
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The policy document. This is a JSON formatted string.
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy", value)


class BucketPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages **Buckets policies** on IonosCloud.

        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumi_ionoscloud as ionoscloud

        example = ionoscloud.objectstorage.Bucket("example", name="example")
        example_bucket_policy = ionoscloud.objectstorage.BucketPolicy("example",
            bucket=example.name,
            policy=json.dumps({
                "Version": "2012-10-17",
                "Statement": [{
                    "Sid": "Delegate certain actions to another user",
                    "Action": [
                        "s3:ListBucket",
                        "s3:PutObject",
                        "s3:GetObject",
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "arn:aws:s3:::example",
                        "arn:aws:s3:::example/*",
                    ],
                    "Condition": {
                        "IpAddress": ["123.123.123.123/32"],
                    },
                    "Principal": ["arn:aws:iam:::user/31000000:9acd8251-2857-410e-b1fd-ca86462bdcec"],
                }],
            }))
        ```

        ## Import

        Resource Policy can be imported using the `bucket name`

        ```sh
        $ pulumi import ionoscloud:objectstorage/bucketPolicy:BucketPolicy example example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: [string] The name of the bucket where the object will be stored.
        :param pulumi.Input[str] policy: [string] The policy document. This is a JSON formatted string.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BucketPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages **Buckets policies** on IonosCloud.

        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumi_ionoscloud as ionoscloud

        example = ionoscloud.objectstorage.Bucket("example", name="example")
        example_bucket_policy = ionoscloud.objectstorage.BucketPolicy("example",
            bucket=example.name,
            policy=json.dumps({
                "Version": "2012-10-17",
                "Statement": [{
                    "Sid": "Delegate certain actions to another user",
                    "Action": [
                        "s3:ListBucket",
                        "s3:PutObject",
                        "s3:GetObject",
                    ],
                    "Effect": "Allow",
                    "Resource": [
                        "arn:aws:s3:::example",
                        "arn:aws:s3:::example/*",
                    ],
                    "Condition": {
                        "IpAddress": ["123.123.123.123/32"],
                    },
                    "Principal": ["arn:aws:iam:::user/31000000:9acd8251-2857-410e-b1fd-ca86462bdcec"],
                }],
            }))
        ```

        ## Import

        Resource Policy can be imported using the `bucket name`

        ```sh
        $ pulumi import ionoscloud:objectstorage/bucketPolicy:BucketPolicy example example
        ```

        :param str resource_name: The name of the resource.
        :param BucketPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BucketPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BucketPolicyArgs.__new__(BucketPolicyArgs)

            if bucket is None and not opts.urn:
                raise TypeError("Missing required property 'bucket'")
            __props__.__dict__["bucket"] = bucket
            if policy is None and not opts.urn:
                raise TypeError("Missing required property 'policy'")
            __props__.__dict__["policy"] = policy
        super(BucketPolicy, __self__).__init__(
            'ionoscloud:objectstorage/bucketPolicy:BucketPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bucket: Optional[pulumi.Input[str]] = None,
            policy: Optional[pulumi.Input[str]] = None) -> 'BucketPolicy':
        """
        Get an existing BucketPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: [string] The name of the bucket where the object will be stored.
        :param pulumi.Input[str] policy: [string] The policy document. This is a JSON formatted string.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BucketPolicyState.__new__(_BucketPolicyState)

        __props__.__dict__["bucket"] = bucket
        __props__.__dict__["policy"] = policy
        return BucketPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[str]:
        """
        [string] The name of the bucket where the object will be stored.
        """
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output[str]:
        """
        [string] The policy document. This is a JSON formatted string.
        """
        return pulumi.get(self, "policy")

