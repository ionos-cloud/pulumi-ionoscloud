// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    public static class GetContainerRegistry
    {
        /// <summary>
        /// The **Container Registry data source** can be used to search for and return an existing Container Registry.
        /// You can provide a string for the name parameter which will be compared with provisioned Container Registry.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search and make sure that your resources have unique names.
        /// 
        /// ## Example Usage
        /// 
        /// ### By Name
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.GetContainerRegistry.Invoke(new()
        ///     {
        ///         Name = "container-registry-example",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Name with Partial Match
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.GetContainerRegistry.Invoke(new()
        ///     {
        ///         Name = "-example",
        ///         PartialMatch = true,
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetContainerRegistryResult> InvokeAsync(GetContainerRegistryArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetContainerRegistryResult>("ionoscloud:index/getContainerRegistry:getContainerRegistry", args ?? new GetContainerRegistryArgs(), options.WithDefaults());

        /// <summary>
        /// The **Container Registry data source** can be used to search for and return an existing Container Registry.
        /// You can provide a string for the name parameter which will be compared with provisioned Container Registry.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search and make sure that your resources have unique names.
        /// 
        /// ## Example Usage
        /// 
        /// ### By Name
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.GetContainerRegistry.Invoke(new()
        ///     {
        ///         Name = "container-registry-example",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Name with Partial Match
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.GetContainerRegistry.Invoke(new()
        ///     {
        ///         Name = "-example",
        ///         PartialMatch = true,
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetContainerRegistryResult> Invoke(GetContainerRegistryInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetContainerRegistryResult>("ionoscloud:index/getContainerRegistry:getContainerRegistry", args ?? new GetContainerRegistryInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The **Container Registry data source** can be used to search for and return an existing Container Registry.
        /// You can provide a string for the name parameter which will be compared with provisioned Container Registry.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search and make sure that your resources have unique names.
        /// 
        /// ## Example Usage
        /// 
        /// ### By Name
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.GetContainerRegistry.Invoke(new()
        ///     {
        ///         Name = "container-registry-example",
        ///     });
        /// 
        /// });
        /// ```
        /// 
        /// ### By Name with Partial Match
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.GetContainerRegistry.Invoke(new()
        ///     {
        ///         Name = "-example",
        ///         PartialMatch = true,
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetContainerRegistryResult> Invoke(GetContainerRegistryInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetContainerRegistryResult>("ionoscloud:index/getContainerRegistry:getContainerRegistry", args ?? new GetContainerRegistryInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetContainerRegistryArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// ID of the container registry you want to search for.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        [Input("location")]
        public string? Location { get; set; }

        /// <summary>
        /// Name of an existing container registry that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// Whether partial matching is allowed or not when using name argument. Default value is false.
        /// 
        /// Either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
        /// </summary>
        [Input("partialMatch")]
        public bool? PartialMatch { get; set; }

        public GetContainerRegistryArgs()
        {
        }
        public static new GetContainerRegistryArgs Empty => new GetContainerRegistryArgs();
    }

    public sealed class GetContainerRegistryInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// ID of the container registry you want to search for.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// Name of an existing container registry that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Whether partial matching is allowed or not when using name argument. Default value is false.
        /// 
        /// Either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
        /// </summary>
        [Input("partialMatch")]
        public Input<bool>? PartialMatch { get; set; }

        public GetContainerRegistryInvokeArgs()
        {
        }
        public static new GetContainerRegistryInvokeArgs Empty => new GetContainerRegistryInvokeArgs();
    }


    [OutputType]
    public sealed class GetContainerRegistryResult
    {
        /// <summary>
        /// The subnet CIDRs that are allowed to connect to the registry.  Specify "a.b.c.d/32" for an individual IP address. __Note__: If this list is empty or not set, there are no restrictions.
        /// </summary>
        public readonly ImmutableArray<string> ApiSubnetAllowLists;
        public readonly ImmutableArray<Outputs.GetContainerRegistryFeatureResult> Features;
        public readonly ImmutableArray<Outputs.GetContainerRegistryGarbageCollectionScheduleResult> GarbageCollectionSchedules;
        public readonly string Hostname;
        /// <summary>
        /// Id of the container registry.
        /// </summary>
        public readonly string? Id;
        public readonly string? Location;
        public readonly ImmutableArray<Outputs.GetContainerRegistryMaintenanceWindowResult> MaintenanceWindows;
        /// <summary>
        /// The name of the container registry.
        /// </summary>
        public readonly string? Name;
        public readonly bool? PartialMatch;
        public readonly ImmutableArray<Outputs.GetContainerRegistryStorageUsageResult> StorageUsages;

        [OutputConstructor]
        private GetContainerRegistryResult(
            ImmutableArray<string> apiSubnetAllowLists,

            ImmutableArray<Outputs.GetContainerRegistryFeatureResult> features,

            ImmutableArray<Outputs.GetContainerRegistryGarbageCollectionScheduleResult> garbageCollectionSchedules,

            string hostname,

            string? id,

            string? location,

            ImmutableArray<Outputs.GetContainerRegistryMaintenanceWindowResult> maintenanceWindows,

            string? name,

            bool? partialMatch,

            ImmutableArray<Outputs.GetContainerRegistryStorageUsageResult> storageUsages)
        {
            ApiSubnetAllowLists = apiSubnetAllowLists;
            Features = features;
            GarbageCollectionSchedules = garbageCollectionSchedules;
            Hostname = hostname;
            Id = id;
            Location = location;
            MaintenanceWindows = maintenanceWindows;
            Name = name;
            PartialMatch = partialMatch;
            StorageUsages = storageUsages;
        }
    }
}
