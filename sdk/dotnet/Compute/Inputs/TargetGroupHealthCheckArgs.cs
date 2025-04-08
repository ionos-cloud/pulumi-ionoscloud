// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Compute.Inputs
{

    public sealed class TargetGroupHealthCheckArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [int] The interval in milliseconds between consecutive health checks; default is 2000.
        /// </summary>
        [Input("checkInterval")]
        public Input<int>? CheckInterval { get; set; }

        /// <summary>
        /// [int] The maximum time in milliseconds to wait for a target to respond to a check. For target VMs with 'Check Interval' set, the lesser of the two  values is used once the TCP connection is established.
        /// </summary>
        [Input("checkTimeout")]
        public Input<int>? CheckTimeout { get; set; }

        /// <summary>
        /// [int] The maximum number of attempts to reconnect to a target after a connection failure. Valid range is 0 to 65535, and default is three reconnection.
        /// </summary>
        [Input("retries")]
        public Input<int>? Retries { get; set; }

        public TargetGroupHealthCheckArgs()
        {
        }
        public static new TargetGroupHealthCheckArgs Empty => new TargetGroupHealthCheckArgs();
    }
}
