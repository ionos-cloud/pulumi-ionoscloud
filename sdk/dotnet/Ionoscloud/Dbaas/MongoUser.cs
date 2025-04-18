// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Dbaas
{
    /// <summary>
    /// Manages a **DbaaS Mongo User**. .
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ionoscloud = Ionoscloud.Pulumi.Ionoscloud;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     // Basic example
    ///     var datacenterExample = new Ionoscloud.Compute.Datacenter("datacenter_example", new()
    ///     {
    ///         Name = "example",
    ///         Location = "de/txl",
    ///         Description = "Datacenter for testing dbaas cluster",
    ///     });
    /// 
    ///     var lanExample = new Ionoscloud.Compute.Lan("lan_example", new()
    ///     {
    ///         DatacenterId = datacenterExample.Id,
    ///         Public = false,
    ///         Name = "example",
    ///     });
    /// 
    ///     var exampleMongoCluster = new Ionoscloud.Dbaas.MongoCluster("example_mongo_cluster", new()
    ///     {
    ///         MaintenanceWindow = new Ionoscloud.Dbaas.Inputs.MongoClusterMaintenanceWindowArgs
    ///         {
    ///             DayOfTheWeek = "Sunday",
    ///             Time = "09:00:00",
    ///         },
    ///         MongodbVersion = "5.0",
    ///         Instances = 1,
    ///         DisplayName = "example_mongo_cluster",
    ///         Location = datacenterExample.Location,
    ///         Connections = new Ionoscloud.Dbaas.Inputs.MongoClusterConnectionsArgs
    ///         {
    ///             DatacenterId = datacenterExample.Id,
    ///             LanId = lanExample.Id,
    ///             CidrLists = new[]
    ///             {
    ///                 "192.168.1.108/24",
    ///             },
    ///         },
    ///         TemplateId = "6b78ea06-ee0e-4689-998c-fc9c46e781f6",
    ///     });
    /// 
    ///     var exampleMongoUser = new Ionoscloud.Dbaas.MongoUser("example_mongo_user", new()
    ///     {
    ///         ClusterId = exampleMongoCluster.Id,
    ///         Username = "myUser",
    ///         Password = "strongPassword",
    ///         Roles = new[]
    ///         {
    ///             new Ionoscloud.Dbaas.Inputs.MongoUserRoleArgs
    ///             {
    ///                 Role = "read",
    ///                 Database = "db1",
    ///             },
    ///             new Ionoscloud.Dbaas.Inputs.MongoUserRoleArgs
    ///             {
    ///                 Role = "readWrite",
    ///                 Database = "db2",
    ///             },
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ionoscloud = Ionoscloud.Pulumi.Ionoscloud;
    /// using Random = Pulumi.Random;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     // Complete example
    ///     var datacenterExample = new Ionoscloud.Compute.Datacenter("datacenter_example", new()
    ///     {
    ///         Name = "example",
    ///         Location = "de/txl",
    ///         Description = "Datacenter for testing dbaas cluster",
    ///     });
    /// 
    ///     var lanExample = new Ionoscloud.Compute.Lan("lan_example", new()
    ///     {
    ///         DatacenterId = datacenterExample.Id,
    ///         Public = false,
    ///         Name = "example",
    ///     });
    /// 
    ///     var exampleMongoCluster = new Ionoscloud.Dbaas.MongoCluster("example_mongo_cluster", new()
    ///     {
    ///         MaintenanceWindow = new Ionoscloud.Dbaas.Inputs.MongoClusterMaintenanceWindowArgs
    ///         {
    ///             DayOfTheWeek = "Sunday",
    ///             Time = "09:00:00",
    ///         },
    ///         MongodbVersion = "5.0",
    ///         Instances = 1,
    ///         DisplayName = "example_mongo_cluster",
    ///         Location = datacenterExample.Location,
    ///         Connections = new Ionoscloud.Dbaas.Inputs.MongoClusterConnectionsArgs
    ///         {
    ///             DatacenterId = datacenterExample.Id,
    ///             LanId = lanExample.Id,
    ///             CidrLists = new[]
    ///             {
    ///                 "192.168.1.108/24",
    ///             },
    ///         },
    ///         TemplateId = "6b78ea06-ee0e-4689-998c-fc9c46e781f6",
    ///     });
    /// 
    ///     var clusterPassword = new Random.Index.Password("cluster_password", new()
    ///     {
    ///         Length = 16,
    ///         Special = true,
    ///         OverrideSpecial = "!#$%&amp;*()-_=+[]{}&lt;&gt;:?",
    ///     });
    /// 
    ///     var userPassword = new Random.Index.Password("user_password", new()
    ///     {
    ///         Length = 16,
    ///         Special = true,
    ///         OverrideSpecial = "!#$%&amp;*()-_=+[]{}&lt;&gt;:?",
    ///     });
    /// 
    ///     var exampleMongoUser = new Ionoscloud.Dbaas.MongoUser("example_mongo_user", new()
    ///     {
    ///         ClusterId = exampleMongoCluster.Id,
    ///         Username = "myUser",
    ///         Password = userPassword.Result,
    ///         Roles = new[]
    ///         {
    ///             new Ionoscloud.Dbaas.Inputs.MongoUserRoleArgs
    ///             {
    ///                 Role = "read",
    ///                 Database = "db1",
    ///             },
    ///             new Ionoscloud.Dbaas.Inputs.MongoUserRoleArgs
    ///             {
    ///                 Role = "readWrite",
    ///                 Database = "db2",
    ///             },
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// Resource DBaaS MongoDB User can be imported using the `clusterID` and the `username`.
    /// 
    /// First, define an empty resource in the plan:
    /// 
    /// hcl
    /// 
    /// resource "ionoscloud_mongo_user" "importeduser" {
    /// 
    /// }
    /// 
    /// Then you can import the user using the following command:
    /// 
    /// ```sh
    /// $ pulumi import ionoscloud:dbaas/mongoUser:MongoUser mycluser clusterid/username
    /// ```
    /// </summary>
    [IonoscloudResourceType("ionoscloud:dbaas/mongoUser:MongoUser")]
    public partial class MongoUser : global::Pulumi.CustomResource
    {
        /// <summary>
        /// [string] The unique ID of the cluster. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Output("clusterId")]
        public Output<string> ClusterId { get; private set; } = null!;

        /// <summary>
        /// [string] User password. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Output("password")]
        public Output<string> Password { get; private set; } = null!;

        /// <summary>
        /// [string] a list of mongodb user roles. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Output("roles")]
        public Output<ImmutableArray<Outputs.MongoUserRole>> Roles { get; private set; } = null!;

        /// <summary>
        /// [string] Used for authentication. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Output("username")]
        public Output<string> Username { get; private set; } = null!;


        /// <summary>
        /// Create a MongoUser resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public MongoUser(string name, MongoUserArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:dbaas/mongoUser:MongoUser", name, args ?? new MongoUserArgs(), MakeResourceOptions(options, ""))
        {
        }

        private MongoUser(string name, Input<string> id, MongoUserState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:dbaas/mongoUser:MongoUser", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing MongoUser resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static MongoUser Get(string name, Input<string> id, MongoUserState? state = null, CustomResourceOptions? options = null)
        {
            return new MongoUser(name, id, state, options);
        }
    }

    public sealed class MongoUserArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] The unique ID of the cluster. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        [Input("password", required: true)]
        private Input<string>? _password;

        /// <summary>
        /// [string] User password. Updates to the value of the field force the cluster to be re-created.
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

        [Input("roles")]
        private InputList<Inputs.MongoUserRoleArgs>? _roles;

        /// <summary>
        /// [string] a list of mongodb user roles. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        public InputList<Inputs.MongoUserRoleArgs> Roles
        {
            get => _roles ?? (_roles = new InputList<Inputs.MongoUserRoleArgs>());
            set => _roles = value;
        }

        /// <summary>
        /// [string] Used for authentication. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Input("username", required: true)]
        public Input<string> Username { get; set; } = null!;

        public MongoUserArgs()
        {
        }
        public static new MongoUserArgs Empty => new MongoUserArgs();
    }

    public sealed class MongoUserState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] The unique ID of the cluster. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Input("clusterId")]
        public Input<string>? ClusterId { get; set; }

        [Input("password")]
        private Input<string>? _password;

        /// <summary>
        /// [string] User password. Updates to the value of the field force the cluster to be re-created.
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

        [Input("roles")]
        private InputList<Inputs.MongoUserRoleGetArgs>? _roles;

        /// <summary>
        /// [string] a list of mongodb user roles. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        public InputList<Inputs.MongoUserRoleGetArgs> Roles
        {
            get => _roles ?? (_roles = new InputList<Inputs.MongoUserRoleGetArgs>());
            set => _roles = value;
        }

        /// <summary>
        /// [string] Used for authentication. Updates to the value of the field force the cluster to be re-created.
        /// </summary>
        [Input("username")]
        public Input<string>? Username { get; set; }

        public MongoUserState()
        {
        }
        public static new MongoUserState Empty => new MongoUserState();
    }
}
