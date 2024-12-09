# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['FirewallArgs', 'Firewall']

@pulumi.input_type
class FirewallArgs:
    def __init__(__self__, *,
                 datacenter_id: pulumi.Input[str],
                 nic_id: pulumi.Input[str],
                 protocol: pulumi.Input[str],
                 server_id: pulumi.Input[str],
                 icmp_code: Optional[pulumi.Input[str]] = None,
                 icmp_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port_range_end: Optional[pulumi.Input[int]] = None,
                 port_range_start: Optional[pulumi.Input[int]] = None,
                 source_ip: Optional[pulumi.Input[str]] = None,
                 source_mac: Optional[pulumi.Input[str]] = None,
                 target_ip: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Firewall resource.
        :param pulumi.Input[str] datacenter_id: [string] The Virtual Data Center ID.
        :param pulumi.Input[str] nic_id: [string] The NIC ID.
        :param pulumi.Input[str] protocol: [string] The protocol for the rule: TCP, UDP, ICMP, ANY. Property cannot be modified after creation (disallowed in update requests).
        :param pulumi.Input[str] server_id: [string] The Server ID.
        :param pulumi.Input[str] icmp_code: [int] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen.
        :param pulumi.Input[str] icmp_type: [string] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen. Value null allows all codes.
        :param pulumi.Input[str] name: [string] The name of the firewall rule.
        :param pulumi.Input[int] port_range_end: [int] Defines the end range of the allowed port (from 1 to 65534) if the protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
        :param pulumi.Input[int] port_range_start: [int] Defines the start range of the allowed port (from 1 to 65534) if protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
        :param pulumi.Input[str] source_ip: [string] Only traffic originating from the respective IPv4 address is allowed. Value null allows all source IPs.
        :param pulumi.Input[str] source_mac: [string] Only traffic originating from the respective MAC address is allowed. Valid format: aa:bb:cc:dd:ee:ff. Value null allows all source MAC address. Valid format: aa:bb:cc:dd:ee:ff.
        :param pulumi.Input[str] target_ip: [string] In case the target NIC has multiple IP addresses, only traffic directed to the respective IP address of the NIC is allowed. Value null allows all target IPs.
        :param pulumi.Input[str] type: [string] The type of firewall rule. If is not specified, it will take the default value INGRESS.
        """
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        pulumi.set(__self__, "nic_id", nic_id)
        pulumi.set(__self__, "protocol", protocol)
        pulumi.set(__self__, "server_id", server_id)
        if icmp_code is not None:
            pulumi.set(__self__, "icmp_code", icmp_code)
        if icmp_type is not None:
            pulumi.set(__self__, "icmp_type", icmp_type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if port_range_end is not None:
            pulumi.set(__self__, "port_range_end", port_range_end)
        if port_range_start is not None:
            pulumi.set(__self__, "port_range_start", port_range_start)
        if source_ip is not None:
            pulumi.set(__self__, "source_ip", source_ip)
        if source_mac is not None:
            pulumi.set(__self__, "source_mac", source_mac)
        if target_ip is not None:
            pulumi.set(__self__, "target_ip", target_ip)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> pulumi.Input[str]:
        """
        [string] The Virtual Data Center ID.
        """
        return pulumi.get(self, "datacenter_id")

    @datacenter_id.setter
    def datacenter_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "datacenter_id", value)

    @property
    @pulumi.getter(name="nicId")
    def nic_id(self) -> pulumi.Input[str]:
        """
        [string] The NIC ID.
        """
        return pulumi.get(self, "nic_id")

    @nic_id.setter
    def nic_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "nic_id", value)

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[str]:
        """
        [string] The protocol for the rule: TCP, UDP, ICMP, ANY. Property cannot be modified after creation (disallowed in update requests).
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: pulumi.Input[str]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Input[str]:
        """
        [string] The Server ID.
        """
        return pulumi.get(self, "server_id")

    @server_id.setter
    def server_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_id", value)

    @property
    @pulumi.getter(name="icmpCode")
    def icmp_code(self) -> Optional[pulumi.Input[str]]:
        """
        [int] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen.
        """
        return pulumi.get(self, "icmp_code")

    @icmp_code.setter
    def icmp_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icmp_code", value)

    @property
    @pulumi.getter(name="icmpType")
    def icmp_type(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen. Value null allows all codes.
        """
        return pulumi.get(self, "icmp_type")

    @icmp_type.setter
    def icmp_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icmp_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The name of the firewall rule.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="portRangeEnd")
    def port_range_end(self) -> Optional[pulumi.Input[int]]:
        """
        [int] Defines the end range of the allowed port (from 1 to 65534) if the protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
        """
        return pulumi.get(self, "port_range_end")

    @port_range_end.setter
    def port_range_end(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port_range_end", value)

    @property
    @pulumi.getter(name="portRangeStart")
    def port_range_start(self) -> Optional[pulumi.Input[int]]:
        """
        [int] Defines the start range of the allowed port (from 1 to 65534) if protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
        """
        return pulumi.get(self, "port_range_start")

    @port_range_start.setter
    def port_range_start(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port_range_start", value)

    @property
    @pulumi.getter(name="sourceIp")
    def source_ip(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Only traffic originating from the respective IPv4 address is allowed. Value null allows all source IPs.
        """
        return pulumi.get(self, "source_ip")

    @source_ip.setter
    def source_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_ip", value)

    @property
    @pulumi.getter(name="sourceMac")
    def source_mac(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Only traffic originating from the respective MAC address is allowed. Valid format: aa:bb:cc:dd:ee:ff. Value null allows all source MAC address. Valid format: aa:bb:cc:dd:ee:ff.
        """
        return pulumi.get(self, "source_mac")

    @source_mac.setter
    def source_mac(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_mac", value)

    @property
    @pulumi.getter(name="targetIp")
    def target_ip(self) -> Optional[pulumi.Input[str]]:
        """
        [string] In case the target NIC has multiple IP addresses, only traffic directed to the respective IP address of the NIC is allowed. Value null allows all target IPs.
        """
        return pulumi.get(self, "target_ip")

    @target_ip.setter
    def target_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_ip", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The type of firewall rule. If is not specified, it will take the default value INGRESS.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class _FirewallState:
    def __init__(__self__, *,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 icmp_code: Optional[pulumi.Input[str]] = None,
                 icmp_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nic_id: Optional[pulumi.Input[str]] = None,
                 port_range_end: Optional[pulumi.Input[int]] = None,
                 port_range_start: Optional[pulumi.Input[int]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 source_ip: Optional[pulumi.Input[str]] = None,
                 source_mac: Optional[pulumi.Input[str]] = None,
                 target_ip: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Firewall resources.
        :param pulumi.Input[str] datacenter_id: [string] The Virtual Data Center ID.
        :param pulumi.Input[str] icmp_code: [int] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen.
        :param pulumi.Input[str] icmp_type: [string] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen. Value null allows all codes.
        :param pulumi.Input[str] name: [string] The name of the firewall rule.
        :param pulumi.Input[str] nic_id: [string] The NIC ID.
        :param pulumi.Input[int] port_range_end: [int] Defines the end range of the allowed port (from 1 to 65534) if the protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
        :param pulumi.Input[int] port_range_start: [int] Defines the start range of the allowed port (from 1 to 65534) if protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
        :param pulumi.Input[str] protocol: [string] The protocol for the rule: TCP, UDP, ICMP, ANY. Property cannot be modified after creation (disallowed in update requests).
        :param pulumi.Input[str] server_id: [string] The Server ID.
        :param pulumi.Input[str] source_ip: [string] Only traffic originating from the respective IPv4 address is allowed. Value null allows all source IPs.
        :param pulumi.Input[str] source_mac: [string] Only traffic originating from the respective MAC address is allowed. Valid format: aa:bb:cc:dd:ee:ff. Value null allows all source MAC address. Valid format: aa:bb:cc:dd:ee:ff.
        :param pulumi.Input[str] target_ip: [string] In case the target NIC has multiple IP addresses, only traffic directed to the respective IP address of the NIC is allowed. Value null allows all target IPs.
        :param pulumi.Input[str] type: [string] The type of firewall rule. If is not specified, it will take the default value INGRESS.
        """
        if datacenter_id is not None:
            pulumi.set(__self__, "datacenter_id", datacenter_id)
        if icmp_code is not None:
            pulumi.set(__self__, "icmp_code", icmp_code)
        if icmp_type is not None:
            pulumi.set(__self__, "icmp_type", icmp_type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if nic_id is not None:
            pulumi.set(__self__, "nic_id", nic_id)
        if port_range_end is not None:
            pulumi.set(__self__, "port_range_end", port_range_end)
        if port_range_start is not None:
            pulumi.set(__self__, "port_range_start", port_range_start)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)
        if server_id is not None:
            pulumi.set(__self__, "server_id", server_id)
        if source_ip is not None:
            pulumi.set(__self__, "source_ip", source_ip)
        if source_mac is not None:
            pulumi.set(__self__, "source_mac", source_mac)
        if target_ip is not None:
            pulumi.set(__self__, "target_ip", target_ip)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The Virtual Data Center ID.
        """
        return pulumi.get(self, "datacenter_id")

    @datacenter_id.setter
    def datacenter_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datacenter_id", value)

    @property
    @pulumi.getter(name="icmpCode")
    def icmp_code(self) -> Optional[pulumi.Input[str]]:
        """
        [int] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen.
        """
        return pulumi.get(self, "icmp_code")

    @icmp_code.setter
    def icmp_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icmp_code", value)

    @property
    @pulumi.getter(name="icmpType")
    def icmp_type(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen. Value null allows all codes.
        """
        return pulumi.get(self, "icmp_type")

    @icmp_type.setter
    def icmp_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icmp_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The name of the firewall rule.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="nicId")
    def nic_id(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The NIC ID.
        """
        return pulumi.get(self, "nic_id")

    @nic_id.setter
    def nic_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "nic_id", value)

    @property
    @pulumi.getter(name="portRangeEnd")
    def port_range_end(self) -> Optional[pulumi.Input[int]]:
        """
        [int] Defines the end range of the allowed port (from 1 to 65534) if the protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
        """
        return pulumi.get(self, "port_range_end")

    @port_range_end.setter
    def port_range_end(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port_range_end", value)

    @property
    @pulumi.getter(name="portRangeStart")
    def port_range_start(self) -> Optional[pulumi.Input[int]]:
        """
        [int] Defines the start range of the allowed port (from 1 to 65534) if protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
        """
        return pulumi.get(self, "port_range_start")

    @port_range_start.setter
    def port_range_start(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port_range_start", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The protocol for the rule: TCP, UDP, ICMP, ANY. Property cannot be modified after creation (disallowed in update requests).
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The Server ID.
        """
        return pulumi.get(self, "server_id")

    @server_id.setter
    def server_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_id", value)

    @property
    @pulumi.getter(name="sourceIp")
    def source_ip(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Only traffic originating from the respective IPv4 address is allowed. Value null allows all source IPs.
        """
        return pulumi.get(self, "source_ip")

    @source_ip.setter
    def source_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_ip", value)

    @property
    @pulumi.getter(name="sourceMac")
    def source_mac(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Only traffic originating from the respective MAC address is allowed. Valid format: aa:bb:cc:dd:ee:ff. Value null allows all source MAC address. Valid format: aa:bb:cc:dd:ee:ff.
        """
        return pulumi.get(self, "source_mac")

    @source_mac.setter
    def source_mac(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_mac", value)

    @property
    @pulumi.getter(name="targetIp")
    def target_ip(self) -> Optional[pulumi.Input[str]]:
        """
        [string] In case the target NIC has multiple IP addresses, only traffic directed to the respective IP address of the NIC is allowed. Value null allows all target IPs.
        """
        return pulumi.get(self, "target_ip")

    @target_ip.setter
    def target_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_ip", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The type of firewall rule. If is not specified, it will take the default value INGRESS.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class Firewall(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 icmp_code: Optional[pulumi.Input[str]] = None,
                 icmp_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nic_id: Optional[pulumi.Input[str]] = None,
                 port_range_end: Optional[pulumi.Input[int]] = None,
                 port_range_start: Optional[pulumi.Input[int]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 source_ip: Optional[pulumi.Input[str]] = None,
                 source_mac: Optional[pulumi.Input[str]] = None,
                 target_ip: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a set of **Firewall Rules** on IonosCloud.

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
            location=example_datacenter.location,
            size=2)
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
            ))
        example_nic = ionoscloud.compute.Nic("exampleNic",
            datacenter_id=example_datacenter.id,
            server_id=example_server.id,
            lan=2,
            dhcp=True,
            firewall_active=True)
        example_firewall = ionoscloud.compute.Firewall("exampleFirewall",
            datacenter_id=example_datacenter.id,
            server_id=example_server.id,
            nic_id=example_nic.id,
            protocol="ICMP",
            source_mac="00:0a:95:9d:68:16",
            source_ip=example_ip_block.ips[0],
            target_ip=example_ip_block.ips[1],
            icmp_type="1",
            icmp_code="8",
            type="INGRESS")
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        Resource Firewall can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import ionoscloud:compute/firewall:Firewall myfwrule {datacenter uuid}/{server uuid}/{nic uuid}/{firewall uuid}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] datacenter_id: [string] The Virtual Data Center ID.
        :param pulumi.Input[str] icmp_code: [int] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen.
        :param pulumi.Input[str] icmp_type: [string] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen. Value null allows all codes.
        :param pulumi.Input[str] name: [string] The name of the firewall rule.
        :param pulumi.Input[str] nic_id: [string] The NIC ID.
        :param pulumi.Input[int] port_range_end: [int] Defines the end range of the allowed port (from 1 to 65534) if the protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
        :param pulumi.Input[int] port_range_start: [int] Defines the start range of the allowed port (from 1 to 65534) if protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
        :param pulumi.Input[str] protocol: [string] The protocol for the rule: TCP, UDP, ICMP, ANY. Property cannot be modified after creation (disallowed in update requests).
        :param pulumi.Input[str] server_id: [string] The Server ID.
        :param pulumi.Input[str] source_ip: [string] Only traffic originating from the respective IPv4 address is allowed. Value null allows all source IPs.
        :param pulumi.Input[str] source_mac: [string] Only traffic originating from the respective MAC address is allowed. Valid format: aa:bb:cc:dd:ee:ff. Value null allows all source MAC address. Valid format: aa:bb:cc:dd:ee:ff.
        :param pulumi.Input[str] target_ip: [string] In case the target NIC has multiple IP addresses, only traffic directed to the respective IP address of the NIC is allowed. Value null allows all target IPs.
        :param pulumi.Input[str] type: [string] The type of firewall rule. If is not specified, it will take the default value INGRESS.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FirewallArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a set of **Firewall Rules** on IonosCloud.

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
            location=example_datacenter.location,
            size=2)
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
            ))
        example_nic = ionoscloud.compute.Nic("exampleNic",
            datacenter_id=example_datacenter.id,
            server_id=example_server.id,
            lan=2,
            dhcp=True,
            firewall_active=True)
        example_firewall = ionoscloud.compute.Firewall("exampleFirewall",
            datacenter_id=example_datacenter.id,
            server_id=example_server.id,
            nic_id=example_nic.id,
            protocol="ICMP",
            source_mac="00:0a:95:9d:68:16",
            source_ip=example_ip_block.ips[0],
            target_ip=example_ip_block.ips[1],
            icmp_type="1",
            icmp_code="8",
            type="INGRESS")
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        Resource Firewall can be imported using the `resource id`, e.g.

        ```sh
        $ pulumi import ionoscloud:compute/firewall:Firewall myfwrule {datacenter uuid}/{server uuid}/{nic uuid}/{firewall uuid}
        ```

        :param str resource_name: The name of the resource.
        :param FirewallArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FirewallArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 icmp_code: Optional[pulumi.Input[str]] = None,
                 icmp_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nic_id: Optional[pulumi.Input[str]] = None,
                 port_range_end: Optional[pulumi.Input[int]] = None,
                 port_range_start: Optional[pulumi.Input[int]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 source_ip: Optional[pulumi.Input[str]] = None,
                 source_mac: Optional[pulumi.Input[str]] = None,
                 target_ip: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FirewallArgs.__new__(FirewallArgs)

            if datacenter_id is None and not opts.urn:
                raise TypeError("Missing required property 'datacenter_id'")
            __props__.__dict__["datacenter_id"] = datacenter_id
            __props__.__dict__["icmp_code"] = icmp_code
            __props__.__dict__["icmp_type"] = icmp_type
            __props__.__dict__["name"] = name
            if nic_id is None and not opts.urn:
                raise TypeError("Missing required property 'nic_id'")
            __props__.__dict__["nic_id"] = nic_id
            __props__.__dict__["port_range_end"] = port_range_end
            __props__.__dict__["port_range_start"] = port_range_start
            if protocol is None and not opts.urn:
                raise TypeError("Missing required property 'protocol'")
            __props__.__dict__["protocol"] = protocol
            if server_id is None and not opts.urn:
                raise TypeError("Missing required property 'server_id'")
            __props__.__dict__["server_id"] = server_id
            __props__.__dict__["source_ip"] = source_ip
            __props__.__dict__["source_mac"] = source_mac
            __props__.__dict__["target_ip"] = target_ip
            __props__.__dict__["type"] = type
        super(Firewall, __self__).__init__(
            'ionoscloud:compute/firewall:Firewall',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            datacenter_id: Optional[pulumi.Input[str]] = None,
            icmp_code: Optional[pulumi.Input[str]] = None,
            icmp_type: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            nic_id: Optional[pulumi.Input[str]] = None,
            port_range_end: Optional[pulumi.Input[int]] = None,
            port_range_start: Optional[pulumi.Input[int]] = None,
            protocol: Optional[pulumi.Input[str]] = None,
            server_id: Optional[pulumi.Input[str]] = None,
            source_ip: Optional[pulumi.Input[str]] = None,
            source_mac: Optional[pulumi.Input[str]] = None,
            target_ip: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'Firewall':
        """
        Get an existing Firewall resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] datacenter_id: [string] The Virtual Data Center ID.
        :param pulumi.Input[str] icmp_code: [int] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen.
        :param pulumi.Input[str] icmp_type: [string] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen. Value null allows all codes.
        :param pulumi.Input[str] name: [string] The name of the firewall rule.
        :param pulumi.Input[str] nic_id: [string] The NIC ID.
        :param pulumi.Input[int] port_range_end: [int] Defines the end range of the allowed port (from 1 to 65534) if the protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
        :param pulumi.Input[int] port_range_start: [int] Defines the start range of the allowed port (from 1 to 65534) if protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
        :param pulumi.Input[str] protocol: [string] The protocol for the rule: TCP, UDP, ICMP, ANY. Property cannot be modified after creation (disallowed in update requests).
        :param pulumi.Input[str] server_id: [string] The Server ID.
        :param pulumi.Input[str] source_ip: [string] Only traffic originating from the respective IPv4 address is allowed. Value null allows all source IPs.
        :param pulumi.Input[str] source_mac: [string] Only traffic originating from the respective MAC address is allowed. Valid format: aa:bb:cc:dd:ee:ff. Value null allows all source MAC address. Valid format: aa:bb:cc:dd:ee:ff.
        :param pulumi.Input[str] target_ip: [string] In case the target NIC has multiple IP addresses, only traffic directed to the respective IP address of the NIC is allowed. Value null allows all target IPs.
        :param pulumi.Input[str] type: [string] The type of firewall rule. If is not specified, it will take the default value INGRESS.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FirewallState.__new__(_FirewallState)

        __props__.__dict__["datacenter_id"] = datacenter_id
        __props__.__dict__["icmp_code"] = icmp_code
        __props__.__dict__["icmp_type"] = icmp_type
        __props__.__dict__["name"] = name
        __props__.__dict__["nic_id"] = nic_id
        __props__.__dict__["port_range_end"] = port_range_end
        __props__.__dict__["port_range_start"] = port_range_start
        __props__.__dict__["protocol"] = protocol
        __props__.__dict__["server_id"] = server_id
        __props__.__dict__["source_ip"] = source_ip
        __props__.__dict__["source_mac"] = source_mac
        __props__.__dict__["target_ip"] = target_ip
        __props__.__dict__["type"] = type
        return Firewall(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> pulumi.Output[str]:
        """
        [string] The Virtual Data Center ID.
        """
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter(name="icmpCode")
    def icmp_code(self) -> pulumi.Output[Optional[str]]:
        """
        [int] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen.
        """
        return pulumi.get(self, "icmp_code")

    @property
    @pulumi.getter(name="icmpType")
    def icmp_type(self) -> pulumi.Output[Optional[str]]:
        """
        [string] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen. Value null allows all codes.
        """
        return pulumi.get(self, "icmp_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        [string] The name of the firewall rule.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nicId")
    def nic_id(self) -> pulumi.Output[str]:
        """
        [string] The NIC ID.
        """
        return pulumi.get(self, "nic_id")

    @property
    @pulumi.getter(name="portRangeEnd")
    def port_range_end(self) -> pulumi.Output[Optional[int]]:
        """
        [int] Defines the end range of the allowed port (from 1 to 65534) if the protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
        """
        return pulumi.get(self, "port_range_end")

    @property
    @pulumi.getter(name="portRangeStart")
    def port_range_start(self) -> pulumi.Output[Optional[int]]:
        """
        [int] Defines the start range of the allowed port (from 1 to 65534) if protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
        """
        return pulumi.get(self, "port_range_start")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[str]:
        """
        [string] The protocol for the rule: TCP, UDP, ICMP, ANY. Property cannot be modified after creation (disallowed in update requests).
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Output[str]:
        """
        [string] The Server ID.
        """
        return pulumi.get(self, "server_id")

    @property
    @pulumi.getter(name="sourceIp")
    def source_ip(self) -> pulumi.Output[str]:
        """
        [string] Only traffic originating from the respective IPv4 address is allowed. Value null allows all source IPs.
        """
        return pulumi.get(self, "source_ip")

    @property
    @pulumi.getter(name="sourceMac")
    def source_mac(self) -> pulumi.Output[Optional[str]]:
        """
        [string] Only traffic originating from the respective MAC address is allowed. Valid format: aa:bb:cc:dd:ee:ff. Value null allows all source MAC address. Valid format: aa:bb:cc:dd:ee:ff.
        """
        return pulumi.get(self, "source_mac")

    @property
    @pulumi.getter(name="targetIp")
    def target_ip(self) -> pulumi.Output[str]:
        """
        [string] In case the target NIC has multiple IP addresses, only traffic directed to the respective IP address of the NIC is allowed. Value null allows all target IPs.
        """
        return pulumi.get(self, "target_ip")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        [string] The type of firewall rule. If is not specified, it will take the default value INGRESS.
        """
        return pulumi.get(self, "type")

