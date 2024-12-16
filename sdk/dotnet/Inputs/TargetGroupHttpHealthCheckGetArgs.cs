// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Inputs
{

    public sealed class TargetGroupHttpHealthCheckGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("matchType", required: true)]
        public Input<string> MatchType { get; set; } = null!;

        /// <summary>
        /// The method for the HTTP health check.
        /// </summary>
        [Input("method")]
        public Input<string>? Method { get; set; }

        [Input("negate")]
        public Input<bool>? Negate { get; set; }

        /// <summary>
        /// The path (destination URL) for the HTTP health check request; the default is /.
        /// </summary>
        [Input("path")]
        public Input<string>? Path { get; set; }

        [Input("regex")]
        public Input<bool>? Regex { get; set; }

        /// <summary>
        /// The response returned by the request, depending on the match type.
        /// </summary>
        [Input("response", required: true)]
        public Input<string> Response { get; set; } = null!;

        public TargetGroupHttpHealthCheckGetArgs()
        {
        }
        public static new TargetGroupHttpHealthCheckGetArgs Empty => new TargetGroupHttpHealthCheckGetArgs();
    }
}
