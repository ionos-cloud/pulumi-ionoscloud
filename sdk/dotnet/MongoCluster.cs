// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    [IonoscloudResourceType("ionoscloud:index/mongoCluster:MongoCluster")]
    public partial class MongoCluster : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Backup related properties.
        /// </summary>
        [Output("backup")]
        public Output<Outputs.MongoClusterBackup?> Backup { get; private set; } = null!;

        /// <summary>
        /// The MongoDB Connector for Business Intelligence allows you to query a MongoDB database using SQL commands to aid in data
        /// analysis.
        /// </summary>
        [Output("biConnector")]
        public Output<Outputs.MongoClusterBiConnector> BiConnector { get; private set; } = null!;

        /// <summary>
        /// The connection string for your cluster.
        /// </summary>
        [Output("connectionString")]
        public Output<string> ConnectionString { get; private set; } = null!;

        /// <summary>
        /// Details about the network connection for your cluster.
        /// </summary>
        [Output("connections")]
        public Output<Outputs.MongoClusterConnections> Connections { get; private set; } = null!;

        /// <summary>
        /// The number of CPU cores per instance.
        /// </summary>
        [Output("cores")]
        public Output<int> Cores { get; private set; } = null!;

        /// <summary>
        /// The name of your cluster.
        /// </summary>
        [Output("displayName")]
        public Output<string> DisplayName { get; private set; } = null!;

        /// <summary>
        /// The cluster edition. Must be one of: playground, business, enterprise
        /// </summary>
        [Output("edition")]
        public Output<string> Edition { get; private set; } = null!;

        /// <summary>
        /// The total number of instances in the cluster (one master and n-1 standbys). Example: 1, 3, 5, 7. For enterprise edition
        /// at least 3.
        /// </summary>
        [Output("instances")]
        public Output<int> Instances { get; private set; } = null!;

        /// <summary>
        /// The physical location where the cluster will be created. This will be where all of your instances live. Property cannot
        /// be modified after datacenter creation (disallowed in update requests). Available locations: de/txl, gb/lhr, es/vit.
        /// Update forces cluster re-creation.
        /// </summary>
        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// A weekly 4 hour-long window, during which maintenance might occur
        /// </summary>
        [Output("maintenanceWindow")]
        public Output<Outputs.MongoClusterMaintenanceWindow> MaintenanceWindow { get; private set; } = null!;

        /// <summary>
        /// The MongoDB version of your cluster. Update forces cluster re-creation.
        /// </summary>
        [Output("mongodbVersion")]
        public Output<string> MongodbVersion { get; private set; } = null!;

        /// <summary>
        /// The amount of memory per instance in megabytes. Multiple of 1024
        /// </summary>
        [Output("ram")]
        public Output<int> Ram { get; private set; } = null!;

        /// <summary>
        /// The total number of shards in the cluster.
        /// </summary>
        [Output("shards")]
        public Output<int?> Shards { get; private set; } = null!;

        /// <summary>
        /// The amount of storage per instance in megabytes. At least 5120, at most 2097152
        /// </summary>
        [Output("storageSize")]
        public Output<int> StorageSize { get; private set; } = null!;

        /// <summary>
        /// The storage type. One of : HDD, SSD, SSD Standard, SSD Premium
        /// </summary>
        [Output("storageType")]
        public Output<string> StorageType { get; private set; } = null!;

        /// <summary>
        /// The unique ID of the template, which specifies the number of cores, storage size, and memory. You cannot downgrade to a
        /// smaller template or minor edition (e.g. from business to playground). To get a list of all templates to confirm the
        /// changes use the /templates endpoint.
        /// </summary>
        [Output("templateId")]
        public Output<string?> TemplateId { get; private set; } = null!;

        /// <summary>
        /// The cluster type, either `replicaset` or `sharded-cluster`
        /// </summary>
        [Output("type")]
        public Output<string> Type { get; private set; } = null!;


        /// <summary>
        /// Create a MongoCluster resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public MongoCluster(string name, MongoClusterArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:index/mongoCluster:MongoCluster", name, args ?? new MongoClusterArgs(), MakeResourceOptions(options, ""))
        {
        }

        private MongoCluster(string name, Input<string> id, MongoClusterState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:index/mongoCluster:MongoCluster", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "https://github.com/ionos-cloud/pulumi-ionoscloud/",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing MongoCluster resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static MongoCluster Get(string name, Input<string> id, MongoClusterState? state = null, CustomResourceOptions? options = null)
        {
            return new MongoCluster(name, id, state, options);
        }
    }

    public sealed class MongoClusterArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Backup related properties.
        /// </summary>
        [Input("backup")]
        public Input<Inputs.MongoClusterBackupArgs>? Backup { get; set; }

        /// <summary>
        /// The MongoDB Connector for Business Intelligence allows you to query a MongoDB database using SQL commands to aid in data
        /// analysis.
        /// </summary>
        [Input("biConnector")]
        public Input<Inputs.MongoClusterBiConnectorArgs>? BiConnector { get; set; }

        /// <summary>
        /// Details about the network connection for your cluster.
        /// </summary>
        [Input("connections", required: true)]
        public Input<Inputs.MongoClusterConnectionsArgs> Connections { get; set; } = null!;

        /// <summary>
        /// The number of CPU cores per instance.
        /// </summary>
        [Input("cores")]
        public Input<int>? Cores { get; set; }

        /// <summary>
        /// The name of your cluster.
        /// </summary>
        [Input("displayName", required: true)]
        public Input<string> DisplayName { get; set; } = null!;

        /// <summary>
        /// The cluster edition. Must be one of: playground, business, enterprise
        /// </summary>
        [Input("edition")]
        public Input<string>? Edition { get; set; }

        /// <summary>
        /// The total number of instances in the cluster (one master and n-1 standbys). Example: 1, 3, 5, 7. For enterprise edition
        /// at least 3.
        /// </summary>
        [Input("instances", required: true)]
        public Input<int> Instances { get; set; } = null!;

        /// <summary>
        /// The physical location where the cluster will be created. This will be where all of your instances live. Property cannot
        /// be modified after datacenter creation (disallowed in update requests). Available locations: de/txl, gb/lhr, es/vit.
        /// Update forces cluster re-creation.
        /// </summary>
        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        /// <summary>
        /// A weekly 4 hour-long window, during which maintenance might occur
        /// </summary>
        [Input("maintenanceWindow")]
        public Input<Inputs.MongoClusterMaintenanceWindowArgs>? MaintenanceWindow { get; set; }

        /// <summary>
        /// The MongoDB version of your cluster. Update forces cluster re-creation.
        /// </summary>
        [Input("mongodbVersion", required: true)]
        public Input<string> MongodbVersion { get; set; } = null!;

        /// <summary>
        /// The amount of memory per instance in megabytes. Multiple of 1024
        /// </summary>
        [Input("ram")]
        public Input<int>? Ram { get; set; }

        /// <summary>
        /// The total number of shards in the cluster.
        /// </summary>
        [Input("shards")]
        public Input<int>? Shards { get; set; }

        /// <summary>
        /// The amount of storage per instance in megabytes. At least 5120, at most 2097152
        /// </summary>
        [Input("storageSize")]
        public Input<int>? StorageSize { get; set; }

        /// <summary>
        /// The storage type. One of : HDD, SSD, SSD Standard, SSD Premium
        /// </summary>
        [Input("storageType")]
        public Input<string>? StorageType { get; set; }

        /// <summary>
        /// The unique ID of the template, which specifies the number of cores, storage size, and memory. You cannot downgrade to a
        /// smaller template or minor edition (e.g. from business to playground). To get a list of all templates to confirm the
        /// changes use the /templates endpoint.
        /// </summary>
        [Input("templateId")]
        public Input<string>? TemplateId { get; set; }

        /// <summary>
        /// The cluster type, either `replicaset` or `sharded-cluster`
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        public MongoClusterArgs()
        {
        }
        public static new MongoClusterArgs Empty => new MongoClusterArgs();
    }

    public sealed class MongoClusterState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Backup related properties.
        /// </summary>
        [Input("backup")]
        public Input<Inputs.MongoClusterBackupGetArgs>? Backup { get; set; }

        /// <summary>
        /// The MongoDB Connector for Business Intelligence allows you to query a MongoDB database using SQL commands to aid in data
        /// analysis.
        /// </summary>
        [Input("biConnector")]
        public Input<Inputs.MongoClusterBiConnectorGetArgs>? BiConnector { get; set; }

        /// <summary>
        /// The connection string for your cluster.
        /// </summary>
        [Input("connectionString")]
        public Input<string>? ConnectionString { get; set; }

        /// <summary>
        /// Details about the network connection for your cluster.
        /// </summary>
        [Input("connections")]
        public Input<Inputs.MongoClusterConnectionsGetArgs>? Connections { get; set; }

        /// <summary>
        /// The number of CPU cores per instance.
        /// </summary>
        [Input("cores")]
        public Input<int>? Cores { get; set; }

        /// <summary>
        /// The name of your cluster.
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// The cluster edition. Must be one of: playground, business, enterprise
        /// </summary>
        [Input("edition")]
        public Input<string>? Edition { get; set; }

        /// <summary>
        /// The total number of instances in the cluster (one master and n-1 standbys). Example: 1, 3, 5, 7. For enterprise edition
        /// at least 3.
        /// </summary>
        [Input("instances")]
        public Input<int>? Instances { get; set; }

        /// <summary>
        /// The physical location where the cluster will be created. This will be where all of your instances live. Property cannot
        /// be modified after datacenter creation (disallowed in update requests). Available locations: de/txl, gb/lhr, es/vit.
        /// Update forces cluster re-creation.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// A weekly 4 hour-long window, during which maintenance might occur
        /// </summary>
        [Input("maintenanceWindow")]
        public Input<Inputs.MongoClusterMaintenanceWindowGetArgs>? MaintenanceWindow { get; set; }

        /// <summary>
        /// The MongoDB version of your cluster. Update forces cluster re-creation.
        /// </summary>
        [Input("mongodbVersion")]
        public Input<string>? MongodbVersion { get; set; }

        /// <summary>
        /// The amount of memory per instance in megabytes. Multiple of 1024
        /// </summary>
        [Input("ram")]
        public Input<int>? Ram { get; set; }

        /// <summary>
        /// The total number of shards in the cluster.
        /// </summary>
        [Input("shards")]
        public Input<int>? Shards { get; set; }

        /// <summary>
        /// The amount of storage per instance in megabytes. At least 5120, at most 2097152
        /// </summary>
        [Input("storageSize")]
        public Input<int>? StorageSize { get; set; }

        /// <summary>
        /// The storage type. One of : HDD, SSD, SSD Standard, SSD Premium
        /// </summary>
        [Input("storageType")]
        public Input<string>? StorageType { get; set; }

        /// <summary>
        /// The unique ID of the template, which specifies the number of cores, storage size, and memory. You cannot downgrade to a
        /// smaller template or minor edition (e.g. from business to playground). To get a list of all templates to confirm the
        /// changes use the /templates endpoint.
        /// </summary>
        [Input("templateId")]
        public Input<string>? TemplateId { get; set; }

        /// <summary>
        /// The cluster type, either `replicaset` or `sharded-cluster`
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        public MongoClusterState()
        {
        }
        public static new MongoClusterState Empty => new MongoClusterState();
    }
}
