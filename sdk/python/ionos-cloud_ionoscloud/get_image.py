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

__all__ = [
    'GetImageResult',
    'AwaitableGetImageResult',
    'get_image',
    'get_image_output',
]

@pulumi.output_type
class GetImageResult:
    """
    A collection of values returned by getImage.
    """
    def __init__(__self__, cloud_init=None, cpu_hot_plug=None, cpu_hot_unplug=None, description=None, disc_scsi_hot_plug=None, disc_scsi_hot_unplug=None, disc_virtio_hot_plug=None, disc_virtio_hot_unplug=None, id=None, image_alias=None, image_aliases=None, licence_type=None, location=None, name=None, nic_hot_plug=None, nic_hot_unplug=None, public=None, ram_hot_plug=None, ram_hot_unplug=None, size=None, type=None, version=None):
        if cloud_init and not isinstance(cloud_init, str):
            raise TypeError("Expected argument 'cloud_init' to be a str")
        pulumi.set(__self__, "cloud_init", cloud_init)
        if cpu_hot_plug and not isinstance(cpu_hot_plug, bool):
            raise TypeError("Expected argument 'cpu_hot_plug' to be a bool")
        pulumi.set(__self__, "cpu_hot_plug", cpu_hot_plug)
        if cpu_hot_unplug and not isinstance(cpu_hot_unplug, bool):
            raise TypeError("Expected argument 'cpu_hot_unplug' to be a bool")
        pulumi.set(__self__, "cpu_hot_unplug", cpu_hot_unplug)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if disc_scsi_hot_plug and not isinstance(disc_scsi_hot_plug, bool):
            raise TypeError("Expected argument 'disc_scsi_hot_plug' to be a bool")
        pulumi.set(__self__, "disc_scsi_hot_plug", disc_scsi_hot_plug)
        if disc_scsi_hot_unplug and not isinstance(disc_scsi_hot_unplug, bool):
            raise TypeError("Expected argument 'disc_scsi_hot_unplug' to be a bool")
        pulumi.set(__self__, "disc_scsi_hot_unplug", disc_scsi_hot_unplug)
        if disc_virtio_hot_plug and not isinstance(disc_virtio_hot_plug, bool):
            raise TypeError("Expected argument 'disc_virtio_hot_plug' to be a bool")
        pulumi.set(__self__, "disc_virtio_hot_plug", disc_virtio_hot_plug)
        if disc_virtio_hot_unplug and not isinstance(disc_virtio_hot_unplug, bool):
            raise TypeError("Expected argument 'disc_virtio_hot_unplug' to be a bool")
        pulumi.set(__self__, "disc_virtio_hot_unplug", disc_virtio_hot_unplug)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image_alias and not isinstance(image_alias, str):
            raise TypeError("Expected argument 'image_alias' to be a str")
        pulumi.set(__self__, "image_alias", image_alias)
        if image_aliases and not isinstance(image_aliases, list):
            raise TypeError("Expected argument 'image_aliases' to be a list")
        pulumi.set(__self__, "image_aliases", image_aliases)
        if licence_type and not isinstance(licence_type, str):
            raise TypeError("Expected argument 'licence_type' to be a str")
        pulumi.set(__self__, "licence_type", licence_type)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if nic_hot_plug and not isinstance(nic_hot_plug, bool):
            raise TypeError("Expected argument 'nic_hot_plug' to be a bool")
        pulumi.set(__self__, "nic_hot_plug", nic_hot_plug)
        if nic_hot_unplug and not isinstance(nic_hot_unplug, bool):
            raise TypeError("Expected argument 'nic_hot_unplug' to be a bool")
        pulumi.set(__self__, "nic_hot_unplug", nic_hot_unplug)
        if public and not isinstance(public, bool):
            raise TypeError("Expected argument 'public' to be a bool")
        pulumi.set(__self__, "public", public)
        if ram_hot_plug and not isinstance(ram_hot_plug, bool):
            raise TypeError("Expected argument 'ram_hot_plug' to be a bool")
        pulumi.set(__self__, "ram_hot_plug", ram_hot_plug)
        if ram_hot_unplug and not isinstance(ram_hot_unplug, bool):
            raise TypeError("Expected argument 'ram_hot_unplug' to be a bool")
        pulumi.set(__self__, "ram_hot_unplug", ram_hot_unplug)
        if size and not isinstance(size, float):
            raise TypeError("Expected argument 'size' to be a float")
        pulumi.set(__self__, "size", size)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="cloudInit")
    def cloud_init(self) -> str:
        """
        Cloud init compatibility
        """
        return pulumi.get(self, "cloud_init")

    @property
    @pulumi.getter(name="cpuHotPlug")
    def cpu_hot_plug(self) -> bool:
        """
        Is capable of CPU hot plug (no reboot required)
        """
        return pulumi.get(self, "cpu_hot_plug")

    @property
    @pulumi.getter(name="cpuHotUnplug")
    def cpu_hot_unplug(self) -> bool:
        """
        Is capable of CPU hot unplug (no reboot required)
        """
        return pulumi.get(self, "cpu_hot_unplug")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        description of the image
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="discScsiHotPlug")
    def disc_scsi_hot_plug(self) -> bool:
        """
        Is capable of SCSI drive hot plug (no reboot required)
        """
        return pulumi.get(self, "disc_scsi_hot_plug")

    @property
    @pulumi.getter(name="discScsiHotUnplug")
    def disc_scsi_hot_unplug(self) -> bool:
        """
        Is capable of SCSI drive hot unplug (no reboot required)
        """
        return pulumi.get(self, "disc_scsi_hot_unplug")

    @property
    @pulumi.getter(name="discVirtioHotPlug")
    def disc_virtio_hot_plug(self) -> bool:
        """
        Is capable of Virt-IO drive hot plug (no reboot required)
        """
        return pulumi.get(self, "disc_virtio_hot_plug")

    @property
    @pulumi.getter(name="discVirtioHotUnplug")
    def disc_virtio_hot_unplug(self) -> bool:
        """
        Is capable of Virt-IO drive hot unplug (no reboot required)
        """
        return pulumi.get(self, "disc_virtio_hot_unplug")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="imageAlias")
    def image_alias(self) -> Optional[str]:
        return pulumi.get(self, "image_alias")

    @property
    @pulumi.getter(name="imageAliases")
    def image_aliases(self) -> Sequence[str]:
        """
        List of image aliases mapped for this Image
        """
        return pulumi.get(self, "image_aliases")

    @property
    @pulumi.getter(name="licenceType")
    def licence_type(self) -> str:
        """
        OS type of this Image
        """
        return pulumi.get(self, "licence_type")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Location of that image/snapshot.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        name of the image
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nicHotPlug")
    def nic_hot_plug(self) -> bool:
        """
        Is capable of nic hot plug (no reboot required)
        """
        return pulumi.get(self, "nic_hot_plug")

    @property
    @pulumi.getter(name="nicHotUnplug")
    def nic_hot_unplug(self) -> bool:
        """
        Is capable of nic hot unplug (no reboot required)
        """
        return pulumi.get(self, "nic_hot_unplug")

    @property
    @pulumi.getter
    def public(self) -> bool:
        """
        Indicates if the image is part of the public repository or not
        """
        return pulumi.get(self, "public")

    @property
    @pulumi.getter(name="ramHotPlug")
    def ram_hot_plug(self) -> bool:
        """
        Is capable of memory hot plug (no reboot required)
        """
        return pulumi.get(self, "ram_hot_plug")

    @property
    @pulumi.getter(name="ramHotUnplug")
    def ram_hot_unplug(self) -> bool:
        """
        Is capable of memory hot unplug (no reboot required)
        """
        return pulumi.get(self, "ram_hot_unplug")

    @property
    @pulumi.getter
    def size(self) -> float:
        """
        The size of the image in GB
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        This indicates the type of image
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        return pulumi.get(self, "version")


class AwaitableGetImageResult(GetImageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetImageResult(
            cloud_init=self.cloud_init,
            cpu_hot_plug=self.cpu_hot_plug,
            cpu_hot_unplug=self.cpu_hot_unplug,
            description=self.description,
            disc_scsi_hot_plug=self.disc_scsi_hot_plug,
            disc_scsi_hot_unplug=self.disc_scsi_hot_unplug,
            disc_virtio_hot_plug=self.disc_virtio_hot_plug,
            disc_virtio_hot_unplug=self.disc_virtio_hot_unplug,
            id=self.id,
            image_alias=self.image_alias,
            image_aliases=self.image_aliases,
            licence_type=self.licence_type,
            location=self.location,
            name=self.name,
            nic_hot_plug=self.nic_hot_plug,
            nic_hot_unplug=self.nic_hot_unplug,
            public=self.public,
            ram_hot_plug=self.ram_hot_plug,
            ram_hot_unplug=self.ram_hot_unplug,
            size=self.size,
            type=self.type,
            version=self.version)


def get_image(cloud_init: Optional[str] = None,
              description: Optional[str] = None,
              image_alias: Optional[str] = None,
              location: Optional[str] = None,
              name: Optional[str] = None,
              type: Optional[str] = None,
              version: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetImageResult:
    """
    The **Image data source** can be used to search for and return an existing image which can then be used to provision a server.\\
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result. In case multiple matches are found, enable debug(`TF_LOG=debug`) to show the name and location of the images.
    ## Example Usage

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    cdrom = ionoscloud.get_image(cloud_init="NONE",
        image_alias="ubuntu:latest_iso",
        location="de/txl",
        type="CDROM")
    ```
    <!--End PulumiCodeChooser -->
    Finds an image with alias `ubuntu:latest_iso`, in location `de/txl`, that does not support `cloud_init` and is of type `CDROM`.

    ### Additional Examples

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_image(image_alias="ubuntu:latest",
        location="de/txl")
    ```
    <!--End PulumiCodeChooser -->

    Finds an image with alias `ubuntu:latest` in location `de/txl`. Uses exact matching on both fields.

    ### Additional Examples

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_image(cloud_init="V1",
        image_alias="ubuntu:latest",
        location="us/ewr",
        type="HDD")
    ```
    <!--End PulumiCodeChooser -->
    Finds an image named `ubuntu-20.04.6` in location `de/txl`. Uses exact matching.


    :param str cloud_init: Cloud init compatibility ("NONE" or "V1"). Exact match.
    :param str description: description of the image
    :param str image_alias: Image alias of the image you are searching for. Exact match. E.g. =`centos:latest`, `ubuntu:latest`
    :param str location: Id of the existing image's location. Exact match. Possible values: `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `us/ewr`, `us/las`
    :param str name: Name of an existing image that you want to search for. It will return an exact match if one exists, otherwise it will retrieve partial matches.
    :param str type: The image type, HDD or CD-ROM. Exact match.
    :param str version: The version of the image that you want to search for.
           
           If both "name" and "version" are provided the plugin will concatenate the two strings in this format [name]-[version].
           The resulting string will be used to search for an exact match. An error will be thrown if one is not found.
    """
    __args__ = dict()
    __args__['cloudInit'] = cloud_init
    __args__['description'] = description
    __args__['imageAlias'] = image_alias
    __args__['location'] = location
    __args__['name'] = name
    __args__['type'] = type
    __args__['version'] = version
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getImage:getImage', __args__, opts=opts, typ=GetImageResult).value

    return AwaitableGetImageResult(
        cloud_init=pulumi.get(__ret__, 'cloud_init'),
        cpu_hot_plug=pulumi.get(__ret__, 'cpu_hot_plug'),
        cpu_hot_unplug=pulumi.get(__ret__, 'cpu_hot_unplug'),
        description=pulumi.get(__ret__, 'description'),
        disc_scsi_hot_plug=pulumi.get(__ret__, 'disc_scsi_hot_plug'),
        disc_scsi_hot_unplug=pulumi.get(__ret__, 'disc_scsi_hot_unplug'),
        disc_virtio_hot_plug=pulumi.get(__ret__, 'disc_virtio_hot_plug'),
        disc_virtio_hot_unplug=pulumi.get(__ret__, 'disc_virtio_hot_unplug'),
        id=pulumi.get(__ret__, 'id'),
        image_alias=pulumi.get(__ret__, 'image_alias'),
        image_aliases=pulumi.get(__ret__, 'image_aliases'),
        licence_type=pulumi.get(__ret__, 'licence_type'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        nic_hot_plug=pulumi.get(__ret__, 'nic_hot_plug'),
        nic_hot_unplug=pulumi.get(__ret__, 'nic_hot_unplug'),
        public=pulumi.get(__ret__, 'public'),
        ram_hot_plug=pulumi.get(__ret__, 'ram_hot_plug'),
        ram_hot_unplug=pulumi.get(__ret__, 'ram_hot_unplug'),
        size=pulumi.get(__ret__, 'size'),
        type=pulumi.get(__ret__, 'type'),
        version=pulumi.get(__ret__, 'version'))
def get_image_output(cloud_init: Optional[pulumi.Input[Optional[str]]] = None,
                     description: Optional[pulumi.Input[Optional[str]]] = None,
                     image_alias: Optional[pulumi.Input[Optional[str]]] = None,
                     location: Optional[pulumi.Input[Optional[str]]] = None,
                     name: Optional[pulumi.Input[Optional[str]]] = None,
                     type: Optional[pulumi.Input[Optional[str]]] = None,
                     version: Optional[pulumi.Input[Optional[str]]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetImageResult]:
    """
    The **Image data source** can be used to search for and return an existing image which can then be used to provision a server.\\
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result. In case multiple matches are found, enable debug(`TF_LOG=debug`) to show the name and location of the images.
    ## Example Usage

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    cdrom = ionoscloud.get_image(cloud_init="NONE",
        image_alias="ubuntu:latest_iso",
        location="de/txl",
        type="CDROM")
    ```
    <!--End PulumiCodeChooser -->
    Finds an image with alias `ubuntu:latest_iso`, in location `de/txl`, that does not support `cloud_init` and is of type `CDROM`.

    ### Additional Examples

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_image(image_alias="ubuntu:latest",
        location="de/txl")
    ```
    <!--End PulumiCodeChooser -->

    Finds an image with alias `ubuntu:latest` in location `de/txl`. Uses exact matching on both fields.

    ### Additional Examples

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_image(cloud_init="V1",
        image_alias="ubuntu:latest",
        location="us/ewr",
        type="HDD")
    ```
    <!--End PulumiCodeChooser -->
    Finds an image named `ubuntu-20.04.6` in location `de/txl`. Uses exact matching.


    :param str cloud_init: Cloud init compatibility ("NONE" or "V1"). Exact match.
    :param str description: description of the image
    :param str image_alias: Image alias of the image you are searching for. Exact match. E.g. =`centos:latest`, `ubuntu:latest`
    :param str location: Id of the existing image's location. Exact match. Possible values: `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `us/ewr`, `us/las`
    :param str name: Name of an existing image that you want to search for. It will return an exact match if one exists, otherwise it will retrieve partial matches.
    :param str type: The image type, HDD or CD-ROM. Exact match.
    :param str version: The version of the image that you want to search for.
           
           If both "name" and "version" are provided the plugin will concatenate the two strings in this format [name]-[version].
           The resulting string will be used to search for an exact match. An error will be thrown if one is not found.
    """
    __args__ = dict()
    __args__['cloudInit'] = cloud_init
    __args__['description'] = description
    __args__['imageAlias'] = image_alias
    __args__['location'] = location
    __args__['name'] = name
    __args__['type'] = type
    __args__['version'] = version
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:index/getImage:getImage', __args__, opts=opts, typ=GetImageResult)
    return __ret__.apply(lambda __response__: GetImageResult(
        cloud_init=pulumi.get(__response__, 'cloud_init'),
        cpu_hot_plug=pulumi.get(__response__, 'cpu_hot_plug'),
        cpu_hot_unplug=pulumi.get(__response__, 'cpu_hot_unplug'),
        description=pulumi.get(__response__, 'description'),
        disc_scsi_hot_plug=pulumi.get(__response__, 'disc_scsi_hot_plug'),
        disc_scsi_hot_unplug=pulumi.get(__response__, 'disc_scsi_hot_unplug'),
        disc_virtio_hot_plug=pulumi.get(__response__, 'disc_virtio_hot_plug'),
        disc_virtio_hot_unplug=pulumi.get(__response__, 'disc_virtio_hot_unplug'),
        id=pulumi.get(__response__, 'id'),
        image_alias=pulumi.get(__response__, 'image_alias'),
        image_aliases=pulumi.get(__response__, 'image_aliases'),
        licence_type=pulumi.get(__response__, 'licence_type'),
        location=pulumi.get(__response__, 'location'),
        name=pulumi.get(__response__, 'name'),
        nic_hot_plug=pulumi.get(__response__, 'nic_hot_plug'),
        nic_hot_unplug=pulumi.get(__response__, 'nic_hot_unplug'),
        public=pulumi.get(__response__, 'public'),
        ram_hot_plug=pulumi.get(__response__, 'ram_hot_plug'),
        ram_hot_unplug=pulumi.get(__response__, 'ram_hot_unplug'),
        size=pulumi.get(__response__, 'size'),
        type=pulumi.get(__response__, 'type'),
        version=pulumi.get(__response__, 'version')))
