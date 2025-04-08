// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Nlb.Outputs
{

    [OutputType]
    public sealed class GetForwardingRuleTargetHealthCheckResult
    {
        /// <summary>
        /// Check specifies whether the target VM's health is checked.
        /// </summary>
        public readonly bool Check;
        /// <summary>
        /// CheckInterval determines the duration (in milliseconds) between consecutive health checks. If unspecified a default of 2000 ms is used.
        /// </summary>
        public readonly int CheckInterval;
        /// <summary>
        /// Maintenance specifies if a target VM should be marked as down, even if it is not.
        /// </summary>
        public readonly bool Maintenance;

        [OutputConstructor]
        private GetForwardingRuleTargetHealthCheckResult(
            bool check,

            int checkInterval,

            bool maintenance)
        {
            Check = check;
            CheckInterval = checkInterval;
            Maintenance = maintenance;
        }
    }
}
