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
    public static class GetRegistry
    {
        /// <summary>
        /// The **Container Registry data source** can be used to search for and return an existing Container Registry.
        /// You can provide a string for the name parameter which will be compared with provisioned Container Registry.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search and make sure that your resources have unique names.
        /// 
        /// ## Example Usage
        /// 
        /// ### By Id
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Creg.GetRegistry.Invoke(new()
        ///     {
        ///         Id = "registry_id",
        ///     });
        /// 
        /// });
        /// ```
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
        ///     var example = Ionoscloud.Creg.GetRegistry.Invoke(new()
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
        ///     var example = Ionoscloud.Creg.GetRegistry.Invoke(new()
        ///     {
        ///         Name = "-example",
        ///         PartialMatch = true,
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetRegistryResult> InvokeAsync(GetRegistryArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetRegistryResult>("ionoscloud:creg/getRegistry:getRegistry", args ?? new GetRegistryArgs(), options.WithDefaults());

        /// <summary>
        /// The **Container Registry data source** can be used to search for and return an existing Container Registry.
        /// You can provide a string for the name parameter which will be compared with provisioned Container Registry.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search and make sure that your resources have unique names.
        /// 
        /// ## Example Usage
        /// 
        /// ### By Id
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Creg.GetRegistry.Invoke(new()
        ///     {
        ///         Id = "registry_id",
        ///     });
        /// 
        /// });
        /// ```
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
        ///     var example = Ionoscloud.Creg.GetRegistry.Invoke(new()
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
        ///     var example = Ionoscloud.Creg.GetRegistry.Invoke(new()
        ///     {
        ///         Name = "-example",
        ///         PartialMatch = true,
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetRegistryResult> Invoke(GetRegistryInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetRegistryResult>("ionoscloud:creg/getRegistry:getRegistry", args ?? new GetRegistryInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The **Container Registry data source** can be used to search for and return an existing Container Registry.
        /// You can provide a string for the name parameter which will be compared with provisioned Container Registry.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search and make sure that your resources have unique names.
        /// 
        /// ## Example Usage
        /// 
        /// ### By Id
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Creg.GetRegistry.Invoke(new()
        ///     {
        ///         Id = "registry_id",
        ///     });
        /// 
        /// });
        /// ```
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
        ///     var example = Ionoscloud.Creg.GetRegistry.Invoke(new()
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
        ///     var example = Ionoscloud.Creg.GetRegistry.Invoke(new()
        ///     {
        ///         Name = "-example",
        ///         PartialMatch = true,
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetRegistryResult> Invoke(GetRegistryInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetRegistryResult>("ionoscloud:creg/getRegistry:getRegistry", args ?? new GetRegistryInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetRegistryArgs : global::Pulumi.InvokeArgs
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

        public GetRegistryArgs()
        {
        }
        public static new GetRegistryArgs Empty => new GetRegistryArgs();
    }

    public sealed class GetRegistryInvokeArgs : global::Pulumi.InvokeArgs
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

        public GetRegistryInvokeArgs()
        {
        }
        public static new GetRegistryInvokeArgs Empty => new GetRegistryInvokeArgs();
    }


    [OutputType]
    public sealed class GetRegistryResult
    {
        /// <summary>
        /// The subnet CIDRs that are allowed to connect to the registry.  Specify "a.b.c.d/32" for an individual IP address. __Note__: If this list is empty or not set, there are no restrictions.
        /// </summary>
        public readonly ImmutableArray<string> ApiSubnetAllowLists;
        public readonly ImmutableArray<Outputs.GetRegistryFeatureResult> Features;
        public readonly ImmutableArray<Outputs.GetRegistryGarbageCollectionScheduleResult> GarbageCollectionSchedules;
        public readonly string Hostname;
        /// <summary>
        /// Id of the container registry.
        /// </summary>
        public readonly string Id;
        public readonly string? Location;
        public readonly ImmutableArray<Outputs.GetRegistryMaintenanceWindowResult> MaintenanceWindows;
        /// <summary>
        /// The name of the container registry.
        /// </summary>
        public readonly string Name;
        public readonly bool? PartialMatch;
        public readonly ImmutableArray<Outputs.GetRegistryStorageUsageResult> StorageUsages;

        [OutputConstructor]
        private GetRegistryResult(
            ImmutableArray<string> apiSubnetAllowLists,

            ImmutableArray<Outputs.GetRegistryFeatureResult> features,

            ImmutableArray<Outputs.GetRegistryGarbageCollectionScheduleResult> garbageCollectionSchedules,

            string hostname,

            string id,

            string? location,

            ImmutableArray<Outputs.GetRegistryMaintenanceWindowResult> maintenanceWindows,

            string name,

            bool? partialMatch,

            ImmutableArray<Outputs.GetRegistryStorageUsageResult> storageUsages)
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
