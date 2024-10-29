// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Inputs
{

    public sealed class CdnDistributionRoutingRuleGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] The prefix of the routing rule.
        /// </summary>
        [Input("prefix", required: true)]
        public Input<string> Prefix { get; set; } = null!;

        /// <summary>
        /// [string] The scheme of the routing rule.
        /// </summary>
        [Input("scheme", required: true)]
        public Input<string> Scheme { get; set; } = null!;

        /// <summary>
        /// [map] - A map of properties for the rule
        /// </summary>
        [Input("upstream", required: true)]
        public Input<Inputs.CdnDistributionRoutingRuleUpstreamGetArgs> Upstream { get; set; } = null!;

        public CdnDistributionRoutingRuleGetArgs()
        {
        }
        public static new CdnDistributionRoutingRuleGetArgs Empty => new CdnDistributionRoutingRuleGetArgs();
    }
}
