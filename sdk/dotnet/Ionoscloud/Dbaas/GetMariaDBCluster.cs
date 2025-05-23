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
    public static class GetMariaDBCluster
    {
        /// <summary>
        /// The **DBaaS MariaDB Cluster data source** can be used to search for and return an existing DBaaS MariaDB Cluster.
        /// 
        /// ## Example Usage
        /// 
        /// ### By ID 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetMariaDBCluster.Invoke(new()
        ///     {
        ///         Id = "cluster_id",
        ///         Location = "de/txl",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Name
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetMariaDBCluster.Invoke(new()
        ///     {
        ///         DisplayName = "MariaDB_cluster",
        ///         Location = "de/txl",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetMariaDBClusterResult> InvokeAsync(GetMariaDBClusterArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetMariaDBClusterResult>("ionoscloud:dbaas/getMariaDBCluster:getMariaDBCluster", args ?? new GetMariaDBClusterArgs(), options.WithDefaults());

        /// <summary>
        /// The **DBaaS MariaDB Cluster data source** can be used to search for and return an existing DBaaS MariaDB Cluster.
        /// 
        /// ## Example Usage
        /// 
        /// ### By ID 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetMariaDBCluster.Invoke(new()
        ///     {
        ///         Id = "cluster_id",
        ///         Location = "de/txl",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Name
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetMariaDBCluster.Invoke(new()
        ///     {
        ///         DisplayName = "MariaDB_cluster",
        ///         Location = "de/txl",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetMariaDBClusterResult> Invoke(GetMariaDBClusterInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetMariaDBClusterResult>("ionoscloud:dbaas/getMariaDBCluster:getMariaDBCluster", args ?? new GetMariaDBClusterInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The **DBaaS MariaDB Cluster data source** can be used to search for and return an existing DBaaS MariaDB Cluster.
        /// 
        /// ## Example Usage
        /// 
        /// ### By ID 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetMariaDBCluster.Invoke(new()
        ///     {
        ///         Id = "cluster_id",
        ///         Location = "de/txl",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Name
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetMariaDBCluster.Invoke(new()
        ///     {
        ///         DisplayName = "MariaDB_cluster",
        ///         Location = "de/txl",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetMariaDBClusterResult> Invoke(GetMariaDBClusterInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetMariaDBClusterResult>("ionoscloud:dbaas/getMariaDBCluster:getMariaDBCluster", args ?? new GetMariaDBClusterInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetMariaDBClusterArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// [string] Display Name of an existing cluster that you want to search for.
        /// </summary>
        [Input("displayName")]
        public string? DisplayName { get; set; }

        /// <summary>
        /// [string] ID of the cluster you want to search for.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// [string] The location of the cluster. Different service endpoints are used based on location, possible options are: "de/fra", "de/txl", "es/vit", "fr/par", "gb/lhr", "us/ewr", "us/las", "us/mci". If not set, the endpoint will be the one corresponding to "de/txl".
        /// 
        /// &gt; **⚠ WARNING:** `Location` attribute will become required in the future.
        /// 
        /// Either `display_name` or `id` must be provided. If none or both are provided, the datasource will return an error.
        /// </summary>
        [Input("location")]
        public string? Location { get; set; }

        public GetMariaDBClusterArgs()
        {
        }
        public static new GetMariaDBClusterArgs Empty => new GetMariaDBClusterArgs();
    }

    public sealed class GetMariaDBClusterInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// [string] Display Name of an existing cluster that you want to search for.
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// [string] ID of the cluster you want to search for.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// [string] The location of the cluster. Different service endpoints are used based on location, possible options are: "de/fra", "de/txl", "es/vit", "fr/par", "gb/lhr", "us/ewr", "us/las", "us/mci". If not set, the endpoint will be the one corresponding to "de/txl".
        /// 
        /// &gt; **⚠ WARNING:** `Location` attribute will become required in the future.
        /// 
        /// Either `display_name` or `id` must be provided. If none or both are provided, the datasource will return an error.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        public GetMariaDBClusterInvokeArgs()
        {
        }
        public static new GetMariaDBClusterInvokeArgs Empty => new GetMariaDBClusterInvokeArgs();
    }


    [OutputType]
    public sealed class GetMariaDBClusterResult
    {
        /// <summary>
        /// The network connection for your cluster. Only one connection is allowed.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetMariaDBClusterConnectionResult> Connections;
        /// <summary>
        /// [int] The number of CPU cores per instance.
        /// </summary>
        public readonly int Cores;
        /// <summary>
        /// [string] The friendly name of your cluster.
        /// </summary>
        public readonly string DisplayName;
        /// <summary>
        /// [string] The DNS name pointing to your cluster.
        /// </summary>
        public readonly string DnsName;
        public readonly string Id;
        /// <summary>
        /// [int] The total number of instances in the cluster (one primary and n-1 secondary).
        /// </summary>
        public readonly int Instances;
        public readonly string? Location;
        /// <summary>
        /// A weekly 4 hour-long window, during which maintenance might occur.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetMariaDBClusterMaintenanceWindowResult> MaintenanceWindows;
        /// <summary>
        /// [string] The MariaDB version of your cluster.
        /// </summary>
        public readonly string MariadbVersion;
        /// <summary>
        /// [int] The amount of memory per instance in gigabytes (GB).
        /// </summary>
        public readonly int Ram;
        /// <summary>
        /// [int] The amount of storage per instance in gigabytes (GB).
        /// </summary>
        public readonly int StorageSize;

        [OutputConstructor]
        private GetMariaDBClusterResult(
            ImmutableArray<Outputs.GetMariaDBClusterConnectionResult> connections,

            int cores,

            string displayName,

            string dnsName,

            string id,

            int instances,

            string? location,

            ImmutableArray<Outputs.GetMariaDBClusterMaintenanceWindowResult> maintenanceWindows,

            string mariadbVersion,

            int ram,

            int storageSize)
        {
            Connections = connections;
            Cores = cores;
            DisplayName = displayName;
            DnsName = dnsName;
            Id = id;
            Instances = instances;
            Location = location;
            MaintenanceWindows = maintenanceWindows;
            MariadbVersion = mariadbVersion;
            Ram = ram;
            StorageSize = storageSize;
        }
    }
}
