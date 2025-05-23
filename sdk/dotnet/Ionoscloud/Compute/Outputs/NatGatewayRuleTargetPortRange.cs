// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Compute.Outputs
{

    [OutputType]
    public sealed class NatGatewayRuleTargetPortRange
    {
        /// <summary>
        /// [int] Target port range end associated with the NAT gateway rule.
        /// </summary>
        public readonly int? End;
        /// <summary>
        /// [int] Target port range start associated with the NAT gateway rule.
        /// </summary>
        public readonly int? Start;

        [OutputConstructor]
        private NatGatewayRuleTargetPortRange(
            int? end,

            int? start)
        {
            End = end;
            Start = start;
        }
    }
}
