// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Dbaas.Outputs
{

    [OutputType]
    public sealed class GetInmemorydbSnapshotMetadataResult
    {
        /// <summary>
        /// The ISO 8601 creation timestamp.
        /// </summary>
        public readonly string CreatedDate;
        /// <summary>
        /// The ID of the datacenter in which the snapshot is located.
        /// </summary>
        public readonly string DatacenterId;
        /// <summary>
        /// The ISO 8601 modified timestamp.
        /// </summary>
        public readonly string LastModifiedDate;
        /// <summary>
        /// The ID of the replica set from which the snapshot was created.
        /// </summary>
        public readonly string ReplicaSetId;
        /// <summary>
        /// The time at which the snapshot was taken.
        /// </summary>
        public readonly string SnapshotTime;

        [OutputConstructor]
        private GetInmemorydbSnapshotMetadataResult(
            string createdDate,

            string datacenterId,

            string lastModifiedDate,

            string replicaSetId,

            string snapshotTime)
        {
            CreatedDate = createdDate;
            DatacenterId = datacenterId;
            LastModifiedDate = lastModifiedDate;
            ReplicaSetId = replicaSetId;
            SnapshotTime = snapshotTime;
        }
    }
}
