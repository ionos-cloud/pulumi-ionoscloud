// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Compute.Outputs
{

    [OutputType]
    public sealed class NicFlowlog
    {
        /// <summary>
        /// Specifies the action to be taken when the rule is matched. Possible values: ACCEPTED, REJECTED, ALL. Immutable, update forces re-creation.
        /// </summary>
        public readonly string Action;
        /// <summary>
        /// Specifies the IONOS Object Storage bucket where the flow log data will be stored. The bucket must exist. Immutable, update forces re-creation.
        /// </summary>
        public readonly string Bucket;
        /// <summary>
        /// Specifies the traffic direction pattern. Valid values: INGRESS, EGRESS, BIDIRECTIONAL. Immutable, update forces re-creation.
        /// </summary>
        public readonly string Direction;
        /// <summary>
        /// The ID of the NIC.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// Specifies the name of the flow log.
        /// </summary>
        public readonly string Name;

        [OutputConstructor]
        private NicFlowlog(
            string action,

            string bucket,

            string direction,

            string? id,

            string name)
        {
            Action = action;
            Bucket = bucket;
            Direction = direction;
            Id = id;
            Name = name;
        }
    }
}
