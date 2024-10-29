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
    public sealed class GetNatgatewayRuleTargetPortRangeResult
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
        private GetNatgatewayRuleTargetPortRangeResult(
            int end,

            int start)
        {
            End = end;
            Start = start;
        }
    }
}
