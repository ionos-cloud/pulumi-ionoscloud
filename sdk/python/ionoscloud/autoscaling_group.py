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
from ._inputs import *

__all__ = ['AutoscalingGroupArgs', 'AutoscalingGroup']

@pulumi.input_type
class AutoscalingGroupArgs:
    def __init__(__self__, *,
                 datacenter_id: pulumi.Input[str],
                 max_replica_count: pulumi.Input[int],
                 min_replica_count: pulumi.Input[int],
                 policy: pulumi.Input['AutoscalingGroupPolicyArgs'],
                 replica_configuration: pulumi.Input['AutoscalingGroupReplicaConfigurationArgs'],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AutoscalingGroup resource.
        :param pulumi.Input[str] datacenter_id: Unique identifier for the resource
        :param pulumi.Input[int] max_replica_count: The maximum value for the number of replicas on a VM Auto Scaling Group. Must be >= 0 and <= 200. Will be enforced for
               both automatic and manual changes.
        :param pulumi.Input[int] min_replica_count: The minimum value for the number of replicas on a VM Auto Scaling Group. Must be >= 0 and <= 200. Will be enforced for
               both automatic and manual changes
        :param pulumi.Input['AutoscalingGroupPolicyArgs'] policy: Defines the behavior of this VM Auto Scaling Group. A policy consists of triggers and actions, where an action is an
               automated behavior, and the trigger defines the circumstances under which the action is triggered. Currently, two
               separate actions are supported, namely scaling inward and outward, triggered by the thresholds defined for a particular
               metric.
        :param pulumi.Input[str] name: User-defined name for the Autoscaling Group.
        """
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        pulumi.set(__self__, "max_replica_count", max_replica_count)
        pulumi.set(__self__, "min_replica_count", min_replica_count)
        pulumi.set(__self__, "policy", policy)
        pulumi.set(__self__, "replica_configuration", replica_configuration)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> pulumi.Input[str]:
        """
        Unique identifier for the resource
        """
        return pulumi.get(self, "datacenter_id")

    @datacenter_id.setter
    def datacenter_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "datacenter_id", value)

    @property
    @pulumi.getter(name="maxReplicaCount")
    def max_replica_count(self) -> pulumi.Input[int]:
        """
        The maximum value for the number of replicas on a VM Auto Scaling Group. Must be >= 0 and <= 200. Will be enforced for
        both automatic and manual changes.
        """
        return pulumi.get(self, "max_replica_count")

    @max_replica_count.setter
    def max_replica_count(self, value: pulumi.Input[int]):
        pulumi.set(self, "max_replica_count", value)

    @property
    @pulumi.getter(name="minReplicaCount")
    def min_replica_count(self) -> pulumi.Input[int]:
        """
        The minimum value for the number of replicas on a VM Auto Scaling Group. Must be >= 0 and <= 200. Will be enforced for
        both automatic and manual changes
        """
        return pulumi.get(self, "min_replica_count")

    @min_replica_count.setter
    def min_replica_count(self, value: pulumi.Input[int]):
        pulumi.set(self, "min_replica_count", value)

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Input['AutoscalingGroupPolicyArgs']:
        """
        Defines the behavior of this VM Auto Scaling Group. A policy consists of triggers and actions, where an action is an
        automated behavior, and the trigger defines the circumstances under which the action is triggered. Currently, two
        separate actions are supported, namely scaling inward and outward, triggered by the thresholds defined for a particular
        metric.
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: pulumi.Input['AutoscalingGroupPolicyArgs']):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter(name="replicaConfiguration")
    def replica_configuration(self) -> pulumi.Input['AutoscalingGroupReplicaConfigurationArgs']:
        return pulumi.get(self, "replica_configuration")

    @replica_configuration.setter
    def replica_configuration(self, value: pulumi.Input['AutoscalingGroupReplicaConfigurationArgs']):
        pulumi.set(self, "replica_configuration", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        User-defined name for the Autoscaling Group.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _AutoscalingGroupState:
    def __init__(__self__, *,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 max_replica_count: Optional[pulumi.Input[int]] = None,
                 min_replica_count: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input['AutoscalingGroupPolicyArgs']] = None,
                 replica_configuration: Optional[pulumi.Input['AutoscalingGroupReplicaConfigurationArgs']] = None):
        """
        Input properties used for looking up and filtering AutoscalingGroup resources.
        :param pulumi.Input[str] datacenter_id: Unique identifier for the resource
        :param pulumi.Input[str] location: Location of the data center.
        :param pulumi.Input[int] max_replica_count: The maximum value for the number of replicas on a VM Auto Scaling Group. Must be >= 0 and <= 200. Will be enforced for
               both automatic and manual changes.
        :param pulumi.Input[int] min_replica_count: The minimum value for the number of replicas on a VM Auto Scaling Group. Must be >= 0 and <= 200. Will be enforced for
               both automatic and manual changes
        :param pulumi.Input[str] name: User-defined name for the Autoscaling Group.
        :param pulumi.Input['AutoscalingGroupPolicyArgs'] policy: Defines the behavior of this VM Auto Scaling Group. A policy consists of triggers and actions, where an action is an
               automated behavior, and the trigger defines the circumstances under which the action is triggered. Currently, two
               separate actions are supported, namely scaling inward and outward, triggered by the thresholds defined for a particular
               metric.
        """
        if datacenter_id is not None:
            pulumi.set(__self__, "datacenter_id", datacenter_id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if max_replica_count is not None:
            pulumi.set(__self__, "max_replica_count", max_replica_count)
        if min_replica_count is not None:
            pulumi.set(__self__, "min_replica_count", min_replica_count)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if policy is not None:
            pulumi.set(__self__, "policy", policy)
        if replica_configuration is not None:
            pulumi.set(__self__, "replica_configuration", replica_configuration)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> Optional[pulumi.Input[str]]:
        """
        Unique identifier for the resource
        """
        return pulumi.get(self, "datacenter_id")

    @datacenter_id.setter
    def datacenter_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datacenter_id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Location of the data center.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="maxReplicaCount")
    def max_replica_count(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum value for the number of replicas on a VM Auto Scaling Group. Must be >= 0 and <= 200. Will be enforced for
        both automatic and manual changes.
        """
        return pulumi.get(self, "max_replica_count")

    @max_replica_count.setter
    def max_replica_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_replica_count", value)

    @property
    @pulumi.getter(name="minReplicaCount")
    def min_replica_count(self) -> Optional[pulumi.Input[int]]:
        """
        The minimum value for the number of replicas on a VM Auto Scaling Group. Must be >= 0 and <= 200. Will be enforced for
        both automatic and manual changes
        """
        return pulumi.get(self, "min_replica_count")

    @min_replica_count.setter
    def min_replica_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_replica_count", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        User-defined name for the Autoscaling Group.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input['AutoscalingGroupPolicyArgs']]:
        """
        Defines the behavior of this VM Auto Scaling Group. A policy consists of triggers and actions, where an action is an
        automated behavior, and the trigger defines the circumstances under which the action is triggered. Currently, two
        separate actions are supported, namely scaling inward and outward, triggered by the thresholds defined for a particular
        metric.
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: Optional[pulumi.Input['AutoscalingGroupPolicyArgs']]):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter(name="replicaConfiguration")
    def replica_configuration(self) -> Optional[pulumi.Input['AutoscalingGroupReplicaConfigurationArgs']]:
        return pulumi.get(self, "replica_configuration")

    @replica_configuration.setter
    def replica_configuration(self, value: Optional[pulumi.Input['AutoscalingGroupReplicaConfigurationArgs']]):
        pulumi.set(self, "replica_configuration", value)


warnings.warn("""ionoscloud.index/autoscalinggroup.AutoscalingGroup has been deprecated in favor of ionoscloud.autoscaling/group.Group""", DeprecationWarning)


class AutoscalingGroup(pulumi.CustomResource):
    warnings.warn("""ionoscloud.index/autoscalinggroup.AutoscalingGroup has been deprecated in favor of ionoscloud.autoscaling/group.Group""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 max_replica_count: Optional[pulumi.Input[int]] = None,
                 min_replica_count: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[pulumi.InputType['AutoscalingGroupPolicyArgs']]] = None,
                 replica_configuration: Optional[pulumi.Input[pulumi.InputType['AutoscalingGroupReplicaConfigurationArgs']]] = None,
                 __props__=None):
        """
        Create a AutoscalingGroup resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] datacenter_id: Unique identifier for the resource
        :param pulumi.Input[int] max_replica_count: The maximum value for the number of replicas on a VM Auto Scaling Group. Must be >= 0 and <= 200. Will be enforced for
               both automatic and manual changes.
        :param pulumi.Input[int] min_replica_count: The minimum value for the number of replicas on a VM Auto Scaling Group. Must be >= 0 and <= 200. Will be enforced for
               both automatic and manual changes
        :param pulumi.Input[str] name: User-defined name for the Autoscaling Group.
        :param pulumi.Input[pulumi.InputType['AutoscalingGroupPolicyArgs']] policy: Defines the behavior of this VM Auto Scaling Group. A policy consists of triggers and actions, where an action is an
               automated behavior, and the trigger defines the circumstances under which the action is triggered. Currently, two
               separate actions are supported, namely scaling inward and outward, triggered by the thresholds defined for a particular
               metric.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AutoscalingGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a AutoscalingGroup resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AutoscalingGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AutoscalingGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 max_replica_count: Optional[pulumi.Input[int]] = None,
                 min_replica_count: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[pulumi.InputType['AutoscalingGroupPolicyArgs']]] = None,
                 replica_configuration: Optional[pulumi.Input[pulumi.InputType['AutoscalingGroupReplicaConfigurationArgs']]] = None,
                 __props__=None):
        pulumi.log.warn("""AutoscalingGroup is deprecated: ionoscloud.index/autoscalinggroup.AutoscalingGroup has been deprecated in favor of ionoscloud.autoscaling/group.Group""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AutoscalingGroupArgs.__new__(AutoscalingGroupArgs)

            if datacenter_id is None and not opts.urn:
                raise TypeError("Missing required property 'datacenter_id'")
            __props__.__dict__["datacenter_id"] = datacenter_id
            if max_replica_count is None and not opts.urn:
                raise TypeError("Missing required property 'max_replica_count'")
            __props__.__dict__["max_replica_count"] = max_replica_count
            if min_replica_count is None and not opts.urn:
                raise TypeError("Missing required property 'min_replica_count'")
            __props__.__dict__["min_replica_count"] = min_replica_count
            __props__.__dict__["name"] = name
            if policy is None and not opts.urn:
                raise TypeError("Missing required property 'policy'")
            __props__.__dict__["policy"] = policy
            if replica_configuration is None and not opts.urn:
                raise TypeError("Missing required property 'replica_configuration'")
            __props__.__dict__["replica_configuration"] = replica_configuration
            __props__.__dict__["location"] = None
        super(AutoscalingGroup, __self__).__init__(
            'ionoscloud:index/autoscalingGroup:AutoscalingGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            datacenter_id: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            max_replica_count: Optional[pulumi.Input[int]] = None,
            min_replica_count: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            policy: Optional[pulumi.Input[pulumi.InputType['AutoscalingGroupPolicyArgs']]] = None,
            replica_configuration: Optional[pulumi.Input[pulumi.InputType['AutoscalingGroupReplicaConfigurationArgs']]] = None) -> 'AutoscalingGroup':
        """
        Get an existing AutoscalingGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] datacenter_id: Unique identifier for the resource
        :param pulumi.Input[str] location: Location of the data center.
        :param pulumi.Input[int] max_replica_count: The maximum value for the number of replicas on a VM Auto Scaling Group. Must be >= 0 and <= 200. Will be enforced for
               both automatic and manual changes.
        :param pulumi.Input[int] min_replica_count: The minimum value for the number of replicas on a VM Auto Scaling Group. Must be >= 0 and <= 200. Will be enforced for
               both automatic and manual changes
        :param pulumi.Input[str] name: User-defined name for the Autoscaling Group.
        :param pulumi.Input[pulumi.InputType['AutoscalingGroupPolicyArgs']] policy: Defines the behavior of this VM Auto Scaling Group. A policy consists of triggers and actions, where an action is an
               automated behavior, and the trigger defines the circumstances under which the action is triggered. Currently, two
               separate actions are supported, namely scaling inward and outward, triggered by the thresholds defined for a particular
               metric.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AutoscalingGroupState.__new__(_AutoscalingGroupState)

        __props__.__dict__["datacenter_id"] = datacenter_id
        __props__.__dict__["location"] = location
        __props__.__dict__["max_replica_count"] = max_replica_count
        __props__.__dict__["min_replica_count"] = min_replica_count
        __props__.__dict__["name"] = name
        __props__.__dict__["policy"] = policy
        __props__.__dict__["replica_configuration"] = replica_configuration
        return AutoscalingGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> pulumi.Output[str]:
        """
        Unique identifier for the resource
        """
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Location of the data center.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maxReplicaCount")
    def max_replica_count(self) -> pulumi.Output[int]:
        """
        The maximum value for the number of replicas on a VM Auto Scaling Group. Must be >= 0 and <= 200. Will be enforced for
        both automatic and manual changes.
        """
        return pulumi.get(self, "max_replica_count")

    @property
    @pulumi.getter(name="minReplicaCount")
    def min_replica_count(self) -> pulumi.Output[int]:
        """
        The minimum value for the number of replicas on a VM Auto Scaling Group. Must be >= 0 and <= 200. Will be enforced for
        both automatic and manual changes
        """
        return pulumi.get(self, "min_replica_count")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        User-defined name for the Autoscaling Group.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output['outputs.AutoscalingGroupPolicy']:
        """
        Defines the behavior of this VM Auto Scaling Group. A policy consists of triggers and actions, where an action is an
        automated behavior, and the trigger defines the circumstances under which the action is triggered. Currently, two
        separate actions are supported, namely scaling inward and outward, triggered by the thresholds defined for a particular
        metric.
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter(name="replicaConfiguration")
    def replica_configuration(self) -> pulumi.Output['outputs.AutoscalingGroupReplicaConfiguration']:
        return pulumi.get(self, "replica_configuration")

