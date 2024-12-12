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

__all__ = ['CdnDistributionArgs', 'CdnDistribution']

@pulumi.input_type
class CdnDistributionArgs:
    def __init__(__self__, *,
                 domain: pulumi.Input[str],
                 routing_rules: pulumi.Input[Sequence[pulumi.Input['CdnDistributionRoutingRuleArgs']]],
                 certificate_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CdnDistribution resource.
        :param pulumi.Input[str] domain: The domain of the distribution.
        :param pulumi.Input[Sequence[pulumi.Input['CdnDistributionRoutingRuleArgs']]] routing_rules: The routing rules for the distribution.
        :param pulumi.Input[str] certificate_id: The ID of the certificate to use for the distribution.
        """
        pulumi.set(__self__, "domain", domain)
        pulumi.set(__self__, "routing_rules", routing_rules)
        if certificate_id is not None:
            pulumi.set(__self__, "certificate_id", certificate_id)

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Input[str]:
        """
        The domain of the distribution.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter(name="routingRules")
    def routing_rules(self) -> pulumi.Input[Sequence[pulumi.Input['CdnDistributionRoutingRuleArgs']]]:
        """
        The routing rules for the distribution.
        """
        return pulumi.get(self, "routing_rules")

    @routing_rules.setter
    def routing_rules(self, value: pulumi.Input[Sequence[pulumi.Input['CdnDistributionRoutingRuleArgs']]]):
        pulumi.set(self, "routing_rules", value)

    @property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the certificate to use for the distribution.
        """
        return pulumi.get(self, "certificate_id")

    @certificate_id.setter
    def certificate_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_id", value)


@pulumi.input_type
class _CdnDistributionState:
    def __init__(__self__, *,
                 certificate_id: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 public_endpoint_v4: Optional[pulumi.Input[str]] = None,
                 public_endpoint_v6: Optional[pulumi.Input[str]] = None,
                 resource_urn: Optional[pulumi.Input[str]] = None,
                 routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input['CdnDistributionRoutingRuleArgs']]]] = None):
        """
        Input properties used for looking up and filtering CdnDistribution resources.
        :param pulumi.Input[str] certificate_id: The ID of the certificate to use for the distribution.
        :param pulumi.Input[str] domain: The domain of the distribution.
        :param pulumi.Input[str] public_endpoint_v4: IP of the distribution, it has to be included on the domain DNS Zone as A record.
        :param pulumi.Input[str] public_endpoint_v6: IP of the distribution, it has to be included on the domain DNS Zone as AAAA record.
        :param pulumi.Input[str] resource_urn: Unique name of the resource.
        :param pulumi.Input[Sequence[pulumi.Input['CdnDistributionRoutingRuleArgs']]] routing_rules: The routing rules for the distribution.
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
        The ID of the certificate to use for the distribution.
        """
        return pulumi.get(self, "certificate_id")

    @certificate_id.setter
    def certificate_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_id", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        The domain of the distribution.
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
        Unique name of the resource.
        """
        return pulumi.get(self, "resource_urn")

    @resource_urn.setter
    def resource_urn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_urn", value)

    @property
    @pulumi.getter(name="routingRules")
    def routing_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CdnDistributionRoutingRuleArgs']]]]:
        """
        The routing rules for the distribution.
        """
        return pulumi.get(self, "routing_rules")

    @routing_rules.setter
    def routing_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CdnDistributionRoutingRuleArgs']]]]):
        pulumi.set(self, "routing_rules", value)


warnings.warn("""ionoscloud.index/cdndistribution.CdnDistribution has been deprecated in favor of ionoscloud.cdn/distribution.Distribution""", DeprecationWarning)


class CdnDistribution(pulumi.CustomResource):
    warnings.warn("""ionoscloud.index/cdndistribution.CdnDistribution has been deprecated in favor of ionoscloud.cdn/distribution.Distribution""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_id: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CdnDistributionRoutingRuleArgs']]]]] = None,
                 __props__=None):
        """
<<<<<<< HEAD
        Manages a **CDN Distribution** on IonosCloud.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ionoscloud as ionoscloud

        #optionally you can add a certificate to the distribution
        cert = ionoscloud.cert.Certificate("cert",
            certificate=(lambda path: open(path).read())("path_to_cert"),
            certificate_chain=(lambda path: open(path).read())("path_to_cert_chain"),
            private_key=(lambda path: open(path).read())("path_to_private_key"))
        example = ionoscloud.CdnDistribution("example",
            domain="example.com",
            certificate_id=cert.id,
            routing_rules=[
                ionoscloud.CdnDistributionRoutingRuleArgs(
                    scheme="https",
                    prefix="/api",
                    upstream=ionoscloud.CdnDistributionRoutingRuleUpstreamArgs(
                        host="server.example.com",
                        caching=True,
                        waf=True,
                        sni_mode="distribution",
                        rate_limit_class="R500",
                        geo_restrictions=ionoscloud.CdnDistributionRoutingRuleUpstreamGeoRestrictionsArgs(
                            allow_lists=[
                                "CN",
                                "RU",
                            ],
                        ),
                    ),
                ),
                ionoscloud.CdnDistributionRoutingRuleArgs(
                    scheme="http/https",
                    prefix="/api2",
                    upstream=ionoscloud.CdnDistributionRoutingRuleUpstreamArgs(
                        host="server2.example.com",
                        caching=False,
                        waf=False,
                        sni_mode="origin",
                        rate_limit_class="R10",
                        geo_restrictions=ionoscloud.CdnDistributionRoutingRuleUpstreamGeoRestrictionsArgs(
                            block_lists=[
                                "CN",
                                "RU",
                            ],
                        ),
                    ),
                ),
            ])
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        Resource Distribution can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import ionoscloud:index/cdnDistribution:CdnDistribution myDistribution {distribution uuid}
        ```

=======
        Create a CdnDistribution resource with the given unique name, props, and options.
>>>>>>> main
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate_id: The ID of the certificate to use for the distribution.
        :param pulumi.Input[str] domain: The domain of the distribution.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CdnDistributionRoutingRuleArgs']]]] routing_rules: The routing rules for the distribution.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CdnDistributionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
<<<<<<< HEAD
        Manages a **CDN Distribution** on IonosCloud.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ionoscloud as ionoscloud

        #optionally you can add a certificate to the distribution
        cert = ionoscloud.cert.Certificate("cert",
            certificate=(lambda path: open(path).read())("path_to_cert"),
            certificate_chain=(lambda path: open(path).read())("path_to_cert_chain"),
            private_key=(lambda path: open(path).read())("path_to_private_key"))
        example = ionoscloud.CdnDistribution("example",
            domain="example.com",
            certificate_id=cert.id,
            routing_rules=[
                ionoscloud.CdnDistributionRoutingRuleArgs(
                    scheme="https",
                    prefix="/api",
                    upstream=ionoscloud.CdnDistributionRoutingRuleUpstreamArgs(
                        host="server.example.com",
                        caching=True,
                        waf=True,
                        sni_mode="distribution",
                        rate_limit_class="R500",
                        geo_restrictions=ionoscloud.CdnDistributionRoutingRuleUpstreamGeoRestrictionsArgs(
                            allow_lists=[
                                "CN",
                                "RU",
                            ],
                        ),
                    ),
                ),
                ionoscloud.CdnDistributionRoutingRuleArgs(
                    scheme="http/https",
                    prefix="/api2",
                    upstream=ionoscloud.CdnDistributionRoutingRuleUpstreamArgs(
                        host="server2.example.com",
                        caching=False,
                        waf=False,
                        sni_mode="origin",
                        rate_limit_class="R10",
                        geo_restrictions=ionoscloud.CdnDistributionRoutingRuleUpstreamGeoRestrictionsArgs(
                            block_lists=[
                                "CN",
                                "RU",
                            ],
                        ),
                    ),
                ),
            ])
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        Resource Distribution can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import ionoscloud:index/cdnDistribution:CdnDistribution myDistribution {distribution uuid}
        ```

=======
        Create a CdnDistribution resource with the given unique name, props, and options.
>>>>>>> main
        :param str resource_name: The name of the resource.
        :param CdnDistributionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CdnDistributionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_id: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CdnDistributionRoutingRuleArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""CdnDistribution is deprecated: ionoscloud.index/cdndistribution.CdnDistribution has been deprecated in favor of ionoscloud.cdn/distribution.Distribution""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CdnDistributionArgs.__new__(CdnDistributionArgs)

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
        super(CdnDistribution, __self__).__init__(
            'ionoscloud:index/cdnDistribution:CdnDistribution',
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
            routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CdnDistributionRoutingRuleArgs']]]]] = None) -> 'CdnDistribution':
        """
        Get an existing CdnDistribution resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate_id: The ID of the certificate to use for the distribution.
        :param pulumi.Input[str] domain: The domain of the distribution.
        :param pulumi.Input[str] public_endpoint_v4: IP of the distribution, it has to be included on the domain DNS Zone as A record.
        :param pulumi.Input[str] public_endpoint_v6: IP of the distribution, it has to be included on the domain DNS Zone as AAAA record.
        :param pulumi.Input[str] resource_urn: Unique name of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CdnDistributionRoutingRuleArgs']]]] routing_rules: The routing rules for the distribution.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CdnDistributionState.__new__(_CdnDistributionState)

        __props__.__dict__["certificate_id"] = certificate_id
        __props__.__dict__["domain"] = domain
        __props__.__dict__["public_endpoint_v4"] = public_endpoint_v4
        __props__.__dict__["public_endpoint_v6"] = public_endpoint_v6
        __props__.__dict__["resource_urn"] = resource_urn
        __props__.__dict__["routing_rules"] = routing_rules
        return CdnDistribution(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the certificate to use for the distribution.
        """
        return pulumi.get(self, "certificate_id")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[str]:
        """
        The domain of the distribution.
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
        Unique name of the resource.
        """
        return pulumi.get(self, "resource_urn")

    @property
    @pulumi.getter(name="routingRules")
    def routing_rules(self) -> pulumi.Output[Sequence['outputs.CdnDistributionRoutingRule']]:
        """
        The routing rules for the distribution.
        """
        return pulumi.get(self, "routing_rules")

