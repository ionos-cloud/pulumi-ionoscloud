# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
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
from . import outputs
from ._inputs import *

__all__ = ['ApigatewayArgs', 'Apigateway']

@pulumi.input_type
class ApigatewayArgs:
    def __init__(__self__, *,
                 custom_domains: Optional[pulumi.Input[Sequence[pulumi.Input['ApigatewayCustomDomainArgs']]]] = None,
                 logs: Optional[pulumi.Input[bool]] = None,
                 metrics: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Apigateway resource.
        :param pulumi.Input[Sequence[pulumi.Input['ApigatewayCustomDomainArgs']]] custom_domains: [list] Custom domains for the API Gateway, a list that contains elements with the following structure:
        :param pulumi.Input[bool] logs: [bool] Enable or disable logging. Defaults to `false`. **NOTE**: Central Logging must be enabled through the Logging API to enable this feature.
        :param pulumi.Input[bool] metrics: [bool] Enable or disable metrics. Defaults to `false`.
        :param pulumi.Input[str] name: [string] The domain name. Externally reachable.
        """
        if custom_domains is not None:
            pulumi.set(__self__, "custom_domains", custom_domains)
        if logs is not None:
            pulumi.set(__self__, "logs", logs)
        if metrics is not None:
            pulumi.set(__self__, "metrics", metrics)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="customDomains")
    def custom_domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApigatewayCustomDomainArgs']]]]:
        """
        [list] Custom domains for the API Gateway, a list that contains elements with the following structure:
        """
        return pulumi.get(self, "custom_domains")

    @custom_domains.setter
    def custom_domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApigatewayCustomDomainArgs']]]]):
        pulumi.set(self, "custom_domains", value)

    @property
    @pulumi.getter
    def logs(self) -> Optional[pulumi.Input[bool]]:
        """
        [bool] Enable or disable logging. Defaults to `false`. **NOTE**: Central Logging must be enabled through the Logging API to enable this feature.
        """
        return pulumi.get(self, "logs")

    @logs.setter
    def logs(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "logs", value)

    @property
    @pulumi.getter
    def metrics(self) -> Optional[pulumi.Input[bool]]:
        """
        [bool] Enable or disable metrics. Defaults to `false`.
        """
        return pulumi.get(self, "metrics")

    @metrics.setter
    def metrics(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "metrics", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The domain name. Externally reachable.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ApigatewayState:
    def __init__(__self__, *,
                 custom_domains: Optional[pulumi.Input[Sequence[pulumi.Input['ApigatewayCustomDomainArgs']]]] = None,
                 logs: Optional[pulumi.Input[bool]] = None,
                 metrics: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 public_endpoint: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Apigateway resources.
        :param pulumi.Input[Sequence[pulumi.Input['ApigatewayCustomDomainArgs']]] custom_domains: [list] Custom domains for the API Gateway, a list that contains elements with the following structure:
        :param pulumi.Input[bool] logs: [bool] Enable or disable logging. Defaults to `false`. **NOTE**: Central Logging must be enabled through the Logging API to enable this feature.
        :param pulumi.Input[bool] metrics: [bool] Enable or disable metrics. Defaults to `false`.
        :param pulumi.Input[str] name: [string] The domain name. Externally reachable.
        :param pulumi.Input[str] public_endpoint: [string] The public endpoint of the API Gateway.
        """
        if custom_domains is not None:
            pulumi.set(__self__, "custom_domains", custom_domains)
        if logs is not None:
            pulumi.set(__self__, "logs", logs)
        if metrics is not None:
            pulumi.set(__self__, "metrics", metrics)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if public_endpoint is not None:
            pulumi.set(__self__, "public_endpoint", public_endpoint)

    @property
    @pulumi.getter(name="customDomains")
    def custom_domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApigatewayCustomDomainArgs']]]]:
        """
        [list] Custom domains for the API Gateway, a list that contains elements with the following structure:
        """
        return pulumi.get(self, "custom_domains")

    @custom_domains.setter
    def custom_domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApigatewayCustomDomainArgs']]]]):
        pulumi.set(self, "custom_domains", value)

    @property
    @pulumi.getter
    def logs(self) -> Optional[pulumi.Input[bool]]:
        """
        [bool] Enable or disable logging. Defaults to `false`. **NOTE**: Central Logging must be enabled through the Logging API to enable this feature.
        """
        return pulumi.get(self, "logs")

    @logs.setter
    def logs(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "logs", value)

    @property
    @pulumi.getter
    def metrics(self) -> Optional[pulumi.Input[bool]]:
        """
        [bool] Enable or disable metrics. Defaults to `false`.
        """
        return pulumi.get(self, "metrics")

    @metrics.setter
    def metrics(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "metrics", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The domain name. Externally reachable.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="publicEndpoint")
    def public_endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The public endpoint of the API Gateway.
        """
        return pulumi.get(self, "public_endpoint")

    @public_endpoint.setter
    def public_endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_endpoint", value)


class Apigateway(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_domains: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ApigatewayCustomDomainArgs', 'ApigatewayCustomDomainArgsDict']]]]] = None,
                 logs: Optional[pulumi.Input[bool]] = None,
                 metrics: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An API gateway consists of the generic rules and configurations.

        ## Usage example

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ionoscloud as ionoscloud

        example = ionoscloud.Apigateway("example", metrics=True)
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        In order to import an API Gateway, you can define an empty API Gateway resource in the plan:

        resource "ionoscloud_apigateway" "example" {

        }

        The resource can be imported using the `gateway_id`, for example:

        ```sh
        $ pulumi import ionoscloud:index/apigateway:Apigateway example {gateway_id}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ApigatewayCustomDomainArgs', 'ApigatewayCustomDomainArgsDict']]]] custom_domains: [list] Custom domains for the API Gateway, a list that contains elements with the following structure:
        :param pulumi.Input[bool] logs: [bool] Enable or disable logging. Defaults to `false`. **NOTE**: Central Logging must be enabled through the Logging API to enable this feature.
        :param pulumi.Input[bool] metrics: [bool] Enable or disable metrics. Defaults to `false`.
        :param pulumi.Input[str] name: [string] The domain name. Externally reachable.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ApigatewayArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An API gateway consists of the generic rules and configurations.

        ## Usage example

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ionoscloud as ionoscloud

        example = ionoscloud.Apigateway("example", metrics=True)
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        In order to import an API Gateway, you can define an empty API Gateway resource in the plan:

        resource "ionoscloud_apigateway" "example" {

        }

        The resource can be imported using the `gateway_id`, for example:

        ```sh
        $ pulumi import ionoscloud:index/apigateway:Apigateway example {gateway_id}
        ```

        :param str resource_name: The name of the resource.
        :param ApigatewayArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApigatewayArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_domains: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ApigatewayCustomDomainArgs', 'ApigatewayCustomDomainArgsDict']]]]] = None,
                 logs: Optional[pulumi.Input[bool]] = None,
                 metrics: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApigatewayArgs.__new__(ApigatewayArgs)

            __props__.__dict__["custom_domains"] = custom_domains
            __props__.__dict__["logs"] = logs
            __props__.__dict__["metrics"] = metrics
            __props__.__dict__["name"] = name
            __props__.__dict__["public_endpoint"] = None
        super(Apigateway, __self__).__init__(
            'ionoscloud:index/apigateway:Apigateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            custom_domains: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ApigatewayCustomDomainArgs', 'ApigatewayCustomDomainArgsDict']]]]] = None,
            logs: Optional[pulumi.Input[bool]] = None,
            metrics: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            public_endpoint: Optional[pulumi.Input[str]] = None) -> 'Apigateway':
        """
        Get an existing Apigateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ApigatewayCustomDomainArgs', 'ApigatewayCustomDomainArgsDict']]]] custom_domains: [list] Custom domains for the API Gateway, a list that contains elements with the following structure:
        :param pulumi.Input[bool] logs: [bool] Enable or disable logging. Defaults to `false`. **NOTE**: Central Logging must be enabled through the Logging API to enable this feature.
        :param pulumi.Input[bool] metrics: [bool] Enable or disable metrics. Defaults to `false`.
        :param pulumi.Input[str] name: [string] The domain name. Externally reachable.
        :param pulumi.Input[str] public_endpoint: [string] The public endpoint of the API Gateway.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ApigatewayState.__new__(_ApigatewayState)

        __props__.__dict__["custom_domains"] = custom_domains
        __props__.__dict__["logs"] = logs
        __props__.__dict__["metrics"] = metrics
        __props__.__dict__["name"] = name
        __props__.__dict__["public_endpoint"] = public_endpoint
        return Apigateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="customDomains")
    def custom_domains(self) -> pulumi.Output[Optional[Sequence['outputs.ApigatewayCustomDomain']]]:
        """
        [list] Custom domains for the API Gateway, a list that contains elements with the following structure:
        """
        return pulumi.get(self, "custom_domains")

    @property
    @pulumi.getter
    def logs(self) -> pulumi.Output[Optional[bool]]:
        """
        [bool] Enable or disable logging. Defaults to `false`. **NOTE**: Central Logging must be enabled through the Logging API to enable this feature.
        """
        return pulumi.get(self, "logs")

    @property
    @pulumi.getter
    def metrics(self) -> pulumi.Output[Optional[bool]]:
        """
        [bool] Enable or disable metrics. Defaults to `false`.
        """
        return pulumi.get(self, "metrics")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        [string] The domain name. Externally reachable.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="publicEndpoint")
    def public_endpoint(self) -> pulumi.Output[str]:
        """
        [string] The public endpoint of the API Gateway.
        """
        return pulumi.get(self, "public_endpoint")

