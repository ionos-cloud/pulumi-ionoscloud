// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Inputs
{

    public sealed class CubeServerNicGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("deviceNumber")]
        public Input<int>? DeviceNumber { get; set; }

        [Input("dhcp")]
        public Input<bool>? Dhcp { get; set; }

        /// <summary>
        /// Indicates whether this NIC receives an IPv6 address through DHCP.
        /// </summary>
        [Input("dhcpv6")]
        public Input<bool>? Dhcpv6 { get; set; }

        [Input("firewall")]
        public Input<Inputs.CubeServerNicFirewallGetArgs>? Firewall { get; set; }

        [Input("firewallActive")]
        public Input<bool>? FirewallActive { get; set; }

        [Input("firewallType")]
        public Input<string>? FirewallType { get; set; }

        [Input("ips")]
        private InputList<string>? _ips;
        public InputList<string> Ips
        {
            get => _ips ?? (_ips = new InputList<string>());
            set => _ips = value;
        }

        /// <summary>
        /// IPv6 CIDR block assigned to the NIC.
        /// </summary>
        [Input("ipv6CidrBlock")]
        public Input<string>? Ipv6CidrBlock { get; set; }

        [Input("ipv6Ips")]
        private InputList<string>? _ipv6Ips;

        /// <summary>
        /// Collection for IPv6 addresses assigned to a nic. Explicitly assigned IPv6 addresses need to come from inside the IPv6 CIDR block assigned to the nic.
        /// </summary>
        public InputList<string> Ipv6Ips
        {
            get => _ipv6Ips ?? (_ipv6Ips = new InputList<string>());
            set => _ipv6Ips = value;
        }

        [Input("lan", required: true)]
        public Input<int> Lan { get; set; } = null!;

        [Input("mac")]
        public Input<string>? Mac { get; set; }

        /// <summary>
        /// [string] The name of the server.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("pciSlot")]
        public Input<int>? PciSlot { get; set; }

        public CubeServerNicGetArgs()
        {
        }
        public static new CubeServerNicGetArgs Empty => new CubeServerNicGetArgs();
    }
}
