# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['IPFailoverArgs', 'IPFailover']

@pulumi.input_type
class IPFailoverArgs:
    def __init__(__self__, *,
                 datacenter_id: pulumi.Input[str],
                 ip: pulumi.Input[str],
                 lan_id: pulumi.Input[str],
                 nicuuid: pulumi.Input[str]):
        """
        The set of arguments for constructing a IPFailover resource.
        :param pulumi.Input[str] datacenter_id: [string] The ID of a Virtual Data Center.
        :param pulumi.Input[str] ip: [string] The reserved IP address to be used in the IP failover group.
        :param pulumi.Input[str] lan_id: [string] The ID of a LAN.
        :param pulumi.Input[str] nicuuid: The UUID of the master NIC
        """
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        pulumi.set(__self__, "ip", ip)
        pulumi.set(__self__, "lan_id", lan_id)
        pulumi.set(__self__, "nicuuid", nicuuid)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> pulumi.Input[str]:
        """
        [string] The ID of a Virtual Data Center.
        """
        return pulumi.get(self, "datacenter_id")

    @datacenter_id.setter
    def datacenter_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "datacenter_id", value)

    @property
    @pulumi.getter
    def ip(self) -> pulumi.Input[str]:
        """
        [string] The reserved IP address to be used in the IP failover group.
        """
        return pulumi.get(self, "ip")

    @ip.setter
    def ip(self, value: pulumi.Input[str]):
        pulumi.set(self, "ip", value)

    @property
    @pulumi.getter(name="lanId")
    def lan_id(self) -> pulumi.Input[str]:
        """
        [string] The ID of a LAN.
        """
        return pulumi.get(self, "lan_id")

    @lan_id.setter
    def lan_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "lan_id", value)

    @property
    @pulumi.getter
    def nicuuid(self) -> pulumi.Input[str]:
        """
        The UUID of the master NIC
        """
        return pulumi.get(self, "nicuuid")

    @nicuuid.setter
    def nicuuid(self, value: pulumi.Input[str]):
        pulumi.set(self, "nicuuid", value)


@pulumi.input_type
class _IPFailoverState:
    def __init__(__self__, *,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 ip: Optional[pulumi.Input[str]] = None,
                 lan_id: Optional[pulumi.Input[str]] = None,
                 nicuuid: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering IPFailover resources.
        :param pulumi.Input[str] datacenter_id: [string] The ID of a Virtual Data Center.
        :param pulumi.Input[str] ip: [string] The reserved IP address to be used in the IP failover group.
        :param pulumi.Input[str] lan_id: [string] The ID of a LAN.
        :param pulumi.Input[str] nicuuid: The UUID of the master NIC
        """
        if datacenter_id is not None:
            pulumi.set(__self__, "datacenter_id", datacenter_id)
        if ip is not None:
            pulumi.set(__self__, "ip", ip)
        if lan_id is not None:
            pulumi.set(__self__, "lan_id", lan_id)
        if nicuuid is not None:
            pulumi.set(__self__, "nicuuid", nicuuid)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The ID of a Virtual Data Center.
        """
        return pulumi.get(self, "datacenter_id")

    @datacenter_id.setter
    def datacenter_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datacenter_id", value)

    @property
    @pulumi.getter
    def ip(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The reserved IP address to be used in the IP failover group.
        """
        return pulumi.get(self, "ip")

    @ip.setter
    def ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip", value)

    @property
    @pulumi.getter(name="lanId")
    def lan_id(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The ID of a LAN.
        """
        return pulumi.get(self, "lan_id")

    @lan_id.setter
    def lan_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lan_id", value)

    @property
    @pulumi.getter
    def nicuuid(self) -> Optional[pulumi.Input[str]]:
        """
        The UUID of the master NIC
        """
        return pulumi.get(self, "nicuuid")

    @nicuuid.setter
    def nicuuid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "nicuuid", value)


class IPFailover(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 ip: Optional[pulumi.Input[str]] = None,
                 lan_id: Optional[pulumi.Input[str]] = None,
                 nicuuid: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages **IP Failover** groups on IonosCloud.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ionoscloud as ionoscloud
        import pulumi_random as random

        example_datacenter = ionoscloud.compute.Datacenter("exampleDatacenter",
            location="us/las",
            description="Datacenter Description",
            sec_auth_protection=False)
        example_ip_block = ionoscloud.compute.IPBlock("exampleIPBlock",
            location="us/las",
            size=1)
        example_lan = ionoscloud.compute.Lan("exampleLan",
            datacenter_id=example_datacenter.id,
            public=True)
        server_image_password = random.RandomPassword("serverImagePassword",
            length=16,
            special=False)
        example_server = ionoscloud.compute.Server("exampleServer",
            datacenter_id=example_datacenter.id,
            cores=1,
            ram=1024,
            availability_zone="ZONE_1",
            cpu_family="INTEL_XEON",
            image_name="Ubuntu-20.04",
            image_password=server_image_password.result,
            volume=ionoscloud.compute.ServerVolumeArgs(
                name="system",
                size=14,
                disk_type="SSD",
            ),
            nic=ionoscloud.compute.ServerNicArgs(
                lan=1,
                dhcp=True,
                firewall_active=True,
                ips=[example_ip_block.ips[0]],
            ))
        example_ip_failover = ionoscloud.compute.IPFailover("exampleIPFailover",
            datacenter_id=example_datacenter.id,
            lan_id=example_lan.id,
            ip=example_ip_block.ips[0],
            nicuuid=example_server.primary_nic,
            opts=pulumi.ResourceOptions(depends_on=[example_lan]))
        ```
        <!--End PulumiCodeChooser -->

        ## A note on multiple NICs on an IP Failover

        If you want to add a secondary NIC to an IP Failover, follow these steps:
        1) Creating NIC A with failover IP on LAN 1
        2) Create NIC B unde the same LAN but with a different IP
        3) Create the IP Failover on LAN 1 with NIC A and failover IP of NIC A (A becomes now "master", no slaves)
        4) Update NIC B IP to be the failover IP ( B becomes now a slave, A remains master)

        After this you can create a new NIC C, NIC D and so on, in LAN 1, directly with the failover IP.

        Please check examples for a full example with the above steps.

        ## Import

        Resource IpFailover can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import ionoscloud:compute/iPFailover:IPFailover myipfailover {datacenter uuid}/{lan uuid}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] datacenter_id: [string] The ID of a Virtual Data Center.
        :param pulumi.Input[str] ip: [string] The reserved IP address to be used in the IP failover group.
        :param pulumi.Input[str] lan_id: [string] The ID of a LAN.
        :param pulumi.Input[str] nicuuid: The UUID of the master NIC
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IPFailoverArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages **IP Failover** groups on IonosCloud.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ionoscloud as ionoscloud
        import pulumi_random as random

        example_datacenter = ionoscloud.compute.Datacenter("exampleDatacenter",
            location="us/las",
            description="Datacenter Description",
            sec_auth_protection=False)
        example_ip_block = ionoscloud.compute.IPBlock("exampleIPBlock",
            location="us/las",
            size=1)
        example_lan = ionoscloud.compute.Lan("exampleLan",
            datacenter_id=example_datacenter.id,
            public=True)
        server_image_password = random.RandomPassword("serverImagePassword",
            length=16,
            special=False)
        example_server = ionoscloud.compute.Server("exampleServer",
            datacenter_id=example_datacenter.id,
            cores=1,
            ram=1024,
            availability_zone="ZONE_1",
            cpu_family="INTEL_XEON",
            image_name="Ubuntu-20.04",
            image_password=server_image_password.result,
            volume=ionoscloud.compute.ServerVolumeArgs(
                name="system",
                size=14,
                disk_type="SSD",
            ),
            nic=ionoscloud.compute.ServerNicArgs(
                lan=1,
                dhcp=True,
                firewall_active=True,
                ips=[example_ip_block.ips[0]],
            ))
        example_ip_failover = ionoscloud.compute.IPFailover("exampleIPFailover",
            datacenter_id=example_datacenter.id,
            lan_id=example_lan.id,
            ip=example_ip_block.ips[0],
            nicuuid=example_server.primary_nic,
            opts=pulumi.ResourceOptions(depends_on=[example_lan]))
        ```
        <!--End PulumiCodeChooser -->

        ## A note on multiple NICs on an IP Failover

        If you want to add a secondary NIC to an IP Failover, follow these steps:
        1) Creating NIC A with failover IP on LAN 1
        2) Create NIC B unde the same LAN but with a different IP
        3) Create the IP Failover on LAN 1 with NIC A and failover IP of NIC A (A becomes now "master", no slaves)
        4) Update NIC B IP to be the failover IP ( B becomes now a slave, A remains master)

        After this you can create a new NIC C, NIC D and so on, in LAN 1, directly with the failover IP.

        Please check examples for a full example with the above steps.

        ## Import

        Resource IpFailover can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import ionoscloud:compute/iPFailover:IPFailover myipfailover {datacenter uuid}/{lan uuid}
        ```

        :param str resource_name: The name of the resource.
        :param IPFailoverArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IPFailoverArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 ip: Optional[pulumi.Input[str]] = None,
                 lan_id: Optional[pulumi.Input[str]] = None,
                 nicuuid: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IPFailoverArgs.__new__(IPFailoverArgs)

            if datacenter_id is None and not opts.urn:
                raise TypeError("Missing required property 'datacenter_id'")
            __props__.__dict__["datacenter_id"] = datacenter_id
            if ip is None and not opts.urn:
                raise TypeError("Missing required property 'ip'")
            __props__.__dict__["ip"] = ip
            if lan_id is None and not opts.urn:
                raise TypeError("Missing required property 'lan_id'")
            __props__.__dict__["lan_id"] = lan_id
            if nicuuid is None and not opts.urn:
                raise TypeError("Missing required property 'nicuuid'")
            __props__.__dict__["nicuuid"] = nicuuid
        super(IPFailover, __self__).__init__(
            'ionoscloud:compute/iPFailover:IPFailover',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            datacenter_id: Optional[pulumi.Input[str]] = None,
            ip: Optional[pulumi.Input[str]] = None,
            lan_id: Optional[pulumi.Input[str]] = None,
            nicuuid: Optional[pulumi.Input[str]] = None) -> 'IPFailover':
        """
        Get an existing IPFailover resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] datacenter_id: [string] The ID of a Virtual Data Center.
        :param pulumi.Input[str] ip: [string] The reserved IP address to be used in the IP failover group.
        :param pulumi.Input[str] lan_id: [string] The ID of a LAN.
        :param pulumi.Input[str] nicuuid: The UUID of the master NIC
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IPFailoverState.__new__(_IPFailoverState)

        __props__.__dict__["datacenter_id"] = datacenter_id
        __props__.__dict__["ip"] = ip
        __props__.__dict__["lan_id"] = lan_id
        __props__.__dict__["nicuuid"] = nicuuid
        return IPFailover(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> pulumi.Output[str]:
        """
        [string] The ID of a Virtual Data Center.
        """
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter
    def ip(self) -> pulumi.Output[str]:
        """
        [string] The reserved IP address to be used in the IP failover group.
        """
        return pulumi.get(self, "ip")

    @property
    @pulumi.getter(name="lanId")
    def lan_id(self) -> pulumi.Output[str]:
        """
        [string] The ID of a LAN.
        """
        return pulumi.get(self, "lan_id")

    @property
    @pulumi.getter
    def nicuuid(self) -> pulumi.Output[str]:
        """
        The UUID of the master NIC
        """
        return pulumi.get(self, "nicuuid")

