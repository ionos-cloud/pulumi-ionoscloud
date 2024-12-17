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
    public sealed class DistributionRoutingRuleUpstream
    {
        /// <summary>
        /// Enable or disable caching. If enabled, the CDN will cache the responses from the upstream host. Subsequent requests for the same resource will be served from the cache.
        /// </summary>
        public readonly bool Caching;
        public readonly Outputs.DistributionRoutingRuleUpstreamGeoRestrictions? GeoRestrictions;
        /// <summary>
        /// The upstream host that handles the requests if not already cached. This host will be protected by the WAF if the option is enabled.
        /// </summary>
        public readonly string Host;
        /// <summary>
        /// Rate limit class that will be applied to limit the number of incoming requests per IP.
        /// </summary>
        public readonly string RateLimitClass;
        /// <summary>
        /// The SNI (Server Name Indication) mode of the upstream host. It supports two modes: 'distribution' and 'origin', for more information about these modes please check the resource docs.
        /// </summary>
        public readonly string SniMode;
        /// <summary>
        /// Enable or disable WAF to protect the upstream host.
        /// </summary>
        public readonly bool Waf;

        [OutputConstructor]
        private DistributionRoutingRuleUpstream(
            bool caching,

            Outputs.DistributionRoutingRuleUpstreamGeoRestrictions? geoRestrictions,

            string host,

            string rateLimitClass,

            string sniMode,

            bool waf)
        {
            Caching = caching;
            GeoRestrictions = geoRestrictions;
            Host = host;
            RateLimitClass = rateLimitClass;
            SniMode = sniMode;
            Waf = waf;
        }
    }
}
