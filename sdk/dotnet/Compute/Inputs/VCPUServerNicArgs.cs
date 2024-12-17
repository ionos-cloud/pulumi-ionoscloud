// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Compute.Inputs
{

    public sealed class VCPUServerNicArgs : global::Pulumi.ResourceArgs
    {
        [Input("deviceNumber")]
        public Input<int>? DeviceNumber { get; set; }

        [Input("dhcp")]
        public Input<bool>? Dhcp { get; set; }

        [Input("dhcpv6")]
        public Input<bool>? Dhcpv6 { get; set; }

        [Input("firewallActive")]
        public Input<bool>? FirewallActive { get; set; }

        [Input("firewallType")]
        public Input<string>? FirewallType { get; set; }

        [Input("firewalls")]
        private InputList<Inputs.VCPUServerNicFirewallArgs>? _firewalls;

        /// <summary>
        /// Allows to define firewall rules inline in the server. See the Firewall section.
        /// </summary>
        public InputList<Inputs.VCPUServerNicFirewallArgs> Firewalls
        {
            get => _firewalls ?? (_firewalls = new InputList<Inputs.VCPUServerNicFirewallArgs>());
            set => _firewalls = value;
        }

        [Input("id")]
        public Input<string>? Id { get; set; }

        [Input("ips")]
        private InputList<string>? _ips;

        /// <summary>
        /// Collection of IP addresses assigned to a nic. Explicitly assigned public IPs need to come from reserved IP blocks, Passing value null or empty array will assign an IP address automatically.
        /// </summary>
        public InputList<string> Ips
        {
            get => _ips ?? (_ips = new InputList<string>());
            set => _ips = value;
        }

        [Input("ipv6CidrBlock")]
        public Input<string>? Ipv6CidrBlock { get; set; }

        [Input("ipv6Ips")]
        private InputList<string>? _ipv6Ips;
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

        public VCPUServerNicArgs()
        {
        }
        public static new VCPUServerNicArgs Empty => new VCPUServerNicArgs();
    }
}
