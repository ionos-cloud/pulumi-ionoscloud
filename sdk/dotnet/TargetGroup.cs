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
    /// Manages a **Target Group** on IonosCloud.
    /// 
    /// ## Example Usage
    /// 
    /// &lt;!--Start PulumiCodeChooser --&gt;
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ionoscloud = Pulumi.Ionoscloud;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var example = new Ionoscloud.TargetGroup("example", new()
    ///     {
    ///         Algorithm = "ROUND_ROBIN",
    ///         HealthCheck = new Ionoscloud.Inputs.TargetGroupHealthCheckArgs
    ///         {
    ///             CheckInterval = 50000,
    ///             CheckTimeout = 5000,
    ///             Retries = 2,
    ///         },
    ///         HttpHealthCheck = new Ionoscloud.Inputs.TargetGroupHttpHealthCheckArgs
    ///         {
    ///             MatchType = "STATUS_CODE",
    ///             Method = "GET",
    ///             Negate = true,
    ///             Path = "/.",
    ///             Regex = true,
    ///             Response = "200",
    ///         },
    ///         Protocol = "HTTP",
    ///         ProtocolVersion = "HTTP1",
    ///         Targets = new[]
    ///         {
    ///             new Ionoscloud.Inputs.TargetGroupTargetArgs
    ///             {
    ///                 HealthCheckEnabled = true,
    ///                 Ip = "22.231.2.2",
    ///                 MaintenanceEnabled = false,
    ///                 Port = 8080,
    ///                 ProxyProtocol = "v2ssl",
    ///                 Weight = 1,
    ///             },
    ///             new Ionoscloud.Inputs.TargetGroupTargetArgs
    ///             {
    ///                 HealthCheckEnabled = false,
    ///                 Ip = "22.231.2.3",
    ///                 MaintenanceEnabled = false,
    ///                 Port = 8081,
    ///                 ProxyProtocol = "v2",
    ///                 Weight = 124,
    ///             },
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// &lt;!--End PulumiCodeChooser --&gt;
    /// 
    /// ## Import
    /// 
    /// Resource Target Group can be imported using the `resource id`, e.g.
    /// 
    /// ```sh
    /// $ pulumi import ionoscloud:index/targetGroup:TargetGroup myTargetGroup {target group uuid}
    /// ```
    /// </summary>
    [IonoscloudResourceType("ionoscloud:index/targetGroup:TargetGroup")]
    public partial class TargetGroup : global::Pulumi.CustomResource
    {
        /// <summary>
        /// [string] Balancing algorithm.
        /// </summary>
        [Output("algorithm")]
        public Output<string> Algorithm { get; private set; } = null!;

        /// <summary>
        /// Health check attributes for Target Group.
        /// </summary>
        [Output("healthCheck")]
        public Output<Outputs.TargetGroupHealthCheck> HealthCheck { get; private set; } = null!;

        /// <summary>
        /// Http health check attributes for Target Group
        /// </summary>
        [Output("httpHealthCheck")]
        public Output<Outputs.TargetGroupHttpHealthCheck> HttpHealthCheck { get; private set; } = null!;

        /// <summary>
        /// [string] The name of the target group.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// [string] Balancing protocol.
        /// </summary>
        [Output("protocol")]
        public Output<string> Protocol { get; private set; } = null!;

        /// <summary>
        /// [string] The forwarding protocol version. Value is ignored when protocol is not 'HTTP'.
        /// </summary>
        [Output("protocolVersion")]
        public Output<string> ProtocolVersion { get; private set; } = null!;

        /// <summary>
        /// [list] Array of items in the collection
        /// </summary>
        [Output("targets")]
        public Output<ImmutableArray<Outputs.TargetGroupTarget>> Targets { get; private set; } = null!;


        /// <summary>
        /// Create a TargetGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public TargetGroup(string name, TargetGroupArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:index/targetGroup:TargetGroup", name, args ?? new TargetGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private TargetGroup(string name, Input<string> id, TargetGroupState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:index/targetGroup:TargetGroup", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing TargetGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static TargetGroup Get(string name, Input<string> id, TargetGroupState? state = null, CustomResourceOptions? options = null)
        {
            return new TargetGroup(name, id, state, options);
        }
    }

    public sealed class TargetGroupArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] Balancing algorithm.
        /// </summary>
        [Input("algorithm", required: true)]
        public Input<string> Algorithm { get; set; } = null!;

        /// <summary>
        /// Health check attributes for Target Group.
        /// </summary>
        [Input("healthCheck")]
        public Input<Inputs.TargetGroupHealthCheckArgs>? HealthCheck { get; set; }

        /// <summary>
        /// Http health check attributes for Target Group
        /// </summary>
        [Input("httpHealthCheck")]
        public Input<Inputs.TargetGroupHttpHealthCheckArgs>? HttpHealthCheck { get; set; }

        /// <summary>
        /// [string] The name of the target group.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// [string] Balancing protocol.
        /// </summary>
        [Input("protocol", required: true)]
        public Input<string> Protocol { get; set; } = null!;

        /// <summary>
        /// [string] The forwarding protocol version. Value is ignored when protocol is not 'HTTP'.
        /// </summary>
        [Input("protocolVersion", required: true)]
        public Input<string> ProtocolVersion { get; set; } = null!;

        [Input("targets")]
        private InputList<Inputs.TargetGroupTargetArgs>? _targets;

        /// <summary>
        /// [list] Array of items in the collection
        /// </summary>
        public InputList<Inputs.TargetGroupTargetArgs> Targets
        {
            get => _targets ?? (_targets = new InputList<Inputs.TargetGroupTargetArgs>());
            set => _targets = value;
        }

        public TargetGroupArgs()
        {
        }
        public static new TargetGroupArgs Empty => new TargetGroupArgs();
    }

    public sealed class TargetGroupState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] Balancing algorithm.
        /// </summary>
        [Input("algorithm")]
        public Input<string>? Algorithm { get; set; }

        /// <summary>
        /// Health check attributes for Target Group.
        /// </summary>
        [Input("healthCheck")]
        public Input<Inputs.TargetGroupHealthCheckGetArgs>? HealthCheck { get; set; }

        /// <summary>
        /// Http health check attributes for Target Group
        /// </summary>
        [Input("httpHealthCheck")]
        public Input<Inputs.TargetGroupHttpHealthCheckGetArgs>? HttpHealthCheck { get; set; }

        /// <summary>
        /// [string] The name of the target group.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// [string] Balancing protocol.
        /// </summary>
        [Input("protocol")]
        public Input<string>? Protocol { get; set; }

        /// <summary>
        /// [string] The forwarding protocol version. Value is ignored when protocol is not 'HTTP'.
        /// </summary>
        [Input("protocolVersion")]
        public Input<string>? ProtocolVersion { get; set; }

        [Input("targets")]
        private InputList<Inputs.TargetGroupTargetGetArgs>? _targets;

        /// <summary>
        /// [list] Array of items in the collection
        /// </summary>
        public InputList<Inputs.TargetGroupTargetGetArgs> Targets
        {
            get => _targets ?? (_targets = new InputList<Inputs.TargetGroupTargetGetArgs>());
            set => _targets = value;
        }

        public TargetGroupState()
        {
        }
        public static new TargetGroupState Empty => new TargetGroupState();
    }
}
