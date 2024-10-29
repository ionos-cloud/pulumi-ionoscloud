// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Inputs
{

    public sealed class VpnWireguardGatewayConnectionGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [String] The ID of the datacenter where the WireGuard Gateway is located.
        /// </summary>
        [Input("datacenterId", required: true)]
        public Input<string> DatacenterId { get; set; } = null!;

        /// <summary>
        /// [String] The IPv4 CIDR for the WireGuard Gateway connection.
        /// </summary>
        [Input("ipv4Cidr")]
        public Input<string>? Ipv4Cidr { get; set; }

        /// <summary>
        /// [String] The IPv6 CIDR for the WireGuard Gateway connection.
        /// </summary>
        [Input("ipv6Cidr")]
        public Input<string>? Ipv6Cidr { get; set; }

        /// <summary>
        /// [String] The ID of the LAN where the WireGuard Gateway is connected.
        /// </summary>
        [Input("lanId", required: true)]
        public Input<string> LanId { get; set; } = null!;

        public VpnWireguardGatewayConnectionGetArgs()
        {
        }
        public static new VpnWireguardGatewayConnectionGetArgs Empty => new VpnWireguardGatewayConnectionGetArgs();
    }
}
