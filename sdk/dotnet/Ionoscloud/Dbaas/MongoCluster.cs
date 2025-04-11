// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Dbaas
{
    /// <summary>
    /// Manages a **DbaaS Mongo Cluster**.
    /// 
    /// ## Example Usage
    /// 
    /// ### Playground Or Business Editions. They Require Template_id Defined.
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ionoscloud = Ionoscloud.Pulumi.Ionoscloud;
    /// using Random = Pulumi.Random;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var datacenterExample = new Ionoscloud.Compute.Datacenter("datacenter_example", new()
    ///     {
    ///         Name = "example",
    ///         Location = "de/txl",
    ///         Description = "Datacenter for testing dbaas cluster",
    ///     });
    /// 
    ///     var lanExample = new Ionoscloud.Compute.Lan("lan_example", new()
    ///     {
    ///         DatacenterId = datacenterExample.Id,
    ///         Public = false,
    ///         Name = "example",
    ///     });
    /// 
    ///     var exampleMongoCluster = new Ionoscloud.Dbaas.MongoCluster("example_mongo_cluster", new()
    ///     {
    ///         MaintenanceWindow = new Ionoscloud.Dbaas.Inputs.MongoClusterMaintenanceWindowArgs
    ///         {
    ///             DayOfTheWeek = "Sunday",
    ///             Time = "09:00:00",
    ///         },
    ///         MongodbVersion = "5.0",
    ///         Instances = 1,
    ///         DisplayName = "example_mongo_cluster",
    ///         Location = datacenterExample.Location,
    ///         Connections = new Ionoscloud.Dbaas.Inputs.MongoClusterConnectionsArgs
    ///         {
    ///             DatacenterId = datacenterExample.Id,
    ///             LanId = lanExample.Id,
    ///             CidrLists = new[]
    ///             {
    ///                 "192.168.1.108/24",
    ///             },
    ///         },
    ///         TemplateId = "6b78ea06-ee0e-4689-998c-fc9c46e781f6",
    ///     });
    /// 
    ///     var clusterPassword = new Random.Index.Password("cluster_password", new()
    ///     {
    ///         Length = 16,
    ///         Special = true,
    ///         OverrideSpecial = "!#$%&amp;*()-_=+[]{}&lt;&gt;:?",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ### Enterprise Edition
    /// 
    /// **Enterprise Support: With MongoDB Enterprise, you gain access to professional support from the MongoDB team ensuring that you receive timely assistance and expert guidance when needed. IONOS offers enterprise-grade Service Level Agreements (SLAs), guaranteeing rapid response times and 24/7 support to address any critical issues that may arise.**
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ionoscloud = Ionoscloud.Pulumi.Ionoscloud;
    /// using Random = Pulumi.Random;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var datacenterExample = new Ionoscloud.Compute.Datacenter("datacenter_example", new()
    ///     {
    ///         Name = "example",
    ///         Location = "de/txl",
    ///         Description = "Datacenter for testing dbaas cluster",
    ///     });
    /// 
    ///     var lanExample = new Ionoscloud.Compute.Lan("lan_example", new()
    ///     {
    ///         DatacenterId = datacenterExample.Id,
    ///         Public = false,
    ///         Name = "example",
    ///     });
    /// 
    ///     var exampleMongoCluster = new Ionoscloud.Dbaas.MongoCluster("example_mongo_cluster", new()
    ///     {
    ///         MaintenanceWindow = new Ionoscloud.Dbaas.Inputs.MongoClusterMaintenanceWindowArgs
    ///         {
    ///             DayOfTheWeek = "Sunday",
    ///             Time = "09:00:00",
    ///         },
    ///         MongodbVersion = "5.0",
    ///         Instances = 3,
    ///         DisplayName = "example_mongo_cluster",
    ///         Location = datacenterExample.Location,
    ///         Connections = new Ionoscloud.Dbaas.Inputs.MongoClusterConnectionsArgs
    ///         {
    ///             DatacenterId = datacenterExample.Id,
    ///             LanId = lanExample.Id,
    ///             CidrLists = new[]
    ///             {
    ///                 "192.168.1.108/24",
    ///                 "192.168.1.109/24",
    ///                 "192.168.1.110/24",
    ///             },
    ///         },
    ///         Type = "sharded-cluster",
    ///         Shards = 2,
    ///         Edition = "enterprise",
    ///         Ram = 2048,
    ///         Cores = 1,
    ///         StorageSize = 5120,
    ///         StorageType = "HDD",
    ///     });
    /// 
    ///     var clusterPassword = new Random.Index.Password("cluster_password", new()
    ///     {
    ///         Length = 16,
    ///         Special = true,
    ///         OverrideSpecial = "!#$%&amp;*()-_=+[]{}&lt;&gt;:?",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// Resource DbaaS MongoDb Cluster can be imported using the `cluster_id`, e.g.
    /// 
    /// ```sh
    /// $ pulumi import ionoscloud:dbaas/mongoCluster:MongoCluster mycluser cluster uuid
    /// ```
    /// </summary>
    [IonoscloudResourceType("ionoscloud:dbaas/mongoCluster:MongoCluster")]
    public partial class MongoCluster : global::Pulumi.CustomResource
    {
        /// <summary>
        /// [list]
        /// </summary>
        [Output("backup")]
        public Output<Outputs.MongoClusterBackup?> Backup { get; private set; } = null!;

        /// <summary>
        /// (Computed)The MongoDB Connector for Business Intelligence allows you to query a MongoDB database using SQL commands to aid in data analysis.
        /// </summary>
        [Output("biConnector")]
        public Output<Outputs.MongoClusterBiConnector> BiConnector { get; private set; } = null!;

        /// <summary>
        /// [string] The physical location where the cluster will be created. This will be where all of your instances live. Updates to the value of the field force the cluster to be re-created. Available locations: de/txl, gb/lhr, es/vit
        /// </summary>
        [Output("connectionString")]
        public Output<string> ConnectionString { get; private set; } = null!;

        /// <summary>
        /// [List] Details about the network connection for your cluster. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Output("connections")]
        public Output<Outputs.MongoClusterConnections> Connections { get; private set; } = null!;

        /// <summary>
        /// (Computed)[int] The number of CPU cores per replica. Required for enterprise edition.
        /// </summary>
        [Output("cores")]
        public Output<int> Cores { get; private set; } = null!;

        /// <summary>
        /// [string] The name of your cluster. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Output("displayName")]
        public Output<string> DisplayName { get; private set; } = null!;

        /// <summary>
        /// (Computed)[string] Cluster edition. Playground, business or enterprise.
        /// </summary>
        [Output("edition")]
        public Output<string> Edition { get; private set; } = null!;

        /// <summary>
        /// [int] The total number of instances in the cluster (one master and n-1 standbys). Example: 1, 3, 5, 7. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Output("instances")]
        public Output<int> Instances { get; private set; } = null!;

        /// <summary>
        /// [string] The physical location where the cluster will be created. Property cannot be modified after datacenter creation (disallowed in update requests). Available locations: de/txl, gb/lhr, es/vit. Update forces cluster re-creation.
        /// </summary>
        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// (Computed) A weekly 4 hour-long window, during which maintenance might occur.  Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Output("maintenanceWindow")]
        public Output<Outputs.MongoClusterMaintenanceWindow> MaintenanceWindow { get; private set; } = null!;

        /// <summary>
        /// [string] The MongoDB version of your cluster. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Output("mongodbVersion")]
        public Output<string> MongodbVersion { get; private set; } = null!;

        /// <summary>
        /// (Computed)[int]The amount of memory per instance in megabytes. Required for enterprise edition.
        /// </summary>
        [Output("ram")]
        public Output<int> Ram { get; private set; } = null!;

        /// <summary>
        /// [int]The total number of shards in the cluster.
        /// </summary>
        [Output("shards")]
        public Output<int?> Shards { get; private set; } = null!;

        /// <summary>
        /// (Computed)[int] The amount of storage per instance in MB. Required for enterprise edition.
        /// </summary>
        [Output("storageSize")]
        public Output<int> StorageSize { get; private set; } = null!;

        /// <summary>
        /// (Computed)[String] The storage type used in your cluster. Required for enterprise edition.
        /// </summary>
        [Output("storageType")]
        public Output<string> StorageType { get; private set; } = null!;

        /// <summary>
        /// [string] The unique ID of the template, which specifies the number of cores, storage size, and memory. Updates to the value of the field force the cluster to be re-created. Required for playground and business editions. Must not be provided for enterprise edition.
        /// </summary>
        [Output("templateId")]
        public Output<string?> TemplateId { get; private set; } = null!;

        /// <summary>
        /// (Computed)[string]The cluster type, either `replicaset` or `sharded-cluster`.
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
            : base("ionoscloud:dbaas/mongoCluster:MongoCluster", name, args ?? new MongoClusterArgs(), MakeResourceOptions(options, ""))
        {
        }

        private MongoCluster(string name, Input<string> id, MongoClusterState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:dbaas/mongoCluster:MongoCluster", name, state, MakeResourceOptions(options, id))
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
        /// [list]
        /// </summary>
        [Input("backup")]
        public Input<Inputs.MongoClusterBackupArgs>? Backup { get; set; }

        /// <summary>
        /// (Computed)The MongoDB Connector for Business Intelligence allows you to query a MongoDB database using SQL commands to aid in data analysis.
        /// </summary>
        [Input("biConnector")]
        public Input<Inputs.MongoClusterBiConnectorArgs>? BiConnector { get; set; }

        /// <summary>
        /// [List] Details about the network connection for your cluster. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Input("connections", required: true)]
        public Input<Inputs.MongoClusterConnectionsArgs> Connections { get; set; } = null!;

        /// <summary>
        /// (Computed)[int] The number of CPU cores per replica. Required for enterprise edition.
        /// </summary>
        [Input("cores")]
        public Input<int>? Cores { get; set; }

        /// <summary>
        /// [string] The name of your cluster. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Input("displayName", required: true)]
        public Input<string> DisplayName { get; set; } = null!;

        /// <summary>
        /// (Computed)[string] Cluster edition. Playground, business or enterprise.
        /// </summary>
        [Input("edition")]
        public Input<string>? Edition { get; set; }

        /// <summary>
        /// [int] The total number of instances in the cluster (one master and n-1 standbys). Example: 1, 3, 5, 7. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Input("instances", required: true)]
        public Input<int> Instances { get; set; } = null!;

        /// <summary>
        /// [string] The physical location where the cluster will be created. Property cannot be modified after datacenter creation (disallowed in update requests). Available locations: de/txl, gb/lhr, es/vit. Update forces cluster re-creation.
        /// </summary>
        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        /// <summary>
        /// (Computed) A weekly 4 hour-long window, during which maintenance might occur.  Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Input("maintenanceWindow")]
        public Input<Inputs.MongoClusterMaintenanceWindowArgs>? MaintenanceWindow { get; set; }

        /// <summary>
        /// [string] The MongoDB version of your cluster. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Input("mongodbVersion", required: true)]
        public Input<string> MongodbVersion { get; set; } = null!;

        /// <summary>
        /// (Computed)[int]The amount of memory per instance in megabytes. Required for enterprise edition.
        /// </summary>
        [Input("ram")]
        public Input<int>? Ram { get; set; }

        /// <summary>
        /// [int]The total number of shards in the cluster.
        /// </summary>
        [Input("shards")]
        public Input<int>? Shards { get; set; }

        /// <summary>
        /// (Computed)[int] The amount of storage per instance in MB. Required for enterprise edition.
        /// </summary>
        [Input("storageSize")]
        public Input<int>? StorageSize { get; set; }

        /// <summary>
        /// (Computed)[String] The storage type used in your cluster. Required for enterprise edition.
        /// </summary>
        [Input("storageType")]
        public Input<string>? StorageType { get; set; }

        /// <summary>
        /// [string] The unique ID of the template, which specifies the number of cores, storage size, and memory. Updates to the value of the field force the cluster to be re-created. Required for playground and business editions. Must not be provided for enterprise edition.
        /// </summary>
        [Input("templateId")]
        public Input<string>? TemplateId { get; set; }

        /// <summary>
        /// (Computed)[string]The cluster type, either `replicaset` or `sharded-cluster`.
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
        /// [list]
        /// </summary>
        [Input("backup")]
        public Input<Inputs.MongoClusterBackupGetArgs>? Backup { get; set; }

        /// <summary>
        /// (Computed)The MongoDB Connector for Business Intelligence allows you to query a MongoDB database using SQL commands to aid in data analysis.
        /// </summary>
        [Input("biConnector")]
        public Input<Inputs.MongoClusterBiConnectorGetArgs>? BiConnector { get; set; }

        /// <summary>
        /// [string] The physical location where the cluster will be created. This will be where all of your instances live. Updates to the value of the field force the cluster to be re-created. Available locations: de/txl, gb/lhr, es/vit
        /// </summary>
        [Input("connectionString")]
        public Input<string>? ConnectionString { get; set; }

        /// <summary>
        /// [List] Details about the network connection for your cluster. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Input("connections")]
        public Input<Inputs.MongoClusterConnectionsGetArgs>? Connections { get; set; }

        /// <summary>
        /// (Computed)[int] The number of CPU cores per replica. Required for enterprise edition.
        /// </summary>
        [Input("cores")]
        public Input<int>? Cores { get; set; }

        /// <summary>
        /// [string] The name of your cluster. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// (Computed)[string] Cluster edition. Playground, business or enterprise.
        /// </summary>
        [Input("edition")]
        public Input<string>? Edition { get; set; }

        /// <summary>
        /// [int] The total number of instances in the cluster (one master and n-1 standbys). Example: 1, 3, 5, 7. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Input("instances")]
        public Input<int>? Instances { get; set; }

        /// <summary>
        /// [string] The physical location where the cluster will be created. Property cannot be modified after datacenter creation (disallowed in update requests). Available locations: de/txl, gb/lhr, es/vit. Update forces cluster re-creation.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// (Computed) A weekly 4 hour-long window, during which maintenance might occur.  Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Input("maintenanceWindow")]
        public Input<Inputs.MongoClusterMaintenanceWindowGetArgs>? MaintenanceWindow { get; set; }

        /// <summary>
        /// [string] The MongoDB version of your cluster. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Input("mongodbVersion")]
        public Input<string>? MongodbVersion { get; set; }

        /// <summary>
        /// (Computed)[int]The amount of memory per instance in megabytes. Required for enterprise edition.
        /// </summary>
        [Input("ram")]
        public Input<int>? Ram { get; set; }

        /// <summary>
        /// [int]The total number of shards in the cluster.
        /// </summary>
        [Input("shards")]
        public Input<int>? Shards { get; set; }

        /// <summary>
        /// (Computed)[int] The amount of storage per instance in MB. Required for enterprise edition.
        /// </summary>
        [Input("storageSize")]
        public Input<int>? StorageSize { get; set; }

        /// <summary>
        /// (Computed)[String] The storage type used in your cluster. Required for enterprise edition.
        /// </summary>
        [Input("storageType")]
        public Input<string>? StorageType { get; set; }

        /// <summary>
        /// [string] The unique ID of the template, which specifies the number of cores, storage size, and memory. Updates to the value of the field force the cluster to be re-created. Required for playground and business editions. Must not be provided for enterprise edition.
        /// </summary>
        [Input("templateId")]
        public Input<string>? TemplateId { get; set; }

        /// <summary>
        /// (Computed)[string]The cluster type, either `replicaset` or `sharded-cluster`.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        public MongoClusterState()
        {
        }
        public static new MongoClusterState Empty => new MongoClusterState();
    }
}
