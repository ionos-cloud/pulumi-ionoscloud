// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    public static class GetPgCluster
    {
        public static Task<GetPgClusterResult> InvokeAsync(GetPgClusterArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetPgClusterResult>("ionoscloud:index/getPgCluster:getPgCluster", args ?? new GetPgClusterArgs(), options.WithDefaults());

        public static Output<GetPgClusterResult> Invoke(GetPgClusterInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetPgClusterResult>("ionoscloud:index/getPgCluster:getPgCluster", args ?? new GetPgClusterInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPgClusterArgs : global::Pulumi.InvokeArgs
    {
        [Input("displayName")]
        public string? DisplayName { get; set; }

        [Input("id")]
        public string? Id { get; set; }

        public GetPgClusterArgs()
        {
        }
        public static new GetPgClusterArgs Empty => new GetPgClusterArgs();
    }

    public sealed class GetPgClusterInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        [Input("id")]
        public Input<string>? Id { get; set; }

        public GetPgClusterInvokeArgs()
        {
        }
        public static new GetPgClusterInvokeArgs Empty => new GetPgClusterInvokeArgs();
    }


    [OutputType]
    public sealed class GetPgClusterResult
    {
        public readonly string BackupLocation;
        public readonly ImmutableArray<Outputs.GetPgClusterConnectionPoolerResult> ConnectionPoolers;
        public readonly ImmutableArray<Outputs.GetPgClusterConnectionResult> Connections;
        public readonly int Cores;
        public readonly string? DisplayName;
        public readonly string DnsName;
        public readonly ImmutableArray<Outputs.GetPgClusterFromBackupResult> FromBackups;
        public readonly string? Id;
        public readonly int Instances;
        public readonly string Location;
        public readonly ImmutableArray<Outputs.GetPgClusterMaintenanceWindowResult> MaintenanceWindows;
        public readonly string PostgresVersion;
        public readonly int Ram;
        public readonly int StorageSize;
        public readonly string StorageType;
        public readonly string SynchronizationMode;

        [OutputConstructor]
        private GetPgClusterResult(
            string backupLocation,

            ImmutableArray<Outputs.GetPgClusterConnectionPoolerResult> connectionPoolers,

            ImmutableArray<Outputs.GetPgClusterConnectionResult> connections,

            int cores,

            string? displayName,

            string dnsName,

            ImmutableArray<Outputs.GetPgClusterFromBackupResult> fromBackups,

            string? id,

            int instances,

            string location,

            ImmutableArray<Outputs.GetPgClusterMaintenanceWindowResult> maintenanceWindows,

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
