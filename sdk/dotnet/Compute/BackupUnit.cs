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
    /// ## Import
    /// 
    /// A Backup Unit resource can be imported using its `resource id`, e.g.
    /// 
    /// ```sh
    /// $ pulumi import ionoscloud:compute/backupUnit:BackupUnit demo {backup_unit_uuid}
    /// ```
    /// 
    /// This can be helpful when you want to import backup units which you have already created manually or using other means, outside of terraform. Please note that you need to manually specify the password when first declaring the resource in terraform, as there is no way to retrieve the password from the Cloud API.
    /// </summary>
    [IonoscloudResourceType("ionoscloud:compute/backupUnit:BackupUnit")]
    public partial class BackupUnit : global::Pulumi.CustomResource
    {
        /// <summary>
        /// [string] The email address assigned to the backup unit
        /// </summary>
        [Output("email")]
        public Output<string> Email { get; private set; } = null!;

        /// <summary>
        /// The login associated with the backup unit. Derived from the contract number
        /// </summary>
        [Output("login")]
        public Output<string> Login { get; private set; } = null!;

        /// <summary>
        /// [string] The name of the Backup Unit. This argument is immutable.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// [string] The desired password for the Backup Unit
        /// </summary>
        [Output("password")]
        public Output<string> Password { get; private set; } = null!;


        /// <summary>
        /// Create a BackupUnit resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public BackupUnit(string name, BackupUnitArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:compute/backupUnit:BackupUnit", name, args ?? new BackupUnitArgs(), MakeResourceOptions(options, ""))
        {
        }

        private BackupUnit(string name, Input<string> id, BackupUnitState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:compute/backupUnit:BackupUnit", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing BackupUnit resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static BackupUnit Get(string name, Input<string> id, BackupUnitState? state = null, CustomResourceOptions? options = null)
        {
            return new BackupUnit(name, id, state, options);
        }
    }

    public sealed class BackupUnitArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] The email address assigned to the backup unit
        /// </summary>
        [Input("email", required: true)]
        public Input<string> Email { get; set; } = null!;

        /// <summary>
        /// [string] The name of the Backup Unit. This argument is immutable.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("password", required: true)]
        private Input<string>? _password;

        /// <summary>
        /// [string] The desired password for the Backup Unit
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

        public BackupUnitArgs()
        {
        }
        public static new BackupUnitArgs Empty => new BackupUnitArgs();
    }

    public sealed class BackupUnitState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] The email address assigned to the backup unit
        /// </summary>
        [Input("email")]
        public Input<string>? Email { get; set; }

        /// <summary>
        /// The login associated with the backup unit. Derived from the contract number
        /// </summary>
        [Input("login")]
        public Input<string>? Login { get; set; }

        /// <summary>
        /// [string] The name of the Backup Unit. This argument is immutable.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("password")]
        private Input<string>? _password;

        /// <summary>
        /// [string] The desired password for the Backup Unit
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

        public BackupUnitState()
        {
        }
        public static new BackupUnitState Empty => new BackupUnitState();
    }
}
