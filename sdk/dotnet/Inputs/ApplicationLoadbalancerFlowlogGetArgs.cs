// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Inputs
{

    public sealed class ApplicationLoadbalancerFlowlogGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] Specifies the action to be taken when the rule is matched. Possible values: ACCEPTED, REJECTED, ALL. Immutable, forces re-creation.
        /// </summary>
        [Input("action", required: true)]
        public Input<string> Action { get; set; } = null!;

        /// <summary>
        /// [string] Specifies the IONOS Object Storage bucket where the flow log data will be stored. The bucket must exist. Immutable, forces re-creation.
        /// </summary>
        [Input("bucket", required: true)]
        public Input<string> Bucket { get; set; } = null!;

        /// <summary>
        /// [string] Specifies the traffic direction pattern. Valid values: INGRESS, EGRESS, BIDIRECTIONAL. Immutable, forces re-creation.
        /// </summary>
        [Input("direction", required: true)]
        public Input<string> Direction { get; set; } = null!;

        /// <summary>
        /// The resource's unique identifier.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// [string] Specifies the name of the flow log.
        /// 
        /// ⚠️ **Note:**: Removing the `flowlog` forces re-creation of the application load balancer resource.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public ApplicationLoadbalancerFlowlogGetArgs()
        {
        }
        public static new ApplicationLoadbalancerFlowlogGetArgs Empty => new ApplicationLoadbalancerFlowlogGetArgs();
    }
}
