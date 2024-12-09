// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Inputs
{

    public sealed class AutoscalingGroupPolicyScaleInActionGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [int] When `amountType=ABSOLUTE` specifies the absolute number of VMs that are added. The value must be between 1 to 10. `amountType=PERCENTAGE` specifies the percentage value that is applied to the current number of replicas of the VM Auto Scaling Group. The value must be between 1 to 200. At least one VM is always added.
        /// </summary>
        [Input("amount", required: true)]
        public Input<int> Amount { get; set; } = null!;

        /// <summary>
        /// [string] The type for the given amount. Possible values are: `ABSOLUTE`, `PERCENTAGE`.
        /// </summary>
        [Input("amountType", required: true)]
        public Input<string> AmountType { get; set; } = null!;

        /// <summary>
        /// [string] Minimum time to pass after this Scaling action has started, until the next Scaling action will be started. Additionally, if a Scaling action is currently in progress, no second Scaling action will be started for the same autoscaling group. Instead, the Metric will be re-evaluated after the current Scaling action is completed (either successfully or with failures). This is validated with a minimum value of 2 minutes and a maximum of 24 hours currently. Default value is 5 minutes if not given. *Note that when you set it to values like 5m the API will automatically transform it in PT5M, so the plan will show you a diff in state that should be ignored.*
        /// </summary>
        [Input("cooldownPeriod")]
        public Input<string>? CooldownPeriod { get; set; }

        /// <summary>
        /// [bool] If set to `true`, when deleting a replica during scale in, any attached volume will also be deleted. When set to `false`, all volumes remain in the datacenter and must be deleted manually. Note that every scale-out creates new volumes. When they are not deleted, they will eventually use all of your contracts resource limits. At this point, scaling out would not be possible anymore.
        /// </summary>
        [Input("deleteVolumes", required: true)]
        public Input<bool> DeleteVolumes { get; set; } = null!;

        /// <summary>
        /// [string] The type of the termination policy for the autoscaling group so that a specific pattern is followed for Scaling-In replicas. Default termination policy is `OLDEST_SERVER_FIRST`. Possible values are: `OLDEST_SERVER_FIRST`, `NEWEST_SERVER_FIRST`, `RANDOM`
        /// </summary>
        [Input("terminationPolicyType")]
        public Input<string>? TerminationPolicyType { get; set; }

        public AutoscalingGroupPolicyScaleInActionGetArgs()
        {
        }
        public static new AutoscalingGroupPolicyScaleInActionGetArgs Empty => new AutoscalingGroupPolicyScaleInActionGetArgs();
    }
}
