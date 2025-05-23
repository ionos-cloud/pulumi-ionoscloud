// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Apigateway
{
    public static class GetRoute
    {
        /// <summary>
        /// The **API Gateway Route data source** can be used to search for and return an existing API Gateway route.
        /// You can provide a string for the name parameter which will be compared with provisioned API Gateway routes.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ### By ID
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Apigateway.GetRoute.Invoke(new()
        ///     {
        ///         Id = "your_apigateway_route_id",
        ///         GatewayId = "your_gateway_id",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Name
        /// 
        /// Needs to have the resource be previously created, or a depends_on clause to ensure that the resource is created before
        /// this data source is called.
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Apigateway.GetRoute.Invoke(new()
        ///     {
        ///         Name = "apigateway-route",
        ///         GatewayId = "your_gateway_id",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetRouteResult> InvokeAsync(GetRouteArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetRouteResult>("ionoscloud:apigateway/getRoute:getRoute", args ?? new GetRouteArgs(), options.WithDefaults());

        /// <summary>
        /// The **API Gateway Route data source** can be used to search for and return an existing API Gateway route.
        /// You can provide a string for the name parameter which will be compared with provisioned API Gateway routes.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ### By ID
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Apigateway.GetRoute.Invoke(new()
        ///     {
        ///         Id = "your_apigateway_route_id",
        ///         GatewayId = "your_gateway_id",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Name
        /// 
        /// Needs to have the resource be previously created, or a depends_on clause to ensure that the resource is created before
        /// this data source is called.
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Apigateway.GetRoute.Invoke(new()
        ///     {
        ///         Name = "apigateway-route",
        ///         GatewayId = "your_gateway_id",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetRouteResult> Invoke(GetRouteInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetRouteResult>("ionoscloud:apigateway/getRoute:getRoute", args ?? new GetRouteInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The **API Gateway Route data source** can be used to search for and return an existing API Gateway route.
        /// You can provide a string for the name parameter which will be compared with provisioned API Gateway routes.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ### By ID
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Apigateway.GetRoute.Invoke(new()
        ///     {
        ///         Id = "your_apigateway_route_id",
        ///         GatewayId = "your_gateway_id",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Name
        /// 
        /// Needs to have the resource be previously created, or a depends_on clause to ensure that the resource is created before
        /// this data source is called.
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Apigateway.GetRoute.Invoke(new()
        ///     {
        ///         Name = "apigateway-route",
        ///         GatewayId = "your_gateway_id",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetRouteResult> Invoke(GetRouteInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetRouteResult>("ionoscloud:apigateway/getRoute:getRoute", args ?? new GetRouteInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetRouteArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the API Gateway that the route belongs to.
        /// </summary>
        [Input("gatewayId", required: true)]
        public string GatewayId { get; set; } = null!;

        /// <summary>
        /// ID of an existing API Gateway Route that you want to search for.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// Name of an existing API Gateway Route that you want to search for.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        [Input("partialMatch")]
        public bool? PartialMatch { get; set; }

        public GetRouteArgs()
        {
        }
        public static new GetRouteArgs Empty => new GetRouteArgs();
    }

    public sealed class GetRouteInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the API Gateway that the route belongs to.
        /// </summary>
        [Input("gatewayId", required: true)]
        public Input<string> GatewayId { get; set; } = null!;

        /// <summary>
        /// ID of an existing API Gateway Route that you want to search for.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Name of an existing API Gateway Route that you want to search for.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("partialMatch")]
        public Input<bool>? PartialMatch { get; set; }

        public GetRouteInvokeArgs()
        {
        }
        public static new GetRouteInvokeArgs Empty => new GetRouteInvokeArgs();
    }


    [OutputType]
    public sealed class GetRouteResult
    {
        public readonly string GatewayId;
        /// <summary>
        /// ID of the API Gateway Route.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The HTTP methods that the route should match.
        /// </summary>
        public readonly ImmutableArray<string> Methods;
        /// <summary>
        /// The name of the API Gateway Route.
        /// </summary>
        public readonly string Name;
        public readonly bool? PartialMatch;
        /// <summary>
        /// The paths that the route should match.
        /// </summary>
        public readonly ImmutableArray<string> Paths;
        /// <summary>
        /// This field specifies the protocol used by the ingress to route traffic to the backend service.
        /// </summary>
        public readonly string Type;
        public readonly ImmutableArray<Outputs.GetRouteUpstreamResult> Upstreams;
        /// <summary>
        /// Shows whether websocket support is enabled or disabled.
        /// </summary>
        public readonly bool Websocket;

        [OutputConstructor]
        private GetRouteResult(
            string gatewayId,

            string id,

            ImmutableArray<string> methods,

            string name,

            bool? partialMatch,

            ImmutableArray<string> paths,

            string type,

            ImmutableArray<Outputs.GetRouteUpstreamResult> upstreams,

            bool websocket)
        {
            GatewayId = gatewayId;
            Id = id;
            Methods = methods;
            Name = name;
            PartialMatch = partialMatch;
            Paths = paths;
            Type = type;
            Upstreams = upstreams;
            Websocket = websocket;
        }
    }
}
