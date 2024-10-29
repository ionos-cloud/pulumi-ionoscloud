// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Inputs
{

    public sealed class CubeServerNicFirewallGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("icmpCode")]
        public Input<string>? IcmpCode { get; set; }

        [Input("icmpType")]
        public Input<string>? IcmpType { get; set; }

        /// <summary>
        /// [string] The name of the server.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("portRangeEnd")]
        public Input<int>? PortRangeEnd { get; set; }

        [Input("portRangeStart")]
        public Input<int>? PortRangeStart { get; set; }

        [Input("protocol", required: true)]
        public Input<string> Protocol { get; set; } = null!;

        [Input("sourceIp")]
        public Input<string>? SourceIp { get; set; }

        [Input("sourceMac")]
        public Input<string>? SourceMac { get; set; }

        [Input("targetIp")]
        public Input<string>? TargetIp { get; set; }

        [Input("type")]
        public Input<string>? Type { get; set; }

        public CubeServerNicFirewallGetArgs()
        {
        }
        public static new CubeServerNicFirewallGetArgs Empty => new CubeServerNicFirewallGetArgs();
    }
}
