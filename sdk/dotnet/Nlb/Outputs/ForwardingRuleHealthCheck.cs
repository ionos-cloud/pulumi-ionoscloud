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
    public sealed class ForwardingRuleHealthCheck
    {
        /// <summary>
        /// [int] ClientTimeout is expressed in milliseconds. This inactivity timeout applies when the client is expected to acknowledge or send data. If unset the default of 50 seconds will be used.
        /// </summary>
        public readonly int? ClientTimeout;
        /// <summary>
        /// [int] It specifies the maximum time (in milliseconds) to wait for a connection attempt to a target VM to succeed. If unset, the default of 5 seconds will be used.
        /// </summary>
        public readonly int? ConnectTimeout;
        /// <summary>
        /// [int] Retries specifies the number of retries to perform on a target VM after a connection failure. If unset, the default value of 3 will be used.
        /// </summary>
        public readonly int? Retries;
        /// <summary>
        /// [int] TargetTimeout specifies the maximum inactivity time (in milliseconds) on the target VM side. If unset, the default of 50 seconds will be used.
        /// </summary>
        public readonly int? TargetTimeout;

        [OutputConstructor]
        private ForwardingRuleHealthCheck(
            int? clientTimeout,

            int? connectTimeout,

            int? retries,

            int? targetTimeout)
        {
            ClientTimeout = clientTimeout;
            ConnectTimeout = connectTimeout;
            Retries = retries;
            TargetTimeout = targetTimeout;
        }
    }
}
