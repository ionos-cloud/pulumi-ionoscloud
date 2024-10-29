// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Outputs
{

    [OutputType]
    public sealed class VpnWireguardGatewayConnection
    {
        /// <summary>
        /// [String] The ID of the datacenter where the WireGuard Gateway is located.
        /// </summary>
        public readonly string DatacenterId;
        /// <summary>
        /// [String] The IPv4 CIDR for the WireGuard Gateway connection.
        /// </summary>
        public readonly string? Ipv4Cidr;
        /// <summary>
        /// [String] The IPv6 CIDR for the WireGuard Gateway connection.
        /// </summary>
        public readonly string? Ipv6Cidr;
        /// <summary>
        /// [String] The ID of the LAN where the WireGuard Gateway is connected.
        /// </summary>
        public readonly string LanId;

        [OutputConstructor]
        private VpnWireguardGatewayConnection(
            string datacenterId,

            string? ipv4Cidr,

            string? ipv6Cidr,

            string lanId)
        {
            DatacenterId = datacenterId;
            Ipv4Cidr = ipv4Cidr;
            Ipv6Cidr = ipv6Cidr;
            LanId = lanId;
        }
    }
}
