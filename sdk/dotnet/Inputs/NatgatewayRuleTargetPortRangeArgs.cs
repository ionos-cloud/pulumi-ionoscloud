// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Inputs
{

    public sealed class NatgatewayRuleTargetPortRangeArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [int] Target port range end associated with the NAT gateway rule.
        /// </summary>
        [Input("end")]
        public Input<int>? End { get; set; }

        /// <summary>
        /// [int] Target port range start associated with the NAT gateway rule.
        /// </summary>
        [Input("start")]
        public Input<int>? Start { get; set; }

        public NatgatewayRuleTargetPortRangeArgs()
        {
        }
        public static new NatgatewayRuleTargetPortRangeArgs Empty => new NatgatewayRuleTargetPortRangeArgs();
    }
}
