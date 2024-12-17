// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Autoscaling.Inputs
{

    public sealed class GroupReplicaConfigurationNicTargetGroupGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The port for the target group.
        /// </summary>
        [Input("port", required: true)]
        public Input<int> Port { get; set; } = null!;

        /// <summary>
        /// The ID of the target group.
        /// </summary>
        [Input("targetGroupId", required: true)]
        public Input<string> TargetGroupId { get; set; } = null!;

        /// <summary>
        /// The weight for the target group.
        /// </summary>
        [Input("weight", required: true)]
        public Input<int> Weight { get; set; } = null!;

        public GroupReplicaConfigurationNicTargetGroupGetArgs()
        {
        }
        public static new GroupReplicaConfigurationNicTargetGroupGetArgs Empty => new GroupReplicaConfigurationNicTargetGroupGetArgs();
    }
}
