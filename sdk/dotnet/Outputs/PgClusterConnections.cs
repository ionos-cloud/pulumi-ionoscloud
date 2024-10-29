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
    public sealed class PgClusterConnections
    {
        /// <summary>
        /// The IP and subnet for the database.
        ///           Note the following unavailable IP ranges:
        ///           10.233.64.0/18
        ///           10.233.0.0/18
        ///           10.233.114.0/24
        /// </summary>
        public readonly string Cidr;
        /// <summary>
        /// The datacenter to connect your cluster to.
        /// </summary>
        public readonly string DatacenterId;
        /// <summary>
        /// The LAN to connect your cluster to.
        /// </summary>
        public readonly string LanId;

        [OutputConstructor]
        private PgClusterConnections(
            string cidr,

            string datacenterId,

            string lanId)
        {
            Cidr = cidr;
            DatacenterId = datacenterId;
            LanId = lanId;
        }
    }
}
