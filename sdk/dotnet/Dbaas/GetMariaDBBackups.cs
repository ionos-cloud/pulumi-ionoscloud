// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Dbaas
{
    public static class GetMariaDBBackups
    {
        /// <summary>
        /// The **DBaaS MariaDB Backups data source** can be used to search for and return existing DBaaS MariaDB Backups for a specific cluster.
        /// 
        /// ## Example Usage
        /// 
        /// ### Get all backups for a specific cluster
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetMariaDBBackups.Invoke(new()
        ///     {
        ///         ClusterId = "cluster_id",
        ///         Location = "de/txl",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### Get a specific backup
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetMariaDBBackups.Invoke(new()
        ///     {
        ///         BackupId = "backup_id",
        ///         Location = "de/txl",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetMariaDBBackupsResult> InvokeAsync(GetMariaDBBackupsArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetMariaDBBackupsResult>("ionoscloud:dbaas/getMariaDBBackups:getMariaDBBackups", args ?? new GetMariaDBBackupsArgs(), options.WithDefaults());

        /// <summary>
        /// The **DBaaS MariaDB Backups data source** can be used to search for and return existing DBaaS MariaDB Backups for a specific cluster.
        /// 
        /// ## Example Usage
        /// 
        /// ### Get all backups for a specific cluster
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetMariaDBBackups.Invoke(new()
        ///     {
        ///         ClusterId = "cluster_id",
        ///         Location = "de/txl",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### Get a specific backup
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetMariaDBBackups.Invoke(new()
        ///     {
        ///         BackupId = "backup_id",
        ///         Location = "de/txl",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetMariaDBBackupsResult> Invoke(GetMariaDBBackupsInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetMariaDBBackupsResult>("ionoscloud:dbaas/getMariaDBBackups:getMariaDBBackups", args ?? new GetMariaDBBackupsInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The **DBaaS MariaDB Backups data source** can be used to search for and return existing DBaaS MariaDB Backups for a specific cluster.
        /// 
        /// ## Example Usage
        /// 
        /// ### Get all backups for a specific cluster
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetMariaDBBackups.Invoke(new()
        ///     {
        ///         ClusterId = "cluster_id",
        ///         Location = "de/txl",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### Get a specific backup
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetMariaDBBackups.Invoke(new()
        ///     {
        ///         BackupId = "backup_id",
        ///         Location = "de/txl",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetMariaDBBackupsResult> Invoke(GetMariaDBBackupsInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetMariaDBBackupsResult>("ionoscloud:dbaas/getMariaDBBackups:getMariaDBBackups", args ?? new GetMariaDBBackupsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetMariaDBBackupsArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// [string] The unique ID of the backup.
        /// </summary>
        [Input("backupId")]
        public string? BackupId { get; set; }

        /// <summary>
        /// [string] The unique ID of the cluster.
        /// </summary>
        [Input("clusterId")]
        public string? ClusterId { get; set; }

        /// <summary>
        /// [string] The location of the cluster. Different service endpoints are used based on location, possible options are: "de/fra", "de/txl", "es/vit", "fr/par", "gb/lhr", "us/ewr", "us/las", "us/mci". If not set, the endpoint will be the one corresponding to "de/txl".
        /// 
        /// ⚠️ **Note:** Either `cluster_id` or `backup_id` must be used, but not both at the same time.
        /// 
        /// &gt; **⚠ WARNING:** `Location` attribute will become required in the future.
        /// </summary>
        [Input("location")]
        public string? Location { get; set; }

        public GetMariaDBBackupsArgs()
        {
        }
        public static new GetMariaDBBackupsArgs Empty => new GetMariaDBBackupsArgs();
    }

    public sealed class GetMariaDBBackupsInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// [string] The unique ID of the backup.
        /// </summary>
        [Input("backupId")]
        public Input<string>? BackupId { get; set; }

        /// <summary>
        /// [string] The unique ID of the cluster.
        /// </summary>
        [Input("clusterId")]
        public Input<string>? ClusterId { get; set; }

        /// <summary>
        /// [string] The location of the cluster. Different service endpoints are used based on location, possible options are: "de/fra", "de/txl", "es/vit", "fr/par", "gb/lhr", "us/ewr", "us/las", "us/mci". If not set, the endpoint will be the one corresponding to "de/txl".
        /// 
        /// ⚠️ **Note:** Either `cluster_id` or `backup_id` must be used, but not both at the same time.
        /// 
        /// &gt; **⚠ WARNING:** `Location` attribute will become required in the future.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        public GetMariaDBBackupsInvokeArgs()
        {
        }
        public static new GetMariaDBBackupsInvokeArgs Empty => new GetMariaDBBackupsInvokeArgs();
    }


    [OutputType]
    public sealed class GetMariaDBBackupsResult
    {
        public readonly string BackupId;
        public readonly ImmutableArray<Outputs.GetMariaDBBackupsBackupResult> Backups;
        /// <summary>
        /// The unique ID of the cluster that was backed up.
        /// </summary>
        public readonly string ClusterId;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string? Location;

        [OutputConstructor]
        private GetMariaDBBackupsResult(
            string backupId,

            ImmutableArray<Outputs.GetMariaDBBackupsBackupResult> backups,

            string clusterId,

            string id,

            string? location)
        {
            BackupId = backupId;
            Backups = backups;
            ClusterId = clusterId;
            Id = id;
            Location = location;
        }
    }
}
