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

__all__ = ['RouteArgs', 'Route']

@pulumi.input_type
class RouteArgs:
    def __init__(__self__, *,
                 gateway_id: pulumi.Input[str],
                 methods: pulumi.Input[Sequence[pulumi.Input[str]]],
                 paths: pulumi.Input[Sequence[pulumi.Input[str]]],
                 upstreams: pulumi.Input[Sequence[pulumi.Input['RouteUpstreamArgs']]],
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 websocket: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Route resource.
        :param pulumi.Input[str] gateway_id: [string] The ID of the API Gateway that the route belongs to.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] methods: [list] The HTTP methods that the route should match. Minimum items: 1. Possible values: `GET`,
               `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, `HEAD`, `CONNECT`, `TRACE`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] paths: [list] The paths that the route should match. Minimum items: 1.
        :param pulumi.Input[Sequence[pulumi.Input['RouteUpstreamArgs']]] upstreams: Upstreams information of the API Gateway Route. Minimum items: 1.
        :param pulumi.Input[str] name: [string] Name of the API Gateway Route. Only alphanumeric characters are allowed.
        :param pulumi.Input[str] type: [string] This field specifies the protocol used by the ingress to route traffic to the backend
               service. Default value: `http`.
        :param pulumi.Input[bool] websocket: [bool] To enable websocket support. Default value: `false`.
        """
        pulumi.set(__self__, "gateway_id", gateway_id)
        pulumi.set(__self__, "methods", methods)
        pulumi.set(__self__, "paths", paths)
        pulumi.set(__self__, "upstreams", upstreams)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if websocket is not None:
            pulumi.set(__self__, "websocket", websocket)

    @property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> pulumi.Input[str]:
        """
        [string] The ID of the API Gateway that the route belongs to.
        """
        return pulumi.get(self, "gateway_id")

    @gateway_id.setter
    def gateway_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "gateway_id", value)

    @property
    @pulumi.getter
    def methods(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        [list] The HTTP methods that the route should match. Minimum items: 1. Possible values: `GET`,
        `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, `HEAD`, `CONNECT`, `TRACE`.
        """
        return pulumi.get(self, "methods")

    @methods.setter
    def methods(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "methods", value)

    @property
    @pulumi.getter
    def paths(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        [list] The paths that the route should match. Minimum items: 1.
        """
        return pulumi.get(self, "paths")

    @paths.setter
    def paths(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "paths", value)

    @property
    @pulumi.getter
    def upstreams(self) -> pulumi.Input[Sequence[pulumi.Input['RouteUpstreamArgs']]]:
        """
        Upstreams information of the API Gateway Route. Minimum items: 1.
        """
        return pulumi.get(self, "upstreams")

    @upstreams.setter
    def upstreams(self, value: pulumi.Input[Sequence[pulumi.Input['RouteUpstreamArgs']]]):
        pulumi.set(self, "upstreams", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Name of the API Gateway Route. Only alphanumeric characters are allowed.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        [string] This field specifies the protocol used by the ingress to route traffic to the backend
        service. Default value: `http`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def websocket(self) -> Optional[pulumi.Input[bool]]:
        """
        [bool] To enable websocket support. Default value: `false`.
        """
        return pulumi.get(self, "websocket")

    @websocket.setter
    def websocket(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "websocket", value)


@pulumi.input_type
class _RouteState:
    def __init__(__self__, *,
                 gateway_id: Optional[pulumi.Input[str]] = None,
                 methods: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 paths: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 upstreams: Optional[pulumi.Input[Sequence[pulumi.Input['RouteUpstreamArgs']]]] = None,
                 websocket: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering Route resources.
        :param pulumi.Input[str] gateway_id: [string] The ID of the API Gateway that the route belongs to.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] methods: [list] The HTTP methods that the route should match. Minimum items: 1. Possible values: `GET`,
               `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, `HEAD`, `CONNECT`, `TRACE`.
        :param pulumi.Input[str] name: [string] Name of the API Gateway Route. Only alphanumeric characters are allowed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] paths: [list] The paths that the route should match. Minimum items: 1.
        :param pulumi.Input[str] type: [string] This field specifies the protocol used by the ingress to route traffic to the backend
               service. Default value: `http`.
        :param pulumi.Input[Sequence[pulumi.Input['RouteUpstreamArgs']]] upstreams: Upstreams information of the API Gateway Route. Minimum items: 1.
        :param pulumi.Input[bool] websocket: [bool] To enable websocket support. Default value: `false`.
        """
        if gateway_id is not None:
            pulumi.set(__self__, "gateway_id", gateway_id)
        if methods is not None:
            pulumi.set(__self__, "methods", methods)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if paths is not None:
            pulumi.set(__self__, "paths", paths)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if upstreams is not None:
            pulumi.set(__self__, "upstreams", upstreams)
        if websocket is not None:
            pulumi.set(__self__, "websocket", websocket)

    @property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The ID of the API Gateway that the route belongs to.
        """
        return pulumi.get(self, "gateway_id")

    @gateway_id.setter
    def gateway_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gateway_id", value)

    @property
    @pulumi.getter
    def methods(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        [list] The HTTP methods that the route should match. Minimum items: 1. Possible values: `GET`,
        `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, `HEAD`, `CONNECT`, `TRACE`.
        """
        return pulumi.get(self, "methods")

    @methods.setter
    def methods(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "methods", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Name of the API Gateway Route. Only alphanumeric characters are allowed.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def paths(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        [list] The paths that the route should match. Minimum items: 1.
        """
        return pulumi.get(self, "paths")

    @paths.setter
    def paths(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "paths", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        [string] This field specifies the protocol used by the ingress to route traffic to the backend
        service. Default value: `http`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def upstreams(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RouteUpstreamArgs']]]]:
        """
        Upstreams information of the API Gateway Route. Minimum items: 1.
        """
        return pulumi.get(self, "upstreams")

    @upstreams.setter
    def upstreams(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RouteUpstreamArgs']]]]):
        pulumi.set(self, "upstreams", value)

    @property
    @pulumi.getter
    def websocket(self) -> Optional[pulumi.Input[bool]]:
        """
        [bool] To enable websocket support. Default value: `false`.
        """
        return pulumi.get(self, "websocket")

    @websocket.setter
    def websocket(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "websocket", value)


class Route(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 gateway_id: Optional[pulumi.Input[str]] = None,
                 methods: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 paths: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 upstreams: Optional[pulumi.Input[Sequence[pulumi.Input[Union['RouteUpstreamArgs', 'RouteUpstreamArgsDict']]]]] = None,
                 websocket: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Manages an **API Gateway Route** on IonosCloud.

        ## Example Usage

        This resource will create an operational API Gateway Route. After this section completes, the provisioner can be called.

        ```python
        import pulumi
        import ionoscloud as ionoscloud

        example = ionoscloud.apigateway.Apigateway("example",
            name="example-gateway",
            metrics=True,
            custom_domains=[
                {
                    "name": "example.com",
                    "certificate_id": "00000000-0000-0000-0000-000000000000",
                },
                {
                    "name": "example.org",
                    "certificate_id": "00000000-0000-0000-0000-000000000000",
                },
            ])
        apigateway_route = ionoscloud.apigateway.Route("apigateway_route",
            name="apigateway-route",
            type="http",
            paths=[
                "/foo/*",
                "/bar",
            ],
            methods=[
                "GET",
                "POST",
            ],
            websocket=False,
            upstreams=[{
                "scheme": "http",
                "loadbalancer": "roundrobin",
                "host": "example.com",
                "port": 80,
                "weight": 100,
            }],
            gateway_id=example.id)
        ```

        ## Import

        API Gateway route can be imported using the `apigateway route id`:

        ```sh
        $ pulumi import ionoscloud:apigateway/route:Route myroute {apigateway uuid}:{apigateway route uuid}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] gateway_id: [string] The ID of the API Gateway that the route belongs to.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] methods: [list] The HTTP methods that the route should match. Minimum items: 1. Possible values: `GET`,
               `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, `HEAD`, `CONNECT`, `TRACE`.
        :param pulumi.Input[str] name: [string] Name of the API Gateway Route. Only alphanumeric characters are allowed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] paths: [list] The paths that the route should match. Minimum items: 1.
        :param pulumi.Input[str] type: [string] This field specifies the protocol used by the ingress to route traffic to the backend
               service. Default value: `http`.
        :param pulumi.Input[Sequence[pulumi.Input[Union['RouteUpstreamArgs', 'RouteUpstreamArgsDict']]]] upstreams: Upstreams information of the API Gateway Route. Minimum items: 1.
        :param pulumi.Input[bool] websocket: [bool] To enable websocket support. Default value: `false`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RouteArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an **API Gateway Route** on IonosCloud.

        ## Example Usage

        This resource will create an operational API Gateway Route. After this section completes, the provisioner can be called.

        ```python
        import pulumi
        import ionoscloud as ionoscloud

        example = ionoscloud.apigateway.Apigateway("example",
            name="example-gateway",
            metrics=True,
            custom_domains=[
                {
                    "name": "example.com",
                    "certificate_id": "00000000-0000-0000-0000-000000000000",
                },
                {
                    "name": "example.org",
                    "certificate_id": "00000000-0000-0000-0000-000000000000",
                },
            ])
        apigateway_route = ionoscloud.apigateway.Route("apigateway_route",
            name="apigateway-route",
            type="http",
            paths=[
                "/foo/*",
                "/bar",
            ],
            methods=[
                "GET",
                "POST",
            ],
            websocket=False,
            upstreams=[{
                "scheme": "http",
                "loadbalancer": "roundrobin",
                "host": "example.com",
                "port": 80,
                "weight": 100,
            }],
            gateway_id=example.id)
        ```

        ## Import

        API Gateway route can be imported using the `apigateway route id`:

        ```sh
        $ pulumi import ionoscloud:apigateway/route:Route myroute {apigateway uuid}:{apigateway route uuid}
        ```

        :param str resource_name: The name of the resource.
        :param RouteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RouteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 gateway_id: Optional[pulumi.Input[str]] = None,
                 methods: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 paths: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 upstreams: Optional[pulumi.Input[Sequence[pulumi.Input[Union['RouteUpstreamArgs', 'RouteUpstreamArgsDict']]]]] = None,
                 websocket: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RouteArgs.__new__(RouteArgs)

            if gateway_id is None and not opts.urn:
                raise TypeError("Missing required property 'gateway_id'")
            __props__.__dict__["gateway_id"] = gateway_id
            if methods is None and not opts.urn:
                raise TypeError("Missing required property 'methods'")
            __props__.__dict__["methods"] = methods
            __props__.__dict__["name"] = name
            if paths is None and not opts.urn:
                raise TypeError("Missing required property 'paths'")
            __props__.__dict__["paths"] = paths
            __props__.__dict__["type"] = type
            if upstreams is None and not opts.urn:
                raise TypeError("Missing required property 'upstreams'")
            __props__.__dict__["upstreams"] = upstreams
            __props__.__dict__["websocket"] = websocket
        super(Route, __self__).__init__(
            'ionoscloud:apigateway/route:Route',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            gateway_id: Optional[pulumi.Input[str]] = None,
            methods: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            paths: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            type: Optional[pulumi.Input[str]] = None,
            upstreams: Optional[pulumi.Input[Sequence[pulumi.Input[Union['RouteUpstreamArgs', 'RouteUpstreamArgsDict']]]]] = None,
            websocket: Optional[pulumi.Input[bool]] = None) -> 'Route':
        """
        Get an existing Route resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] gateway_id: [string] The ID of the API Gateway that the route belongs to.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] methods: [list] The HTTP methods that the route should match. Minimum items: 1. Possible values: `GET`,
               `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, `HEAD`, `CONNECT`, `TRACE`.
        :param pulumi.Input[str] name: [string] Name of the API Gateway Route. Only alphanumeric characters are allowed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] paths: [list] The paths that the route should match. Minimum items: 1.
        :param pulumi.Input[str] type: [string] This field specifies the protocol used by the ingress to route traffic to the backend
               service. Default value: `http`.
        :param pulumi.Input[Sequence[pulumi.Input[Union['RouteUpstreamArgs', 'RouteUpstreamArgsDict']]]] upstreams: Upstreams information of the API Gateway Route. Minimum items: 1.
        :param pulumi.Input[bool] websocket: [bool] To enable websocket support. Default value: `false`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RouteState.__new__(_RouteState)

        __props__.__dict__["gateway_id"] = gateway_id
        __props__.__dict__["methods"] = methods
        __props__.__dict__["name"] = name
        __props__.__dict__["paths"] = paths
        __props__.__dict__["type"] = type
        __props__.__dict__["upstreams"] = upstreams
        __props__.__dict__["websocket"] = websocket
        return Route(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> pulumi.Output[str]:
        """
        [string] The ID of the API Gateway that the route belongs to.
        """
        return pulumi.get(self, "gateway_id")

    @property
    @pulumi.getter
    def methods(self) -> pulumi.Output[Sequence[str]]:
        """
        [list] The HTTP methods that the route should match. Minimum items: 1. Possible values: `GET`,
        `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, `HEAD`, `CONNECT`, `TRACE`.
        """
        return pulumi.get(self, "methods")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        [string] Name of the API Gateway Route. Only alphanumeric characters are allowed.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def paths(self) -> pulumi.Output[Sequence[str]]:
        """
        [list] The paths that the route should match. Minimum items: 1.
        """
        return pulumi.get(self, "paths")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        [string] This field specifies the protocol used by the ingress to route traffic to the backend
        service. Default value: `http`.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def upstreams(self) -> pulumi.Output[Sequence['outputs.RouteUpstream']]:
        """
        Upstreams information of the API Gateway Route. Minimum items: 1.
        """
        return pulumi.get(self, "upstreams")

    @property
    @pulumi.getter
    def websocket(self) -> pulumi.Output[Optional[bool]]:
        """
        [bool] To enable websocket support. Default value: `false`.
        """
        return pulumi.get(self, "websocket")

