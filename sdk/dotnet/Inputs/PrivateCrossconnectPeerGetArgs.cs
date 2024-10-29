// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Inputs
{

    public sealed class PrivateCrossconnectPeerGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The id of the cross-connected datacenter
        /// </summary>
        [Input("datacenterId")]
        public Input<string>? DatacenterId { get; set; }

        /// <summary>
        /// The name of the cross-connected datacenter
        /// </summary>
        [Input("datacenterName")]
        public Input<string>? DatacenterName { get; set; }

        /// <summary>
        /// The id of the cross-connected LAN
        /// </summary>
        [Input("lanId")]
        public Input<string>? LanId { get; set; }

        /// <summary>
        /// The name of the cross-connected LAN
        /// </summary>
        [Input("lanName")]
        public Input<string>? LanName { get; set; }

        /// <summary>
        /// The location of the cross-connected datacenter
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        public PrivateCrossconnectPeerGetArgs()
        {
        }
        public static new PrivateCrossconnectPeerGetArgs Empty => new PrivateCrossconnectPeerGetArgs();
    }
}
