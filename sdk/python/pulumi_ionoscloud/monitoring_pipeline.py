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
from . import outputs
from ._inputs import *

__all__ = ['MonitoringPipelineArgs', 'MonitoringPipeline']

@pulumi.input_type
class MonitoringPipelineArgs:
    def __init__(__self__, *,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input['MonitoringPipelineTimeoutsArgs']] = None):
        """
        The set of arguments for constructing a MonitoringPipeline resource.
        :param pulumi.Input[str] location: [string] The location of the Monitoring pipeline. Default is `de/fra`. It can be one of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`. If this is not set and if no value is provided for the `IONOS_API_URL_MONITORING` env var, the default `location` will be: `de/fra`.
        :param pulumi.Input[str] name: [string] The name of the Monitoring pipeline.
        """
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if timeouts is not None:
            pulumi.set(__self__, "timeouts", timeouts)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The location of the Monitoring pipeline. Default is `de/fra`. It can be one of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`. If this is not set and if no value is provided for the `IONOS_API_URL_MONITORING` env var, the default `location` will be: `de/fra`.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The name of the Monitoring pipeline.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input['MonitoringPipelineTimeoutsArgs']]:
        return pulumi.get(self, "timeouts")

    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input['MonitoringPipelineTimeoutsArgs']]):
        pulumi.set(self, "timeouts", value)


@pulumi.input_type
class _MonitoringPipelineState:
    def __init__(__self__, *,
                 grafana_endpoint: Optional[pulumi.Input[str]] = None,
                 http_endpoint: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input['MonitoringPipelineTimeoutsArgs']] = None):
        """
        Input properties used for looking up and filtering MonitoringPipeline resources.
        :param pulumi.Input[str] grafana_endpoint: [string] The endpoint of the Grafana instance.
        :param pulumi.Input[str] http_endpoint: [string] The HTTP endpoint of the monitoring instance.
        :param pulumi.Input[str] key: (Sensitive)[string] The key used to connect to the monitoring pipeline.
               
               > **⚠ NOTE:** `IONOS_API_URL_MONITORING` can be used to set a custom API URL for the resource. `location` field needs to be empty, otherwise it will override the custom API URL.
        :param pulumi.Input[str] location: [string] The location of the Monitoring pipeline. Default is `de/fra`. It can be one of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`. If this is not set and if no value is provided for the `IONOS_API_URL_MONITORING` env var, the default `location` will be: `de/fra`.
        :param pulumi.Input[str] name: [string] The name of the Monitoring pipeline.
        """
        if grafana_endpoint is not None:
            pulumi.set(__self__, "grafana_endpoint", grafana_endpoint)
        if http_endpoint is not None:
            pulumi.set(__self__, "http_endpoint", http_endpoint)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if timeouts is not None:
            pulumi.set(__self__, "timeouts", timeouts)

    @property
    @pulumi.getter(name="grafanaEndpoint")
    def grafana_endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The endpoint of the Grafana instance.
        """
        return pulumi.get(self, "grafana_endpoint")

    @grafana_endpoint.setter
    def grafana_endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "grafana_endpoint", value)

    @property
    @pulumi.getter(name="httpEndpoint")
    def http_endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The HTTP endpoint of the monitoring instance.
        """
        return pulumi.get(self, "http_endpoint")

    @http_endpoint.setter
    def http_endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "http_endpoint", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        (Sensitive)[string] The key used to connect to the monitoring pipeline.

        > **⚠ NOTE:** `IONOS_API_URL_MONITORING` can be used to set a custom API URL for the resource. `location` field needs to be empty, otherwise it will override the custom API URL.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The location of the Monitoring pipeline. Default is `de/fra`. It can be one of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`. If this is not set and if no value is provided for the `IONOS_API_URL_MONITORING` env var, the default `location` will be: `de/fra`.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The name of the Monitoring pipeline.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input['MonitoringPipelineTimeoutsArgs']]:
        return pulumi.get(self, "timeouts")

    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input['MonitoringPipelineTimeoutsArgs']]):
        pulumi.set(self, "timeouts", value)


class MonitoringPipeline(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input[Union['MonitoringPipelineTimeoutsArgs', 'MonitoringPipelineTimeoutsArgsDict']]] = None,
                 __props__=None):
        """
        Manages a **Monitoring pipeline**.

        > ⚠️  Only tokens are accepted for authorization in the **monitoring_pipeline** resource. Please ensure you are using tokens as other methods will not be valid.

        ## Usage example

        ```python
        import pulumi
        import pulumi_ionoscloud as ionoscloud

        example = ionoscloud.MonitoringPipeline("example",
            location="es/vit",
            name="pipelineExample")
        ```

        **NOTE:** The default timeout for all operations is 60 minutes. If you want to change the default value, you can use `timeouts` attribute inside the resource:

        ```python
        import pulumi
        import pulumi_ionoscloud as ionoscloud

        example = ionoscloud.MonitoringPipeline("example",
            location="es/vit",
            name="pipelineExample")
        ```

        ## Import

        In order to import a Monitoring pipeline, you can define an empty Monitoring pipeline resource in the plan:

        hcl

        resource "ionoscloud_monitoring_pipeline" "example" {

        }

        The resource can be imported using the `location` and `pipeline_id`, for example:

        ```sh
        $ pulumi import ionoscloud:index/monitoringPipeline:MonitoringPipeline example location:pipeline_id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: [string] The location of the Monitoring pipeline. Default is `de/fra`. It can be one of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`. If this is not set and if no value is provided for the `IONOS_API_URL_MONITORING` env var, the default `location` will be: `de/fra`.
        :param pulumi.Input[str] name: [string] The name of the Monitoring pipeline.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[MonitoringPipelineArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a **Monitoring pipeline**.

        > ⚠️  Only tokens are accepted for authorization in the **monitoring_pipeline** resource. Please ensure you are using tokens as other methods will not be valid.

        ## Usage example

        ```python
        import pulumi
        import pulumi_ionoscloud as ionoscloud

        example = ionoscloud.MonitoringPipeline("example",
            location="es/vit",
            name="pipelineExample")
        ```

        **NOTE:** The default timeout for all operations is 60 minutes. If you want to change the default value, you can use `timeouts` attribute inside the resource:

        ```python
        import pulumi
        import pulumi_ionoscloud as ionoscloud

        example = ionoscloud.MonitoringPipeline("example",
            location="es/vit",
            name="pipelineExample")
        ```

        ## Import

        In order to import a Monitoring pipeline, you can define an empty Monitoring pipeline resource in the plan:

        hcl

        resource "ionoscloud_monitoring_pipeline" "example" {

        }

        The resource can be imported using the `location` and `pipeline_id`, for example:

        ```sh
        $ pulumi import ionoscloud:index/monitoringPipeline:MonitoringPipeline example location:pipeline_id
        ```

        :param str resource_name: The name of the resource.
        :param MonitoringPipelineArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MonitoringPipelineArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input[Union['MonitoringPipelineTimeoutsArgs', 'MonitoringPipelineTimeoutsArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MonitoringPipelineArgs.__new__(MonitoringPipelineArgs)

            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["timeouts"] = timeouts
            __props__.__dict__["grafana_endpoint"] = None
            __props__.__dict__["http_endpoint"] = None
            __props__.__dict__["key"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["key"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(MonitoringPipeline, __self__).__init__(
            'ionoscloud:index/monitoringPipeline:MonitoringPipeline',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            grafana_endpoint: Optional[pulumi.Input[str]] = None,
            http_endpoint: Optional[pulumi.Input[str]] = None,
            key: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            timeouts: Optional[pulumi.Input[Union['MonitoringPipelineTimeoutsArgs', 'MonitoringPipelineTimeoutsArgsDict']]] = None) -> 'MonitoringPipeline':
        """
        Get an existing MonitoringPipeline resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] grafana_endpoint: [string] The endpoint of the Grafana instance.
        :param pulumi.Input[str] http_endpoint: [string] The HTTP endpoint of the monitoring instance.
        :param pulumi.Input[str] key: (Sensitive)[string] The key used to connect to the monitoring pipeline.
               
               > **⚠ NOTE:** `IONOS_API_URL_MONITORING` can be used to set a custom API URL for the resource. `location` field needs to be empty, otherwise it will override the custom API URL.
        :param pulumi.Input[str] location: [string] The location of the Monitoring pipeline. Default is `de/fra`. It can be one of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`. If this is not set and if no value is provided for the `IONOS_API_URL_MONITORING` env var, the default `location` will be: `de/fra`.
        :param pulumi.Input[str] name: [string] The name of the Monitoring pipeline.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MonitoringPipelineState.__new__(_MonitoringPipelineState)

        __props__.__dict__["grafana_endpoint"] = grafana_endpoint
        __props__.__dict__["http_endpoint"] = http_endpoint
        __props__.__dict__["key"] = key
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["timeouts"] = timeouts
        return MonitoringPipeline(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="grafanaEndpoint")
    def grafana_endpoint(self) -> pulumi.Output[str]:
        """
        [string] The endpoint of the Grafana instance.
        """
        return pulumi.get(self, "grafana_endpoint")

    @property
    @pulumi.getter(name="httpEndpoint")
    def http_endpoint(self) -> pulumi.Output[str]:
        """
        [string] The HTTP endpoint of the monitoring instance.
        """
        return pulumi.get(self, "http_endpoint")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        """
        (Sensitive)[string] The key used to connect to the monitoring pipeline.

        > **⚠ NOTE:** `IONOS_API_URL_MONITORING` can be used to set a custom API URL for the resource. `location` field needs to be empty, otherwise it will override the custom API URL.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        [string] The location of the Monitoring pipeline. Default is `de/fra`. It can be one of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`. If this is not set and if no value is provided for the `IONOS_API_URL_MONITORING` env var, the default `location` will be: `de/fra`.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        [string] The name of the Monitoring pipeline.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional['outputs.MonitoringPipelineTimeouts']]:
        return pulumi.get(self, "timeouts")

