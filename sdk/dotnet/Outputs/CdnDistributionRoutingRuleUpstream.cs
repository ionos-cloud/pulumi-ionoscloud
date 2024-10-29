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
    public sealed class CdnDistributionRoutingRuleUpstream
    {
        /// <summary>
        /// [bool] Enable or disable caching. If enabled, the CDN will cache the responses from the upstream host. Subsequent requests for the same resource will be served from the cache.
        /// </summary>
        public readonly bool Caching;
        /// <summary>
        /// [map] - A map of geo_restrictions
        /// </summary>
        public readonly Outputs.CdnDistributionRoutingRuleUpstreamGeoRestrictions? GeoRestrictions;
        /// <summary>
        /// [string] The upstream host that handles the requests if not already cached. This host will be protected by the WAF if the option is enabled.
        /// </summary>
        public readonly string Host;
        /// <summary>
        /// [string] Rate limit class that will be applied to limit the number of incoming requests per IP.
        /// </summary>
        public readonly string RateLimitClass;
        /// <summary>
        /// [bool] Enable or disable WAF to protect the upstream host.
        /// </summary>
        public readonly bool Waf;

        [OutputConstructor]
        private CdnDistributionRoutingRuleUpstream(
            bool caching,

            Outputs.CdnDistributionRoutingRuleUpstreamGeoRestrictions? geoRestrictions,

            string host,

            string rateLimitClass,

            bool waf)
        {
            Caching = caching;
            GeoRestrictions = geoRestrictions;
            Host = host;
            RateLimitClass = rateLimitClass;
            Waf = waf;
        }
    }
}
