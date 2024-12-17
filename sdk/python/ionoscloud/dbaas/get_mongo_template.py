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

__all__ = [
    'GetMongoTemplateResult',
    'AwaitableGetMongoTemplateResult',
    'get_mongo_template',
    'get_mongo_template_output',
]

@pulumi.output_type
class GetMongoTemplateResult:
    """
    A collection of values returned by getMongoTemplate.
    """
    def __init__(__self__, cores=None, edition=None, id=None, name=None, partial_match=None, ram=None, storage_size=None):
        if cores and not isinstance(cores, int):
            raise TypeError("Expected argument 'cores' to be a int")
        pulumi.set(__self__, "cores", cores)
        if edition and not isinstance(edition, str):
            raise TypeError("Expected argument 'edition' to be a str")
        pulumi.set(__self__, "edition", edition)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if partial_match and not isinstance(partial_match, bool):
            raise TypeError("Expected argument 'partial_match' to be a bool")
        pulumi.set(__self__, "partial_match", partial_match)
        if ram and not isinstance(ram, int):
            raise TypeError("Expected argument 'ram' to be a int")
        pulumi.set(__self__, "ram", ram)
        if storage_size and not isinstance(storage_size, int):
            raise TypeError("Expected argument 'storage_size' to be a int")
        pulumi.set(__self__, "storage_size", storage_size)

    @property
    @pulumi.getter
    def cores(self) -> int:
        """
        The number of CPU cores.
        """
        return pulumi.get(self, "cores")

    @property
    @pulumi.getter
    def edition(self) -> str:
        """
        The edition of the template (e.g. enterprise).
        """
        return pulumi.get(self, "edition")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the template.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the template.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partialMatch")
    def partial_match(self) -> Optional[bool]:
        return pulumi.get(self, "partial_match")

    @property
    @pulumi.getter
    def ram(self) -> int:
        """
        The amount of memory in GB.
        """
        return pulumi.get(self, "ram")

    @property
    @pulumi.getter(name="storageSize")
    def storage_size(self) -> int:
        """
        The amount of storage size in GB.
        """
        return pulumi.get(self, "storage_size")


class AwaitableGetMongoTemplateResult(GetMongoTemplateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMongoTemplateResult(
            cores=self.cores,
            edition=self.edition,
            id=self.id,
            name=self.name,
            partial_match=self.partial_match,
            ram=self.ram,
            storage_size=self.storage_size)


def get_mongo_template(id: Optional[str] = None,
                       name: Optional[str] = None,
                       partial_match: Optional[bool] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMongoTemplateResult:
    """
    The **DbaaS Mongo Template data source** can be used to search for and return an existing DbaaS MongoDB Template.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage


    :param str id: The ID of the template.
    :param str name: The name of the template.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['partialMatch'] = partial_match
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:dbaas/getMongoTemplate:getMongoTemplate', __args__, opts=opts, typ=GetMongoTemplateResult).value

    return AwaitableGetMongoTemplateResult(
        cores=pulumi.get(__ret__, 'cores'),
        edition=pulumi.get(__ret__, 'edition'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        partial_match=pulumi.get(__ret__, 'partial_match'),
        ram=pulumi.get(__ret__, 'ram'),
        storage_size=pulumi.get(__ret__, 'storage_size'))
def get_mongo_template_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                              name: Optional[pulumi.Input[Optional[str]]] = None,
                              partial_match: Optional[pulumi.Input[Optional[bool]]] = None,
                              opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetMongoTemplateResult]:
    """
    The **DbaaS Mongo Template data source** can be used to search for and return an existing DbaaS MongoDB Template.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage


    :param str id: The ID of the template.
    :param str name: The name of the template.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['partialMatch'] = partial_match
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:dbaas/getMongoTemplate:getMongoTemplate', __args__, opts=opts, typ=GetMongoTemplateResult)
    return __ret__.apply(lambda __response__: GetMongoTemplateResult(
        cores=pulumi.get(__response__, 'cores'),
        edition=pulumi.get(__response__, 'edition'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        partial_match=pulumi.get(__response__, 'partial_match'),
        ram=pulumi.get(__response__, 'ram'),
        storage_size=pulumi.get(__response__, 'storage_size')))
