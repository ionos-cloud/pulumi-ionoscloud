// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Compute.Outputs
{

    [OutputType]
    public sealed class CubeServerNic
    {
        public readonly int? DeviceNumber;
        public readonly bool? Dhcp;
        /// <summary>
        /// Indicates whether this NIC receives an IPv6 address through DHCP.
        /// </summary>
        public readonly bool? Dhcpv6;
        public readonly Outputs.CubeServerNicFirewall? Firewall;
        public readonly bool? FirewallActive;
        public readonly string? FirewallType;
        public readonly ImmutableArray<string> Ips;
        /// <summary>
        /// IPv6 CIDR block assigned to the NIC.
        /// </summary>
        public readonly string? Ipv6CidrBlock;
        /// <summary>
        /// Collection for IPv6 addresses assigned to a nic. Explicitly assigned IPv6 addresses need to come from inside the IPv6 CIDR block assigned to the nic.
        /// </summary>
        public readonly ImmutableArray<string> Ipv6Ips;
        public readonly int Lan;
        public readonly string? Mac;
        public readonly string? Name;
        public readonly int? PciSlot;

        [OutputConstructor]
        private CubeServerNic(
            int? deviceNumber,

            bool? dhcp,

            bool? dhcpv6,

            Outputs.CubeServerNicFirewall? firewall,

            bool? firewallActive,

            string? firewallType,

            ImmutableArray<string> ips,

            string? ipv6CidrBlock,

            ImmutableArray<string> ipv6Ips,

            int lan,

            string? mac,

            string? name,

            int? pciSlot)
        {
            DeviceNumber = deviceNumber;
            Dhcp = dhcp;
            Dhcpv6 = dhcpv6;
            Firewall = firewall;
            FirewallActive = firewallActive;
            FirewallType = firewallType;
            Ips = ips;
            Ipv6CidrBlock = ipv6CidrBlock;
            Ipv6Ips = ipv6Ips;
            Lan = lan;
            Mac = mac;
            Name = name;
            PciSlot = pciSlot;
        }
    }
}
