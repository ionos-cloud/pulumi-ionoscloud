# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetTemplateResult',
    'AwaitableGetTemplateResult',
    'get_template',
    'get_template_output',
]

@pulumi.output_type
class GetTemplateResult:
    """
    A collection of values returned by getTemplate.
    """
    def __init__(__self__, cores=None, id=None, name=None, ram=None, storage_size=None):
        if cores and not isinstance(cores, float):
            raise TypeError("Expected argument 'cores' to be a float")
        pulumi.set(__self__, "cores", cores)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if ram and not isinstance(ram, float):
            raise TypeError("Expected argument 'ram' to be a float")
        pulumi.set(__self__, "ram", ram)
        if storage_size and not isinstance(storage_size, float):
            raise TypeError("Expected argument 'storage_size' to be a float")
        pulumi.set(__self__, "storage_size", storage_size)

    @property
    @pulumi.getter
    def cores(self) -> float:
        """
        The CPU cores count
        """
        return pulumi.get(self, "cores")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Id of template
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of template
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def ram(self) -> float:
        """
        The RAM size in MB
        """
        return pulumi.get(self, "ram")

    @property
    @pulumi.getter(name="storageSize")
    def storage_size(self) -> float:
        """
        The storage size in GB
        """
        return pulumi.get(self, "storage_size")


class AwaitableGetTemplateResult(GetTemplateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTemplateResult(
            cores=self.cores,
            id=self.id,
            name=self.name,
            ram=self.ram,
            storage_size=self.storage_size)


def get_template(cores: Optional[float] = None,
                 name: Optional[str] = None,
                 ram: Optional[float] = None,
                 storage_size: Optional[float] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTemplateResult:
    """
    The **Template data source** can be used to search for and return existing templates by providing any of template properties (name, cores, ram, storage_size).
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage

    ### By Name
    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_template(name="CUBES S")
    ```
    <!--End PulumiCodeChooser -->

    ### By Cores
    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_template(cores=6)
    ```
    <!--End PulumiCodeChooser -->

    ### By Ram
    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_template(ram=49152)
    ```
    <!--End PulumiCodeChooser -->

    ### By Storage Size
    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_template(storage_size=80)
    ```
    <!--End PulumiCodeChooser -->


    :param float cores: The CPU cores count.
    :param str name: A name of that resource.
    :param float ram: The RAM size in MB.
    :param float storage_size: The storage size in GB.
           
           Any of the arguments ca be provided. If none, the datasource will return an error.
    """
    __args__ = dict()
    __args__['cores'] = cores
    __args__['name'] = name
    __args__['ram'] = ram
    __args__['storageSize'] = storage_size
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getTemplate:getTemplate', __args__, opts=opts, typ=GetTemplateResult).value

    return AwaitableGetTemplateResult(
        cores=pulumi.get(__ret__, 'cores'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        ram=pulumi.get(__ret__, 'ram'),
        storage_size=pulumi.get(__ret__, 'storage_size'))


@_utilities.lift_output_func(get_template)
def get_template_output(cores: Optional[pulumi.Input[Optional[float]]] = None,
                        name: Optional[pulumi.Input[Optional[str]]] = None,
                        ram: Optional[pulumi.Input[Optional[float]]] = None,
                        storage_size: Optional[pulumi.Input[Optional[float]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTemplateResult]:
    """
    The **Template data source** can be used to search for and return existing templates by providing any of template properties (name, cores, ram, storage_size).
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage

    ### By Name
    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_template(name="CUBES S")
    ```
    <!--End PulumiCodeChooser -->

    ### By Cores
    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_template(cores=6)
    ```
    <!--End PulumiCodeChooser -->

    ### By Ram
    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_template(ram=49152)
    ```
    <!--End PulumiCodeChooser -->

    ### By Storage Size
    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_template(storage_size=80)
    ```
    <!--End PulumiCodeChooser -->


    :param float cores: The CPU cores count.
    :param str name: A name of that resource.
    :param float ram: The RAM size in MB.
    :param float storage_size: The storage size in GB.
           
           Any of the arguments ca be provided. If none, the datasource will return an error.
    """
    ...
