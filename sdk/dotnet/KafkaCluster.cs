// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    [IonoscloudResourceType("ionoscloud:index/kafkaCluster:KafkaCluster")]
    public partial class KafkaCluster : global::Pulumi.CustomResource
    {
        /// <summary>
        /// IP address and port of cluster brokers.
        /// </summary>
        [Output("brokerAddresses")]
        public Output<ImmutableArray<string>> BrokerAddresses { get; private set; } = null!;

        /// <summary>
        /// The network connection for your Kafka Cluster. Only one connection is allowed.
        /// </summary>
        [Output("connections")]
        public Output<Outputs.KafkaClusterConnections> Connections { get; private set; } = null!;

        /// <summary>
        /// The location of your Kafka Cluster. Supported locations: de/fra, de/txl
        /// </summary>
        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// The name of your Kafka Cluster. Must be 63 characters or less and must begin and end with an alphanumeric character
        /// (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The size of your Kafka Cluster. The size of the Kafka Cluster is given in T-shirt sizes. Valid values are: XS, S
        /// </summary>
        [Output("size")]
        public Output<string> Size { get; private set; } = null!;

        /// <summary>
        /// The desired Kafka Version. Supported version: 3.7.0
        /// </summary>
        [Output("version")]
        public Output<string> Version { get; private set; } = null!;


        /// <summary>
        /// Create a KafkaCluster resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public KafkaCluster(string name, KafkaClusterArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:index/kafkaCluster:KafkaCluster", name, args ?? new KafkaClusterArgs(), MakeResourceOptions(options, ""))
        {
        }

        private KafkaCluster(string name, Input<string> id, KafkaClusterState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:index/kafkaCluster:KafkaCluster", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing KafkaCluster resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static KafkaCluster Get(string name, Input<string> id, KafkaClusterState? state = null, CustomResourceOptions? options = null)
        {
            return new KafkaCluster(name, id, state, options);
        }
    }

    public sealed class KafkaClusterArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The network connection for your Kafka Cluster. Only one connection is allowed.
        /// </summary>
        [Input("connections", required: true)]
        public Input<Inputs.KafkaClusterConnectionsArgs> Connections { get; set; } = null!;

        /// <summary>
        /// The location of your Kafka Cluster. Supported locations: de/fra, de/txl
        /// </summary>
        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        /// <summary>
        /// The name of your Kafka Cluster. Must be 63 characters or less and must begin and end with an alphanumeric character
        /// (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The size of your Kafka Cluster. The size of the Kafka Cluster is given in T-shirt sizes. Valid values are: XS, S
        /// </summary>
        [Input("size", required: true)]
        public Input<string> Size { get; set; } = null!;

        /// <summary>
        /// The desired Kafka Version. Supported version: 3.7.0
        /// </summary>
        [Input("version", required: true)]
        public Input<string> Version { get; set; } = null!;

        public KafkaClusterArgs()
        {
        }
        public static new KafkaClusterArgs Empty => new KafkaClusterArgs();
    }

    public sealed class KafkaClusterState : global::Pulumi.ResourceArgs
    {
        [Input("brokerAddresses")]
        private InputList<string>? _brokerAddresses;

        /// <summary>
        /// IP address and port of cluster brokers.
        /// </summary>
        public InputList<string> BrokerAddresses
        {
            get => _brokerAddresses ?? (_brokerAddresses = new InputList<string>());
            set => _brokerAddresses = value;
        }

        /// <summary>
        /// The network connection for your Kafka Cluster. Only one connection is allowed.
        /// </summary>
        [Input("connections")]
        public Input<Inputs.KafkaClusterConnectionsGetArgs>? Connections { get; set; }

        /// <summary>
        /// The location of your Kafka Cluster. Supported locations: de/fra, de/txl
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// The name of your Kafka Cluster. Must be 63 characters or less and must begin and end with an alphanumeric character
        /// (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The size of your Kafka Cluster. The size of the Kafka Cluster is given in T-shirt sizes. Valid values are: XS, S
        /// </summary>
        [Input("size")]
        public Input<string>? Size { get; set; }

        /// <summary>
        /// The desired Kafka Version. Supported version: 3.7.0
        /// </summary>
        [Input("version")]
        public Input<string>? Version { get; set; }

        public KafkaClusterState()
        {
        }
        public static new KafkaClusterState Empty => new KafkaClusterState();
    }
}
