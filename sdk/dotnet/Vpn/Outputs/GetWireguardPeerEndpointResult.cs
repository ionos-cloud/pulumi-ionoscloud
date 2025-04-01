// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Vpn.Outputs
{

    [OutputType]
    public sealed class GetWireguardPeerEndpointResult
    {
        /// <summary>
        /// Hostname or IPV4 address that the WireGuard Server will connect to.
        /// </summary>
        public readonly string Host;
        /// <summary>
        /// Port that the WireGuard Server will connect to. Default: 51820
        /// </summary>
        public readonly int Port;

        [OutputConstructor]
        private GetWireguardPeerEndpointResult(
            string host,

            int port)
        {
            Host = host;
            Port = port;
        }
    }
}
