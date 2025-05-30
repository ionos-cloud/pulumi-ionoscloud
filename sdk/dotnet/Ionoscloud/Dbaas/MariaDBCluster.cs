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
    /// Manages a **DBaaS MariaDB Cluster**.
    /// 
    /// ## Example Usage
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
    ///     var example = new Ionoscloud.Compute.Datacenter("example", new()
    ///     {
    ///         Name = "example",
    ///         Location = "de/txl",
    ///         Description = "Datacenter for testing DBaaS cluster",
    ///     });
    /// 
    ///     var exampleLan = new Ionoscloud.Compute.Lan("example", new()
    ///     {
    ///         DatacenterId = example.Id,
    ///         Public = false,
    ///         Name = "example",
    ///     });
    /// 
    ///     var exampleServer = new Ionoscloud.Compute.Server("example", new()
    ///     {
    ///         Name = "example",
    ///         DatacenterId = example.Id,
    ///         Cores = 2,
    ///         Ram = 2048,
    ///         AvailabilityZone = "ZONE_1",
    ///         CpuFamily = "INTEL_SKYLAKE",
    ///         ImageName = "rockylinux-8-GenericCloud-20230518",
    ///         ImagePassword = "password",
    ///         Volume = new Ionoscloud.Compute.Inputs.ServerVolumeArgs
    ///         {
    ///             Name = "example",
    ///             Size = 10,
    ///             DiskType = "SSD Standard",
    ///         },
    ///         Nic = new Ionoscloud.Compute.Inputs.ServerNicArgs
    ///         {
    ///             Lan = exampleLan.Id,
    ///             Name = "example",
    ///             Dhcp = true,
    ///         },
    ///     });
    /// 
    ///     var clusterPassword = new Random.Index.Password("cluster_password", new()
    ///     {
    ///         Length = 16,
    ///         Special = true,
    ///         OverrideSpecial = "!#$%&amp;*()-_=+[]{}&lt;&gt;:?",
    ///     });
    /// 
    ///     var exampleMariaDBCluster = new Ionoscloud.Dbaas.MariaDBCluster("example", new()
    ///     {
    ///         MariadbVersion = "10.6",
    ///         Location = "de/txl",
    ///         Instances = 1,
    ///         Cores = 4,
    ///         Ram = 4,
    ///         StorageSize = 10,
    ///         Connections = new Ionoscloud.Dbaas.Inputs.MariaDBClusterConnectionsArgs
    ///         {
    ///             DatacenterId = example.Id,
    ///             LanId = exampleLan.Id,
    ///             Cidr = "database_ip_cidr_from_nic",
    ///         },
    ///         DisplayName = "MariaDB_cluster",
    ///         MaintenanceWindow = new Ionoscloud.Dbaas.Inputs.MariaDBClusterMaintenanceWindowArgs
    ///         {
    ///             DayOfTheWeek = "Sunday",
    ///             Time = "09:00:00",
    ///         },
    ///         Credentials = new Ionoscloud.Dbaas.Inputs.MariaDBClusterCredentialsArgs
    ///         {
    ///             Username = "username",
    ///             Password = clusterPassword.Result,
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// Resource DBaaS MariaDB Cluster can be imported using the `cluster_id` and the `location`, separated by `:`, e.g.
    /// 
    /// ```sh
    /// $ pulumi import ionoscloud:dbaas/mariaDBCluster:MariaDBCluster mycluster location:cluster uuid
    /// ```
    /// </summary>
    [IonoscloudResourceType("ionoscloud:dbaas/mariaDBCluster:MariaDBCluster")]
    public partial class MariaDBCluster : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The network connection for your cluster. Only one connection is allowed.
        /// </summary>
        [Output("connections")]
        public Output<Outputs.MariaDBClusterConnections> Connections { get; private set; } = null!;

        /// <summary>
        /// [int] The number of CPU cores per instance.
        /// </summary>
        [Output("cores")]
        public Output<int> Cores { get; private set; } = null!;

        /// <summary>
        /// Credentials for the database user to be created.
        /// </summary>
        [Output("credentials")]
        public Output<Outputs.MariaDBClusterCredentials> Credentials { get; private set; } = null!;

        /// <summary>
        /// [string] The friendly name of your cluster.
        /// </summary>
        [Output("displayName")]
        public Output<string> DisplayName { get; private set; } = null!;

        /// <summary>
        /// [string] The DNS name pointing to your cluster.
        /// 
        /// &gt; **⚠ WARNING:** `IONOS_API_URL_MARIADB` can be used to set a custom API URL for the MariaDB Cluster. `location` field needs to be empty, otherwise it will override the custom API URL. Setting `endpoint` or `IONOS_API_URL` does not have any effect.
        /// </summary>
        [Output("dnsName")]
        public Output<string> DnsName { get; private set; } = null!;

        /// <summary>
        /// [int] The total number of instances in the cluster (one primary and n-1 secondary).
        /// </summary>
        [Output("instances")]
        public Output<int> Instances { get; private set; } = null!;

        /// <summary>
        /// [string] The location in which the cluster will be created. Different service endpoints are used based on location, possible options are: "de/fra", "de/txl", "es/vit", "fr/par", "gb/lhr", "us/ewr", "us/las", "us/mci". If not set, the endpoint will be the one corresponding to "de/txl".
        /// </summary>
        [Output("location")]
        public Output<string?> Location { get; private set; } = null!;

        /// <summary>
        /// (Computed) A weekly 4 hour-long window, during which maintenance might occur
        /// </summary>
        [Output("maintenanceWindow")]
        public Output<Outputs.MariaDBClusterMaintenanceWindow> MaintenanceWindow { get; private set; } = null!;

        /// <summary>
        /// [string] The MariaDB version of your cluster. Cannot be downgraded.
        /// </summary>
        [Output("mariadbVersion")]
        public Output<string> MariadbVersion { get; private set; } = null!;

        /// <summary>
        /// [int] The amount of memory per instance in gigabytes (GB).
        /// </summary>
        [Output("ram")]
        public Output<int> Ram { get; private set; } = null!;

        /// <summary>
        /// [int] The amount of storage per instance in gigabytes (GB).
        /// </summary>
        [Output("storageSize")]
        public Output<int> StorageSize { get; private set; } = null!;


        /// <summary>
        /// Create a MariaDBCluster resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public MariaDBCluster(string name, MariaDBClusterArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:dbaas/mariaDBCluster:MariaDBCluster", name, args ?? new MariaDBClusterArgs(), MakeResourceOptions(options, ""))
        {
        }

        private MariaDBCluster(string name, Input<string> id, MariaDBClusterState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:dbaas/mariaDBCluster:MariaDBCluster", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing MariaDBCluster resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static MariaDBCluster Get(string name, Input<string> id, MariaDBClusterState? state = null, CustomResourceOptions? options = null)
        {
            return new MariaDBCluster(name, id, state, options);
        }
    }

    public sealed class MariaDBClusterArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The network connection for your cluster. Only one connection is allowed.
        /// </summary>
        [Input("connections", required: true)]
        public Input<Inputs.MariaDBClusterConnectionsArgs> Connections { get; set; } = null!;

        /// <summary>
        /// [int] The number of CPU cores per instance.
        /// </summary>
        [Input("cores", required: true)]
        public Input<int> Cores { get; set; } = null!;

        /// <summary>
        /// Credentials for the database user to be created.
        /// </summary>
        [Input("credentials", required: true)]
        public Input<Inputs.MariaDBClusterCredentialsArgs> Credentials { get; set; } = null!;

        /// <summary>
        /// [string] The friendly name of your cluster.
        /// </summary>
        [Input("displayName", required: true)]
        public Input<string> DisplayName { get; set; } = null!;

        /// <summary>
        /// [int] The total number of instances in the cluster (one primary and n-1 secondary).
        /// </summary>
        [Input("instances", required: true)]
        public Input<int> Instances { get; set; } = null!;

        /// <summary>
        /// [string] The location in which the cluster will be created. Different service endpoints are used based on location, possible options are: "de/fra", "de/txl", "es/vit", "fr/par", "gb/lhr", "us/ewr", "us/las", "us/mci". If not set, the endpoint will be the one corresponding to "de/txl".
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// (Computed) A weekly 4 hour-long window, during which maintenance might occur
        /// </summary>
        [Input("maintenanceWindow")]
        public Input<Inputs.MariaDBClusterMaintenanceWindowArgs>? MaintenanceWindow { get; set; }

        /// <summary>
        /// [string] The MariaDB version of your cluster. Cannot be downgraded.
        /// </summary>
        [Input("mariadbVersion", required: true)]
        public Input<string> MariadbVersion { get; set; } = null!;

        /// <summary>
        /// [int] The amount of memory per instance in gigabytes (GB).
        /// </summary>
        [Input("ram", required: true)]
        public Input<int> Ram { get; set; } = null!;

        /// <summary>
        /// [int] The amount of storage per instance in gigabytes (GB).
        /// </summary>
        [Input("storageSize", required: true)]
        public Input<int> StorageSize { get; set; } = null!;

        public MariaDBClusterArgs()
        {
        }
        public static new MariaDBClusterArgs Empty => new MariaDBClusterArgs();
    }

    public sealed class MariaDBClusterState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The network connection for your cluster. Only one connection is allowed.
        /// </summary>
        [Input("connections")]
        public Input<Inputs.MariaDBClusterConnectionsGetArgs>? Connections { get; set; }

        /// <summary>
        /// [int] The number of CPU cores per instance.
        /// </summary>
        [Input("cores")]
        public Input<int>? Cores { get; set; }

        /// <summary>
        /// Credentials for the database user to be created.
        /// </summary>
        [Input("credentials")]
        public Input<Inputs.MariaDBClusterCredentialsGetArgs>? Credentials { get; set; }

        /// <summary>
        /// [string] The friendly name of your cluster.
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// [string] The DNS name pointing to your cluster.
        /// 
        /// &gt; **⚠ WARNING:** `IONOS_API_URL_MARIADB` can be used to set a custom API URL for the MariaDB Cluster. `location` field needs to be empty, otherwise it will override the custom API URL. Setting `endpoint` or `IONOS_API_URL` does not have any effect.
        /// </summary>
        [Input("dnsName")]
        public Input<string>? DnsName { get; set; }

        /// <summary>
        /// [int] The total number of instances in the cluster (one primary and n-1 secondary).
        /// </summary>
        [Input("instances")]
        public Input<int>? Instances { get; set; }

        /// <summary>
        /// [string] The location in which the cluster will be created. Different service endpoints are used based on location, possible options are: "de/fra", "de/txl", "es/vit", "fr/par", "gb/lhr", "us/ewr", "us/las", "us/mci". If not set, the endpoint will be the one corresponding to "de/txl".
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// (Computed) A weekly 4 hour-long window, during which maintenance might occur
        /// </summary>
        [Input("maintenanceWindow")]
        public Input<Inputs.MariaDBClusterMaintenanceWindowGetArgs>? MaintenanceWindow { get; set; }

        /// <summary>
        /// [string] The MariaDB version of your cluster. Cannot be downgraded.
        /// </summary>
        [Input("mariadbVersion")]
        public Input<string>? MariadbVersion { get; set; }

        /// <summary>
        /// [int] The amount of memory per instance in gigabytes (GB).
        /// </summary>
        [Input("ram")]
        public Input<int>? Ram { get; set; }

        /// <summary>
        /// [int] The amount of storage per instance in gigabytes (GB).
        /// </summary>
        [Input("storageSize")]
        public Input<int>? StorageSize { get; set; }

        public MariaDBClusterState()
        {
        }
        public static new MariaDBClusterState Empty => new MariaDBClusterState();
    }
}
