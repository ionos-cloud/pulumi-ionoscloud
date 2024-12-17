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

__all__ = [
    'GetApigatewayRouteResult',
    'AwaitableGetApigatewayRouteResult',
    'get_apigateway_route',
    'get_apigateway_route_output',
]

warnings.warn("""ionoscloud.index/getapigatewayroute.getApigatewayRoute has been deprecated in favor of ionoscloud.apigateway/getroute.getRoute""", DeprecationWarning)

@pulumi.output_type
class GetApigatewayRouteResult:
    """
    A collection of values returned by getApigatewayRoute.
    """
    def __init__(__self__, gateway_id=None, id=None, methods=None, name=None, partial_match=None, paths=None, type=None, upstreams=None, websocket=None):
        if gateway_id and not isinstance(gateway_id, str):
            raise TypeError("Expected argument 'gateway_id' to be a str")
        pulumi.set(__self__, "gateway_id", gateway_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if methods and not isinstance(methods, list):
            raise TypeError("Expected argument 'methods' to be a list")
        pulumi.set(__self__, "methods", methods)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if partial_match and not isinstance(partial_match, bool):
            raise TypeError("Expected argument 'partial_match' to be a bool")
        pulumi.set(__self__, "partial_match", partial_match)
        if paths and not isinstance(paths, list):
            raise TypeError("Expected argument 'paths' to be a list")
        pulumi.set(__self__, "paths", paths)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if upstreams and not isinstance(upstreams, list):
            raise TypeError("Expected argument 'upstreams' to be a list")
        pulumi.set(__self__, "upstreams", upstreams)
        if websocket and not isinstance(websocket, bool):
            raise TypeError("Expected argument 'websocket' to be a bool")
        pulumi.set(__self__, "websocket", websocket)

    @property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> str:
        return pulumi.get(self, "gateway_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        ID of the API Gateway Route.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def methods(self) -> Sequence[str]:
        """
        The HTTP methods that the route should match.
        """
        return pulumi.get(self, "methods")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the API Gateway Route.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partialMatch")
    def partial_match(self) -> Optional[bool]:
        return pulumi.get(self, "partial_match")

    @property
    @pulumi.getter
    def paths(self) -> Sequence[str]:
        """
        The paths that the route should match.
        """
        return pulumi.get(self, "paths")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        This field specifies the protocol used by the ingress to route traffic to the backend service.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def upstreams(self) -> Sequence['outputs.GetApigatewayRouteUpstreamResult']:
        return pulumi.get(self, "upstreams")

    @property
    @pulumi.getter
    def websocket(self) -> bool:
        """
        Shows whether websocket support is enabled or disabled.
        """
        return pulumi.get(self, "websocket")


class AwaitableGetApigatewayRouteResult(GetApigatewayRouteResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApigatewayRouteResult(
            gateway_id=self.gateway_id,
            id=self.id,
            methods=self.methods,
            name=self.name,
            partial_match=self.partial_match,
            paths=self.paths,
            type=self.type,
            upstreams=self.upstreams,
            websocket=self.websocket)


def get_apigateway_route(gateway_id: Optional[str] = None,
                         id: Optional[str] = None,
                         name: Optional[str] = None,
                         partial_match: Optional[bool] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApigatewayRouteResult:
    """
    The **API Gateway Route data source** can be used to search for and return an existing API Gateway route.
    You can provide a string for the name parameter which will be compared with provisioned API Gateway routes.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage


    :param str gateway_id: The ID of the API Gateway that the route belongs to.
    :param str id: ID of an existing API Gateway Route that you want to search for.
    :param str name: Name of an existing API Gateway Route that you want to search for.
    """
    pulumi.log.warn("""get_apigateway_route is deprecated: ionoscloud.index/getapigatewayroute.getApigatewayRoute has been deprecated in favor of ionoscloud.apigateway/getroute.getRoute""")
    __args__ = dict()
    __args__['gatewayId'] = gateway_id
    __args__['id'] = id
    __args__['name'] = name
    __args__['partialMatch'] = partial_match
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getApigatewayRoute:getApigatewayRoute', __args__, opts=opts, typ=GetApigatewayRouteResult).value

    return AwaitableGetApigatewayRouteResult(
        gateway_id=pulumi.get(__ret__, 'gateway_id'),
        id=pulumi.get(__ret__, 'id'),
        methods=pulumi.get(__ret__, 'methods'),
        name=pulumi.get(__ret__, 'name'),
        partial_match=pulumi.get(__ret__, 'partial_match'),
        paths=pulumi.get(__ret__, 'paths'),
        type=pulumi.get(__ret__, 'type'),
        upstreams=pulumi.get(__ret__, 'upstreams'),
        websocket=pulumi.get(__ret__, 'websocket'))
def get_apigateway_route_output(gateway_id: Optional[pulumi.Input[str]] = None,
                                id: Optional[pulumi.Input[Optional[str]]] = None,
                                name: Optional[pulumi.Input[Optional[str]]] = None,
                                partial_match: Optional[pulumi.Input[Optional[bool]]] = None,
                                opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetApigatewayRouteResult]:
    """
    The **API Gateway Route data source** can be used to search for and return an existing API Gateway route.
    You can provide a string for the name parameter which will be compared with provisioned API Gateway routes.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage


    :param str gateway_id: The ID of the API Gateway that the route belongs to.
    :param str id: ID of an existing API Gateway Route that you want to search for.
    :param str name: Name of an existing API Gateway Route that you want to search for.
    """
    pulumi.log.warn("""get_apigateway_route is deprecated: ionoscloud.index/getapigatewayroute.getApigatewayRoute has been deprecated in favor of ionoscloud.apigateway/getroute.getRoute""")
    __args__ = dict()
    __args__['gatewayId'] = gateway_id
    __args__['id'] = id
    __args__['name'] = name
    __args__['partialMatch'] = partial_match
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:index/getApigatewayRoute:getApigatewayRoute', __args__, opts=opts, typ=GetApigatewayRouteResult)
    return __ret__.apply(lambda __response__: GetApigatewayRouteResult(
        gateway_id=pulumi.get(__response__, 'gateway_id'),
        id=pulumi.get(__response__, 'id'),
        methods=pulumi.get(__response__, 'methods'),
        name=pulumi.get(__response__, 'name'),
        partial_match=pulumi.get(__response__, 'partial_match'),
        paths=pulumi.get(__response__, 'paths'),
        type=pulumi.get(__response__, 'type'),
        upstreams=pulumi.get(__response__, 'upstreams'),
        websocket=pulumi.get(__response__, 'websocket')))
