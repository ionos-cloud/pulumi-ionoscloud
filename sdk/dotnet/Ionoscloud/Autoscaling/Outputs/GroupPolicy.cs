// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Autoscaling.Outputs
{

    [OutputType]
    public sealed class GroupPolicy
    {
        /// <summary>
        /// [string] The Metric that should trigger the scaling actions. Metric values are checked at fixed intervals. Possible values: `INSTANCE_CPU_UTILIZATION_AVERAGE`, `INSTANCE_NETWORK_IN_BYTES`, `INSTANCE_NETWORK_IN_PACKETS`, `INSTANCE_NETWORK_OUT_BYTES`, `INSTANCE_NETWORK_OUT_PACKETS`
        /// </summary>
        public readonly string Metric;
        /// <summary>
        /// [string] Defines the time range, for which the samples will be aggregated. Default is 120s. *Note that when you set it to values like 5m the API will automatically transform it in PT5M, so the plan will show you a diff in state that should be ignored.*
        /// </summary>
        public readonly string? Range;
        /// <summary>
        /// [list] Specifies the action to take when the `scaleInThreshold` is exceeded. Hereby, scaling in is always about removing VMs that are currently associated with this autoscaling group. Default termination policy is OLDEST_SERVER_FIRST.
        /// </summary>
        public readonly Outputs.GroupPolicyScaleInAction ScaleInAction;
        /// <summary>
        /// [int] A lower threshold on the value of `metric`. Will be used with `less than` (&lt;) operator. Exceeding this will start a Scale-In Action as specified by the `scaleInAction` property. The value must have a higher minimum delta to the `scaleOutThreshold` depending on the `metric` to avoid competitive actions at the same time.
        /// </summary>
        public readonly int ScaleInThreshold;
        /// <summary>
        /// [list] Specifies the action to take when the `scaleOutThreshold` is exceeded. Hereby, scaling out is always about adding new VMs to this autoscaling group.
        /// </summary>
        public readonly Outputs.GroupPolicyScaleOutAction ScaleOutAction;
        /// <summary>
        /// [int] The upper threshold for the value of the `metric`. Used with the `greater than` (&gt;) operator. A scale-out action is triggered when this value is exceeded, specified by the `scaleOutAction` property. The value must have a lower minimum delta to the `scaleInThreshold`, depending on the metric, to avoid competing for actions simultaneously. If `properties.policy.unit=TOTAL`, a value &gt;= 40 must be chosen.
        /// </summary>
        public readonly int ScaleOutThreshold;
        /// <summary>
        /// [string] Units of the applied Metric. Possible values are: `PER_HOUR`, `PER_MINUTE`, `PER_SECOND`, `TOTAL`.
        /// </summary>
        public readonly string Unit;

        [OutputConstructor]
        private GroupPolicy(
            string metric,

            string? range,

            Outputs.GroupPolicyScaleInAction scaleInAction,

            int scaleInThreshold,

            Outputs.GroupPolicyScaleOutAction scaleOutAction,

            int scaleOutThreshold,

            string unit)
        {
            Metric = metric;
            Range = range;
            ScaleInAction = scaleInAction;
            ScaleInThreshold = scaleInThreshold;
            ScaleOutAction = scaleOutAction;
            ScaleOutThreshold = scaleOutThreshold;
            Unit = unit;
        }
    }
}
