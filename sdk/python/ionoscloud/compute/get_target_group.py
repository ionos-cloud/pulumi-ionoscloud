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

__all__ = [
    'GetTargetGroupResult',
    'AwaitableGetTargetGroupResult',
    'get_target_group',
    'get_target_group_output',
]

@pulumi.output_type
class GetTargetGroupResult:
    """
    A collection of values returned by getTargetGroup.
    """
    def __init__(__self__, algorithm=None, health_checks=None, http_health_checks=None, id=None, name=None, partial_match=None, protocol=None, protocol_version=None, targets=None):
        if algorithm and not isinstance(algorithm, str):
            raise TypeError("Expected argument 'algorithm' to be a str")
        pulumi.set(__self__, "algorithm", algorithm)
        if health_checks and not isinstance(health_checks, list):
            raise TypeError("Expected argument 'health_checks' to be a list")
        pulumi.set(__self__, "health_checks", health_checks)
        if http_health_checks and not isinstance(http_health_checks, list):
            raise TypeError("Expected argument 'http_health_checks' to be a list")
        pulumi.set(__self__, "http_health_checks", http_health_checks)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if partial_match and not isinstance(partial_match, bool):
            raise TypeError("Expected argument 'partial_match' to be a bool")
        pulumi.set(__self__, "partial_match", partial_match)
        if protocol and not isinstance(protocol, str):
            raise TypeError("Expected argument 'protocol' to be a str")
        pulumi.set(__self__, "protocol", protocol)
        if protocol_version and not isinstance(protocol_version, str):
            raise TypeError("Expected argument 'protocol_version' to be a str")
        pulumi.set(__self__, "protocol_version", protocol_version)
        if targets and not isinstance(targets, list):
            raise TypeError("Expected argument 'targets' to be a list")
        pulumi.set(__self__, "targets", targets)

    @property
    @pulumi.getter
    def algorithm(self) -> str:
        """
        Balancing algorithm.
        """
        return pulumi.get(self, "algorithm")

    @property
    @pulumi.getter(name="healthChecks")
    def health_checks(self) -> Sequence['outputs.GetTargetGroupHealthCheckResult']:
        """
        Health check attributes for Target Group.
        """
        return pulumi.get(self, "health_checks")

    @property
    @pulumi.getter(name="httpHealthChecks")
    def http_health_checks(self) -> Sequence['outputs.GetTargetGroupHttpHealthCheckResult']:
        """
        Http health check attributes for Target Group
        """
        return pulumi.get(self, "http_health_checks")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The Id of that Target group
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of that Target Group.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partialMatch")
    def partial_match(self) -> Optional[bool]:
        return pulumi.get(self, "partial_match")

    @property
    @pulumi.getter
    def protocol(self) -> str:
        """
        Balancing protocol.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="protocolVersion")
    def protocol_version(self) -> str:
        """
        The forwarding protocol version. Value is ignored when protocol is not 'HTTP'.
        """
        return pulumi.get(self, "protocol_version")

    @property
    @pulumi.getter
    def targets(self) -> Sequence['outputs.GetTargetGroupTargetResult']:
        """
        Array of items in the collection
        """
        return pulumi.get(self, "targets")


class AwaitableGetTargetGroupResult(GetTargetGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTargetGroupResult(
            algorithm=self.algorithm,
            health_checks=self.health_checks,
            http_health_checks=self.http_health_checks,
            id=self.id,
            name=self.name,
            partial_match=self.partial_match,
            protocol=self.protocol,
            protocol_version=self.protocol_version,
            targets=self.targets)


def get_target_group(id: Optional[str] = None,
                     name: Optional[str] = None,
                     partial_match: Optional[bool] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTargetGroupResult:
    """
    The **Target Group** data source can be used to search for and return an existing Application Load Balancer Target Group.
    You can provide a string for the name parameter which will be compared with provisioned Application Load Balancer Target Groups.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search and make sure that your resources have unique names.

    ## Example Usage

    ### By Id
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.compute.get_target_group(id="target_group_id")
    ```

    ### By Name
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.compute.get_target_group(name="Target Group Example")
    ```

    ### By Name with Partial Match
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.compute.get_target_group(name="Example",
        partial_match=True)
    ```


    :param str id: ID of the target group you want to search for.
    :param str name: Name of an existing target group that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
    :param bool partial_match: Whether partial matching is allowed or not when using name argument. Default value is false.
           
           Either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['partialMatch'] = partial_match
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:compute/getTargetGroup:getTargetGroup', __args__, opts=opts, typ=GetTargetGroupResult).value

    return AwaitableGetTargetGroupResult(
        algorithm=pulumi.get(__ret__, 'algorithm'),
        health_checks=pulumi.get(__ret__, 'health_checks'),
        http_health_checks=pulumi.get(__ret__, 'http_health_checks'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        partial_match=pulumi.get(__ret__, 'partial_match'),
        protocol=pulumi.get(__ret__, 'protocol'),
        protocol_version=pulumi.get(__ret__, 'protocol_version'),
        targets=pulumi.get(__ret__, 'targets'))
def get_target_group_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                            name: Optional[pulumi.Input[Optional[str]]] = None,
                            partial_match: Optional[pulumi.Input[Optional[bool]]] = None,
                            opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetTargetGroupResult]:
    """
    The **Target Group** data source can be used to search for and return an existing Application Load Balancer Target Group.
    You can provide a string for the name parameter which will be compared with provisioned Application Load Balancer Target Groups.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search and make sure that your resources have unique names.

    ## Example Usage

    ### By Id
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.compute.get_target_group(id="target_group_id")
    ```

    ### By Name
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.compute.get_target_group(name="Target Group Example")
    ```

    ### By Name with Partial Match
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.compute.get_target_group(name="Example",
        partial_match=True)
    ```


    :param str id: ID of the target group you want to search for.
    :param str name: Name of an existing target group that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
    :param bool partial_match: Whether partial matching is allowed or not when using name argument. Default value is false.
           
           Either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['partialMatch'] = partial_match
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:compute/getTargetGroup:getTargetGroup', __args__, opts=opts, typ=GetTargetGroupResult)
    return __ret__.apply(lambda __response__: GetTargetGroupResult(
        algorithm=pulumi.get(__response__, 'algorithm'),
        health_checks=pulumi.get(__response__, 'health_checks'),
        http_health_checks=pulumi.get(__response__, 'http_health_checks'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        partial_match=pulumi.get(__response__, 'partial_match'),
        protocol=pulumi.get(__response__, 'protocol'),
        protocol_version=pulumi.get(__response__, 'protocol_version'),
        targets=pulumi.get(__response__, 'targets')))
