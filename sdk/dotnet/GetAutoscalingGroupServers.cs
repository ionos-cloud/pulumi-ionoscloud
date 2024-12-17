// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    public static class GetAutoscalingGroupServers
    {
        public static Task<GetAutoscalingGroupServersResult> InvokeAsync(GetAutoscalingGroupServersArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetAutoscalingGroupServersResult>("ionoscloud:index/getAutoscalingGroupServers:getAutoscalingGroupServers", args ?? new GetAutoscalingGroupServersArgs(), options.WithDefaults());

        public static Output<GetAutoscalingGroupServersResult> Invoke(GetAutoscalingGroupServersInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetAutoscalingGroupServersResult>("ionoscloud:index/getAutoscalingGroupServers:getAutoscalingGroupServers", args ?? new GetAutoscalingGroupServersInvokeArgs(), options.WithDefaults());

        public static Output<GetAutoscalingGroupServersResult> Invoke(GetAutoscalingGroupServersInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetAutoscalingGroupServersResult>("ionoscloud:index/getAutoscalingGroupServers:getAutoscalingGroupServers", args ?? new GetAutoscalingGroupServersInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetAutoscalingGroupServersArgs : global::Pulumi.InvokeArgs
    {
        [Input("groupId", required: true)]
        public string GroupId { get; set; } = null!;

        public GetAutoscalingGroupServersArgs()
        {
        }
        public static new GetAutoscalingGroupServersArgs Empty => new GetAutoscalingGroupServersArgs();
    }

    public sealed class GetAutoscalingGroupServersInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("groupId", required: true)]
        public Input<string> GroupId { get; set; } = null!;

        public GetAutoscalingGroupServersInvokeArgs()
        {
        }
        public static new GetAutoscalingGroupServersInvokeArgs Empty => new GetAutoscalingGroupServersInvokeArgs();
    }


    [OutputType]
    public sealed class GetAutoscalingGroupServersResult
    {
        public readonly string GroupId;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly ImmutableArray<Outputs.GetAutoscalingGroupServersServerResult> Servers;

        [OutputConstructor]
        private GetAutoscalingGroupServersResult(
            string groupId,

            string id,

            ImmutableArray<Outputs.GetAutoscalingGroupServersServerResult> servers)
        {
            GroupId = groupId;
            Id = id;
            Servers = servers;
        }
    }
}
