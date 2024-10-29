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
    public sealed class MongoClusterBackup
    {
        /// <summary>
        /// The location where the cluster backups will be stored. If not set, the backup is stored in the nearest location of the cluster. Examples: de, eu-sounth-2, eu-central-2
        /// </summary>
        public readonly string? Location;
        /// <summary>
        /// Number of hours in the past for which a point-in-time snapshot can be created.
        /// </summary>
        public readonly int? PointInTimeWindowHours;
        /// <summary>
        /// Number of hours between snapshots.
        /// </summary>
        public readonly int? SnapshotIntervalHours;

        [OutputConstructor]
        private MongoClusterBackup(
            string? location,

            int? pointInTimeWindowHours,

            int? snapshotIntervalHours)
        {
            Location = location;
            PointInTimeWindowHours = pointInTimeWindowHours;
            SnapshotIntervalHours = snapshotIntervalHours;
        }
    }
}
