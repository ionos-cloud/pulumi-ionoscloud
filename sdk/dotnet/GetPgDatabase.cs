// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    public static class GetPgDatabase
    {
        public static Task<GetPgDatabaseResult> InvokeAsync(GetPgDatabaseArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetPgDatabaseResult>("ionoscloud:index/getPgDatabase:getPgDatabase", args ?? new GetPgDatabaseArgs(), options.WithDefaults());

        public static Output<GetPgDatabaseResult> Invoke(GetPgDatabaseInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetPgDatabaseResult>("ionoscloud:index/getPgDatabase:getPgDatabase", args ?? new GetPgDatabaseInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPgDatabaseArgs : global::Pulumi.InvokeArgs
    {
        [Input("clusterId", required: true)]
        public string ClusterId { get; set; } = null!;

        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetPgDatabaseArgs()
        {
        }
        public static new GetPgDatabaseArgs Empty => new GetPgDatabaseArgs();
    }

    public sealed class GetPgDatabaseInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetPgDatabaseInvokeArgs()
        {
        }
        public static new GetPgDatabaseInvokeArgs Empty => new GetPgDatabaseInvokeArgs();
    }


    [OutputType]
    public sealed class GetPgDatabaseResult
    {
        public readonly string ClusterId;
        public readonly string Id;
        public readonly string Name;
        public readonly string Owner;

        [OutputConstructor]
        private GetPgDatabaseResult(
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
