// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Compute.Outputs
{

    [OutputType]
    public sealed class GetNatGatewayRuleTargetPortRangeResult
    {
        /// <summary>
        /// Target port range end associated with the NAT gateway rule.
        /// </summary>
        public readonly int End;
        /// <summary>
        /// Target port range start associated with the NAT gateway rule.
        /// </summary>
        public readonly int Start;

        [OutputConstructor]
        private GetNatGatewayRuleTargetPortRangeResult(
            int end,

            int start)
        {
            End = end;
            Start = start;
        }
    }
}
