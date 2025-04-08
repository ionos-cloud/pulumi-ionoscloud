// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Dbaas
{
    public static class GetPSQLCluster
    {
        /// <summary>
        /// The **DbaaS Postgres Cluster data source** can be used to search for and return an existing DbaaS Postgres Cluster.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
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
        ///     var example = Ionoscloud.Dbaas.GetPSQLCluster.Invoke(new()
        ///     {
        ///         Id = "cluster_id",
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
        ///     var example = Ionoscloud.Dbaas.GetPSQLCluster.Invoke(new()
        ///     {
        ///         DisplayName = "PostgreSQL_cluster",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetPSQLClusterResult> InvokeAsync(GetPSQLClusterArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetPSQLClusterResult>("ionoscloud:dbaas/getPSQLCluster:getPSQLCluster", args ?? new GetPSQLClusterArgs(), options.WithDefaults());

        /// <summary>
        /// The **DbaaS Postgres Cluster data source** can be used to search for and return an existing DbaaS Postgres Cluster.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
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
        ///     var example = Ionoscloud.Dbaas.GetPSQLCluster.Invoke(new()
        ///     {
        ///         Id = "cluster_id",
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
        ///     var example = Ionoscloud.Dbaas.GetPSQLCluster.Invoke(new()
        ///     {
        ///         DisplayName = "PostgreSQL_cluster",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetPSQLClusterResult> Invoke(GetPSQLClusterInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetPSQLClusterResult>("ionoscloud:dbaas/getPSQLCluster:getPSQLCluster", args ?? new GetPSQLClusterInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The **DbaaS Postgres Cluster data source** can be used to search for and return an existing DbaaS Postgres Cluster.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
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
        ///     var example = Ionoscloud.Dbaas.GetPSQLCluster.Invoke(new()
        ///     {
        ///         Id = "cluster_id",
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
        ///     var example = Ionoscloud.Dbaas.GetPSQLCluster.Invoke(new()
        ///     {
        ///         DisplayName = "PostgreSQL_cluster",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetPSQLClusterResult> Invoke(GetPSQLClusterInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetPSQLClusterResult>("ionoscloud:dbaas/getPSQLCluster:getPSQLCluster", args ?? new GetPSQLClusterInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPSQLClusterArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Display Name of an existing cluster that you want to search for.
        /// </summary>
        [Input("displayName")]
        public string? DisplayName { get; set; }

        /// <summary>
        /// ID of the cluster you want to search for.
        /// 
        /// Either `display_name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        public GetPSQLClusterArgs()
        {
        }
        public static new GetPSQLClusterArgs Empty => new GetPSQLClusterArgs();
    }

    public sealed class GetPSQLClusterInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Display Name of an existing cluster that you want to search for.
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// ID of the cluster you want to search for.
        /// 
        /// Either `display_name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        public GetPSQLClusterInvokeArgs()
        {
        }
        public static new GetPSQLClusterInvokeArgs Empty => new GetPSQLClusterInvokeArgs();
    }


    [OutputType]
    public sealed class GetPSQLClusterResult
    {
        /// <summary>
        /// The IONOS Object Storage location where the backups will be stored.
        /// </summary>
        public readonly string BackupLocation;
        /// <summary>
        /// Details about the connection pooler.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetPSQLClusterConnectionPoolerResult> ConnectionPoolers;
        /// <summary>
        /// Details about the network connection for your cluster.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetPSQLClusterConnectionResult> Connections;
        /// <summary>
        /// The number of CPU cores per replica.
        /// </summary>
        public readonly int Cores;
        /// <summary>
        /// The friendly name of your cluster.
        /// </summary>
        public readonly string DisplayName;
        /// <summary>
        /// The DNS name pointing to your cluster.
        /// </summary>
        public readonly string DnsName;
        /// <summary>
        /// The unique ID of the backup you want to restore.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetPSQLClusterFromBackupResult> FromBackups;
        public readonly string Id;
        /// <summary>
        /// The total number of instances in the cluster (one master and n-1 standbys)
        /// </summary>
        public readonly int Instances;
        /// <summary>
        /// The physical location where the cluster will be created. This will be where all of your instances live.
        /// </summary>
        public readonly string Location;
        /// <summary>
        /// A weekly 4 hour-long window, during which maintenance might occur
        /// </summary>
        public readonly ImmutableArray<Outputs.GetPSQLClusterMaintenanceWindowResult> MaintenanceWindows;
        /// <summary>
        /// The PostgreSQL version of your cluster.
        /// </summary>
        public readonly string PostgresVersion;
        /// <summary>
        /// The amount of memory per instance in megabytes.
        /// </summary>
        public readonly int Ram;
        /// <summary>
        /// The amount of storage per instance in MB.
        /// </summary>
        public readonly int StorageSize;
        /// <summary>
        /// The storage type used in your cluster.
        /// </summary>
        public readonly string StorageType;
        /// <summary>
        /// Represents different modes of replication.
        /// </summary>
        public readonly string SynchronizationMode;

        [OutputConstructor]
        private GetPSQLClusterResult(
            string backupLocation,

            ImmutableArray<Outputs.GetPSQLClusterConnectionPoolerResult> connectionPoolers,

            ImmutableArray<Outputs.GetPSQLClusterConnectionResult> connections,

            int cores,

            string displayName,

            string dnsName,

            ImmutableArray<Outputs.GetPSQLClusterFromBackupResult> fromBackups,

            string id,

            int instances,

            string location,

            ImmutableArray<Outputs.GetPSQLClusterMaintenanceWindowResult> maintenanceWindows,

            string postgresVersion,

            int ram,

            int storageSize,

            string storageType,

            string synchronizationMode)
        {
            BackupLocation = backupLocation;
            ConnectionPoolers = connectionPoolers;
            Connections = connections;
            Cores = cores;
            DisplayName = displayName;
            DnsName = dnsName;
            FromBackups = fromBackups;
            Id = id;
            Instances = instances;
            Location = location;
            MaintenanceWindows = maintenanceWindows;
            PostgresVersion = postgresVersion;
            Ram = ram;
            StorageSize = storageSize;
            StorageType = storageType;
            SynchronizationMode = synchronizationMode;
        }
    }
}
