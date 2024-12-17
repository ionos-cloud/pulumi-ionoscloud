// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Autoscaling
{
    public static class GetServers
    {
        /// <summary>
        /// The autoscaling group servers data source can be used to search for and return existing servers that are part of a specific autoscaling group.
        /// </summary>
        public static Task<GetServersResult> InvokeAsync(GetServersArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetServersResult>("ionoscloud:autoscaling/getServers:getServers", args ?? new GetServersArgs(), options.WithDefaults());

        /// <summary>
        /// The autoscaling group servers data source can be used to search for and return existing servers that are part of a specific autoscaling group.
        /// </summary>
        public static Output<GetServersResult> Invoke(GetServersInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetServersResult>("ionoscloud:autoscaling/getServers:getServers", args ?? new GetServersInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The autoscaling group servers data source can be used to search for and return existing servers that are part of a specific autoscaling group.
        /// </summary>
        public static Output<GetServersResult> Invoke(GetServersInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetServersResult>("ionoscloud:autoscaling/getServers:getServers", args ?? new GetServersInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetServersArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The unique ID of the autoscaling group.
        /// 
        /// `group_id` must be provided. If it is not provided, the datasource will return an error.
        /// </summary>
        [Input("groupId", required: true)]
        public string GroupId { get; set; } = null!;

        public GetServersArgs()
        {
        }
        public static new GetServersArgs Empty => new GetServersArgs();
    }

    public sealed class GetServersInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The unique ID of the autoscaling group.
        /// 
        /// `group_id` must be provided. If it is not provided, the datasource will return an error.
        /// </summary>
        [Input("groupId", required: true)]
        public Input<string> GroupId { get; set; } = null!;

        public GetServersInvokeArgs()
        {
        }
        public static new GetServersInvokeArgs Empty => new GetServersInvokeArgs();
    }


    [OutputType]
    public sealed class GetServersResult
    {
        /// <summary>
        /// Id of the autoscaling group.
        /// </summary>
        public readonly string GroupId;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// List of servers.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetServersServerResult> Servers;

        [OutputConstructor]
        private GetServersResult(
            string groupId,

            string id,

            ImmutableArray<Outputs.GetServersServerResult> servers)
        {
            GroupId = groupId;
            Id = id;
            Servers = servers;
        }
    }
}
