// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    [IonoscloudResourceType("ionoscloud:index/loadbalancer:Loadbalancer")]
    public partial class Loadbalancer : global::Pulumi.CustomResource
    {
        [Output("datacenterId")]
        public Output<string> DatacenterId { get; private set; } = null!;

        [Output("dhcp")]
        public Output<bool?> Dhcp { get; private set; } = null!;

        [Output("ip")]
        public Output<string> Ip { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("nicIds")]
        public Output<ImmutableArray<string>> NicIds { get; private set; } = null!;


        /// <summary>
        /// Create a Loadbalancer resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Loadbalancer(string name, LoadbalancerArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:index/loadbalancer:Loadbalancer", name, args ?? new LoadbalancerArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Loadbalancer(string name, Input<string> id, LoadbalancerState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:index/loadbalancer:Loadbalancer", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Loadbalancer resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Loadbalancer Get(string name, Input<string> id, LoadbalancerState? state = null, CustomResourceOptions? options = null)
        {
            return new Loadbalancer(name, id, state, options);
        }
    }

    public sealed class LoadbalancerArgs : global::Pulumi.ResourceArgs
    {
        [Input("datacenterId", required: true)]
        public Input<string> DatacenterId { get; set; } = null!;

        [Input("dhcp")]
        public Input<bool>? Dhcp { get; set; }

        [Input("ip")]
        public Input<string>? Ip { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("nicIds", required: true)]
        private InputList<string>? _nicIds;
        public InputList<string> NicIds
        {
            get => _nicIds ?? (_nicIds = new InputList<string>());
            set => _nicIds = value;
        }

        public LoadbalancerArgs()
        {
        }
        public static new LoadbalancerArgs Empty => new LoadbalancerArgs();
    }

    public sealed class LoadbalancerState : global::Pulumi.ResourceArgs
    {
        [Input("datacenterId")]
        public Input<string>? DatacenterId { get; set; }

        [Input("dhcp")]
        public Input<bool>? Dhcp { get; set; }

        [Input("ip")]
        public Input<string>? Ip { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("nicIds")]
        private InputList<string>? _nicIds;
        public InputList<string> NicIds
        {
            get => _nicIds ?? (_nicIds = new InputList<string>());
            set => _nicIds = value;
        }

        public LoadbalancerState()
        {
        }
        public static new LoadbalancerState Empty => new LoadbalancerState();
    }
}
