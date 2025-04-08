// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.K8s
{
    public static class GetNodePoolNodes
    {
        /// <summary>
        /// The **k8s Node Pool Nodes** data source can be used to search for and return a list of existing k8s Node Pool nodes.
        /// ## Example Usage
        /// 
        /// ### By IDs
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.K8s.GetNodePoolNodes.Invoke(new()
        ///     {
        ///         NodePoolId = "k8s_nodepool_id",
        ///         K8sClusterId = "k8s_cluster_id",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetNodePoolNodesResult> InvokeAsync(GetNodePoolNodesArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetNodePoolNodesResult>("ionoscloud:k8s/getNodePoolNodes:getNodePoolNodes", args ?? new GetNodePoolNodesArgs(), options.WithDefaults());

        /// <summary>
        /// The **k8s Node Pool Nodes** data source can be used to search for and return a list of existing k8s Node Pool nodes.
        /// ## Example Usage
        /// 
        /// ### By IDs
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.K8s.GetNodePoolNodes.Invoke(new()
        ///     {
        ///         NodePoolId = "k8s_nodepool_id",
        ///         K8sClusterId = "k8s_cluster_id",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetNodePoolNodesResult> Invoke(GetNodePoolNodesInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetNodePoolNodesResult>("ionoscloud:k8s/getNodePoolNodes:getNodePoolNodes", args ?? new GetNodePoolNodesInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The **k8s Node Pool Nodes** data source can be used to search for and return a list of existing k8s Node Pool nodes.
        /// ## Example Usage
        /// 
        /// ### By IDs
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.K8s.GetNodePoolNodes.Invoke(new()
        ///     {
        ///         NodePoolId = "k8s_nodepool_id",
        ///         K8sClusterId = "k8s_cluster_id",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetNodePoolNodesResult> Invoke(GetNodePoolNodesInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetNodePoolNodesResult>("ionoscloud:k8s/getNodePoolNodes:getNodePoolNodes", args ?? new GetNodePoolNodesInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetNodePoolNodesArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// K8s Cluster' UUID
        /// </summary>
        [Input("k8sClusterId", required: true)]
        public string K8sClusterId { get; set; } = null!;

        [Input("nodePoolId", required: true)]
        public string NodePoolId { get; set; } = null!;

        public GetNodePoolNodesArgs()
        {
        }
        public static new GetNodePoolNodesArgs Empty => new GetNodePoolNodesArgs();
    }

    public sealed class GetNodePoolNodesInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// K8s Cluster' UUID
        /// </summary>
        [Input("k8sClusterId", required: true)]
        public Input<string> K8sClusterId { get; set; } = null!;

        [Input("nodePoolId", required: true)]
        public Input<string> NodePoolId { get; set; } = null!;

        public GetNodePoolNodesInvokeArgs()
        {
        }
        public static new GetNodePoolNodesInvokeArgs Empty => new GetNodePoolNodesInvokeArgs();
    }


    [OutputType]
    public sealed class GetNodePoolNodesResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string K8sClusterId;
        public readonly string NodePoolId;
        /// <summary>
        /// a list of the nodes that are in the nodepool
        /// </summary>
        public readonly ImmutableArray<Outputs.GetNodePoolNodesNodeResult> Nodes;

        [OutputConstructor]
        private GetNodePoolNodesResult(
            string id,

            string k8sClusterId,

            string nodePoolId,

            ImmutableArray<Outputs.GetNodePoolNodesNodeResult> nodes)
        {
            Id = id;
            K8sClusterId = k8sClusterId;
            NodePoolId = nodePoolId;
            Nodes = nodes;
        }
    }
}
