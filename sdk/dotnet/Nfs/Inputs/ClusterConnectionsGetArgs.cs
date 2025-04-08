// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Nfs.Inputs
{

    public sealed class ClusterConnectionsGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the datacenter where the Network File Storage cluster is located.
        /// </summary>
        [Input("datacenterId", required: true)]
        public Input<string> DatacenterId { get; set; } = null!;

        /// <summary>
        /// The IP address and prefix of the Network File Storage cluster. The IP address can be either IPv4 or IPv6. The IP address has to be given with CIDR notation.
        /// </summary>
        [Input("ipAddress", required: true)]
        public Input<string> IpAddress { get; set; } = null!;

        /// <summary>
        /// The Private LAN to which the Network File Storage cluster must be connected.
        /// -
        /// &gt; **⚠ NOTE:** `IONOS_API_URL_NFS` can be used to set a custom API URL for the resource. `location` field needs to be empty, otherwise it will override the custom API URL. Setting `endpoint` or `IONOS_API_URL` does not have any effect.
        /// </summary>
        [Input("lan", required: true)]
        public Input<string> Lan { get; set; } = null!;

        public ClusterConnectionsGetArgs()
        {
        }
        public static new ClusterConnectionsGetArgs Empty => new ClusterConnectionsGetArgs();
    }
}
