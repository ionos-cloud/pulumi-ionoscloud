// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    /// <summary>
    /// Manages **Shares** and list shares permissions granted to the group members for each shared resource.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ionoscloud = Pulumi.Ionoscloud;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var exampleDatacenter = new Ionoscloud.Compute.Datacenter("exampleDatacenter", new()
    ///     {
    ///         Location = "us/las",
    ///         Description = "Datacenter Description",
    ///         SecAuthProtection = false,
    ///     });
    /// 
    ///     var exampleGroup = new Ionoscloud.Compute.Group("exampleGroup", new()
    ///     {
    ///         CreateDatacenter = true,
    ///         CreateSnapshot = true,
    ///         ReserveIp = true,
    ///         AccessActivityLog = true,
    ///         CreatePcc = true,
    ///         S3Privilege = true,
    ///         CreateBackupUnit = true,
    ///         CreateInternetAccess = true,
    ///         CreateK8sCluster = true,
    ///     });
    /// 
    ///     var exampleShare = new Ionoscloud.Share("exampleShare", new()
    ///     {
    ///         GroupId = exampleGroup.Id,
    ///         ResourceId = exampleDatacenter.Id,
    ///         EditPrivilege = true,
    ///         SharePrivilege = false,
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// Resource Share can be imported using the `resource id`, e.g.
    /// 
    /// ```sh
    /// $ pulumi import ionoscloud:index/share:Share myshare {group uuid}/{resource uuid}
    /// ```
    /// </summary>
    [IonoscloudResourceType("ionoscloud:index/share:Share")]
    public partial class Share : global::Pulumi.CustomResource
    {
        /// <summary>
        /// [Boolean] The group has permission to edit privileges on this resource.
        /// </summary>
        [Output("editPrivilege")]
        public Output<bool?> EditPrivilege { get; private set; } = null!;

        /// <summary>
        /// [string] The ID of the specific group containing the resource to update.
        /// </summary>
        [Output("groupId")]
        public Output<string> GroupId { get; private set; } = null!;

        /// <summary>
        /// [string] The ID of the specific resource to update.
        /// </summary>
        [Output("resourceId")]
        public Output<string> ResourceId { get; private set; } = null!;

        /// <summary>
        /// [Boolean] The group has permission to share this resource.
        /// 
        /// ⚠️ **Note:** There is a limitation due to which the creation of several shares at the same time leads
        /// to an error. To avoid this, `parallelism=1` can be used when running `pulumi up` command in order
        /// to create the resources in a sequential manner. Another solution involves the usage of `depends_on`
        /// attributes inside the `ionoscloud.Share` resource to enforce the sequential creation of the shares.
        /// </summary>
        [Output("sharePrivilege")]
        public Output<bool?> SharePrivilege { get; private set; } = null!;


        /// <summary>
        /// Create a Share resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Share(string name, ShareArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:index/share:Share", name, args ?? new ShareArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Share(string name, Input<string> id, ShareState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:index/share:Share", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Share resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Share Get(string name, Input<string> id, ShareState? state = null, CustomResourceOptions? options = null)
        {
            return new Share(name, id, state, options);
        }
    }

    public sealed class ShareArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [Boolean] The group has permission to edit privileges on this resource.
        /// </summary>
        [Input("editPrivilege")]
        public Input<bool>? EditPrivilege { get; set; }

        /// <summary>
        /// [string] The ID of the specific group containing the resource to update.
        /// </summary>
        [Input("groupId", required: true)]
        public Input<string> GroupId { get; set; } = null!;

        /// <summary>
        /// [string] The ID of the specific resource to update.
        /// </summary>
        [Input("resourceId", required: true)]
        public Input<string> ResourceId { get; set; } = null!;

        /// <summary>
        /// [Boolean] The group has permission to share this resource.
        /// 
        /// ⚠️ **Note:** There is a limitation due to which the creation of several shares at the same time leads
        /// to an error. To avoid this, `parallelism=1` can be used when running `pulumi up` command in order
        /// to create the resources in a sequential manner. Another solution involves the usage of `depends_on`
        /// attributes inside the `ionoscloud.Share` resource to enforce the sequential creation of the shares.
        /// </summary>
        [Input("sharePrivilege")]
        public Input<bool>? SharePrivilege { get; set; }

        public ShareArgs()
        {
        }
        public static new ShareArgs Empty => new ShareArgs();
    }

    public sealed class ShareState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [Boolean] The group has permission to edit privileges on this resource.
        /// </summary>
        [Input("editPrivilege")]
        public Input<bool>? EditPrivilege { get; set; }

        /// <summary>
        /// [string] The ID of the specific group containing the resource to update.
        /// </summary>
        [Input("groupId")]
        public Input<string>? GroupId { get; set; }

        /// <summary>
        /// [string] The ID of the specific resource to update.
        /// </summary>
        [Input("resourceId")]
        public Input<string>? ResourceId { get; set; }

        /// <summary>
        /// [Boolean] The group has permission to share this resource.
        /// 
        /// ⚠️ **Note:** There is a limitation due to which the creation of several shares at the same time leads
        /// to an error. To avoid this, `parallelism=1` can be used when running `pulumi up` command in order
        /// to create the resources in a sequential manner. Another solution involves the usage of `depends_on`
        /// attributes inside the `ionoscloud.Share` resource to enforce the sequential creation of the shares.
        /// </summary>
        [Input("sharePrivilege")]
        public Input<bool>? SharePrivilege { get; set; }

        public ShareState()
        {
        }
        public static new ShareState Empty => new ShareState();
    }
}
