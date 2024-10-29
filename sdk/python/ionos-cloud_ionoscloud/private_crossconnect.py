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
from . import outputs
from ._inputs import *

__all__ = ['PrivateCrossconnectArgs', 'PrivateCrossconnect']

@pulumi.input_type
class PrivateCrossconnectArgs:
    def __init__(__self__, *,
                 connectable_datacenters: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateCrossconnectConnectableDatacenterArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 peers: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateCrossconnectPeerArgs']]]] = None):
        """
        The set of arguments for constructing a PrivateCrossconnect resource.
        :param pulumi.Input[Sequence[pulumi.Input['PrivateCrossconnectConnectableDatacenterArgs']]] connectable_datacenters: A list containing all the connectable datacenters
        :param pulumi.Input[str] description: [string] A short description for the cross-connection.
               - `connectable datacenters` - (Computed) A list containing all the connectable datacenters
        :param pulumi.Input[str] name: The name of the connectable datacenter
        :param pulumi.Input[Sequence[pulumi.Input['PrivateCrossconnectPeerArgs']]] peers: Lists LAN's joined to this cross connect
        """
        if connectable_datacenters is not None:
            pulumi.set(__self__, "connectable_datacenters", connectable_datacenters)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if peers is not None:
            pulumi.set(__self__, "peers", peers)

    @property
    @pulumi.getter(name="connectableDatacenters")
    def connectable_datacenters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrivateCrossconnectConnectableDatacenterArgs']]]]:
        """
        A list containing all the connectable datacenters
        """
        return pulumi.get(self, "connectable_datacenters")

    @connectable_datacenters.setter
    def connectable_datacenters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateCrossconnectConnectableDatacenterArgs']]]]):
        pulumi.set(self, "connectable_datacenters", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        [string] A short description for the cross-connection.
        - `connectable datacenters` - (Computed) A list containing all the connectable datacenters
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the connectable datacenter
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def peers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrivateCrossconnectPeerArgs']]]]:
        """
        Lists LAN's joined to this cross connect
        """
        return pulumi.get(self, "peers")

    @peers.setter
    def peers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateCrossconnectPeerArgs']]]]):
        pulumi.set(self, "peers", value)


@pulumi.input_type
class _PrivateCrossconnectState:
    def __init__(__self__, *,
                 connectable_datacenters: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateCrossconnectConnectableDatacenterArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 peers: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateCrossconnectPeerArgs']]]] = None):
        """
        Input properties used for looking up and filtering PrivateCrossconnect resources.
        :param pulumi.Input[Sequence[pulumi.Input['PrivateCrossconnectConnectableDatacenterArgs']]] connectable_datacenters: A list containing all the connectable datacenters
        :param pulumi.Input[str] description: [string] A short description for the cross-connection.
               - `connectable datacenters` - (Computed) A list containing all the connectable datacenters
        :param pulumi.Input[str] name: The name of the connectable datacenter
        :param pulumi.Input[Sequence[pulumi.Input['PrivateCrossconnectPeerArgs']]] peers: Lists LAN's joined to this cross connect
        """
        if connectable_datacenters is not None:
            pulumi.set(__self__, "connectable_datacenters", connectable_datacenters)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if peers is not None:
            pulumi.set(__self__, "peers", peers)

    @property
    @pulumi.getter(name="connectableDatacenters")
    def connectable_datacenters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrivateCrossconnectConnectableDatacenterArgs']]]]:
        """
        A list containing all the connectable datacenters
        """
        return pulumi.get(self, "connectable_datacenters")

    @connectable_datacenters.setter
    def connectable_datacenters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateCrossconnectConnectableDatacenterArgs']]]]):
        pulumi.set(self, "connectable_datacenters", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        [string] A short description for the cross-connection.
        - `connectable datacenters` - (Computed) A list containing all the connectable datacenters
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the connectable datacenter
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def peers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrivateCrossconnectPeerArgs']]]]:
        """
        Lists LAN's joined to this cross connect
        """
        return pulumi.get(self, "peers")

    @peers.setter
    def peers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateCrossconnectPeerArgs']]]]):
        pulumi.set(self, "peers", value)


class PrivateCrossconnect(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connectable_datacenters: Optional[pulumi.Input[Sequence[pulumi.Input[Union['PrivateCrossconnectConnectableDatacenterArgs', 'PrivateCrossconnectConnectableDatacenterArgsDict']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 peers: Optional[pulumi.Input[Sequence[pulumi.Input[Union['PrivateCrossconnectPeerArgs', 'PrivateCrossconnectPeerArgsDict']]]]] = None,
                 __props__=None):
        """
        Manages a **Cross Connect** on IonosCloud.
        Cross Connect allows you to connect virtual data centers (VDC) with each other using a private LAN.
        The VDCs to be connected need to belong to the same IONOS Cloud contract and location.
        You can only use private LANs for a Cross Connect connection. A LAN can only be a part of one Cross Connect.

        The IP addresses of the NICs used for the Cross Connect connection may not be used in more than one NIC and they need to belong to the same IP range.

        ## Example Usage

        To connect two datacenters we need 2 lans defined, one in each datacenter. After, we reference the cross-connect through which we want the connection to be established.

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ionos-cloud_ionoscloud as ionoscloud

        cross_connect_test_resource = ionoscloud.PrivateCrossconnect("crossConnectTestResource", description="CrossConnectTestResource")
        dc1 = ionoscloud.compute.Datacenter("dc1", location="de/txl")
        dc2 = ionoscloud.compute.Datacenter("dc2", location="de/txl")
        dc1lan = ionoscloud.Lan("dc1lan",
            datacenter_id=dc1.id,
            public=False,
            pcc=cross_connect_test_resource.id)
        dc2lan = ionoscloud.Lan("dc2lan",
            datacenter_id=dc2.id,
            public=False,
            pcc=cross_connect_test_resource.id)
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        A Cross Connect resource can be imported using its `resource id`, e.g.

        ```sh
        $ pulumi import ionoscloud:index/privateCrossconnect:PrivateCrossconnect demo {ionoscloud_private_crossconnect_uuid}
        ```

        This can be helpful when you want to import cross-connects which you have already created manually or using other means, outside of terraform.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['PrivateCrossconnectConnectableDatacenterArgs', 'PrivateCrossconnectConnectableDatacenterArgsDict']]]] connectable_datacenters: A list containing all the connectable datacenters
        :param pulumi.Input[str] description: [string] A short description for the cross-connection.
               - `connectable datacenters` - (Computed) A list containing all the connectable datacenters
        :param pulumi.Input[str] name: The name of the connectable datacenter
        :param pulumi.Input[Sequence[pulumi.Input[Union['PrivateCrossconnectPeerArgs', 'PrivateCrossconnectPeerArgsDict']]]] peers: Lists LAN's joined to this cross connect
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[PrivateCrossconnectArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a **Cross Connect** on IonosCloud.
        Cross Connect allows you to connect virtual data centers (VDC) with each other using a private LAN.
        The VDCs to be connected need to belong to the same IONOS Cloud contract and location.
        You can only use private LANs for a Cross Connect connection. A LAN can only be a part of one Cross Connect.

        The IP addresses of the NICs used for the Cross Connect connection may not be used in more than one NIC and they need to belong to the same IP range.

        ## Example Usage

        To connect two datacenters we need 2 lans defined, one in each datacenter. After, we reference the cross-connect through which we want the connection to be established.

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ionos-cloud_ionoscloud as ionoscloud

        cross_connect_test_resource = ionoscloud.PrivateCrossconnect("crossConnectTestResource", description="CrossConnectTestResource")
        dc1 = ionoscloud.compute.Datacenter("dc1", location="de/txl")
        dc2 = ionoscloud.compute.Datacenter("dc2", location="de/txl")
        dc1lan = ionoscloud.Lan("dc1lan",
            datacenter_id=dc1.id,
            public=False,
            pcc=cross_connect_test_resource.id)
        dc2lan = ionoscloud.Lan("dc2lan",
            datacenter_id=dc2.id,
            public=False,
            pcc=cross_connect_test_resource.id)
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        A Cross Connect resource can be imported using its `resource id`, e.g.

        ```sh
        $ pulumi import ionoscloud:index/privateCrossconnect:PrivateCrossconnect demo {ionoscloud_private_crossconnect_uuid}
        ```

        This can be helpful when you want to import cross-connects which you have already created manually or using other means, outside of terraform.

        :param str resource_name: The name of the resource.
        :param PrivateCrossconnectArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PrivateCrossconnectArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connectable_datacenters: Optional[pulumi.Input[Sequence[pulumi.Input[Union['PrivateCrossconnectConnectableDatacenterArgs', 'PrivateCrossconnectConnectableDatacenterArgsDict']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 peers: Optional[pulumi.Input[Sequence[pulumi.Input[Union['PrivateCrossconnectPeerArgs', 'PrivateCrossconnectPeerArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PrivateCrossconnectArgs.__new__(PrivateCrossconnectArgs)

            __props__.__dict__["connectable_datacenters"] = connectable_datacenters
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["peers"] = peers
        super(PrivateCrossconnect, __self__).__init__(
            'ionoscloud:index/privateCrossconnect:PrivateCrossconnect',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            connectable_datacenters: Optional[pulumi.Input[Sequence[pulumi.Input[Union['PrivateCrossconnectConnectableDatacenterArgs', 'PrivateCrossconnectConnectableDatacenterArgsDict']]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            peers: Optional[pulumi.Input[Sequence[pulumi.Input[Union['PrivateCrossconnectPeerArgs', 'PrivateCrossconnectPeerArgsDict']]]]] = None) -> 'PrivateCrossconnect':
        """
        Get an existing PrivateCrossconnect resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['PrivateCrossconnectConnectableDatacenterArgs', 'PrivateCrossconnectConnectableDatacenterArgsDict']]]] connectable_datacenters: A list containing all the connectable datacenters
        :param pulumi.Input[str] description: [string] A short description for the cross-connection.
               - `connectable datacenters` - (Computed) A list containing all the connectable datacenters
        :param pulumi.Input[str] name: The name of the connectable datacenter
        :param pulumi.Input[Sequence[pulumi.Input[Union['PrivateCrossconnectPeerArgs', 'PrivateCrossconnectPeerArgsDict']]]] peers: Lists LAN's joined to this cross connect
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PrivateCrossconnectState.__new__(_PrivateCrossconnectState)

        __props__.__dict__["connectable_datacenters"] = connectable_datacenters
        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["peers"] = peers
        return PrivateCrossconnect(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="connectableDatacenters")
    def connectable_datacenters(self) -> pulumi.Output[Sequence['outputs.PrivateCrossconnectConnectableDatacenter']]:
        """
        A list containing all the connectable datacenters
        """
        return pulumi.get(self, "connectable_datacenters")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        [string] A short description for the cross-connection.
        - `connectable datacenters` - (Computed) A list containing all the connectable datacenters
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the connectable datacenter
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def peers(self) -> pulumi.Output[Sequence['outputs.PrivateCrossconnectPeer']]:
        """
        Lists LAN's joined to this cross connect
        """
        return pulumi.get(self, "peers")

