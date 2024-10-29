// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Inputs
{

    public sealed class KafkaClusterConnectionsGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("brokerAddresses", required: true)]
        private InputList<string>? _brokerAddresses;

        /// <summary>
        /// [list] IP address and port of cluster brokers.
        /// </summary>
        public InputList<string> BrokerAddresses
        {
            get => _brokerAddresses ?? (_brokerAddresses = new InputList<string>());
            set => _brokerAddresses = value;
        }

        /// <summary>
        /// [string] The datacenter to connect your instance to.
        /// </summary>
        [Input("datacenterId", required: true)]
        public Input<string> DatacenterId { get; set; } = null!;

        /// <summary>
        /// [string] The numeric LAN ID to connect your instance to.
        /// </summary>
        [Input("lanId", required: true)]
        public Input<string> LanId { get; set; } = null!;

        public KafkaClusterConnectionsGetArgs()
        {
        }
        public static new KafkaClusterConnectionsGetArgs Empty => new KafkaClusterConnectionsGetArgs();
    }
}
