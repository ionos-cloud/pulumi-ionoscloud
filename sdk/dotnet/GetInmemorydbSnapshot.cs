// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    public static class GetInmemorydbSnapshot
    {
        public static Task<GetInmemorydbSnapshotResult> InvokeAsync(GetInmemorydbSnapshotArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetInmemorydbSnapshotResult>("ionoscloud:index/getInmemorydbSnapshot:getInmemorydbSnapshot", args ?? new GetInmemorydbSnapshotArgs(), options.WithDefaults());

        public static Output<GetInmemorydbSnapshotResult> Invoke(GetInmemorydbSnapshotInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetInmemorydbSnapshotResult>("ionoscloud:index/getInmemorydbSnapshot:getInmemorydbSnapshot", args ?? new GetInmemorydbSnapshotInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetInmemorydbSnapshotArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        [Input("location", required: true)]
        public string Location { get; set; } = null!;

        public GetInmemorydbSnapshotArgs()
        {
        }
        public static new GetInmemorydbSnapshotArgs Empty => new GetInmemorydbSnapshotArgs();
    }

    public sealed class GetInmemorydbSnapshotInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        public GetInmemorydbSnapshotInvokeArgs()
        {
        }
        public static new GetInmemorydbSnapshotInvokeArgs Empty => new GetInmemorydbSnapshotInvokeArgs();
    }


    [OutputType]
    public sealed class GetInmemorydbSnapshotResult
    {
        public readonly string Id;
        public readonly string Location;
        public readonly ImmutableArray<Outputs.GetInmemorydbSnapshotMetadataResult> Metadatas;

        [OutputConstructor]
        private GetInmemorydbSnapshotResult(
            string id,

            string location,

            ImmutableArray<Outputs.GetInmemorydbSnapshotMetadataResult> metadatas)
        {
            Id = id;
            Location = location;
            Metadatas = metadatas;
        }
    }
}
