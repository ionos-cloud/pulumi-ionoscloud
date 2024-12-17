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
    'GetApigatewayResult',
    'AwaitableGetApigatewayResult',
    'get_apigateway',
    'get_apigateway_output',
]

warnings.warn("""ionoscloud.index/getapigateway.getApigateway has been deprecated in favor of ionoscloud.apigateway/getapigateway.getApigateway""", DeprecationWarning)

@pulumi.output_type
class GetApigatewayResult:
    """
    A collection of values returned by getApigateway.
    """
    def __init__(__self__, custom_domains=None, id=None, logs=None, metrics=None, name=None, partial_match=None, public_endpoint=None):
        if custom_domains and not isinstance(custom_domains, list):
            raise TypeError("Expected argument 'custom_domains' to be a list")
        pulumi.set(__self__, "custom_domains", custom_domains)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if logs and not isinstance(logs, bool):
            raise TypeError("Expected argument 'logs' to be a bool")
        pulumi.set(__self__, "logs", logs)
        if metrics and not isinstance(metrics, bool):
            raise TypeError("Expected argument 'metrics' to be a bool")
        pulumi.set(__self__, "metrics", metrics)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if partial_match and not isinstance(partial_match, bool):
            raise TypeError("Expected argument 'partial_match' to be a bool")
        pulumi.set(__self__, "partial_match", partial_match)
        if public_endpoint and not isinstance(public_endpoint, str):
            raise TypeError("Expected argument 'public_endpoint' to be a str")
        pulumi.set(__self__, "public_endpoint", public_endpoint)

    @property
    @pulumi.getter(name="customDomains")
    def custom_domains(self) -> Sequence['outputs.GetApigatewayCustomDomainResult']:
        return pulumi.get(self, "custom_domains")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def logs(self) -> bool:
        return pulumi.get(self, "logs")

    @property
    @pulumi.getter
    def metrics(self) -> bool:
        return pulumi.get(self, "metrics")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partialMatch")
    def partial_match(self) -> Optional[bool]:
        return pulumi.get(self, "partial_match")

    @property
    @pulumi.getter(name="publicEndpoint")
    def public_endpoint(self) -> str:
        return pulumi.get(self, "public_endpoint")


class AwaitableGetApigatewayResult(GetApigatewayResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApigatewayResult(
            custom_domains=self.custom_domains,
            id=self.id,
            logs=self.logs,
            metrics=self.metrics,
            name=self.name,
            partial_match=self.partial_match,
            public_endpoint=self.public_endpoint)


def get_apigateway(id: Optional[str] = None,
                   name: Optional[str] = None,
                   partial_match: Optional[bool] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApigatewayResult:
    """
<<<<<<< HEAD
    The **API Gateway data source** can be used to search for and return an existing API Gateway.
    You can provide a string for the name parameter which will be compared with provisioned API Gateways.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage

    ### By Name

    Needs to have the resource be previously created, or a depends_on clause to ensure that the resource is created before
    this data source is called.

    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.apigateway.get_apigateway(name="example-apigateway")
    ```


    :param str id: ID of an existing API Gateway that you want to search for.
    :param str name: Name of an existing API Gateway that you want to search for.
    :param bool partial_match: Whether partial matching is allowed or not when using the name filter. Defaults to `false`.
=======
    Use this data source to access information about an existing resource.
>>>>>>> main
    """
    pulumi.log.warn("""get_apigateway is deprecated: ionoscloud.index/getapigateway.getApigateway has been deprecated in favor of ionoscloud.apigateway/getapigateway.getApigateway""")
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['partialMatch'] = partial_match
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getApigateway:getApigateway', __args__, opts=opts, typ=GetApigatewayResult).value

    return AwaitableGetApigatewayResult(
        custom_domains=pulumi.get(__ret__, 'custom_domains'),
        id=pulumi.get(__ret__, 'id'),
        logs=pulumi.get(__ret__, 'logs'),
        metrics=pulumi.get(__ret__, 'metrics'),
        name=pulumi.get(__ret__, 'name'),
        partial_match=pulumi.get(__ret__, 'partial_match'),
        public_endpoint=pulumi.get(__ret__, 'public_endpoint'))
def get_apigateway_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                          name: Optional[pulumi.Input[Optional[str]]] = None,
                          partial_match: Optional[pulumi.Input[Optional[bool]]] = None,
                          opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetApigatewayResult]:
    """
<<<<<<< HEAD
    The **API Gateway data source** can be used to search for and return an existing API Gateway.
    You can provide a string for the name parameter which will be compared with provisioned API Gateways.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage

    ### By Name

    Needs to have the resource be previously created, or a depends_on clause to ensure that the resource is created before
    this data source is called.

    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.apigateway.get_apigateway(name="example-apigateway")
    ```


    :param str id: ID of an existing API Gateway that you want to search for.
    :param str name: Name of an existing API Gateway that you want to search for.
    :param bool partial_match: Whether partial matching is allowed or not when using the name filter. Defaults to `false`.
    """
    pulumi.log.warn("""get_apigateway is deprecated: ionoscloud.index/getapigateway.getApigateway has been deprecated in favor of ionoscloud.apigateway/getapigateway.getApigateway""")
=======
    Use this data source to access information about an existing resource.
    """
>>>>>>> main
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['partialMatch'] = partial_match
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:index/getApigateway:getApigateway', __args__, opts=opts, typ=GetApigatewayResult)
    return __ret__.apply(lambda __response__: GetApigatewayResult(
        custom_domains=pulumi.get(__response__, 'custom_domains'),
        id=pulumi.get(__response__, 'id'),
        logs=pulumi.get(__response__, 'logs'),
        metrics=pulumi.get(__response__, 'metrics'),
        name=pulumi.get(__response__, 'name'),
        partial_match=pulumi.get(__response__, 'partial_match'),
        public_endpoint=pulumi.get(__response__, 'public_endpoint')))
