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
    public sealed class K8sNodePoolLanRoute
    {
        /// <summary>
        /// [string] IPv4 or IPv6 Gateway IP for the route
        /// </summary>
        public readonly string GatewayIp;
        /// <summary>
        /// [string] IPv4 or IPv6 CIDR to be routed via the interface
        /// </summary>
        public readonly string Network;

        [OutputConstructor]
        private K8sNodePoolLanRoute(
            string gatewayIp,

            string network)
        {
            GatewayIp = gatewayIp;
            Network = network;
        }
    }
}
