# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['BalancerArgs', 'Balancer']

@pulumi.input_type
class BalancerArgs:
    def __init__(__self__, *,
                 datacenter_id: pulumi.Input[str],
                 listener_lan: pulumi.Input[int],
                 target_lan: pulumi.Input[int],
                 central_logging: Optional[pulumi.Input[bool]] = None,
                 flowlog: Optional[pulumi.Input['BalancerFlowlogArgs']] = None,
                 ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 lb_private_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 logging_format: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Balancer resource.
        :param pulumi.Input[str] datacenter_id: [string] ID of the datacenter.
        :param pulumi.Input[int] listener_lan: [int] ID of the listening (inbound) LAN.
        :param pulumi.Input[int] target_lan: [int] ID of the balanced private target LAN (outbound).
        :param pulumi.Input[bool] central_logging: [bool] Turn logging on and off for this product. Default value is 'false'.
        :param pulumi.Input['BalancerFlowlogArgs'] flowlog: [list] Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ips: [set] Collection of the Application Load Balancer IP addresses. (Inbound and outbound) IPs of the listenerLan are customer-reserved public IPs for the public Load Balancers, and private IPs for the private Load Balancers.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] lb_private_ips: [set] Collection of private IP addresses with the subnet mask of the Application Load Balancer. IPs must contain valid a subnet mask. If no IP is provided, the system will generate an IP with /24 subnet.
        :param pulumi.Input[str] logging_format: Specifies the format of the logs.
        :param pulumi.Input[str] name: [string] Specifies the name of the flow log.
               
               ⚠️ **Note:**: Removing the `flowlog` forces re-creation of the application load balancer resource.
        """
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        pulumi.set(__self__, "listener_lan", listener_lan)
        pulumi.set(__self__, "target_lan", target_lan)
        if central_logging is not None:
            pulumi.set(__self__, "central_logging", central_logging)
        if flowlog is not None:
            pulumi.set(__self__, "flowlog", flowlog)
        if ips is not None:
            pulumi.set(__self__, "ips", ips)
        if lb_private_ips is not None:
            pulumi.set(__self__, "lb_private_ips", lb_private_ips)
        if logging_format is not None:
            pulumi.set(__self__, "logging_format", logging_format)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> pulumi.Input[str]:
        """
        [string] ID of the datacenter.
        """
        return pulumi.get(self, "datacenter_id")

    @datacenter_id.setter
    def datacenter_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "datacenter_id", value)

    @property
    @pulumi.getter(name="listenerLan")
    def listener_lan(self) -> pulumi.Input[int]:
        """
        [int] ID of the listening (inbound) LAN.
        """
        return pulumi.get(self, "listener_lan")

    @listener_lan.setter
    def listener_lan(self, value: pulumi.Input[int]):
        pulumi.set(self, "listener_lan", value)

    @property
    @pulumi.getter(name="targetLan")
    def target_lan(self) -> pulumi.Input[int]:
        """
        [int] ID of the balanced private target LAN (outbound).
        """
        return pulumi.get(self, "target_lan")

    @target_lan.setter
    def target_lan(self, value: pulumi.Input[int]):
        pulumi.set(self, "target_lan", value)

    @property
    @pulumi.getter(name="centralLogging")
    def central_logging(self) -> Optional[pulumi.Input[bool]]:
        """
        [bool] Turn logging on and off for this product. Default value is 'false'.
        """
        return pulumi.get(self, "central_logging")

    @central_logging.setter
    def central_logging(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "central_logging", value)

    @property
    @pulumi.getter
    def flowlog(self) -> Optional[pulumi.Input['BalancerFlowlogArgs']]:
        """
        [list] Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
        """
        return pulumi.get(self, "flowlog")

    @flowlog.setter
    def flowlog(self, value: Optional[pulumi.Input['BalancerFlowlogArgs']]):
        pulumi.set(self, "flowlog", value)

    @property
    @pulumi.getter
    def ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        [set] Collection of the Application Load Balancer IP addresses. (Inbound and outbound) IPs of the listenerLan are customer-reserved public IPs for the public Load Balancers, and private IPs for the private Load Balancers.
        """
        return pulumi.get(self, "ips")

    @ips.setter
    def ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ips", value)

    @property
    @pulumi.getter(name="lbPrivateIps")
    def lb_private_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        [set] Collection of private IP addresses with the subnet mask of the Application Load Balancer. IPs must contain valid a subnet mask. If no IP is provided, the system will generate an IP with /24 subnet.
        """
        return pulumi.get(self, "lb_private_ips")

    @lb_private_ips.setter
    def lb_private_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "lb_private_ips", value)

    @property
    @pulumi.getter(name="loggingFormat")
    def logging_format(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the format of the logs.
        """
        return pulumi.get(self, "logging_format")

    @logging_format.setter
    def logging_format(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "logging_format", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Specifies the name of the flow log.

        ⚠️ **Note:**: Removing the `flowlog` forces re-creation of the application load balancer resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _BalancerState:
    def __init__(__self__, *,
                 central_logging: Optional[pulumi.Input[bool]] = None,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 flowlog: Optional[pulumi.Input['BalancerFlowlogArgs']] = None,
                 ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 lb_private_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 listener_lan: Optional[pulumi.Input[int]] = None,
                 logging_format: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 target_lan: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Balancer resources.
        :param pulumi.Input[bool] central_logging: [bool] Turn logging on and off for this product. Default value is 'false'.
        :param pulumi.Input[str] datacenter_id: [string] ID of the datacenter.
        :param pulumi.Input['BalancerFlowlogArgs'] flowlog: [list] Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ips: [set] Collection of the Application Load Balancer IP addresses. (Inbound and outbound) IPs of the listenerLan are customer-reserved public IPs for the public Load Balancers, and private IPs for the private Load Balancers.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] lb_private_ips: [set] Collection of private IP addresses with the subnet mask of the Application Load Balancer. IPs must contain valid a subnet mask. If no IP is provided, the system will generate an IP with /24 subnet.
        :param pulumi.Input[int] listener_lan: [int] ID of the listening (inbound) LAN.
        :param pulumi.Input[str] logging_format: Specifies the format of the logs.
        :param pulumi.Input[str] name: [string] Specifies the name of the flow log.
               
               ⚠️ **Note:**: Removing the `flowlog` forces re-creation of the application load balancer resource.
        :param pulumi.Input[int] target_lan: [int] ID of the balanced private target LAN (outbound).
        """
        if central_logging is not None:
            pulumi.set(__self__, "central_logging", central_logging)
        if datacenter_id is not None:
            pulumi.set(__self__, "datacenter_id", datacenter_id)
        if flowlog is not None:
            pulumi.set(__self__, "flowlog", flowlog)
        if ips is not None:
            pulumi.set(__self__, "ips", ips)
        if lb_private_ips is not None:
            pulumi.set(__self__, "lb_private_ips", lb_private_ips)
        if listener_lan is not None:
            pulumi.set(__self__, "listener_lan", listener_lan)
        if logging_format is not None:
            pulumi.set(__self__, "logging_format", logging_format)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if target_lan is not None:
            pulumi.set(__self__, "target_lan", target_lan)

    @property
    @pulumi.getter(name="centralLogging")
    def central_logging(self) -> Optional[pulumi.Input[bool]]:
        """
        [bool] Turn logging on and off for this product. Default value is 'false'.
        """
        return pulumi.get(self, "central_logging")

    @central_logging.setter
    def central_logging(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "central_logging", value)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> Optional[pulumi.Input[str]]:
        """
        [string] ID of the datacenter.
        """
        return pulumi.get(self, "datacenter_id")

    @datacenter_id.setter
    def datacenter_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datacenter_id", value)

    @property
    @pulumi.getter
    def flowlog(self) -> Optional[pulumi.Input['BalancerFlowlogArgs']]:
        """
        [list] Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
        """
        return pulumi.get(self, "flowlog")

    @flowlog.setter
    def flowlog(self, value: Optional[pulumi.Input['BalancerFlowlogArgs']]):
        pulumi.set(self, "flowlog", value)

    @property
    @pulumi.getter
    def ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        [set] Collection of the Application Load Balancer IP addresses. (Inbound and outbound) IPs of the listenerLan are customer-reserved public IPs for the public Load Balancers, and private IPs for the private Load Balancers.
        """
        return pulumi.get(self, "ips")

    @ips.setter
    def ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ips", value)

    @property
    @pulumi.getter(name="lbPrivateIps")
    def lb_private_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        [set] Collection of private IP addresses with the subnet mask of the Application Load Balancer. IPs must contain valid a subnet mask. If no IP is provided, the system will generate an IP with /24 subnet.
        """
        return pulumi.get(self, "lb_private_ips")

    @lb_private_ips.setter
    def lb_private_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "lb_private_ips", value)

    @property
    @pulumi.getter(name="listenerLan")
    def listener_lan(self) -> Optional[pulumi.Input[int]]:
        """
        [int] ID of the listening (inbound) LAN.
        """
        return pulumi.get(self, "listener_lan")

    @listener_lan.setter
    def listener_lan(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "listener_lan", value)

    @property
    @pulumi.getter(name="loggingFormat")
    def logging_format(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the format of the logs.
        """
        return pulumi.get(self, "logging_format")

    @logging_format.setter
    def logging_format(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "logging_format", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Specifies the name of the flow log.

        ⚠️ **Note:**: Removing the `flowlog` forces re-creation of the application load balancer resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="targetLan")
    def target_lan(self) -> Optional[pulumi.Input[int]]:
        """
        [int] ID of the balanced private target LAN (outbound).
        """
        return pulumi.get(self, "target_lan")

    @target_lan.setter
    def target_lan(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "target_lan", value)


class Balancer(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 central_logging: Optional[pulumi.Input[bool]] = None,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 flowlog: Optional[pulumi.Input[pulumi.InputType['BalancerFlowlogArgs']]] = None,
                 ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 lb_private_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 listener_lan: Optional[pulumi.Input[int]] = None,
                 logging_format: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 target_lan: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Manages an **Application Load Balancer** on IonosCloud.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ionoscloud as ionoscloud

        example_datacenter = ionoscloud.compute.Datacenter("exampleDatacenter",
            location="us/las",
            description="datacenter description",
            sec_auth_protection=False)
        example1 = ionoscloud.compute.Lan("example1",
            datacenter_id=example_datacenter.id,
            public=True)
        example2 = ionoscloud.compute.Lan("example2",
            datacenter_id=example_datacenter.id,
            public=True)
        example_balancer = ionoscloud.alb.Balancer("exampleBalancer",
            datacenter_id=example_datacenter.id,
            listener_lan=example1.id,
            ips=["10.12.118.224"],
            target_lan=example2.id,
            lb_private_ips=["10.13.72.225/24"],
            central_logging=True,
            logging_format="%{+Q}o %{-Q}ci - - [%trg] %r %ST %B \\"\\" \\"\\" %cp %ms %ft %b %s %TR %Tw %Tc %Tr %Ta %tsc %ac %fc %bc %sc %rc %sq %bq %CC %CS %hrl %hsl")
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        Resource Application Load Balancer can be imported using the `resource id` and `datacenter id`, e.g.

        ```sh
        $ pulumi import ionoscloud:alb/balancer:Balancer myalb {datacenter uuid}/{applicationLoadBalancer uuid}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] central_logging: [bool] Turn logging on and off for this product. Default value is 'false'.
        :param pulumi.Input[str] datacenter_id: [string] ID of the datacenter.
        :param pulumi.Input[pulumi.InputType['BalancerFlowlogArgs']] flowlog: [list] Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ips: [set] Collection of the Application Load Balancer IP addresses. (Inbound and outbound) IPs of the listenerLan are customer-reserved public IPs for the public Load Balancers, and private IPs for the private Load Balancers.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] lb_private_ips: [set] Collection of private IP addresses with the subnet mask of the Application Load Balancer. IPs must contain valid a subnet mask. If no IP is provided, the system will generate an IP with /24 subnet.
        :param pulumi.Input[int] listener_lan: [int] ID of the listening (inbound) LAN.
        :param pulumi.Input[str] logging_format: Specifies the format of the logs.
        :param pulumi.Input[str] name: [string] Specifies the name of the flow log.
               
               ⚠️ **Note:**: Removing the `flowlog` forces re-creation of the application load balancer resource.
        :param pulumi.Input[int] target_lan: [int] ID of the balanced private target LAN (outbound).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BalancerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an **Application Load Balancer** on IonosCloud.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ionoscloud as ionoscloud

        example_datacenter = ionoscloud.compute.Datacenter("exampleDatacenter",
            location="us/las",
            description="datacenter description",
            sec_auth_protection=False)
        example1 = ionoscloud.compute.Lan("example1",
            datacenter_id=example_datacenter.id,
            public=True)
        example2 = ionoscloud.compute.Lan("example2",
            datacenter_id=example_datacenter.id,
            public=True)
        example_balancer = ionoscloud.alb.Balancer("exampleBalancer",
            datacenter_id=example_datacenter.id,
            listener_lan=example1.id,
            ips=["10.12.118.224"],
            target_lan=example2.id,
            lb_private_ips=["10.13.72.225/24"],
            central_logging=True,
            logging_format="%{+Q}o %{-Q}ci - - [%trg] %r %ST %B \\"\\" \\"\\" %cp %ms %ft %b %s %TR %Tw %Tc %Tr %Ta %tsc %ac %fc %bc %sc %rc %sq %bq %CC %CS %hrl %hsl")
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        Resource Application Load Balancer can be imported using the `resource id` and `datacenter id`, e.g.

        ```sh
        $ pulumi import ionoscloud:alb/balancer:Balancer myalb {datacenter uuid}/{applicationLoadBalancer uuid}
        ```

        :param str resource_name: The name of the resource.
        :param BalancerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BalancerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 central_logging: Optional[pulumi.Input[bool]] = None,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 flowlog: Optional[pulumi.Input[pulumi.InputType['BalancerFlowlogArgs']]] = None,
                 ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 lb_private_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 listener_lan: Optional[pulumi.Input[int]] = None,
                 logging_format: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 target_lan: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BalancerArgs.__new__(BalancerArgs)

            __props__.__dict__["central_logging"] = central_logging
            if datacenter_id is None and not opts.urn:
                raise TypeError("Missing required property 'datacenter_id'")
            __props__.__dict__["datacenter_id"] = datacenter_id
            __props__.__dict__["flowlog"] = flowlog
            __props__.__dict__["ips"] = ips
            __props__.__dict__["lb_private_ips"] = lb_private_ips
            if listener_lan is None and not opts.urn:
                raise TypeError("Missing required property 'listener_lan'")
            __props__.__dict__["listener_lan"] = listener_lan
            __props__.__dict__["logging_format"] = logging_format
            __props__.__dict__["name"] = name
            if target_lan is None and not opts.urn:
                raise TypeError("Missing required property 'target_lan'")
            __props__.__dict__["target_lan"] = target_lan
        super(Balancer, __self__).__init__(
            'ionoscloud:alb/balancer:Balancer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            central_logging: Optional[pulumi.Input[bool]] = None,
            datacenter_id: Optional[pulumi.Input[str]] = None,
            flowlog: Optional[pulumi.Input[pulumi.InputType['BalancerFlowlogArgs']]] = None,
            ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            lb_private_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            listener_lan: Optional[pulumi.Input[int]] = None,
            logging_format: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            target_lan: Optional[pulumi.Input[int]] = None) -> 'Balancer':
        """
        Get an existing Balancer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] central_logging: [bool] Turn logging on and off for this product. Default value is 'false'.
        :param pulumi.Input[str] datacenter_id: [string] ID of the datacenter.
        :param pulumi.Input[pulumi.InputType['BalancerFlowlogArgs']] flowlog: [list] Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ips: [set] Collection of the Application Load Balancer IP addresses. (Inbound and outbound) IPs of the listenerLan are customer-reserved public IPs for the public Load Balancers, and private IPs for the private Load Balancers.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] lb_private_ips: [set] Collection of private IP addresses with the subnet mask of the Application Load Balancer. IPs must contain valid a subnet mask. If no IP is provided, the system will generate an IP with /24 subnet.
        :param pulumi.Input[int] listener_lan: [int] ID of the listening (inbound) LAN.
        :param pulumi.Input[str] logging_format: Specifies the format of the logs.
        :param pulumi.Input[str] name: [string] Specifies the name of the flow log.
               
               ⚠️ **Note:**: Removing the `flowlog` forces re-creation of the application load balancer resource.
        :param pulumi.Input[int] target_lan: [int] ID of the balanced private target LAN (outbound).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BalancerState.__new__(_BalancerState)

        __props__.__dict__["central_logging"] = central_logging
        __props__.__dict__["datacenter_id"] = datacenter_id
        __props__.__dict__["flowlog"] = flowlog
        __props__.__dict__["ips"] = ips
        __props__.__dict__["lb_private_ips"] = lb_private_ips
        __props__.__dict__["listener_lan"] = listener_lan
        __props__.__dict__["logging_format"] = logging_format
        __props__.__dict__["name"] = name
        __props__.__dict__["target_lan"] = target_lan
        return Balancer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="centralLogging")
    def central_logging(self) -> pulumi.Output[Optional[bool]]:
        """
        [bool] Turn logging on and off for this product. Default value is 'false'.
        """
        return pulumi.get(self, "central_logging")

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> pulumi.Output[str]:
        """
        [string] ID of the datacenter.
        """
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter
    def flowlog(self) -> pulumi.Output[Optional['outputs.BalancerFlowlog']]:
        """
        [list] Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
        """
        return pulumi.get(self, "flowlog")

    @property
    @pulumi.getter
    def ips(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        [set] Collection of the Application Load Balancer IP addresses. (Inbound and outbound) IPs of the listenerLan are customer-reserved public IPs for the public Load Balancers, and private IPs for the private Load Balancers.
        """
        return pulumi.get(self, "ips")

    @property
    @pulumi.getter(name="lbPrivateIps")
    def lb_private_ips(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        [set] Collection of private IP addresses with the subnet mask of the Application Load Balancer. IPs must contain valid a subnet mask. If no IP is provided, the system will generate an IP with /24 subnet.
        """
        return pulumi.get(self, "lb_private_ips")

    @property
    @pulumi.getter(name="listenerLan")
    def listener_lan(self) -> pulumi.Output[int]:
        """
        [int] ID of the listening (inbound) LAN.
        """
        return pulumi.get(self, "listener_lan")

    @property
    @pulumi.getter(name="loggingFormat")
    def logging_format(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the format of the logs.
        """
        return pulumi.get(self, "logging_format")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        [string] Specifies the name of the flow log.

        ⚠️ **Note:**: Removing the `flowlog` forces re-creation of the application load balancer resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="targetLan")
    def target_lan(self) -> pulumi.Output[int]:
        """
        [int] ID of the balanced private target LAN (outbound).
        """
        return pulumi.get(self, "target_lan")

