// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Nlb.Inputs
{

    public sealed class ForwardingRuleTargetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Health check attributes for Network Load Balancer forwarding rule target.
        /// </summary>
        [Input("healthCheck")]
        public Input<Inputs.ForwardingRuleTargetHealthCheckArgs>? HealthCheck { get; set; }

        /// <summary>
        /// [string] IP of a balanced target VM.
        /// </summary>
        [Input("ip", required: true)]
        public Input<string> Ip { get; set; } = null!;

        /// <summary>
        /// [int] Port of the balanced target service. (range: 1 to 65535).
        /// </summary>
        [Input("port", required: true)]
        public Input<int> Port { get; set; } = null!;

        /// <summary>
        /// [string] The proxy protocol version. Accepted values are `none`, `v1`, `v2`, `v2ssl`. If unspecified, the default value of `none` is used.
        /// </summary>
        [Input("proxyProtocol")]
        public Input<string>? ProxyProtocol { get; set; }

        /// <summary>
        /// [int] Weight parameter is used to adjust the target VM's weight relative to other target VMs.
        /// </summary>
        [Input("weight", required: true)]
        public Input<int> Weight { get; set; } = null!;

        public ForwardingRuleTargetArgs()
        {
        }
        public static new ForwardingRuleTargetArgs Empty => new ForwardingRuleTargetArgs();
    }
}
