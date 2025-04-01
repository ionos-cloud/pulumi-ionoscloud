// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Nlb.Outputs
{

    [OutputType]
    public sealed class GetForwardingRuleTargetResult
    {
        /// <summary>
        /// Health check attributes for Network Load Balancer forwarding rule target.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetForwardingRuleTargetHealthCheckResult> HealthChecks;
        /// <summary>
        /// IP of a balanced target VM.
        /// </summary>
        public readonly string Ip;
        /// <summary>
        /// Port of the balanced target service. (range: 1 to 65535).
        /// </summary>
        public readonly int Port;
        /// <summary>
        /// The proxy protocol version.
        /// </summary>
        public readonly string ProxyProtocol;
        /// <summary>
        /// Weight parameter is used to adjust the target VM's weight relative to other target VMs.
        /// </summary>
        public readonly int Weight;

        [OutputConstructor]
        private GetForwardingRuleTargetResult(
            ImmutableArray<Outputs.GetForwardingRuleTargetHealthCheckResult> healthChecks,

            string ip,

            int port,

            string proxyProtocol,

            int weight)
        {
            HealthChecks = healthChecks;
            Ip = ip;
            Port = port;
            ProxyProtocol = proxyProtocol;
            Weight = weight;
        }
    }
}
