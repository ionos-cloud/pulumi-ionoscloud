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
    public sealed class GetTargetGroupHealthCheckResult
    {
        /// <summary>
        /// The interval in milliseconds between consecutive health checks; default is 2000.
        /// </summary>
        public readonly int CheckInterval;
        /// <summary>
        /// The maximum time in milliseconds to wait for a target to respond to a check. For target VMs with 'Check Interval' set, the lesser of the two  values is used once the TCP connection is established.
        /// </summary>
        public readonly int CheckTimeout;
        /// <summary>
        /// The maximum number of attempts to reconnect to a target after a connection failure. Valid range is 0 to 65535, and default is three reconnection.
        /// </summary>
        public readonly int Retries;

        [OutputConstructor]
        private GetTargetGroupHealthCheckResult(
            int checkInterval,

            int checkTimeout,

            int retries)
        {
            CheckInterval = checkInterval;
            CheckTimeout = checkTimeout;
            Retries = retries;
        }
    }
}
