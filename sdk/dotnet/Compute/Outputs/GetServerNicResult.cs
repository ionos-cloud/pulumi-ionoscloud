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
    public sealed class GetServerNicResult
    {
        /// <summary>
        /// The Logical Unit Number (LUN) of the storage volume
        /// </summary>
        public readonly int DeviceNumber;
        /// <summary>
        /// Indicates if the nic will reserve an IP using DHCP
        /// </summary>
        public readonly bool Dhcp;
        public readonly bool? Dhcpv6;
        /// <summary>
        /// Activate or deactivate the firewall
        /// </summary>
        public readonly bool FirewallActive;
        /// <summary>
        /// list of
        /// </summary>
        public readonly ImmutableArray<Outputs.GetServerNicFirewallRuleResult> FirewallRules;
        /// <summary>
        /// The type of firewall rules that will be allowed on the NIC
        /// </summary>
        public readonly string FirewallType;
        /// <summary>
        /// ID of the server you want to search for.
        /// 
        /// `datacenter_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Collection of IP addresses assigned to a nic
        /// </summary>
        public readonly ImmutableArray<string> Ips;
        public readonly string Ipv6CidrBlock;
        public readonly ImmutableArray<string> Ipv6Ips;
        /// <summary>
        /// The LAN ID the NIC will sit on
        /// </summary>
        public readonly int Lan;
        /// <summary>
        /// The MAC address of the NIC
        /// </summary>
        public readonly string Mac;
        /// <summary>
        /// Name of an existing server that you want to search for.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The PCI slot number of the Nic
        /// </summary>
        public readonly int PciSlot;
        /// <summary>
        /// The list of Security Group IDs for the resource.
        /// </summary>
        public readonly ImmutableArray<string> SecurityGroupsIds;

        [OutputConstructor]
        private GetServerNicResult(
            int deviceNumber,

            bool dhcp,

            bool? dhcpv6,

            bool firewallActive,

            ImmutableArray<Outputs.GetServerNicFirewallRuleResult> firewallRules,

            string firewallType,

            string id,

            ImmutableArray<string> ips,

            string ipv6CidrBlock,

            ImmutableArray<string> ipv6Ips,

            int lan,

            string mac,

            string name,

            int pciSlot,

            ImmutableArray<string> securityGroupsIds)
        {
            DeviceNumber = deviceNumber;
            Dhcp = dhcp;
            Dhcpv6 = dhcpv6;
            FirewallActive = firewallActive;
            FirewallRules = firewallRules;
            FirewallType = firewallType;
            Id = id;
            Ips = ips;
            Ipv6CidrBlock = ipv6CidrBlock;
            Ipv6Ips = ipv6Ips;
            Lan = lan;
            Mac = mac;
            Name = name;
            PciSlot = pciSlot;
            SecurityGroupsIds = securityGroupsIds;
        }
    }
}
