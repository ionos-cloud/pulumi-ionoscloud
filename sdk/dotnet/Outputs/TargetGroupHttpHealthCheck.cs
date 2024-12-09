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
    public sealed class TargetGroupHttpHealthCheck
    {
        /// <summary>
        /// [string]
        /// </summary>
        public readonly string MatchType;
        /// <summary>
        /// [string] The method for the HTTP health check.
        /// </summary>
        public readonly string? Method;
        /// <summary>
        /// [bool]
        /// </summary>
        public readonly bool? Negate;
        /// <summary>
        /// [string] The path (destination URL) for the HTTP health check request; the default is /.
        /// </summary>
        public readonly string? Path;
        /// <summary>
        /// [bool]
        /// </summary>
        public readonly bool? Regex;
        /// <summary>
        /// [string] The response returned by the request, depending on the match type.
        /// </summary>
        public readonly string Response;

        [OutputConstructor]
        private TargetGroupHttpHealthCheck(
            string matchType,

            string? method,

            bool? negate,

            string? path,

            bool? regex,

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
