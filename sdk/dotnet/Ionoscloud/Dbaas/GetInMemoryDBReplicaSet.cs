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
    public static class GetInMemoryDBReplicaSet
    {
        /// <summary>
        /// The `ionoscloud.dbaas.InMemoryDBReplicaSet` data source can be used to retrieve information about an existing InMemoryDB Replica Set.
        /// 
        /// ## Example Usage
        /// 
        /// ### By id
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetInMemoryDBReplicaSet.Invoke(new()
        ///     {
        ///         Id = "example-id",
        ///         Location = "es/vit",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By display_name
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetInMemoryDBReplicaSet.Invoke(new()
        ///     {
        ///         DisplayName = "example-id",
        ///         Location = "us/las",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetInMemoryDBReplicaSetResult> InvokeAsync(GetInMemoryDBReplicaSetArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetInMemoryDBReplicaSetResult>("ionoscloud:dbaas/getInMemoryDBReplicaSet:getInMemoryDBReplicaSet", args ?? new GetInMemoryDBReplicaSetArgs(), options.WithDefaults());

        /// <summary>
        /// The `ionoscloud.dbaas.InMemoryDBReplicaSet` data source can be used to retrieve information about an existing InMemoryDB Replica Set.
        /// 
        /// ## Example Usage
        /// 
        /// ### By id
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetInMemoryDBReplicaSet.Invoke(new()
        ///     {
        ///         Id = "example-id",
        ///         Location = "es/vit",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By display_name
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetInMemoryDBReplicaSet.Invoke(new()
        ///     {
        ///         DisplayName = "example-id",
        ///         Location = "us/las",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetInMemoryDBReplicaSetResult> Invoke(GetInMemoryDBReplicaSetInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetInMemoryDBReplicaSetResult>("ionoscloud:dbaas/getInMemoryDBReplicaSet:getInMemoryDBReplicaSet", args ?? new GetInMemoryDBReplicaSetInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The `ionoscloud.dbaas.InMemoryDBReplicaSet` data source can be used to retrieve information about an existing InMemoryDB Replica Set.
        /// 
        /// ## Example Usage
        /// 
        /// ### By id
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetInMemoryDBReplicaSet.Invoke(new()
        ///     {
        ///         Id = "example-id",
        ///         Location = "es/vit",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By display_name
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Dbaas.GetInMemoryDBReplicaSet.Invoke(new()
        ///     {
        ///         DisplayName = "example-id",
        ///         Location = "us/las",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetInMemoryDBReplicaSetResult> Invoke(GetInMemoryDBReplicaSetInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetInMemoryDBReplicaSetResult>("ionoscloud:dbaas/getInMemoryDBReplicaSet:getInMemoryDBReplicaSet", args ?? new GetInMemoryDBReplicaSetInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetInMemoryDBReplicaSetArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The display name of the InMemoryDB Replica Set.
        /// </summary>
        [Input("displayName")]
        public string? DisplayName { get; set; }

        /// <summary>
        /// The ID of the InMemoryDB Replica Set.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// The location of the InMemoryDB Replica Set.
        /// 
        /// &gt; **Note:** Either `id` or `display_name` must be provided. If none, or both are provided, the datasource will return an error.
        /// </summary>
        [Input("location")]
        public string? Location { get; set; }

        public GetInMemoryDBReplicaSetArgs()
        {
        }
        public static new GetInMemoryDBReplicaSetArgs Empty => new GetInMemoryDBReplicaSetArgs();
    }

    public sealed class GetInMemoryDBReplicaSetInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The display name of the InMemoryDB Replica Set.
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// The ID of the InMemoryDB Replica Set.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// The location of the InMemoryDB Replica Set.
        /// 
        /// &gt; **Note:** Either `id` or `display_name` must be provided. If none, or both are provided, the datasource will return an error.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        public GetInMemoryDBReplicaSetInvokeArgs()
        {
        }
        public static new GetInMemoryDBReplicaSetInvokeArgs Empty => new GetInMemoryDBReplicaSetInvokeArgs();
    }


    [OutputType]
    public sealed class GetInMemoryDBReplicaSetResult
    {
        /// <summary>
        /// [object] The network connection for your replica set. Only one connection is allowed. It includes:
        /// </summary>
        public readonly ImmutableArray<Outputs.GetInMemoryDBReplicaSetConnectionResult> Connections;
        /// <summary>
        /// [object] Credentials for the InMemoryDB replicaset, only one type of password can be used since they are mutually exclusive. It includes:
        /// </summary>
        public readonly ImmutableArray<Outputs.GetInMemoryDBReplicaSetCredentialResult> Credentials;
        public readonly string DisplayName;
        /// <summary>
        /// [string] The DNS name pointing to your replica set. Will be used to connect to the active/standalone instance.
        /// </summary>
        public readonly string DnsName;
        /// <summary>
        /// [string] The eviction policy for the replica set, possible values are:
        /// </summary>
        public readonly string EvictionPolicy;
        public readonly string Id;
        public readonly string? Location;
        /// <summary>
        /// A weekly 4 hour-long window, during which maintenance might occur. It includes:
        /// </summary>
        public readonly ImmutableArray<Outputs.GetInMemoryDBReplicaSetMaintenanceWindowResult> MaintenanceWindows;
        /// <summary>
        /// [string] Specifies How and If data is persisted, possible values are:
        /// * `None` - Data is inMemory only and will not be persisted. Useful for cache only applications.
        /// * `AOF` - (Append Only File) AOF persistence logs every write operation received by the server. These operations can then be replayed again at server startup, reconstructing the original dataset. Commands are logged using the same format as the InMemoryDB protocol itself.
        /// * `RDB` - RDB persistence performs snapshots of the current in memory state.
        /// * `RDB_AOF` - Both, RDB and AOF persistence are enabled.
        /// </summary>
        public readonly string PersistenceMode;
        /// <summary>
        /// [int] The total number of replicas in the replica set (one active and n-1 passive). In case of a standalone instance, the value is 1. In all other cases, the value is &gt; 1. The replicas will not be available as read replicas, they are only standby for a failure of the active instance.
        /// </summary>
        public readonly int Replicas;
        /// <summary>
        /// [object] The resources of the individual replicas. It includes:
        /// </summary>
        public readonly ImmutableArray<Outputs.GetInMemoryDBReplicaSetResourceResult> Resources;
        /// <summary>
        /// [string] The InMemoryDB version of your replica set.
        /// </summary>
        public readonly string Version;

        [OutputConstructor]
        private GetInMemoryDBReplicaSetResult(
            ImmutableArray<Outputs.GetInMemoryDBReplicaSetConnectionResult> connections,

            ImmutableArray<Outputs.GetInMemoryDBReplicaSetCredentialResult> credentials,

            string displayName,

            string dnsName,

            string evictionPolicy,

            string id,

            string? location,

            ImmutableArray<Outputs.GetInMemoryDBReplicaSetMaintenanceWindowResult> maintenanceWindows,

            string persistenceMode,

            int replicas,

            ImmutableArray<Outputs.GetInMemoryDBReplicaSetResourceResult> resources,

            string version)
        {
            Connections = connections;
            Credentials = credentials;
            DisplayName = displayName;
            DnsName = dnsName;
            EvictionPolicy = evictionPolicy;
            Id = id;
            Location = location;
            MaintenanceWindows = maintenanceWindows;
            PersistenceMode = persistenceMode;
            Replicas = replicas;
            Resources = resources;
            Version = version;
        }
    }
}
