// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Nlb.Outputs
{

    [OutputType]
    public sealed class ForwardingRuleTarget
    {
        /// <summary>
        /// Health check attributes for Network Load Balancer forwarding rule target.
        /// </summary>
        public readonly Outputs.ForwardingRuleTargetHealthCheck? HealthCheck;
        /// <summary>
        /// [string] IP of a balanced target VM.
        /// </summary>
        public readonly string Ip;
        /// <summary>
        /// [int] Port of the balanced target service. (range: 1 to 65535).
        /// </summary>
        public readonly int Port;
        /// <summary>
        /// [string] The proxy protocol version. Accepted values are `none`, `v1`, `v2`, `v2ssl`. If unspecified, the default value of `none` is used.
        /// </summary>
        public readonly string? ProxyProtocol;
        /// <summary>
        /// [int] Weight parameter is used to adjust the target VM's weight relative to other target VMs.
        /// </summary>
        public readonly int Weight;

        [OutputConstructor]
        private ForwardingRuleTarget(
            Outputs.ForwardingRuleTargetHealthCheck? healthCheck,

            string ip,

            int port,

            string? proxyProtocol,

            int weight)
        {
            HealthCheck = healthCheck;
            Ip = ip;
            Port = port;
            ProxyProtocol = proxyProtocol;
            Weight = weight;
        }
    }
}
