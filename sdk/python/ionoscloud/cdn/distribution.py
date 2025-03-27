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

__all__ = ['DistributionArgs', 'Distribution']

@pulumi.input_type
class DistributionArgs:
    def __init__(__self__, *,
                 domain: pulumi.Input[str],
                 routing_rules: pulumi.Input[Sequence[pulumi.Input['DistributionRoutingRuleArgs']]],
                 certificate_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Distribution resource.
        :param pulumi.Input[str] domain: [string] The domain of the distribution.
        :param pulumi.Input[Sequence[pulumi.Input['DistributionRoutingRuleArgs']]] routing_rules: [list] The routing rules for the distribution.
        :param pulumi.Input[str] certificate_id: [string] The ID of the certificate to use for the distribution. You can create certificates with the certificate resource.
        """
        pulumi.set(__self__, "domain", domain)
        pulumi.set(__self__, "routing_rules", routing_rules)
        if certificate_id is not None:
            pulumi.set(__self__, "certificate_id", certificate_id)

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Input[str]:
        """
        [string] The domain of the distribution.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter(name="routingRules")
    def routing_rules(self) -> pulumi.Input[Sequence[pulumi.Input['DistributionRoutingRuleArgs']]]:
        """
        [list] The routing rules for the distribution.
        """
        return pulumi.get(self, "routing_rules")

    @routing_rules.setter
    def routing_rules(self, value: pulumi.Input[Sequence[pulumi.Input['DistributionRoutingRuleArgs']]]):
        pulumi.set(self, "routing_rules", value)

    @property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The ID of the certificate to use for the distribution. You can create certificates with the certificate resource.
        """
        return pulumi.get(self, "certificate_id")

    @certificate_id.setter
    def certificate_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_id", value)


@pulumi.input_type
class _DistributionState:
    def __init__(__self__, *,
                 certificate_id: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 public_endpoint_v4: Optional[pulumi.Input[str]] = None,
                 public_endpoint_v6: Optional[pulumi.Input[str]] = None,
                 resource_urn: Optional[pulumi.Input[str]] = None,
                 routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input['DistributionRoutingRuleArgs']]]] = None):
        """
        Input properties used for looking up and filtering Distribution resources.
        :param pulumi.Input[str] certificate_id: [string] The ID of the certificate to use for the distribution. You can create certificates with the certificate resource.
        :param pulumi.Input[str] domain: [string] The domain of the distribution.
        :param pulumi.Input[str] public_endpoint_v4: IP of the distribution, it has to be included on the domain DNS Zone as A record.
        :param pulumi.Input[str] public_endpoint_v6: IP of the distribution, it has to be included on the domain DNS Zone as AAAA record.
        :param pulumi.Input[str] resource_urn: Unique resource indentifier.
        :param pulumi.Input[Sequence[pulumi.Input['DistributionRoutingRuleArgs']]] routing_rules: [list] The routing rules for the distribution.
        """
        if certificate_id is not None:
            pulumi.set(__self__, "certificate_id", certificate_id)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if public_endpoint_v4 is not None:
            pulumi.set(__self__, "public_endpoint_v4", public_endpoint_v4)
        if public_endpoint_v6 is not None:
            pulumi.set(__self__, "public_endpoint_v6", public_endpoint_v6)
        if resource_urn is not None:
            pulumi.set(__self__, "resource_urn", resource_urn)
        if routing_rules is not None:
            pulumi.set(__self__, "routing_rules", routing_rules)

    @property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The ID of the certificate to use for the distribution. You can create certificates with the certificate resource.
        """
        return pulumi.get(self, "certificate_id")

    @certificate_id.setter
    def certificate_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_id", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The domain of the distribution.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter(name="publicEndpointV4")
    def public_endpoint_v4(self) -> Optional[pulumi.Input[str]]:
        """
        IP of the distribution, it has to be included on the domain DNS Zone as A record.
        """
        return pulumi.get(self, "public_endpoint_v4")

    @public_endpoint_v4.setter
    def public_endpoint_v4(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_endpoint_v4", value)

    @property
    @pulumi.getter(name="publicEndpointV6")
    def public_endpoint_v6(self) -> Optional[pulumi.Input[str]]:
        """
        IP of the distribution, it has to be included on the domain DNS Zone as AAAA record.
        """
        return pulumi.get(self, "public_endpoint_v6")

    @public_endpoint_v6.setter
    def public_endpoint_v6(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_endpoint_v6", value)

    @property
    @pulumi.getter(name="resourceUrn")
    def resource_urn(self) -> Optional[pulumi.Input[str]]:
        """
        Unique resource indentifier.
        """
        return pulumi.get(self, "resource_urn")

    @resource_urn.setter
    def resource_urn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_urn", value)

    @property
    @pulumi.getter(name="routingRules")
    def routing_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DistributionRoutingRuleArgs']]]]:
        """
        [list] The routing rules for the distribution.
        """
        return pulumi.get(self, "routing_rules")

    @routing_rules.setter
    def routing_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DistributionRoutingRuleArgs']]]]):
        pulumi.set(self, "routing_rules", value)


class Distribution(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_id: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union['DistributionRoutingRuleArgs', 'DistributionRoutingRuleArgsDict']]]]] = None,
                 __props__=None):
        """
        Manages a **CDN Distribution** on IonosCloud.

        ## Import

        Resource Distribution can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import ionoscloud:cdn/distribution:Distribution myDistribution distribution uuid
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate_id: [string] The ID of the certificate to use for the distribution. You can create certificates with the certificate resource.
        :param pulumi.Input[str] domain: [string] The domain of the distribution.
        :param pulumi.Input[Sequence[pulumi.Input[Union['DistributionRoutingRuleArgs', 'DistributionRoutingRuleArgsDict']]]] routing_rules: [list] The routing rules for the distribution.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DistributionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a **CDN Distribution** on IonosCloud.

        ## Import

        Resource Distribution can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import ionoscloud:cdn/distribution:Distribution myDistribution distribution uuid
        ```

        :param str resource_name: The name of the resource.
        :param DistributionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DistributionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_id: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union['DistributionRoutingRuleArgs', 'DistributionRoutingRuleArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DistributionArgs.__new__(DistributionArgs)

            __props__.__dict__["certificate_id"] = certificate_id
            if domain is None and not opts.urn:
                raise TypeError("Missing required property 'domain'")
            __props__.__dict__["domain"] = domain
            if routing_rules is None and not opts.urn:
                raise TypeError("Missing required property 'routing_rules'")
            __props__.__dict__["routing_rules"] = routing_rules
            __props__.__dict__["public_endpoint_v4"] = None
            __props__.__dict__["public_endpoint_v6"] = None
            __props__.__dict__["resource_urn"] = None
        super(Distribution, __self__).__init__(
            'ionoscloud:cdn/distribution:Distribution',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            certificate_id: Optional[pulumi.Input[str]] = None,
            domain: Optional[pulumi.Input[str]] = None,
            public_endpoint_v4: Optional[pulumi.Input[str]] = None,
            public_endpoint_v6: Optional[pulumi.Input[str]] = None,
            resource_urn: Optional[pulumi.Input[str]] = None,
            routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union['DistributionRoutingRuleArgs', 'DistributionRoutingRuleArgsDict']]]]] = None) -> 'Distribution':
        """
        Get an existing Distribution resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate_id: [string] The ID of the certificate to use for the distribution. You can create certificates with the certificate resource.
        :param pulumi.Input[str] domain: [string] The domain of the distribution.
        :param pulumi.Input[str] public_endpoint_v4: IP of the distribution, it has to be included on the domain DNS Zone as A record.
        :param pulumi.Input[str] public_endpoint_v6: IP of the distribution, it has to be included on the domain DNS Zone as AAAA record.
        :param pulumi.Input[str] resource_urn: Unique resource indentifier.
        :param pulumi.Input[Sequence[pulumi.Input[Union['DistributionRoutingRuleArgs', 'DistributionRoutingRuleArgsDict']]]] routing_rules: [list] The routing rules for the distribution.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DistributionState.__new__(_DistributionState)

        __props__.__dict__["certificate_id"] = certificate_id
        __props__.__dict__["domain"] = domain
        __props__.__dict__["public_endpoint_v4"] = public_endpoint_v4
        __props__.__dict__["public_endpoint_v6"] = public_endpoint_v6
        __props__.__dict__["resource_urn"] = resource_urn
        __props__.__dict__["routing_rules"] = routing_rules
        return Distribution(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> pulumi.Output[Optional[str]]:
        """
        [string] The ID of the certificate to use for the distribution. You can create certificates with the certificate resource.
        """
        return pulumi.get(self, "certificate_id")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[str]:
        """
        [string] The domain of the distribution.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="publicEndpointV4")
    def public_endpoint_v4(self) -> pulumi.Output[str]:
        """
        IP of the distribution, it has to be included on the domain DNS Zone as A record.
        """
        return pulumi.get(self, "public_endpoint_v4")

    @property
    @pulumi.getter(name="publicEndpointV6")
    def public_endpoint_v6(self) -> pulumi.Output[str]:
        """
        IP of the distribution, it has to be included on the domain DNS Zone as AAAA record.
        """
        return pulumi.get(self, "public_endpoint_v6")

    @property
    @pulumi.getter(name="resourceUrn")
    def resource_urn(self) -> pulumi.Output[str]:
        """
        Unique resource indentifier.
        """
        return pulumi.get(self, "resource_urn")

    @property
    @pulumi.getter(name="routingRules")
    def routing_rules(self) -> pulumi.Output[Sequence['outputs.DistributionRoutingRule']]:
        """
        [list] The routing rules for the distribution.
        """
        return pulumi.get(self, "routing_rules")

