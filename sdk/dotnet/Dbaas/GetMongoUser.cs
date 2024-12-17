// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Dbaas
{
    public static class GetMongoUser
    {
        /// <summary>
        /// The **DbaaS Mongo User data source** can be used to search for and return an existing DbaaS MongoDB User.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// </summary>
        public static Task<GetMongoUserResult> InvokeAsync(GetMongoUserArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetMongoUserResult>("ionoscloud:dbaas/getMongoUser:getMongoUser", args ?? new GetMongoUserArgs(), options.WithDefaults());

        /// <summary>
        /// The **DbaaS Mongo User data source** can be used to search for and return an existing DbaaS MongoDB User.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// </summary>
        public static Output<GetMongoUserResult> Invoke(GetMongoUserInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetMongoUserResult>("ionoscloud:dbaas/getMongoUser:getMongoUser", args ?? new GetMongoUserInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The **DbaaS Mongo User data source** can be used to search for and return an existing DbaaS MongoDB User.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// </summary>
        public static Output<GetMongoUserResult> Invoke(GetMongoUserInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetMongoUserResult>("ionoscloud:dbaas/getMongoUser:getMongoUser", args ?? new GetMongoUserInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetMongoUserArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// [string] The unique ID of the cluster. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Input("clusterId", required: true)]
        public string ClusterId { get; set; } = null!;

        /// <summary>
        /// [string] The user database to use for authentication. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Input("database")]
        public string? Database { get; set; }

        [Input("id")]
        public string? Id { get; set; }

        [Input("roles")]
        private List<Inputs.GetMongoUserRoleArgs>? _roles;

        /// <summary>
        /// [string] a list of mongodb user roles. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        public List<Inputs.GetMongoUserRoleArgs> Roles
        {
            get => _roles ?? (_roles = new List<Inputs.GetMongoUserRoleArgs>());
            set => _roles = value;
        }

        /// <summary>
        /// [string] Used for authentication. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Input("username", required: true)]
        public string Username { get; set; } = null!;

        public GetMongoUserArgs()
        {
        }
        public static new GetMongoUserArgs Empty => new GetMongoUserArgs();
    }

    public sealed class GetMongoUserInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// [string] The unique ID of the cluster. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        /// <summary>
        /// [string] The user database to use for authentication. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Input("database")]
        public Input<string>? Database { get; set; }

        [Input("id")]
        public Input<string>? Id { get; set; }

        [Input("roles")]
        private InputList<Inputs.GetMongoUserRoleInputArgs>? _roles;

        /// <summary>
        /// [string] a list of mongodb user roles. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        public InputList<Inputs.GetMongoUserRoleInputArgs> Roles
        {
            get => _roles ?? (_roles = new InputList<Inputs.GetMongoUserRoleInputArgs>());
            set => _roles = value;
        }

        /// <summary>
        /// [string] Used for authentication. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Input("username", required: true)]
        public Input<string> Username { get; set; } = null!;

        public GetMongoUserInvokeArgs()
        {
        }
        public static new GetMongoUserInvokeArgs Empty => new GetMongoUserInvokeArgs();
    }


    [OutputType]
    public sealed class GetMongoUserResult
    {
        public readonly string ClusterId;
        public readonly string Database;
        public readonly string? Id;
        public readonly ImmutableArray<Outputs.GetMongoUserRoleResult> Roles;
        public readonly string Username;

        [OutputConstructor]
        private GetMongoUserResult(
            string clusterId,

            string database,

            string? id,

            ImmutableArray<Outputs.GetMongoUserRoleResult> roles,

            string username)
        {
            ClusterId = clusterId;
            Database = database;
            Id = id;
            Roles = roles;
            Username = username;
        }
    }
}
