// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Cdn.Outputs
{

    [OutputType]
    public sealed class DistributionRoutingRule
    {
        /// <summary>
        /// The prefix of the routing rule.
        /// </summary>
        public readonly string Prefix;
        /// <summary>
        /// The scheme of the routing rule.
        /// </summary>
        public readonly string Scheme;
        public readonly Outputs.DistributionRoutingRuleUpstream Upstream;

        [OutputConstructor]
        private DistributionRoutingRule(
            string prefix,

            string scheme,

            Outputs.DistributionRoutingRuleUpstream upstream)
        {
            Prefix = prefix;
            Scheme = scheme;
            Upstream = upstream;
        }
    }
}
