// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Inputs
{

    public sealed class AutoscalingGroupReplicaConfigurationNicFirewallRuleGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [int] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen.
        /// </summary>
        [Input("icmpCode")]
        public Input<int>? IcmpCode { get; set; }

        /// <summary>
        /// [string] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen. Value null allows all codes.
        /// </summary>
        [Input("icmpType")]
        public Input<int>? IcmpType { get; set; }

        /// <summary>
        /// [string] Name for this replica volume.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// [int] Defines the end range of the allowed port (from 1 to 65534) if the protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
        /// </summary>
        [Input("portRangeEnd")]
        public Input<int>? PortRangeEnd { get; set; }

        /// <summary>
        /// [int] Defines the start range of the allowed port (from 1 to 65534) if protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
        /// </summary>
        [Input("portRangeStart")]
        public Input<int>? PortRangeStart { get; set; }

        /// <summary>
        /// [string] The protocol for the rule: TCP, UDP, ICMP, ANY. Property cannot be modified after creation (disallowed in update requests).
        /// </summary>
        [Input("protocol", required: true)]
        public Input<string> Protocol { get; set; } = null!;

        /// <summary>
        /// [string] Only traffic originating from the respective IPv4 address is allowed. Value null allows all source IPs.
        /// </summary>
        [Input("sourceIp")]
        public Input<string>? SourceIp { get; set; }

        /// <summary>
        /// [string] Only traffic originating from the respective MAC address is allowed. Valid format: aa:bb:cc:dd:ee:ff. Value null allows all source MAC address. Valid format: aa:bb:cc:dd:ee:ff.
        /// </summary>
        [Input("sourceMac")]
        public Input<string>? SourceMac { get; set; }

        /// <summary>
        /// [string] In case the target NIC has multiple IP addresses, only traffic directed to the respective IP address of the NIC is allowed. Value null allows all target IPs.
        /// </summary>
        [Input("targetIp")]
        public Input<string>? TargetIp { get; set; }

        /// <summary>
        /// [string] Storage Type for this replica volume. Possible values: `SSD`, `HDD`, `SSD_STANDARD` or `SSD_PREMIUM`.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        public AutoscalingGroupReplicaConfigurationNicFirewallRuleGetArgs()
        {
        }
        public static new AutoscalingGroupReplicaConfigurationNicFirewallRuleGetArgs Empty => new AutoscalingGroupReplicaConfigurationNicFirewallRuleGetArgs();
    }
}
