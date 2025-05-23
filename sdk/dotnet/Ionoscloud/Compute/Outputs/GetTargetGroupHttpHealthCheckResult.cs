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
    public sealed class GetTargetGroupHttpHealthCheckResult
    {
        public readonly string MatchType;
        /// <summary>
        /// The method for the HTTP health check.
        /// </summary>
        public readonly string Method;
        public readonly bool Negate;
        /// <summary>
        /// The path (destination URL) for the HTTP health check request; the default is /.
        /// </summary>
        public readonly string Path;
        public readonly bool Regex;
        /// <summary>
        /// The response returned by the request, depending on the match type.
        /// </summary>
        public readonly string Response;

        [OutputConstructor]
        private GetTargetGroupHttpHealthCheckResult(
            string matchType,

            string method,

            bool negate,

            string path,

            bool regex,

            string response)
        {
            MatchType = matchType;
            Method = method;
            Negate = negate;
            Path = path;
            Regex = regex;
            Response = response;
        }
    }
}
