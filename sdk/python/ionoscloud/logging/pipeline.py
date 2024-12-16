# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['PipelineArgs', 'Pipeline']

@pulumi.input_type
class PipelineArgs:
    def __init__(__self__, *,
                 logs: pulumi.Input[Sequence[pulumi.Input['PipelineLogArgs']]],
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Pipeline resource.
        :param pulumi.Input[Sequence[pulumi.Input['PipelineLogArgs']]] logs: [list] Pipeline logs, a list that contains elements with the following structure:
        :param pulumi.Input[str] location: [string] The location of the Logging pipeline. Default: `de/txl` One of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`.
        :param pulumi.Input[str] name: [string] The name of the Logging pipeline.
        """
        pulumi.set(__self__, "logs", logs)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def logs(self) -> pulumi.Input[Sequence[pulumi.Input['PipelineLogArgs']]]:
        """
        [list] Pipeline logs, a list that contains elements with the following structure:
        """
        return pulumi.get(self, "logs")

    @logs.setter
    def logs(self, value: pulumi.Input[Sequence[pulumi.Input['PipelineLogArgs']]]):
        pulumi.set(self, "logs", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The location of the Logging pipeline. Default: `de/txl` One of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The name of the Logging pipeline.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _PipelineState:
    def __init__(__self__, *,
                 grafana_address: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 logs: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineLogArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Pipeline resources.
        :param pulumi.Input[str] grafana_address: [string] The address of the client's grafana instance.
        :param pulumi.Input[str] location: [string] The location of the Logging pipeline. Default: `de/txl` One of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`.
        :param pulumi.Input[Sequence[pulumi.Input['PipelineLogArgs']]] logs: [list] Pipeline logs, a list that contains elements with the following structure:
        :param pulumi.Input[str] name: [string] The name of the Logging pipeline.
        """
        if grafana_address is not None:
            pulumi.set(__self__, "grafana_address", grafana_address)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if logs is not None:
            pulumi.set(__self__, "logs", logs)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="grafanaAddress")
    def grafana_address(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The address of the client's grafana instance.
        """
        return pulumi.get(self, "grafana_address")

    @grafana_address.setter
    def grafana_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "grafana_address", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The location of the Logging pipeline. Default: `de/txl` One of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def logs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PipelineLogArgs']]]]:
        """
        [list] Pipeline logs, a list that contains elements with the following structure:
        """
        return pulumi.get(self, "logs")

    @logs.setter
    def logs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineLogArgs']]]]):
        pulumi.set(self, "logs", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The name of the Logging pipeline.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class Pipeline(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 logs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineLogArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Import

        In order to import a Logging pipeline, you can define an empty Logging pipeline resource in the plan:

        hcl

        resource "ionoscloud_logging_pipeline" "example" {

        }

        The resource can be imported using the `location` and `pipeline_id`, for example:

        ```sh
        $ pulumi import ionoscloud:logging/pipeline:Pipeline example {location}:{pipeline_id}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: [string] The location of the Logging pipeline. Default: `de/txl` One of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineLogArgs']]]] logs: [list] Pipeline logs, a list that contains elements with the following structure:
        :param pulumi.Input[str] name: [string] The name of the Logging pipeline.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PipelineArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        In order to import a Logging pipeline, you can define an empty Logging pipeline resource in the plan:

        hcl

        resource "ionoscloud_logging_pipeline" "example" {

        }

        The resource can be imported using the `location` and `pipeline_id`, for example:

        ```sh
        $ pulumi import ionoscloud:logging/pipeline:Pipeline example {location}:{pipeline_id}
        ```

        :param str resource_name: The name of the resource.
        :param PipelineArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PipelineArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 logs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineLogArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PipelineArgs.__new__(PipelineArgs)

            __props__.__dict__["location"] = location
            if logs is None and not opts.urn:
                raise TypeError("Missing required property 'logs'")
            __props__.__dict__["logs"] = logs
            __props__.__dict__["name"] = name
            __props__.__dict__["grafana_address"] = None
        super(Pipeline, __self__).__init__(
            'ionoscloud:logging/pipeline:Pipeline',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            grafana_address: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            logs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineLogArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'Pipeline':
        """
        Get an existing Pipeline resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] grafana_address: [string] The address of the client's grafana instance.
        :param pulumi.Input[str] location: [string] The location of the Logging pipeline. Default: `de/txl` One of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineLogArgs']]]] logs: [list] Pipeline logs, a list that contains elements with the following structure:
        :param pulumi.Input[str] name: [string] The name of the Logging pipeline.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PipelineState.__new__(_PipelineState)

        __props__.__dict__["grafana_address"] = grafana_address
        __props__.__dict__["location"] = location
        __props__.__dict__["logs"] = logs
        __props__.__dict__["name"] = name
        return Pipeline(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="grafanaAddress")
    def grafana_address(self) -> pulumi.Output[str]:
        """
        [string] The address of the client's grafana instance.
        """
        return pulumi.get(self, "grafana_address")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        [string] The location of the Logging pipeline. Default: `de/txl` One of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def logs(self) -> pulumi.Output[Sequence['outputs.PipelineLog']]:
        """
        [list] Pipeline logs, a list that contains elements with the following structure:
        """
        return pulumi.get(self, "logs")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        [string] The name of the Logging pipeline.
        """
        return pulumi.get(self, "name")

