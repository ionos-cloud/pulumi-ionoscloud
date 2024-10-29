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
    public sealed class GetAutoscalingGroupPolicyScaleInActionResult
    {
        /// <summary>
        /// When `amountType == ABSOLUTE`, this is the number of VMs added or removed in one step. When `amountType == PERCENTAGE`, this is a percentage value, which will be applied to the Autoscaling Group's current `targetReplicaCount` in order to derive the number of VMs that will be added or removed in one step. There will always be at least one VM added or removed.
        /// </summary>
        public readonly int Amount;
        /// <summary>
        /// The type for the given amount. Possible values are: [ABSOLUTE, PERCENTAGE].
        /// </summary>
        public readonly string AmountType;
        /// <summary>
        /// Minimum time to pass after this Scaling Action has started, until the next Scaling Action will be started. Additionally, if a Scaling Action is currently in progress, no second Scaling Action will be started for the same Autoscaling Group. Instead, the Metric will be re-evaluated after the current Scaling Action completed (either successful or with failures).
        /// *Note that when you set it to values like 5m the API will automatically transform it in PT5M, so the plan will show you a diff in state that should be ignored.*
        /// </summary>
        public readonly string CooldownPeriod;
        /// <summary>
        /// If set to 'true', when deleting an replica during scale in, any attached volume will also be deleted. When set to 'false', all volumes remain in the datacenter and must be deleted manually. Note that every scale-out creates new volumes. When they are not deleted, they will eventually use all of your contracts resource limits. At this point, scaling out would not be possible anymore.
        /// </summary>
        public readonly bool DeleteVolumes;
        /// <summary>
        /// The type of the termination policy for the autoscaling group so that a specific pattern is followed for Scaling-In instances. Default termination policy is OLDEST_SERVER_FIRST.
        /// </summary>
        public readonly string TerminationPolicyType;

        [OutputConstructor]
        private GetAutoscalingGroupPolicyScaleInActionResult(
            int amount,

            string amountType,

            string cooldownPeriod,

            bool deleteVolumes,

            string terminationPolicyType)
        {
            Amount = amount;
            AmountType = amountType;
            CooldownPeriod = cooldownPeriod;
            DeleteVolumes = deleteVolumes;
            TerminationPolicyType = terminationPolicyType;
        }
    }
}
