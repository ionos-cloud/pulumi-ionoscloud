// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Nlb.Inputs
{

    public sealed class ForwardingRuleTargetHealthCheckArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [boolean] Check specifies whether the target VM's health is checked.
        /// </summary>
        [Input("check")]
        public Input<bool>? Check { get; set; }

        /// <summary>
        /// [int] CheckInterval determines the duration (in milliseconds) between consecutive health checks. If unspecified a default of 2000 ms is used.
        /// </summary>
        [Input("checkInterval")]
        public Input<int>? CheckInterval { get; set; }

        /// <summary>
        /// [boolean] Maintenance specifies if a target VM should be marked as down, even if it is not.
        /// </summary>
        [Input("maintenance")]
        public Input<bool>? Maintenance { get; set; }

        public ForwardingRuleTargetHealthCheckArgs()
        {
        }
        public static new ForwardingRuleTargetHealthCheckArgs Empty => new ForwardingRuleTargetHealthCheckArgs();
    }
}
