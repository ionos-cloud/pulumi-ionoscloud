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
    public sealed class AutoscalingGroupReplicaConfigurationNicTargetGroup
    {
        /// <summary>
        /// The port for the target group.
        /// </summary>
        public readonly int Port;
        /// <summary>
        /// The ID of the target group.
        /// </summary>
        public readonly string TargetGroupId;
        /// <summary>
        /// The weight for the target group.
        /// </summary>
        public readonly int Weight;

        [OutputConstructor]
        private AutoscalingGroupReplicaConfigurationNicTargetGroup(
            int port,

            string targetGroupId,

            int weight)
        {
            Port = port;
            TargetGroupId = targetGroupId;
            Weight = weight;
        }
    }
}
