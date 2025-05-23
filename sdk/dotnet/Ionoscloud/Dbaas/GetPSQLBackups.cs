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
    public static class GetPSQLBackups
    {
        /// <summary>
        /// The **DbaaS Postgres Backups data source** can be used to search for and return existing DbaaS Postgres Backups for a specific Cluster.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetPSQLBackups.Invoke(new()
        ///     {
        ///         ClusterId = "cluster_id",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetPSQLBackupsResult> InvokeAsync(GetPSQLBackupsArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetPSQLBackupsResult>("ionoscloud:dbaas/getPSQLBackups:getPSQLBackups", args ?? new GetPSQLBackupsArgs(), options.WithDefaults());

        /// <summary>
        /// The **DbaaS Postgres Backups data source** can be used to search for and return existing DbaaS Postgres Backups for a specific Cluster.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetPSQLBackups.Invoke(new()
        ///     {
        ///         ClusterId = "cluster_id",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetPSQLBackupsResult> Invoke(GetPSQLBackupsInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetPSQLBackupsResult>("ionoscloud:dbaas/getPSQLBackups:getPSQLBackups", args ?? new GetPSQLBackupsInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The **DbaaS Postgres Backups data source** can be used to search for and return existing DbaaS Postgres Backups for a specific Cluster.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetPSQLBackups.Invoke(new()
        ///     {
        ///         ClusterId = "cluster_id",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetPSQLBackupsResult> Invoke(GetPSQLBackupsInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetPSQLBackupsResult>("ionoscloud:dbaas/getPSQLBackups:getPSQLBackups", args ?? new GetPSQLBackupsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPSQLBackupsArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The unique ID of the cluster.
        /// 
        /// `cluster_id` must be provided. If it is not provided, the datasource will return an error.
        /// </summary>
        [Input("clusterId", required: true)]
        public string ClusterId { get; set; } = null!;

        public GetPSQLBackupsArgs()
        {
        }
        public static new GetPSQLBackupsArgs Empty => new GetPSQLBackupsArgs();
    }

    public sealed class GetPSQLBackupsInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The unique ID of the cluster.
        /// 
        /// `cluster_id` must be provided. If it is not provided, the datasource will return an error.
        /// </summary>
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        public GetPSQLBackupsInvokeArgs()
        {
        }
        public static new GetPSQLBackupsInvokeArgs Empty => new GetPSQLBackupsInvokeArgs();
    }


    [OutputType]
    public sealed class GetPSQLBackupsResult
    {
        /// <summary>
        /// List of backups.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetPSQLBackupsClusterBackupResult> ClusterBackups;
        /// <summary>
        /// The unique ID of the cluster
        /// </summary>
        public readonly string ClusterId;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetPSQLBackupsResult(
            ImmutableArray<Outputs.GetPSQLBackupsClusterBackupResult> clusterBackups,

            string clusterId,

            string id)
        {
            ClusterBackups = clusterBackups;
            ClusterId = clusterId;
            Id = id;
        }
    }
}
