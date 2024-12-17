// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.K8s.Inputs
{

    public sealed class NodePoolAutoScalingGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The maximum number of worker nodes that the node pool can scale to. Should be greater than min_node_count
        /// </summary>
        [Input("maxNodeCount", required: true)]
        public Input<int> MaxNodeCount { get; set; } = null!;

        /// <summary>
        /// The minimum number of worker nodes the node pool can scale down to. Should be less than max_node_count
        /// </summary>
        [Input("minNodeCount", required: true)]
        public Input<int> MinNodeCount { get; set; } = null!;

        public NodePoolAutoScalingGetArgs()
        {
        }
        public static new NodePoolAutoScalingGetArgs Empty => new NodePoolAutoScalingGetArgs();
    }
}
