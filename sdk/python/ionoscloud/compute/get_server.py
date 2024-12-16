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
    'GetServerResult',
    'AwaitableGetServerResult',
    'get_server',
    'get_server_output',
]

@pulumi.output_type
class GetServerResult:
    """
    A collection of values returned by getServer.
    """
    def __init__(__self__, availability_zone=None, boot_cdrom=None, boot_image=None, boot_volume=None, cdroms=None, cores=None, cpu_family=None, datacenter_id=None, id=None, labels=None, name=None, nics=None, ram=None, template_uuid=None, token=None, type=None, vm_state=None, volumes=None):
        if availability_zone and not isinstance(availability_zone, str):
            raise TypeError("Expected argument 'availability_zone' to be a str")
        pulumi.set(__self__, "availability_zone", availability_zone)
        if boot_cdrom and not isinstance(boot_cdrom, str):
            raise TypeError("Expected argument 'boot_cdrom' to be a str")
        pulumi.set(__self__, "boot_cdrom", boot_cdrom)
        if boot_image and not isinstance(boot_image, str):
            raise TypeError("Expected argument 'boot_image' to be a str")
        pulumi.set(__self__, "boot_image", boot_image)
        if boot_volume and not isinstance(boot_volume, str):
            raise TypeError("Expected argument 'boot_volume' to be a str")
        pulumi.set(__self__, "boot_volume", boot_volume)
        if cdroms and not isinstance(cdroms, list):
            raise TypeError("Expected argument 'cdroms' to be a list")
        pulumi.set(__self__, "cdroms", cdroms)
        if cores and not isinstance(cores, int):
            raise TypeError("Expected argument 'cores' to be a int")
        pulumi.set(__self__, "cores", cores)
        if cpu_family and not isinstance(cpu_family, str):
            raise TypeError("Expected argument 'cpu_family' to be a str")
        pulumi.set(__self__, "cpu_family", cpu_family)
        if datacenter_id and not isinstance(datacenter_id, str):
            raise TypeError("Expected argument 'datacenter_id' to be a str")
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if labels and not isinstance(labels, list):
            raise TypeError("Expected argument 'labels' to be a list")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if nics and not isinstance(nics, list):
            raise TypeError("Expected argument 'nics' to be a list")
        pulumi.set(__self__, "nics", nics)
        if ram and not isinstance(ram, int):
            raise TypeError("Expected argument 'ram' to be a int")
        pulumi.set(__self__, "ram", ram)
        if template_uuid and not isinstance(template_uuid, str):
            raise TypeError("Expected argument 'template_uuid' to be a str")
        pulumi.set(__self__, "template_uuid", template_uuid)
        if token and not isinstance(token, str):
            raise TypeError("Expected argument 'token' to be a str")
        pulumi.set(__self__, "token", token)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if vm_state and not isinstance(vm_state, str):
            raise TypeError("Expected argument 'vm_state' to be a str")
        pulumi.set(__self__, "vm_state", vm_state)
        if volumes and not isinstance(volumes, list):
            raise TypeError("Expected argument 'volumes' to be a list")
        pulumi.set(__self__, "volumes", volumes)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> str:
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="bootCdrom")
    def boot_cdrom(self) -> str:
        return pulumi.get(self, "boot_cdrom")

    @property
    @pulumi.getter(name="bootImage")
    def boot_image(self) -> str:
        return pulumi.get(self, "boot_image")

    @property
    @pulumi.getter(name="bootVolume")
    def boot_volume(self) -> str:
        return pulumi.get(self, "boot_volume")

    @property
    @pulumi.getter
    def cdroms(self) -> Sequence['outputs.GetServerCdromResult']:
        return pulumi.get(self, "cdroms")

    @property
    @pulumi.getter
    def cores(self) -> int:
        return pulumi.get(self, "cores")

    @property
    @pulumi.getter(name="cpuFamily")
    def cpu_family(self) -> str:
        return pulumi.get(self, "cpu_family")

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> str:
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def labels(self) -> Sequence['outputs.GetServerLabelResult']:
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def nics(self) -> Sequence['outputs.GetServerNicResult']:
        return pulumi.get(self, "nics")

    @property
    @pulumi.getter
    def ram(self) -> int:
        return pulumi.get(self, "ram")

    @property
    @pulumi.getter(name="templateUuid")
    def template_uuid(self) -> Optional[str]:
        return pulumi.get(self, "template_uuid")

    @property
    @pulumi.getter
    def token(self) -> str:
        return pulumi.get(self, "token")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vmState")
    def vm_state(self) -> str:
        return pulumi.get(self, "vm_state")

    @property
    @pulumi.getter
    def volumes(self) -> Sequence['outputs.GetServerVolumeResult']:
        return pulumi.get(self, "volumes")


class AwaitableGetServerResult(GetServerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerResult(
            availability_zone=self.availability_zone,
            boot_cdrom=self.boot_cdrom,
            boot_image=self.boot_image,
            boot_volume=self.boot_volume,
            cdroms=self.cdroms,
            cores=self.cores,
            cpu_family=self.cpu_family,
            datacenter_id=self.datacenter_id,
            id=self.id,
            labels=self.labels,
            name=self.name,
            nics=self.nics,
            ram=self.ram,
            template_uuid=self.template_uuid,
            token=self.token,
            type=self.type,
            vm_state=self.vm_state,
            volumes=self.volumes)


def get_server(datacenter_id: Optional[str] = None,
               id: Optional[str] = None,
               name: Optional[str] = None,
               template_uuid: Optional[str] = None,
               type: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServerResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['datacenterId'] = datacenter_id
    __args__['id'] = id
    __args__['name'] = name
    __args__['templateUuid'] = template_uuid
    __args__['type'] = type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:compute/getServer:getServer', __args__, opts=opts, typ=GetServerResult).value

    return AwaitableGetServerResult(
        availability_zone=pulumi.get(__ret__, 'availability_zone'),
        boot_cdrom=pulumi.get(__ret__, 'boot_cdrom'),
        boot_image=pulumi.get(__ret__, 'boot_image'),
        boot_volume=pulumi.get(__ret__, 'boot_volume'),
        cdroms=pulumi.get(__ret__, 'cdroms'),
        cores=pulumi.get(__ret__, 'cores'),
        cpu_family=pulumi.get(__ret__, 'cpu_family'),
        datacenter_id=pulumi.get(__ret__, 'datacenter_id'),
        id=pulumi.get(__ret__, 'id'),
        labels=pulumi.get(__ret__, 'labels'),
        name=pulumi.get(__ret__, 'name'),
        nics=pulumi.get(__ret__, 'nics'),
        ram=pulumi.get(__ret__, 'ram'),
        template_uuid=pulumi.get(__ret__, 'template_uuid'),
        token=pulumi.get(__ret__, 'token'),
        type=pulumi.get(__ret__, 'type'),
        vm_state=pulumi.get(__ret__, 'vm_state'),
        volumes=pulumi.get(__ret__, 'volumes'))
def get_server_output(datacenter_id: Optional[pulumi.Input[str]] = None,
                      id: Optional[pulumi.Input[Optional[str]]] = None,
                      name: Optional[pulumi.Input[Optional[str]]] = None,
                      template_uuid: Optional[pulumi.Input[Optional[str]]] = None,
                      type: Optional[pulumi.Input[Optional[str]]] = None,
                      opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetServerResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['datacenterId'] = datacenter_id
    __args__['id'] = id
    __args__['name'] = name
    __args__['templateUuid'] = template_uuid
    __args__['type'] = type
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:compute/getServer:getServer', __args__, opts=opts, typ=GetServerResult)
    return __ret__.apply(lambda __response__: GetServerResult(
        availability_zone=pulumi.get(__response__, 'availability_zone'),
        boot_cdrom=pulumi.get(__response__, 'boot_cdrom'),
        boot_image=pulumi.get(__response__, 'boot_image'),
        boot_volume=pulumi.get(__response__, 'boot_volume'),
        cdroms=pulumi.get(__response__, 'cdroms'),
        cores=pulumi.get(__response__, 'cores'),
        cpu_family=pulumi.get(__response__, 'cpu_family'),
        datacenter_id=pulumi.get(__response__, 'datacenter_id'),
        id=pulumi.get(__response__, 'id'),
        labels=pulumi.get(__response__, 'labels'),
        name=pulumi.get(__response__, 'name'),
        nics=pulumi.get(__response__, 'nics'),
        ram=pulumi.get(__response__, 'ram'),
        template_uuid=pulumi.get(__response__, 'template_uuid'),
        token=pulumi.get(__response__, 'token'),
        type=pulumi.get(__response__, 'type'),
        vm_state=pulumi.get(__response__, 'vm_state'),
        volumes=pulumi.get(__response__, 'volumes')))
