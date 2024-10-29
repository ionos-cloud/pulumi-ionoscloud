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
    public sealed class PrivateCrossconnectPeer
    {
        /// <summary>
        /// The id of the cross-connected datacenter
        /// </summary>
        public readonly string? DatacenterId;
        /// <summary>
        /// The name of the cross-connected datacenter
        /// </summary>
        public readonly string? DatacenterName;
        /// <summary>
        /// The id of the cross-connected LAN
        /// </summary>
        public readonly string? LanId;
        /// <summary>
        /// The name of the cross-connected LAN
        /// </summary>
        public readonly string? LanName;
        /// <summary>
        /// The location of the cross-connected datacenter
        /// </summary>
        public readonly string? Location;

        [OutputConstructor]
        private PrivateCrossconnectPeer(
            string? datacenterId,

            string? datacenterName,

            string? lanId,

            string? lanName,

            string? location)
        {
            DatacenterId = datacenterId;
            DatacenterName = datacenterName;
            LanId = lanId;
            LanName = lanName;
            Location = location;
        }
    }
}
