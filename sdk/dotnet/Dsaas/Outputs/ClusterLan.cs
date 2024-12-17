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
    public sealed class ClusterLan
    {
        /// <summary>
        /// [bool] Indicates if the Kubernetes node pool LAN will reserve an IP using DHCP. The default value is 'true'.
        /// </summary>
        public readonly bool? Dhcp;
        /// <summary>
        /// [string] The LAN ID of an existing LAN at the related data center.
        /// </summary>
        public readonly string LanId;
        /// <summary>
        /// [list] An array of additional LANs attached to worker nodes.
        /// </summary>
        public readonly ImmutableArray<Outputs.ClusterLanRoute> Routes;

        [OutputConstructor]
        private ClusterLan(
            bool? dhcp,

            string lanId,

            ImmutableArray<Outputs.ClusterLanRoute> routes)
        {
            Dhcp = dhcp;
            LanId = lanId;
            Routes = routes;
        }
    }
}
