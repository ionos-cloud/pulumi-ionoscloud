// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Cdn.Outputs
{

    [OutputType]
    public sealed class GetDistributionRoutingRuleUpstreamGeoRestrictionResult
    {
        /// <summary>
        /// List of allowed countries
        /// </summary>
        public readonly ImmutableArray<string> AllowLists;
        /// <summary>
        /// List of blocked countries
        /// </summary>
        public readonly ImmutableArray<string> BlockLists;

        [OutputConstructor]
        private GetDistributionRoutingRuleUpstreamGeoRestrictionResult(
            ImmutableArray<string> allowLists,

            ImmutableArray<string> blockLists)
        {
            AllowLists = allowLists;
            BlockLists = blockLists;
        }
    }
}
