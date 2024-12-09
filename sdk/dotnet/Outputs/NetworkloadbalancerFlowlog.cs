// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Outputs
{

    [OutputType]
    public sealed class NetworkloadbalancerFlowlog
    {
        /// <summary>
        /// [string] Specifies the action to be taken when the rule is matched. Possible values: ACCEPTED, REJECTED, ALL. Immutable, forces re-creation.
        /// </summary>
        public readonly string Action;
        /// <summary>
        /// [string] Specifies the IONOS Object Storage bucket where the flow log data will be stored. The bucket must exist. Immutable, forces re-creation.
        /// </summary>
        public readonly string Bucket;
        /// <summary>
        /// [string] Specifies the traffic direction pattern. Valid values: INGRESS, EGRESS, BIDIRECTIONAL. Immutable, forces re-creation.
        /// </summary>
        public readonly string Direction;
        /// <summary>
        /// The resource's unique identifier.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// [string] Specifies the name of the flow log.
        /// 
        /// ⚠️ **Note:**: Removing the `flowlog` forces re-creation of the network load balancer resource.
        /// </summary>
        public readonly string Name;

        [OutputConstructor]
        private NetworkloadbalancerFlowlog(
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
