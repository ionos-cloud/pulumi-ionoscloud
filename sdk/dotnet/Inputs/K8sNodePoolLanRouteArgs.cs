// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Inputs
{

    public sealed class K8sNodePoolLanRouteArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] IPv4 or IPv6 Gateway IP for the route
        /// </summary>
        [Input("gatewayIp", required: true)]
        public Input<string> GatewayIp { get; set; } = null!;

        /// <summary>
        /// [string] IPv4 or IPv6 CIDR to be routed via the interface
        /// </summary>
        [Input("network", required: true)]
        public Input<string> Network { get; set; } = null!;

        public K8sNodePoolLanRouteArgs()
        {
        }
        public static new K8sNodePoolLanRouteArgs Empty => new K8sNodePoolLanRouteArgs();
    }
}
