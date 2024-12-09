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
    /// Manages an **API Gateway Route** on IonosCloud.
    /// 
    /// ## Example Usage
    /// 
    /// This resource will create an operational API Gateway Route. After this section completes, the provisioner can be called.
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ionoscloud = Pulumi.Ionoscloud;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var example = new Ionoscloud.Apigateway("example", new()
    ///     {
    ///         Metrics = true,
    ///         CustomDomains = new[]
    ///         {
    ///             new Ionoscloud.Inputs.ApigatewayCustomDomainArgs
    ///             {
    ///                 Name = "example.com",
    ///                 CertificateId = "00000000-0000-0000-0000-000000000000",
    ///             },
    ///             new Ionoscloud.Inputs.ApigatewayCustomDomainArgs
    ///             {
    ///                 Name = "example.org",
    ///                 CertificateId = "00000000-0000-0000-0000-000000000000",
    ///             },
    ///         },
    ///     });
    /// 
    ///     var apigatewayRoute = new Ionoscloud.ApigatewayRoute("apigatewayRoute", new()
    ///     {
    ///         Type = "http",
    ///         Paths = new[]
    ///         {
    ///             "/foo/*",
    ///             "/bar",
    ///         },
    ///         Methods = new[]
    ///         {
    ///             "GET",
    ///             "POST",
    ///         },
    ///         Websocket = false,
    ///         Upstreams = new[]
    ///         {
    ///             new Ionoscloud.Inputs.ApigatewayRouteUpstreamArgs
    ///             {
    ///                 Scheme = "http",
    ///                 Loadbalancer = "roundrobin",
    ///                 Host = "example.com",
    ///                 Port = 80,
    ///                 Weight = 100,
    ///             },
    ///         },
    ///         GatewayId = example.Id,
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// API Gateway route can be imported using the `apigateway route id`:
    /// 
    /// ```sh
    /// $ pulumi import ionoscloud:index/apigatewayRoute:ApigatewayRoute myroute {apigateway uuid}:{apigateway route uuid}
    /// ```
    /// </summary>
    [IonoscloudResourceType("ionoscloud:index/apigatewayRoute:ApigatewayRoute")]
    public partial class ApigatewayRoute : global::Pulumi.CustomResource
    {
        /// <summary>
        /// [string] The ID of the API Gateway that the route belongs to.
        /// </summary>
        [Output("gatewayId")]
        public Output<string> GatewayId { get; private set; } = null!;

        /// <summary>
        /// [list] The HTTP methods that the route should match. Minimum items: 1. Possible values: `GET`,
        /// `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, `HEAD`, `CONNECT`, `TRACE`.
        /// </summary>
        [Output("methods")]
        public Output<ImmutableArray<string>> Methods { get; private set; } = null!;

        /// <summary>
        /// [string] Name of the API Gateway Route. Only alphanumeric characters are allowed.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// [list] The paths that the route should match. Minimum items: 1.
        /// </summary>
        [Output("paths")]
        public Output<ImmutableArray<string>> Paths { get; private set; } = null!;

        /// <summary>
        /// [string] This field specifies the protocol used by the ingress to route traffic to the backend
        /// service. Default value: `http`.
        /// </summary>
        [Output("type")]
        public Output<string?> Type { get; private set; } = null!;

        /// <summary>
        /// Upstreams information of the API Gateway Route. Minimum items: 1.
        /// </summary>
        [Output("upstreams")]
        public Output<ImmutableArray<Outputs.ApigatewayRouteUpstream>> Upstreams { get; private set; } = null!;

        /// <summary>
        /// [bool] To enable websocket support. Default value: `false`.
        /// </summary>
        [Output("websocket")]
        public Output<bool?> Websocket { get; private set; } = null!;


        /// <summary>
        /// Create a ApigatewayRoute resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ApigatewayRoute(string name, ApigatewayRouteArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:index/apigatewayRoute:ApigatewayRoute", name, args ?? new ApigatewayRouteArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ApigatewayRoute(string name, Input<string> id, ApigatewayRouteState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:index/apigatewayRoute:ApigatewayRoute", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ApigatewayRoute resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ApigatewayRoute Get(string name, Input<string> id, ApigatewayRouteState? state = null, CustomResourceOptions? options = null)
        {
            return new ApigatewayRoute(name, id, state, options);
        }
    }

    public sealed class ApigatewayRouteArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] The ID of the API Gateway that the route belongs to.
        /// </summary>
        [Input("gatewayId", required: true)]
        public Input<string> GatewayId { get; set; } = null!;

        [Input("methods", required: true)]
        private InputList<string>? _methods;

        /// <summary>
        /// [list] The HTTP methods that the route should match. Minimum items: 1. Possible values: `GET`,
        /// `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, `HEAD`, `CONNECT`, `TRACE`.
        /// </summary>
        public InputList<string> Methods
        {
            get => _methods ?? (_methods = new InputList<string>());
            set => _methods = value;
        }

        /// <summary>
        /// [string] Name of the API Gateway Route. Only alphanumeric characters are allowed.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("paths", required: true)]
        private InputList<string>? _paths;

        /// <summary>
        /// [list] The paths that the route should match. Minimum items: 1.
        /// </summary>
        public InputList<string> Paths
        {
            get => _paths ?? (_paths = new InputList<string>());
            set => _paths = value;
        }

        /// <summary>
        /// [string] This field specifies the protocol used by the ingress to route traffic to the backend
        /// service. Default value: `http`.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        [Input("upstreams", required: true)]
        private InputList<Inputs.ApigatewayRouteUpstreamArgs>? _upstreams;

        /// <summary>
        /// Upstreams information of the API Gateway Route. Minimum items: 1.
        /// </summary>
        public InputList<Inputs.ApigatewayRouteUpstreamArgs> Upstreams
        {
            get => _upstreams ?? (_upstreams = new InputList<Inputs.ApigatewayRouteUpstreamArgs>());
            set => _upstreams = value;
        }

        /// <summary>
        /// [bool] To enable websocket support. Default value: `false`.
        /// </summary>
        [Input("websocket")]
        public Input<bool>? Websocket { get; set; }

        public ApigatewayRouteArgs()
        {
        }
        public static new ApigatewayRouteArgs Empty => new ApigatewayRouteArgs();
    }

    public sealed class ApigatewayRouteState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] The ID of the API Gateway that the route belongs to.
        /// </summary>
        [Input("gatewayId")]
        public Input<string>? GatewayId { get; set; }

        [Input("methods")]
        private InputList<string>? _methods;

        /// <summary>
        /// [list] The HTTP methods that the route should match. Minimum items: 1. Possible values: `GET`,
        /// `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, `HEAD`, `CONNECT`, `TRACE`.
        /// </summary>
        public InputList<string> Methods
        {
            get => _methods ?? (_methods = new InputList<string>());
            set => _methods = value;
        }

        /// <summary>
        /// [string] Name of the API Gateway Route. Only alphanumeric characters are allowed.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("paths")]
        private InputList<string>? _paths;

        /// <summary>
        /// [list] The paths that the route should match. Minimum items: 1.
        /// </summary>
        public InputList<string> Paths
        {
            get => _paths ?? (_paths = new InputList<string>());
            set => _paths = value;
        }

        /// <summary>
        /// [string] This field specifies the protocol used by the ingress to route traffic to the backend
        /// service. Default value: `http`.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        [Input("upstreams")]
        private InputList<Inputs.ApigatewayRouteUpstreamGetArgs>? _upstreams;

        /// <summary>
        /// Upstreams information of the API Gateway Route. Minimum items: 1.
        /// </summary>
        public InputList<Inputs.ApigatewayRouteUpstreamGetArgs> Upstreams
        {
            get => _upstreams ?? (_upstreams = new InputList<Inputs.ApigatewayRouteUpstreamGetArgs>());
            set => _upstreams = value;
        }

        /// <summary>
        /// [bool] To enable websocket support. Default value: `false`.
        /// </summary>
        [Input("websocket")]
        public Input<bool>? Websocket { get; set; }

        public ApigatewayRouteState()
        {
        }
        public static new ApigatewayRouteState Empty => new ApigatewayRouteState();
    }
}
