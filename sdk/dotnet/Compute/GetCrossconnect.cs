// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Compute
{
    public static class GetCrossconnect
    {
        public static Task<GetCrossconnectResult> InvokeAsync(GetCrossconnectArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetCrossconnectResult>("ionoscloud:compute/getCrossconnect:getCrossconnect", args ?? new GetCrossconnectArgs(), options.WithDefaults());

        public static Output<GetCrossconnectResult> Invoke(GetCrossconnectInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetCrossconnectResult>("ionoscloud:compute/getCrossconnect:getCrossconnect", args ?? new GetCrossconnectInvokeArgs(), options.WithDefaults());

        public static Output<GetCrossconnectResult> Invoke(GetCrossconnectInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetCrossconnectResult>("ionoscloud:compute/getCrossconnect:getCrossconnect", args ?? new GetCrossconnectInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetCrossconnectArgs : global::Pulumi.InvokeArgs
    {
        [Input("description")]
        public string? Description { get; set; }

        [Input("id")]
        public string? Id { get; set; }

        [Input("name")]
        public string? Name { get; set; }

        public GetCrossconnectArgs()
        {
        }
        public static new GetCrossconnectArgs Empty => new GetCrossconnectArgs();
    }

    public sealed class GetCrossconnectInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("id")]
        public Input<string>? Id { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        public GetCrossconnectInvokeArgs()
        {
        }
        public static new GetCrossconnectInvokeArgs Empty => new GetCrossconnectInvokeArgs();
    }


    [OutputType]
    public sealed class GetCrossconnectResult
    {
        public readonly ImmutableArray<Outputs.GetCrossconnectConnectableDatacenterResult> ConnectableDatacenters;
        public readonly string? Description;
        public readonly string? Id;
        public readonly string? Name;
        public readonly ImmutableArray<Outputs.GetCrossconnectPeerResult> Peers;

        [OutputConstructor]
        private GetCrossconnectResult(
            ImmutableArray<Outputs.GetCrossconnectConnectableDatacenterResult> connectableDatacenters,

            string? description,

            string? id,

            string? name,

            ImmutableArray<Outputs.GetCrossconnectPeerResult> peers)
        {
            ConnectableDatacenters = connectableDatacenters;
            Description = description;
            Id = id;
            Name = name;
            Peers = peers;
        }
    }
}
