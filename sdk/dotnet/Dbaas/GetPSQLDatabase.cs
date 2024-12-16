// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Dbaas
{
    public static class GetPSQLDatabase
    {
        public static Task<GetPSQLDatabaseResult> InvokeAsync(GetPSQLDatabaseArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetPSQLDatabaseResult>("ionoscloud:dbaas/getPSQLDatabase:getPSQLDatabase", args ?? new GetPSQLDatabaseArgs(), options.WithDefaults());

        public static Output<GetPSQLDatabaseResult> Invoke(GetPSQLDatabaseInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetPSQLDatabaseResult>("ionoscloud:dbaas/getPSQLDatabase:getPSQLDatabase", args ?? new GetPSQLDatabaseInvokeArgs(), options.WithDefaults());

        public static Output<GetPSQLDatabaseResult> Invoke(GetPSQLDatabaseInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetPSQLDatabaseResult>("ionoscloud:dbaas/getPSQLDatabase:getPSQLDatabase", args ?? new GetPSQLDatabaseInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPSQLDatabaseArgs : global::Pulumi.InvokeArgs
    {
        [Input("clusterId", required: true)]
        public string ClusterId { get; set; } = null!;

        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetPSQLDatabaseArgs()
        {
        }
        public static new GetPSQLDatabaseArgs Empty => new GetPSQLDatabaseArgs();
    }

    public sealed class GetPSQLDatabaseInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetPSQLDatabaseInvokeArgs()
        {
        }
        public static new GetPSQLDatabaseInvokeArgs Empty => new GetPSQLDatabaseInvokeArgs();
    }


    [OutputType]
    public sealed class GetPSQLDatabaseResult
    {
        public readonly string ClusterId;
        public readonly string Id;
        public readonly string Name;
        public readonly string Owner;

        [OutputConstructor]
        private GetPSQLDatabaseResult(
            string clusterId,

            string id,

            string name,

            string owner)
        {
            ClusterId = clusterId;
            Id = id;
            Name = name;
            Owner = owner;
        }
    }
}
