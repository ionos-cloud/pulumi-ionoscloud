// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Compute
{
    /// <summary>
    /// Manages an **IONOS Object Storage Key** on IonosCloud.
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
    ///     var exampleUser = new Ionoscloud.Compute.User("exampleUser", new()
    ///     {
    ///         FirstName = "example",
    ///         LastName = "example",
    ///         Email = "unique@email.com",
    ///         Password = "abc123-321CBA",
    ///         Administrator = false,
    ///         ForceSecAuth = false,
    ///     });
    /// 
    ///     var exampleS3Key = new Ionoscloud.Compute.S3Key("exampleS3Key", new()
    ///     {
    ///         UserId = exampleUser.Id,
    ///         Active = true,
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// An IONOS Object Storage Unit resource can be imported using its user id as well as its `resource id`, e.g.
    /// 
    /// ```sh
    /// $ pulumi import ionoscloud:compute/s3Key:S3Key demo {userId}/{s3KeyId}
    /// ```
    /// 
    /// This can be helpful when you want to import IONOS Object Storage Keys which you have already created manually or using other means, outside of terraform.
    /// </summary>
    [IonoscloudResourceType("ionoscloud:compute/s3Key:S3Key")]
    public partial class S3Key : global::Pulumi.CustomResource
    {
        /// <summary>
        /// [boolean] Whether the IONOS Object Storage is active / enabled or not - Please keep in mind this is only required on create. Default value in true
        /// </summary>
        [Output("active")]
        public Output<bool?> Active { get; private set; } = null!;

        /// <summary>
        /// The IONOS Object Storage Secret key.
        /// </summary>
        [Output("secretKey")]
        public Output<string> SecretKey { get; private set; } = null!;

        /// <summary>
        /// [string] The UUID of the user owning the IONOS Object Storage Key.
        /// </summary>
        [Output("userId")]
        public Output<string> UserId { get; private set; } = null!;


        /// <summary>
        /// Create a S3Key resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public S3Key(string name, S3KeyArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:compute/s3Key:S3Key", name, args ?? new S3KeyArgs(), MakeResourceOptions(options, ""))
        {
        }

        private S3Key(string name, Input<string> id, S3KeyState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:compute/s3Key:S3Key", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing S3Key resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static S3Key Get(string name, Input<string> id, S3KeyState? state = null, CustomResourceOptions? options = null)
        {
            return new S3Key(name, id, state, options);
        }
    }

    public sealed class S3KeyArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [boolean] Whether the IONOS Object Storage is active / enabled or not - Please keep in mind this is only required on create. Default value in true
        /// </summary>
        [Input("active")]
        public Input<bool>? Active { get; set; }

        /// <summary>
        /// [string] The UUID of the user owning the IONOS Object Storage Key.
        /// </summary>
        [Input("userId", required: true)]
        public Input<string> UserId { get; set; } = null!;

        public S3KeyArgs()
        {
        }
        public static new S3KeyArgs Empty => new S3KeyArgs();
    }

    public sealed class S3KeyState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [boolean] Whether the IONOS Object Storage is active / enabled or not - Please keep in mind this is only required on create. Default value in true
        /// </summary>
        [Input("active")]
        public Input<bool>? Active { get; set; }

        /// <summary>
        /// The IONOS Object Storage Secret key.
        /// </summary>
        [Input("secretKey")]
        public Input<string>? SecretKey { get; set; }

        /// <summary>
        /// [string] The UUID of the user owning the IONOS Object Storage Key.
        /// </summary>
        [Input("userId")]
        public Input<string>? UserId { get; set; }

        public S3KeyState()
        {
        }
        public static new S3KeyState Empty => new S3KeyState();
    }
}
