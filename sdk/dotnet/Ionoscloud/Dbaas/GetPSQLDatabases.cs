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
    public static class GetPSQLDatabases
    {
        /// <summary>
        /// The **PgSql Databases data source** can be used to search for and return multiple existing PgSql databases.
        /// 
        /// ## Example Usage
        /// 
        /// ### All databases from a specific cluster
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetPSQLDatabases.Invoke(new()
        ///     {
        ///         ClusterId = "cluster_id",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### Filter by owner
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetPSQLDatabases.Invoke(new()
        ///     {
        ///         ClusterId = "cluster_id",
        ///         Owner = "owner",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetPSQLDatabasesResult> InvokeAsync(GetPSQLDatabasesArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetPSQLDatabasesResult>("ionoscloud:dbaas/getPSQLDatabases:getPSQLDatabases", args ?? new GetPSQLDatabasesArgs(), options.WithDefaults());

        /// <summary>
        /// The **PgSql Databases data source** can be used to search for and return multiple existing PgSql databases.
        /// 
        /// ## Example Usage
        /// 
        /// ### All databases from a specific cluster
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetPSQLDatabases.Invoke(new()
        ///     {
        ///         ClusterId = "cluster_id",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### Filter by owner
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetPSQLDatabases.Invoke(new()
        ///     {
        ///         ClusterId = "cluster_id",
        ///         Owner = "owner",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetPSQLDatabasesResult> Invoke(GetPSQLDatabasesInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetPSQLDatabasesResult>("ionoscloud:dbaas/getPSQLDatabases:getPSQLDatabases", args ?? new GetPSQLDatabasesInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The **PgSql Databases data source** can be used to search for and return multiple existing PgSql databases.
        /// 
        /// ## Example Usage
        /// 
        /// ### All databases from a specific cluster
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetPSQLDatabases.Invoke(new()
        ///     {
        ///         ClusterId = "cluster_id",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### Filter by owner
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetPSQLDatabases.Invoke(new()
        ///     {
        ///         ClusterId = "cluster_id",
        ///         Owner = "owner",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetPSQLDatabasesResult> Invoke(GetPSQLDatabasesInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetPSQLDatabasesResult>("ionoscloud:dbaas/getPSQLDatabases:getPSQLDatabases", args ?? new GetPSQLDatabasesInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPSQLDatabasesArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// [string] The ID of the cluster.
        /// </summary>
        [Input("clusterId", required: true)]
        public string ClusterId { get; set; } = null!;

        /// <summary>
        /// [string] Filter using a specific owner.
        /// </summary>
        [Input("owner")]
        public string? Owner { get; set; }

        public GetPSQLDatabasesArgs()
        {
        }
        public static new GetPSQLDatabasesArgs Empty => new GetPSQLDatabasesArgs();
    }

    public sealed class GetPSQLDatabasesInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// [string] The ID of the cluster.
        /// </summary>
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        /// <summary>
        /// [string] Filter using a specific owner.
        /// </summary>
        [Input("owner")]
        public Input<string>? Owner { get; set; }

        public GetPSQLDatabasesInvokeArgs()
        {
        }
        public static new GetPSQLDatabasesInvokeArgs Empty => new GetPSQLDatabasesInvokeArgs();
    }


    [OutputType]
    public sealed class GetPSQLDatabasesResult
    {
        public readonly string ClusterId;
        /// <summary>
        /// [list] A list that contains either all databases, either some of them (filter by owner). A database from list has the following format:
        /// </summary>
        public readonly ImmutableArray<Outputs.GetPSQLDatabasesDatabaseResult> Databases;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// [string] The owner of the database.
        /// </summary>
        public readonly string? Owner;

        [OutputConstructor]
        private GetPSQLDatabasesResult(
            string clusterId,

            ImmutableArray<Outputs.GetPSQLDatabasesDatabaseResult> databases,

            string id,

            string? owner)
        {
            ClusterId = clusterId;
            Databases = databases;
            Id = id;
            Owner = owner;
        }
    }
}
