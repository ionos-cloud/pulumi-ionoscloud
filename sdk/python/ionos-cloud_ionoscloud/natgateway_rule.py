# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['NatgatewayRuleArgs', 'NatgatewayRule']

@pulumi.input_type
class NatgatewayRuleArgs:
    def __init__(__self__, *,
                 datacenter_id: pulumi.Input[str],
                 natgateway_id: pulumi.Input[str],
                 public_ip: pulumi.Input[str],
                 source_subnet: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 target_port_range: Optional[pulumi.Input['NatgatewayRuleTargetPortRangeArgs']] = None,
                 target_subnet: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a NatgatewayRule resource.
        :param pulumi.Input[str] datacenter_id: [string] A Datacenter's UUID.
        :param pulumi.Input[str] natgateway_id: [string] Nat Gateway's UUID.
        :param pulumi.Input[str] public_ip: [string] Public IP address of the NAT gateway rule. Specifies the address used for masking outgoing packets source address field. Should be one of the customer reserved IP address already configured on the NAT gateway resource.
        :param pulumi.Input[str] source_subnet: [string] Source subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets source IP address.
        :param pulumi.Input[str] name: [string] Name of the NAT gateway rule.
        :param pulumi.Input[str] protocol: [string] Protocol of the NAT gateway rule. Defaults to ALL. If protocol is 'ICMP' then targetPortRange start and end cannot be set.
        :param pulumi.Input['NatgatewayRuleTargetPortRangeArgs'] target_port_range: Target port range of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on destination port. If none is provided, rule will match any port.
        :param pulumi.Input[str] target_subnet: [string] Target or destination subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets destination IP address. If none is provided, rule will match any address.
        :param pulumi.Input[str] type: [string] Type of the NAT gateway rule.
        """
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        pulumi.set(__self__, "natgateway_id", natgateway_id)
        pulumi.set(__self__, "public_ip", public_ip)
        pulumi.set(__self__, "source_subnet", source_subnet)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)
        if target_port_range is not None:
            pulumi.set(__self__, "target_port_range", target_port_range)
        if target_subnet is not None:
            pulumi.set(__self__, "target_subnet", target_subnet)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> pulumi.Input[str]:
        """
        [string] A Datacenter's UUID.
        """
        return pulumi.get(self, "datacenter_id")

    @datacenter_id.setter
    def datacenter_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "datacenter_id", value)

    @property
    @pulumi.getter(name="natgatewayId")
    def natgateway_id(self) -> pulumi.Input[str]:
        """
        [string] Nat Gateway's UUID.
        """
        return pulumi.get(self, "natgateway_id")

    @natgateway_id.setter
    def natgateway_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "natgateway_id", value)

    @property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> pulumi.Input[str]:
        """
        [string] Public IP address of the NAT gateway rule. Specifies the address used for masking outgoing packets source address field. Should be one of the customer reserved IP address already configured on the NAT gateway resource.
        """
        return pulumi.get(self, "public_ip")

    @public_ip.setter
    def public_ip(self, value: pulumi.Input[str]):
        pulumi.set(self, "public_ip", value)

    @property
    @pulumi.getter(name="sourceSubnet")
    def source_subnet(self) -> pulumi.Input[str]:
        """
        [string] Source subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets source IP address.
        """
        return pulumi.get(self, "source_subnet")

    @source_subnet.setter
    def source_subnet(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_subnet", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Name of the NAT gateway rule.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Protocol of the NAT gateway rule. Defaults to ALL. If protocol is 'ICMP' then targetPortRange start and end cannot be set.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter(name="targetPortRange")
    def target_port_range(self) -> Optional[pulumi.Input['NatgatewayRuleTargetPortRangeArgs']]:
        """
        Target port range of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on destination port. If none is provided, rule will match any port.
        """
        return pulumi.get(self, "target_port_range")

    @target_port_range.setter
    def target_port_range(self, value: Optional[pulumi.Input['NatgatewayRuleTargetPortRangeArgs']]):
        pulumi.set(self, "target_port_range", value)

    @property
    @pulumi.getter(name="targetSubnet")
    def target_subnet(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Target or destination subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets destination IP address. If none is provided, rule will match any address.
        """
        return pulumi.get(self, "target_subnet")

    @target_subnet.setter
    def target_subnet(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_subnet", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Type of the NAT gateway rule.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class _NatgatewayRuleState:
    def __init__(__self__, *,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 natgateway_id: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 public_ip: Optional[pulumi.Input[str]] = None,
                 source_subnet: Optional[pulumi.Input[str]] = None,
                 target_port_range: Optional[pulumi.Input['NatgatewayRuleTargetPortRangeArgs']] = None,
                 target_subnet: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering NatgatewayRule resources.
        :param pulumi.Input[str] datacenter_id: [string] A Datacenter's UUID.
        :param pulumi.Input[str] name: [string] Name of the NAT gateway rule.
        :param pulumi.Input[str] natgateway_id: [string] Nat Gateway's UUID.
        :param pulumi.Input[str] protocol: [string] Protocol of the NAT gateway rule. Defaults to ALL. If protocol is 'ICMP' then targetPortRange start and end cannot be set.
        :param pulumi.Input[str] public_ip: [string] Public IP address of the NAT gateway rule. Specifies the address used for masking outgoing packets source address field. Should be one of the customer reserved IP address already configured on the NAT gateway resource.
        :param pulumi.Input[str] source_subnet: [string] Source subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets source IP address.
        :param pulumi.Input['NatgatewayRuleTargetPortRangeArgs'] target_port_range: Target port range of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on destination port. If none is provided, rule will match any port.
        :param pulumi.Input[str] target_subnet: [string] Target or destination subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets destination IP address. If none is provided, rule will match any address.
        :param pulumi.Input[str] type: [string] Type of the NAT gateway rule.
        """
        if datacenter_id is not None:
            pulumi.set(__self__, "datacenter_id", datacenter_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if natgateway_id is not None:
            pulumi.set(__self__, "natgateway_id", natgateway_id)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)
        if public_ip is not None:
            pulumi.set(__self__, "public_ip", public_ip)
        if source_subnet is not None:
            pulumi.set(__self__, "source_subnet", source_subnet)
        if target_port_range is not None:
            pulumi.set(__self__, "target_port_range", target_port_range)
        if target_subnet is not None:
            pulumi.set(__self__, "target_subnet", target_subnet)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> Optional[pulumi.Input[str]]:
        """
        [string] A Datacenter's UUID.
        """
        return pulumi.get(self, "datacenter_id")

    @datacenter_id.setter
    def datacenter_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datacenter_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Name of the NAT gateway rule.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="natgatewayId")
    def natgateway_id(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Nat Gateway's UUID.
        """
        return pulumi.get(self, "natgateway_id")

    @natgateway_id.setter
    def natgateway_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "natgateway_id", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Protocol of the NAT gateway rule. Defaults to ALL. If protocol is 'ICMP' then targetPortRange start and end cannot be set.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Public IP address of the NAT gateway rule. Specifies the address used for masking outgoing packets source address field. Should be one of the customer reserved IP address already configured on the NAT gateway resource.
        """
        return pulumi.get(self, "public_ip")

    @public_ip.setter
    def public_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_ip", value)

    @property
    @pulumi.getter(name="sourceSubnet")
    def source_subnet(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Source subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets source IP address.
        """
        return pulumi.get(self, "source_subnet")

    @source_subnet.setter
    def source_subnet(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_subnet", value)

    @property
    @pulumi.getter(name="targetPortRange")
    def target_port_range(self) -> Optional[pulumi.Input['NatgatewayRuleTargetPortRangeArgs']]:
        """
        Target port range of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on destination port. If none is provided, rule will match any port.
        """
        return pulumi.get(self, "target_port_range")

    @target_port_range.setter
    def target_port_range(self, value: Optional[pulumi.Input['NatgatewayRuleTargetPortRangeArgs']]):
        pulumi.set(self, "target_port_range", value)

    @property
    @pulumi.getter(name="targetSubnet")
    def target_subnet(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Target or destination subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets destination IP address. If none is provided, rule will match any address.
        """
        return pulumi.get(self, "target_subnet")

    @target_subnet.setter
    def target_subnet(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_subnet", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Type of the NAT gateway rule.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class NatgatewayRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 natgateway_id: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 public_ip: Optional[pulumi.Input[str]] = None,
                 source_subnet: Optional[pulumi.Input[str]] = None,
                 target_port_range: Optional[pulumi.Input[pulumi.InputType['NatgatewayRuleTargetPortRangeArgs']]] = None,
                 target_subnet: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a **Nat Gateway Rule** on IonosCloud.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ionos-cloud_ionoscloud as ionoscloud

        example_datacenter = ionoscloud.compute.Datacenter("exampleDatacenter",
            location="us/las",
            description="Datacenter Description",
            sec_auth_protection=False)
        example_ip_block = ionoscloud.compute.IPBlock("exampleIPBlock",
            location="us/las",
            size=2)
        example_lan = ionoscloud.compute.Lan("exampleLan",
            datacenter_id=example_datacenter.id,
            public=True)
        example_natgateway = ionoscloud.Natgateway("exampleNatgateway",
            datacenter_id=example_datacenter.id,
            public_ips=[
                example_ip_block.ips[0],
                example_ip_block.ips[1],
            ],
            lans=[ionoscloud.NatgatewayLanArgs(
                id=example_lan.id,
                gateway_ips=["10.11.2.5"],
            )])
        example_natgateway_rule = ionoscloud.NatgatewayRule("exampleNatgatewayRule",
            datacenter_id=example_datacenter.id,
            natgateway_id=example_natgateway.id,
            type="SNAT",
            protocol="TCP",
            source_subnet="10.0.1.0/24",
            public_ip=example_ip_block.ips[0],
            target_subnet="10.0.1.0/24",
            target_port_range=ionoscloud.NatgatewayRuleTargetPortRangeArgs(
                start=500,
                end=1000,
            ))
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        A Nat Gateway Rule resource can be imported using its `resource id`, the `datacenter id` and the `natgateway id , e.g.

        ```sh
        $ pulumi import ionoscloud:index/natgatewayRule:NatgatewayRule my_natgateway_rule {datacenter uuid}/{nat gateway uuid}/{nat gateway rule uuid}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] datacenter_id: [string] A Datacenter's UUID.
        :param pulumi.Input[str] name: [string] Name of the NAT gateway rule.
        :param pulumi.Input[str] natgateway_id: [string] Nat Gateway's UUID.
        :param pulumi.Input[str] protocol: [string] Protocol of the NAT gateway rule. Defaults to ALL. If protocol is 'ICMP' then targetPortRange start and end cannot be set.
        :param pulumi.Input[str] public_ip: [string] Public IP address of the NAT gateway rule. Specifies the address used for masking outgoing packets source address field. Should be one of the customer reserved IP address already configured on the NAT gateway resource.
        :param pulumi.Input[str] source_subnet: [string] Source subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets source IP address.
        :param pulumi.Input[pulumi.InputType['NatgatewayRuleTargetPortRangeArgs']] target_port_range: Target port range of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on destination port. If none is provided, rule will match any port.
        :param pulumi.Input[str] target_subnet: [string] Target or destination subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets destination IP address. If none is provided, rule will match any address.
        :param pulumi.Input[str] type: [string] Type of the NAT gateway rule.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NatgatewayRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a **Nat Gateway Rule** on IonosCloud.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ionos-cloud_ionoscloud as ionoscloud

        example_datacenter = ionoscloud.compute.Datacenter("exampleDatacenter",
            location="us/las",
            description="Datacenter Description",
            sec_auth_protection=False)
        example_ip_block = ionoscloud.compute.IPBlock("exampleIPBlock",
            location="us/las",
            size=2)
        example_lan = ionoscloud.compute.Lan("exampleLan",
            datacenter_id=example_datacenter.id,
            public=True)
        example_natgateway = ionoscloud.Natgateway("exampleNatgateway",
            datacenter_id=example_datacenter.id,
            public_ips=[
                example_ip_block.ips[0],
                example_ip_block.ips[1],
            ],
            lans=[ionoscloud.NatgatewayLanArgs(
                id=example_lan.id,
                gateway_ips=["10.11.2.5"],
            )])
        example_natgateway_rule = ionoscloud.NatgatewayRule("exampleNatgatewayRule",
            datacenter_id=example_datacenter.id,
            natgateway_id=example_natgateway.id,
            type="SNAT",
            protocol="TCP",
            source_subnet="10.0.1.0/24",
            public_ip=example_ip_block.ips[0],
            target_subnet="10.0.1.0/24",
            target_port_range=ionoscloud.NatgatewayRuleTargetPortRangeArgs(
                start=500,
                end=1000,
            ))
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        A Nat Gateway Rule resource can be imported using its `resource id`, the `datacenter id` and the `natgateway id , e.g.

        ```sh
        $ pulumi import ionoscloud:index/natgatewayRule:NatgatewayRule my_natgateway_rule {datacenter uuid}/{nat gateway uuid}/{nat gateway rule uuid}
        ```

        :param str resource_name: The name of the resource.
        :param NatgatewayRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NatgatewayRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 natgateway_id: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 public_ip: Optional[pulumi.Input[str]] = None,
                 source_subnet: Optional[pulumi.Input[str]] = None,
                 target_port_range: Optional[pulumi.Input[pulumi.InputType['NatgatewayRuleTargetPortRangeArgs']]] = None,
                 target_subnet: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NatgatewayRuleArgs.__new__(NatgatewayRuleArgs)

            if datacenter_id is None and not opts.urn:
                raise TypeError("Missing required property 'datacenter_id'")
            __props__.__dict__["datacenter_id"] = datacenter_id
            __props__.__dict__["name"] = name
            if natgateway_id is None and not opts.urn:
                raise TypeError("Missing required property 'natgateway_id'")
            __props__.__dict__["natgateway_id"] = natgateway_id
            __props__.__dict__["protocol"] = protocol
            if public_ip is None and not opts.urn:
                raise TypeError("Missing required property 'public_ip'")
            __props__.__dict__["public_ip"] = public_ip
            if source_subnet is None and not opts.urn:
                raise TypeError("Missing required property 'source_subnet'")
            __props__.__dict__["source_subnet"] = source_subnet
            __props__.__dict__["target_port_range"] = target_port_range
            __props__.__dict__["target_subnet"] = target_subnet
            __props__.__dict__["type"] = type
        super(NatgatewayRule, __self__).__init__(
            'ionoscloud:index/natgatewayRule:NatgatewayRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            datacenter_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            natgateway_id: Optional[pulumi.Input[str]] = None,
            protocol: Optional[pulumi.Input[str]] = None,
            public_ip: Optional[pulumi.Input[str]] = None,
            source_subnet: Optional[pulumi.Input[str]] = None,
            target_port_range: Optional[pulumi.Input[pulumi.InputType['NatgatewayRuleTargetPortRangeArgs']]] = None,
            target_subnet: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'NatgatewayRule':
        """
        Get an existing NatgatewayRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] datacenter_id: [string] A Datacenter's UUID.
        :param pulumi.Input[str] name: [string] Name of the NAT gateway rule.
        :param pulumi.Input[str] natgateway_id: [string] Nat Gateway's UUID.
        :param pulumi.Input[str] protocol: [string] Protocol of the NAT gateway rule. Defaults to ALL. If protocol is 'ICMP' then targetPortRange start and end cannot be set.
        :param pulumi.Input[str] public_ip: [string] Public IP address of the NAT gateway rule. Specifies the address used for masking outgoing packets source address field. Should be one of the customer reserved IP address already configured on the NAT gateway resource.
        :param pulumi.Input[str] source_subnet: [string] Source subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets source IP address.
        :param pulumi.Input[pulumi.InputType['NatgatewayRuleTargetPortRangeArgs']] target_port_range: Target port range of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on destination port. If none is provided, rule will match any port.
        :param pulumi.Input[str] target_subnet: [string] Target or destination subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets destination IP address. If none is provided, rule will match any address.
        :param pulumi.Input[str] type: [string] Type of the NAT gateway rule.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NatgatewayRuleState.__new__(_NatgatewayRuleState)

        __props__.__dict__["datacenter_id"] = datacenter_id
        __props__.__dict__["name"] = name
        __props__.__dict__["natgateway_id"] = natgateway_id
        __props__.__dict__["protocol"] = protocol
        __props__.__dict__["public_ip"] = public_ip
        __props__.__dict__["source_subnet"] = source_subnet
        __props__.__dict__["target_port_range"] = target_port_range
        __props__.__dict__["target_subnet"] = target_subnet
        __props__.__dict__["type"] = type
        return NatgatewayRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> pulumi.Output[str]:
        """
        [string] A Datacenter's UUID.
        """
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        [string] Name of the NAT gateway rule.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="natgatewayId")
    def natgateway_id(self) -> pulumi.Output[str]:
        """
        [string] Nat Gateway's UUID.
        """
        return pulumi.get(self, "natgateway_id")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[str]:
        """
        [string] Protocol of the NAT gateway rule. Defaults to ALL. If protocol is 'ICMP' then targetPortRange start and end cannot be set.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="publicIp")
    def public_ip(self) -> pulumi.Output[str]:
        """
        [string] Public IP address of the NAT gateway rule. Specifies the address used for masking outgoing packets source address field. Should be one of the customer reserved IP address already configured on the NAT gateway resource.
        """
        return pulumi.get(self, "public_ip")

    @property
    @pulumi.getter(name="sourceSubnet")
    def source_subnet(self) -> pulumi.Output[str]:
        """
        [string] Source subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets source IP address.
        """
        return pulumi.get(self, "source_subnet")

    @property
    @pulumi.getter(name="targetPortRange")
    def target_port_range(self) -> pulumi.Output['outputs.NatgatewayRuleTargetPortRange']:
        """
        Target port range of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on destination port. If none is provided, rule will match any port.
        """
        return pulumi.get(self, "target_port_range")

    @property
    @pulumi.getter(name="targetSubnet")
    def target_subnet(self) -> pulumi.Output[str]:
        """
        [string] Target or destination subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets destination IP address. If none is provided, rule will match any address.
        """
        return pulumi.get(self, "target_subnet")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        [string] Type of the NAT gateway rule.
        """
        return pulumi.get(self, "type")

