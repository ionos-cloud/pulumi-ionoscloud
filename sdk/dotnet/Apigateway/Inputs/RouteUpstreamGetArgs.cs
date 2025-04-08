// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Apigateway.Inputs
{

    public sealed class RouteUpstreamGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] The host of the upstream.
        /// </summary>
        [Input("host", required: true)]
        public Input<string> Host { get; set; } = null!;

        /// <summary>
        /// [string] The load balancer algorithm. Default value: `roundrobin`.
        /// </summary>
        [Input("loadbalancer")]
        public Input<string>? Loadbalancer { get; set; }

        /// <summary>
        /// [int] The port of the upstream. Default value: `80`.
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        /// <summary>
        /// [string] The target URL of the upstream. Default value: `http`.
        /// </summary>
        [Input("scheme")]
        public Input<string>? Scheme { get; set; }

        /// <summary>
        /// [int] Weight with which to split traffic to the upstream. Default value: `100`.
        /// </summary>
        [Input("weight")]
        public Input<int>? Weight { get; set; }

        public RouteUpstreamGetArgs()
        {
        }
        public static new RouteUpstreamGetArgs Empty => new RouteUpstreamGetArgs();
    }
}
