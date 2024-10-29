// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    public static class GetMongoCluster
    {
        public static Task<GetMongoClusterResult> InvokeAsync(GetMongoClusterArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetMongoClusterResult>("ionoscloud:index/getMongoCluster:getMongoCluster", args ?? new GetMongoClusterArgs(), options.WithDefaults());

        public static Output<GetMongoClusterResult> Invoke(GetMongoClusterInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetMongoClusterResult>("ionoscloud:index/getMongoCluster:getMongoCluster", args ?? new GetMongoClusterInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetMongoClusterArgs : global::Pulumi.InvokeArgs
    {
        [Input("displayName")]
        public string? DisplayName { get; set; }

        [Input("id")]
        public string? Id { get; set; }

        public GetMongoClusterArgs()
        {
        }
        public static new GetMongoClusterArgs Empty => new GetMongoClusterArgs();
    }

    public sealed class GetMongoClusterInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        [Input("id")]
        public Input<string>? Id { get; set; }

        public GetMongoClusterInvokeArgs()
        {
        }
        public static new GetMongoClusterInvokeArgs Empty => new GetMongoClusterInvokeArgs();
    }


    [OutputType]
    public sealed class GetMongoClusterResult
    {
        public readonly ImmutableArray<Outputs.GetMongoClusterBackupResult> Backups;
        public readonly ImmutableArray<Outputs.GetMongoClusterBiConnectorResult> BiConnectors;
        public readonly string ConnectionString;
        public readonly ImmutableArray<Outputs.GetMongoClusterConnectionResult> Connections;
        public readonly int Cores;
        public readonly string? DisplayName;
        public readonly string Edition;
        public readonly string? Id;
        public readonly int Instances;
        public readonly string Location;
        public readonly ImmutableArray<Outputs.GetMongoClusterMaintenanceWindowResult> MaintenanceWindows;
        public readonly string MongodbVersion;
        public readonly int Ram;
        public readonly int Shards;
        public readonly int StorageSize;
        public readonly string StorageType;
        public readonly string TemplateId;
        public readonly string Type;

        [OutputConstructor]
        private GetMongoClusterResult(
            ImmutableArray<Outputs.GetMongoClusterBackupResult> backups,

            ImmutableArray<Outputs.GetMongoClusterBiConnectorResult> biConnectors,

            string connectionString,

            ImmutableArray<Outputs.GetMongoClusterConnectionResult> connections,

            int cores,

            string? displayName,

            string edition,

            string? id,

            int instances,

            string location,

            ImmutableArray<Outputs.GetMongoClusterMaintenanceWindowResult> maintenanceWindows,

            string mongodbVersion,

            int ram,

            int shards,

            int storageSize,

            string storageType,

            string templateId,

            string type)
        {
            Backups = backups;
            BiConnectors = biConnectors;
            ConnectionString = connectionString;
            Connections = connections;
            Cores = cores;
            DisplayName = displayName;
            Edition = edition;
            Id = id;
            Instances = instances;
            Location = location;
            MaintenanceWindows = maintenanceWindows;
            MongodbVersion = mongodbVersion;
            Ram = ram;
            Shards = shards;
            StorageSize = storageSize;
            StorageType = storageType;
            TemplateId = templateId;
            Type = type;
        }
    }
}
