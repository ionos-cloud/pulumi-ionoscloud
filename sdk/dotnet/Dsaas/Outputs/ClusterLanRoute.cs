// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Dsaas.Outputs
{

    [OutputType]
    public sealed class ClusterLanRoute
    {
        /// <summary>
        /// [string] IPv4 or IPv6 gateway IP for the route.
        /// </summary>
        public readonly string Gateway;
        /// <summary>
        /// [string] IPv4 or IPv6 CIDR to be routed via the interface.
        /// </summary>
        public readonly string Network;

        [OutputConstructor]
        private ClusterLanRoute(
            string gateway,

            string network)
        {
            Gateway = gateway;
            Network = network;
        }
    }
}
