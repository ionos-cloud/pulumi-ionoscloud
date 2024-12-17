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
    /// Manages **Users** and list users and groups associated with that user.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ionoscloud = Pulumi.Ionoscloud;
    /// using Random = Pulumi.Random;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var group1 = new Ionoscloud.Compute.Group("group1", new()
    ///     {
    ///         CreateDatacenter = true,
    ///         CreateSnapshot = true,
    ///         ReserveIp = true,
    ///         AccessActivityLog = false,
    ///         CreateK8sCluster = true,
    ///     });
    /// 
    ///     var group2 = new Ionoscloud.Compute.Group("group2", new()
    ///     {
    ///         CreateDatacenter = true,
    ///         CreateSnapshot = true,
    ///         ReserveIp = true,
    ///         AccessActivityLog = false,
    ///         CreateK8sCluster = true,
    ///     });
    /// 
    ///     var group3 = new Ionoscloud.Compute.Group("group3", new()
    ///     {
    ///         CreateDatacenter = true,
    ///         CreateSnapshot = true,
    ///         ReserveIp = true,
    ///         AccessActivityLog = false,
    ///     });
    /// 
    ///     var userPassword = new Random.RandomPassword("userPassword", new()
    ///     {
    ///         Length = 16,
    ///         Special = true,
    ///         OverrideSpecial = "!#$%&amp;*()-_=+[]{}&lt;&gt;:?",
    ///     });
    /// 
    ///     var example = new Ionoscloud.Compute.User("example", new()
    ///     {
    ///         FirstName = "example",
    ///         LastName = "example",
    ///         Email = "unique@email.com",
    ///         Password = userPassword.Result,
    ///         Administrator = false,
    ///         ForceSecAuth = false,
    ///         Active = true,
    ///         GroupIds = new[]
    ///         {
    ///             group1.Id,
    ///             group2.Id,
    ///             group3.Id,
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// Resource User can be imported using the `resource id`, e.g.
    /// 
    /// ```sh
    /// $ pulumi import ionoscloud:compute/user:User myuser {user uuid}
    /// ```
    /// </summary>
    [IonoscloudResourceType("ionoscloud:compute/user:User")]
    public partial class User : global::Pulumi.CustomResource
    {
        /// <summary>
        /// [Boolean] Indicates if the user is active
        /// </summary>
        [Output("active")]
        public Output<bool?> Active { get; private set; } = null!;

        /// <summary>
        /// [Boolean] Indicates if the user has administrative rights. Administrators do not need to be managed in groups, as they automatically have access to all resources associated with the contract.
        /// </summary>
        [Output("administrator")]
        public Output<bool?> Administrator { get; private set; } = null!;

        /// <summary>
        /// [string] An e-mail address for the user.
        /// </summary>
        [Output("email")]
        public Output<string> Email { get; private set; } = null!;

        /// <summary>
        /// [string] A first name for the user.
        /// </summary>
        [Output("firstName")]
        public Output<string> FirstName { get; private set; } = null!;

        /// <summary>
        /// [Boolean] Indicates if secure (two-factor) authentication should be forced for the user (true) or not (false).
        /// </summary>
        [Output("forceSecAuth")]
        public Output<bool?> ForceSecAuth { get; private set; } = null!;

        /// <summary>
        /// [Set] The groups that this user will be a member of
        /// 
        /// **NOTE:** Group_ids field cannot be used at the same time with user_ids field in group resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
        /// </summary>
        [Output("groupIds")]
        public Output<ImmutableArray<string>> GroupIds { get; private set; } = null!;

        /// <summary>
        /// [string] A last name for the user.
        /// </summary>
        [Output("lastName")]
        public Output<string> LastName { get; private set; } = null!;

        /// <summary>
        /// [string] A password for the user.
        /// </summary>
        [Output("password")]
        public Output<string> Password { get; private set; } = null!;

        /// <summary>
        /// Canonical (IONOS Object Storage) id of the user for a given identity
        /// </summary>
        [Output("s3CanonicalUserId")]
        public Output<string> S3CanonicalUserId { get; private set; } = null!;

        /// <summary>
        /// [Boolean] Indicates if secure authentication is active for the user or not. *it can not be used in create requests - can be used in update*
        /// </summary>
        [Output("secAuthActive")]
        public Output<bool> SecAuthActive { get; private set; } = null!;


        /// <summary>
        /// Create a User resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public User(string name, UserArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:compute/user:User", name, args ?? new UserArgs(), MakeResourceOptions(options, ""))
        {
        }

        private User(string name, Input<string> id, UserState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:compute/user:User", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                AdditionalSecretOutputs =
                {
                    "password",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing User resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static User Get(string name, Input<string> id, UserState? state = null, CustomResourceOptions? options = null)
        {
            return new User(name, id, state, options);
        }
    }

    public sealed class UserArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [Boolean] Indicates if the user is active
        /// </summary>
        [Input("active")]
        public Input<bool>? Active { get; set; }

        /// <summary>
        /// [Boolean] Indicates if the user has administrative rights. Administrators do not need to be managed in groups, as they automatically have access to all resources associated with the contract.
        /// </summary>
        [Input("administrator")]
        public Input<bool>? Administrator { get; set; }

        /// <summary>
        /// [string] An e-mail address for the user.
        /// </summary>
        [Input("email", required: true)]
        public Input<string> Email { get; set; } = null!;

        /// <summary>
        /// [string] A first name for the user.
        /// </summary>
        [Input("firstName", required: true)]
        public Input<string> FirstName { get; set; } = null!;

        /// <summary>
        /// [Boolean] Indicates if secure (two-factor) authentication should be forced for the user (true) or not (false).
        /// </summary>
        [Input("forceSecAuth")]
        public Input<bool>? ForceSecAuth { get; set; }

        [Input("groupIds")]
        private InputList<string>? _groupIds;

        /// <summary>
        /// [Set] The groups that this user will be a member of
        /// 
        /// **NOTE:** Group_ids field cannot be used at the same time with user_ids field in group resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
        /// </summary>
        public InputList<string> GroupIds
        {
            get => _groupIds ?? (_groupIds = new InputList<string>());
            set => _groupIds = value;
        }

        /// <summary>
        /// [string] A last name for the user.
        /// </summary>
        [Input("lastName", required: true)]
        public Input<string> LastName { get; set; } = null!;

        [Input("password", required: true)]
        private Input<string>? _password;

        /// <summary>
        /// [string] A password for the user.
        /// </summary>
        public Input<string>? Password
        {
            get => _password;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _password = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        public UserArgs()
        {
        }
        public static new UserArgs Empty => new UserArgs();
    }

    public sealed class UserState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [Boolean] Indicates if the user is active
        /// </summary>
        [Input("active")]
        public Input<bool>? Active { get; set; }

        /// <summary>
        /// [Boolean] Indicates if the user has administrative rights. Administrators do not need to be managed in groups, as they automatically have access to all resources associated with the contract.
        /// </summary>
        [Input("administrator")]
        public Input<bool>? Administrator { get; set; }

        /// <summary>
        /// [string] An e-mail address for the user.
        /// </summary>
        [Input("email")]
        public Input<string>? Email { get; set; }

        /// <summary>
        /// [string] A first name for the user.
        /// </summary>
        [Input("firstName")]
        public Input<string>? FirstName { get; set; }

        /// <summary>
        /// [Boolean] Indicates if secure (two-factor) authentication should be forced for the user (true) or not (false).
        /// </summary>
        [Input("forceSecAuth")]
        public Input<bool>? ForceSecAuth { get; set; }

        [Input("groupIds")]
        private InputList<string>? _groupIds;

        /// <summary>
        /// [Set] The groups that this user will be a member of
        /// 
        /// **NOTE:** Group_ids field cannot be used at the same time with user_ids field in group resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
        /// </summary>
        public InputList<string> GroupIds
        {
            get => _groupIds ?? (_groupIds = new InputList<string>());
            set => _groupIds = value;
        }

        /// <summary>
        /// [string] A last name for the user.
        /// </summary>
        [Input("lastName")]
        public Input<string>? LastName { get; set; }

        [Input("password")]
        private Input<string>? _password;

        /// <summary>
        /// [string] A password for the user.
        /// </summary>
        public Input<string>? Password
        {
            get => _password;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _password = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// Canonical (IONOS Object Storage) id of the user for a given identity
        /// </summary>
        [Input("s3CanonicalUserId")]
        public Input<string>? S3CanonicalUserId { get; set; }

        /// <summary>
        /// [Boolean] Indicates if secure authentication is active for the user or not. *it can not be used in create requests - can be used in update*
        /// </summary>
        [Input("secAuthActive")]
        public Input<bool>? SecAuthActive { get; set; }

        public UserState()
        {
        }
        public static new UserState Empty => new UserState();
    }
}
