// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Creg
{
    /// <summary>
    /// Manages an **Container Registry Token** on IonosCloud.
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
    ///     var example = new Ionoscloud.Creg.Registry("example", new()
    ///     {
    ///         GarbageCollectionSchedule = new Ionoscloud.Creg.Inputs.RegistryGarbageCollectionScheduleArgs
    ///         {
    ///             Days = new[]
    ///             {
    ///                 "Monday",
    ///                 "Tuesday",
    ///             },
    ///             Time = "05:19:00+00:00",
    ///         },
    ///         Location = "de/fra",
    ///         Name = "container-registry-example",
    ///     });
    /// 
    ///     var exampleRegistryToken = new Ionoscloud.Creg.RegistryToken("example", new()
    ///     {
    ///         ExpiryDate = "2023-01-13 16:27:42Z",
    ///         Name = "container-registry-token-example",
    ///         Scopes = new[]
    ///         {
    ///             new Ionoscloud.Creg.Inputs.RegistryTokenScopeArgs
    ///             {
    ///                 Actions = new[]
    ///                 {
    ///                     "push",
    ///                 },
    ///                 Name = "Scope1",
    ///                 Type = "repository",
    ///             },
    ///         },
    ///         Status = "enabled",
    ///         RegistryId = example.Id,
    ///         SavePasswordToFile = "pass.txt",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// Resource Container Registry Token can be imported using the `container registry id` and `resource id`, e.g.
    /// 
    /// ```sh
    /// $ pulumi import ionoscloud:creg/registryToken:RegistryToken mycrtoken container_registry uuid/container_registry_token uuid
    /// ```
    /// </summary>
    [IonoscloudResourceType("ionoscloud:creg/registryToken:RegistryToken")]
    public partial class RegistryToken : global::Pulumi.CustomResource
    {
        [Output("credentials")]
        public Output<ImmutableArray<Outputs.RegistryTokenCredential>> Credentials { get; private set; } = null!;

        [Output("expiryDate")]
        public Output<string?> ExpiryDate { get; private set; } = null!;

        /// <summary>
        /// [string] The name of the container registry token. Immutable, update forces re-creation of the resource.
        /// * `expiry-date`           - (Optional)[string] The value must be supplied as ISO 8601 timestamp
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("registryId")]
        public Output<string> RegistryId { get; private set; } = null!;

        /// <summary>
        /// [string] Saves token password to file. Only works on create. Takes as argument a file name, or a file path
        /// 
        /// &gt; **⚠ WARNING** `save_password_to_file` must be used with caution.
        /// &gt; It will save the password(token) returned on create to a file. This is the only way to get the token.
        /// </summary>
        [Output("savePasswordToFile")]
        public Output<string?> SavePasswordToFile { get; private set; } = null!;

        /// <summary>
        /// [map]
        /// </summary>
        [Output("scopes")]
        public Output<ImmutableArray<Outputs.RegistryTokenScope>> Scopes { get; private set; } = null!;

        /// <summary>
        /// [string] Must have on of the values: `enabled`, `disabled`
        /// </summary>
        [Output("status")]
        public Output<string> Status { get; private set; } = null!;


        /// <summary>
        /// Create a RegistryToken resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public RegistryToken(string name, RegistryTokenArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:creg/registryToken:RegistryToken", name, args ?? new RegistryTokenArgs(), MakeResourceOptions(options, ""))
        {
        }

        private RegistryToken(string name, Input<string> id, RegistryTokenState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:creg/registryToken:RegistryToken", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing RegistryToken resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static RegistryToken Get(string name, Input<string> id, RegistryTokenState? state = null, CustomResourceOptions? options = null)
        {
            return new RegistryToken(name, id, state, options);
        }
    }

    public sealed class RegistryTokenArgs : global::Pulumi.ResourceArgs
    {
        [Input("expiryDate")]
        public Input<string>? ExpiryDate { get; set; }

        /// <summary>
        /// [string] The name of the container registry token. Immutable, update forces re-creation of the resource.
        /// * `expiry-date`           - (Optional)[string] The value must be supplied as ISO 8601 timestamp
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("registryId", required: true)]
        public Input<string> RegistryId { get; set; } = null!;

        /// <summary>
        /// [string] Saves token password to file. Only works on create. Takes as argument a file name, or a file path
        /// 
        /// &gt; **⚠ WARNING** `save_password_to_file` must be used with caution.
        /// &gt; It will save the password(token) returned on create to a file. This is the only way to get the token.
        /// </summary>
        [Input("savePasswordToFile")]
        public Input<string>? SavePasswordToFile { get; set; }

        [Input("scopes")]
        private InputList<Inputs.RegistryTokenScopeArgs>? _scopes;

        /// <summary>
        /// [map]
        /// </summary>
        public InputList<Inputs.RegistryTokenScopeArgs> Scopes
        {
            get => _scopes ?? (_scopes = new InputList<Inputs.RegistryTokenScopeArgs>());
            set => _scopes = value;
        }

        /// <summary>
        /// [string] Must have on of the values: `enabled`, `disabled`
        /// </summary>
        [Input("status")]
        public Input<string>? Status { get; set; }

        public RegistryTokenArgs()
        {
        }
        public static new RegistryTokenArgs Empty => new RegistryTokenArgs();
    }

    public sealed class RegistryTokenState : global::Pulumi.ResourceArgs
    {
        [Input("credentials")]
        private InputList<Inputs.RegistryTokenCredentialGetArgs>? _credentials;
        public InputList<Inputs.RegistryTokenCredentialGetArgs> Credentials
        {
            get => _credentials ?? (_credentials = new InputList<Inputs.RegistryTokenCredentialGetArgs>());
            set => _credentials = value;
        }

        [Input("expiryDate")]
        public Input<string>? ExpiryDate { get; set; }

        /// <summary>
        /// [string] The name of the container registry token. Immutable, update forces re-creation of the resource.
        /// * `expiry-date`           - (Optional)[string] The value must be supplied as ISO 8601 timestamp
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("registryId")]
        public Input<string>? RegistryId { get; set; }

        /// <summary>
        /// [string] Saves token password to file. Only works on create. Takes as argument a file name, or a file path
        /// 
        /// &gt; **⚠ WARNING** `save_password_to_file` must be used with caution.
        /// &gt; It will save the password(token) returned on create to a file. This is the only way to get the token.
        /// </summary>
        [Input("savePasswordToFile")]
        public Input<string>? SavePasswordToFile { get; set; }

        [Input("scopes")]
        private InputList<Inputs.RegistryTokenScopeGetArgs>? _scopes;

        /// <summary>
        /// [map]
        /// </summary>
        public InputList<Inputs.RegistryTokenScopeGetArgs> Scopes
        {
            get => _scopes ?? (_scopes = new InputList<Inputs.RegistryTokenScopeGetArgs>());
            set => _scopes = value;
        }

        /// <summary>
        /// [string] Must have on of the values: `enabled`, `disabled`
        /// </summary>
        [Input("status")]
        public Input<string>? Status { get; set; }

        public RegistryTokenState()
        {
        }
        public static new RegistryTokenState Empty => new RegistryTokenState();
    }
}
