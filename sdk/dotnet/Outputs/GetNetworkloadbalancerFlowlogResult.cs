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
    public sealed class GetNetworkloadbalancerFlowlogResult
    {
        /// <summary>
        /// Specifies the action to be taken when the rule is matched. Possible values: ACCEPTED, REJECTED, ALL. Immutable, forces re-creation.
        /// </summary>
        public readonly string Action;
        /// <summary>
        /// Specifies the S3 IONOS bucket where the flow log data will be stored. The bucket must exist. Immutable, forces re-creation.
        /// </summary>
        public readonly string Bucket;
        /// <summary>
        /// Specifies the traffic direction pattern. Valid values: INGRESS, EGRESS, BIDIRECTIONAL. Immutable, forces re-creation.
        /// </summary>
        public readonly string Direction;
        /// <summary>
        /// ID of the network load balancer you want to search for.
        /// 
        /// `datacenter_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Name of an existing network load balancer that you want to search for.
        /// </summary>
        public readonly string Name;

        [OutputConstructor]
        private GetNetworkloadbalancerFlowlogResult(
            string action,

            string bucket,

            string direction,

            string id,

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
