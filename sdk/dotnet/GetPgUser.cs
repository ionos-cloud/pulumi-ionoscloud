// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    public static class GetPgUser
    {
        public static Task<GetPgUserResult> InvokeAsync(GetPgUserArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetPgUserResult>("ionoscloud:index/getPgUser:getPgUser", args ?? new GetPgUserArgs(), options.WithDefaults());

        public static Output<GetPgUserResult> Invoke(GetPgUserInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetPgUserResult>("ionoscloud:index/getPgUser:getPgUser", args ?? new GetPgUserInvokeArgs(), options.WithDefaults());

        public static Output<GetPgUserResult> Invoke(GetPgUserInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetPgUserResult>("ionoscloud:index/getPgUser:getPgUser", args ?? new GetPgUserInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPgUserArgs : global::Pulumi.InvokeArgs
    {
        [Input("clusterId", required: true)]
        public string ClusterId { get; set; } = null!;

        [Input("username", required: true)]
        public string Username { get; set; } = null!;

        public GetPgUserArgs()
        {
        }
        public static new GetPgUserArgs Empty => new GetPgUserArgs();
    }

    public sealed class GetPgUserInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        [Input("username", required: true)]
        public Input<string> Username { get; set; } = null!;

        public GetPgUserInvokeArgs()
        {
        }
        public static new GetPgUserInvokeArgs Empty => new GetPgUserInvokeArgs();
    }


    [OutputType]
    public sealed class GetPgUserResult
    {
        public readonly string ClusterId;
        public readonly string Id;
        public readonly bool IsSystemUser;
        public readonly string Username;

        [OutputConstructor]
        private GetPgUserResult(
            string clusterId,

            string id,

            bool isSystemUser,

            string username)
        {
            ClusterId = clusterId;
            Id = id;
            IsSystemUser = isSystemUser;
            Username = username;
        }
    }
}
