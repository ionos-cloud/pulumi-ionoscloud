// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Compute.Inputs
{

    public sealed class NicFlowlogGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specifies the action to be taken when the rule is matched. Possible values: ACCEPTED, REJECTED, ALL. Immutable, update forces re-creation.
        /// </summary>
        [Input("action", required: true)]
        public Input<string> Action { get; set; } = null!;

        /// <summary>
        /// Specifies the IONOS Object Storage bucket where the flow log data will be stored. The bucket must exist. Immutable, update forces re-creation.
        /// </summary>
        [Input("bucket", required: true)]
        public Input<string> Bucket { get; set; } = null!;

        /// <summary>
        /// Specifies the traffic direction pattern. Valid values: INGRESS, EGRESS, BIDIRECTIONAL. Immutable, update forces re-creation.
        /// </summary>
        [Input("direction", required: true)]
        public Input<string> Direction { get; set; } = null!;

        /// <summary>
        /// The ID of the NIC.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Specifies the name of the flow log.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public NicFlowlogGetArgs()
        {
        }
        public static new NicFlowlogGetArgs Empty => new NicFlowlogGetArgs();
    }
}
