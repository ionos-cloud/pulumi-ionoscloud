// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Autoscaling.Outputs
{

    [OutputType]
    public sealed class GroupPolicyScaleInAction
    {
        /// <summary>
        /// [int] When `amountType == ABSOLUTE`, this is the number of VMs removed in one step. When `amountType == PERCENTAGE`, this is a percentage value, which will be applied to the autoscaling group's current `targetReplicaCount` in order to derive the number of VMs that will be removed in one step. There will always be at least one VM removed. For SCALE_IN operation new volumes are NOT deleted after the server deletion.
        /// </summary>
        public readonly int Amount;
        /// <summary>
        /// [string] The type for the given amount. Possible values are: `ABSOLUTE`, `PERCENTAGE`.
        /// </summary>
        public readonly string AmountType;
        /// <summary>
        /// [string] Minimum time to pass after this Scaling action has started, until the next Scaling action will be started. Additionally, if a Scaling action is currently in progress, no second Scaling action will be started for the same autoscaling group. Instead, the Metric will be re-evaluated after the current Scaling action is completed (either successfully or with failures). This is validated with a minimum value of 2 minutes and a maximum of 24 hours currently. Default value is 5 minutes if not given. *Note that when you set it to values like 5m the API will automatically transform it in PT5M, so the plan will show you a diff in state that should be ignored.*
        /// </summary>
        public readonly string? CooldownPeriod;
        /// <summary>
        /// [bool] If set to `true`, when deleting a replica during scale in, any attached volume will also be deleted. When set to `false`, all volumes remain in the datacenter and must be deleted manually. Note that every scale-out creates new volumes. When they are not deleted, they will eventually use all of your contracts resource limits. At this point, scaling out would not be possible anymore.
        /// </summary>
        public readonly bool DeleteVolumes;
        /// <summary>
        /// [string] The type of the termination policy for the autoscaling group so that a specific pattern is followed for Scaling-In replicas. Default termination policy is `OLDEST_SERVER_FIRST`. Possible values are: `OLDEST_SERVER_FIRST`, `NEWEST_SERVER_FIRST`, `RANDOM`
        /// </summary>
        public readonly string? TerminationPolicyType;

        [OutputConstructor]
        private GroupPolicyScaleInAction(
            int amount,

            string amountType,

            string? cooldownPeriod,

            bool deleteVolumes,

            string? terminationPolicyType)
        {
            Amount = amount;
            AmountType = amountType;
            CooldownPeriod = cooldownPeriod;
            DeleteVolumes = deleteVolumes;
            TerminationPolicyType = terminationPolicyType;
        }
    }
}
