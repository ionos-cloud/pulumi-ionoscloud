// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Outputs
{

    [OutputType]
    public sealed class CdnDistributionRoutingRuleUpstreamGeoRestrictions
    {
        /// <summary>
        /// [string] List of allowed countries
        /// </summary>
        public readonly ImmutableArray<string> AllowLists;
        /// <summary>
        /// [string] List of blocked countries
        /// </summary>
        public readonly ImmutableArray<string> BlockLists;

        [OutputConstructor]
        private CdnDistributionRoutingRuleUpstreamGeoRestrictions(
            ImmutableArray<string> allowLists,

            ImmutableArray<string> blockLists)
        {
            AllowLists = allowLists;
            BlockLists = blockLists;
        }
    }
}
