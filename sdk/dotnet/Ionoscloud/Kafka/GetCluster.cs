// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Kafka
{
    public static class GetCluster
    {
        /// <summary>
        /// The **Kafka Cluster data source** can be used to search for and return an existing Kafka Cluster.
        /// You can provide a string for the name parameter which will be compared with provisioned Kafka Clusters.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ### By ID
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Kafka.GetCluster.Invoke(new()
        ///     {
        ///         Id = "your_kafka_cluster_id",
        ///         Location = "location_of_kafka_cluster",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Name
        /// 
        /// Needs to have the resource be previously created, or a depends_on clause to ensure that the resource is created before
        /// this data source is called.
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Kafka.GetCluster.Invoke(new()
        ///     {
        ///         Name = "kafka-cluster",
        ///         Location = "location_of_kafka_cluster",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetClusterResult> InvokeAsync(GetClusterArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetClusterResult>("ionoscloud:kafka/getCluster:getCluster", args ?? new GetClusterArgs(), options.WithDefaults());

        /// <summary>
        /// The **Kafka Cluster data source** can be used to search for and return an existing Kafka Cluster.
        /// You can provide a string for the name parameter which will be compared with provisioned Kafka Clusters.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ### By ID
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Kafka.GetCluster.Invoke(new()
        ///     {
        ///         Id = "your_kafka_cluster_id",
        ///         Location = "location_of_kafka_cluster",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Name
        /// 
        /// Needs to have the resource be previously created, or a depends_on clause to ensure that the resource is created before
        /// this data source is called.
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Kafka.GetCluster.Invoke(new()
        ///     {
        ///         Name = "kafka-cluster",
        ///         Location = "location_of_kafka_cluster",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetClusterResult> Invoke(GetClusterInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetClusterResult>("ionoscloud:kafka/getCluster:getCluster", args ?? new GetClusterInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The **Kafka Cluster data source** can be used to search for and return an existing Kafka Cluster.
        /// You can provide a string for the name parameter which will be compared with provisioned Kafka Clusters.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ### By ID
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Kafka.GetCluster.Invoke(new()
        ///     {
        ///         Id = "your_kafka_cluster_id",
        ///         Location = "location_of_kafka_cluster",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Name
        /// 
        /// Needs to have the resource be previously created, or a depends_on clause to ensure that the resource is created before
        /// this data source is called.
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Kafka.GetCluster.Invoke(new()
        ///     {
        ///         Name = "kafka-cluster",
        ///         Location = "location_of_kafka_cluster",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetClusterResult> Invoke(GetClusterInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetClusterResult>("ionoscloud:kafka/getCluster:getCluster", args ?? new GetClusterInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetClusterArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// ID of an existing Kafka Cluster that you want to search for.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// The location of the Kafka Cluster. Possible values: `de/fra`, `de/txl`
        /// </summary>
        [Input("location", required: true)]
        public string Location { get; set; } = null!;

        /// <summary>
        /// Name of an existing Kafka Cluster that you want to search for.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        [Input("partialMatch")]
        public bool? PartialMatch { get; set; }

        public GetClusterArgs()
        {
        }
        public static new GetClusterArgs Empty => new GetClusterArgs();
    }

    public sealed class GetClusterInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// ID of an existing Kafka Cluster that you want to search for.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// The location of the Kafka Cluster. Possible values: `de/fra`, `de/txl`
        /// </summary>
        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        /// <summary>
        /// Name of an existing Kafka Cluster that you want to search for.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("partialMatch")]
        public Input<bool>? PartialMatch { get; set; }

        public GetClusterInvokeArgs()
        {
        }
        public static new GetClusterInvokeArgs Empty => new GetClusterInvokeArgs();
    }


    [OutputType]
    public sealed class GetClusterResult
    {
        /// <summary>
        /// IP address and port of cluster brokers.
        /// </summary>
        public readonly ImmutableArray<string> BrokerAddresses;
        /// <summary>
        /// Connection information of the Kafka Cluster. Minimum items: 1, maximum items: 1.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetClusterConnectionResult> Connections;
        /// <summary>
        /// UUID of the Kafka Cluster.
        /// </summary>
        public readonly string Id;
        public readonly string Location;
        /// <summary>
        /// The name of the Kafka Cluster.
        /// </summary>
        public readonly string Name;
        public readonly bool? PartialMatch;
        /// <summary>
        /// The size of the Kafka Cluster.
        /// </summary>
        public readonly string Size;
        /// <summary>
        /// The version of the Kafka Cluster.
        /// </summary>
        public readonly string Version;

        [OutputConstructor]
        private GetClusterResult(
            ImmutableArray<string> brokerAddresses,

            ImmutableArray<Outputs.GetClusterConnectionResult> connections,

            string id,

            string location,

            string name,

            bool? partialMatch,

            string size,

            string version)
        {
            BrokerAddresses = brokerAddresses;
            Connections = connections;
            Id = id;
            Location = location;
            Name = name;
            PartialMatch = partialMatch;
            Size = size;
            Version = version;
        }
    }
}
