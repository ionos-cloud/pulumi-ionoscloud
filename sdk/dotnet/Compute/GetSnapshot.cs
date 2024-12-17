// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Compute
{
    public static class GetSnapshot
    {
        /// <summary>
        /// The **Snapshot data source** can be used to search for and return an existing snapshot which can then be used to provision a server. If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned. When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ### By Name &amp; Size &amp; Location
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Compute.GetSnapshot.Invoke(new()
        ///     {
        ///         Location = "us/las",
        ///         Name = "Snapshot Example",
        ///         Size = 2,
        ///     });
        /// 
        /// });
        /// ```
        /// Note: The size argument is in GB
        /// </summary>
        public static Task<GetSnapshotResult> InvokeAsync(GetSnapshotArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetSnapshotResult>("ionoscloud:compute/getSnapshot:getSnapshot", args ?? new GetSnapshotArgs(), options.WithDefaults());

        /// <summary>
        /// The **Snapshot data source** can be used to search for and return an existing snapshot which can then be used to provision a server. If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned. When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ### By Name &amp; Size &amp; Location
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Compute.GetSnapshot.Invoke(new()
        ///     {
        ///         Location = "us/las",
        ///         Name = "Snapshot Example",
        ///         Size = 2,
        ///     });
        /// 
        /// });
        /// ```
        /// Note: The size argument is in GB
        /// </summary>
        public static Output<GetSnapshotResult> Invoke(GetSnapshotInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetSnapshotResult>("ionoscloud:compute/getSnapshot:getSnapshot", args ?? new GetSnapshotInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The **Snapshot data source** can be used to search for and return an existing snapshot which can then be used to provision a server. If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned. When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ### By Name &amp; Size &amp; Location
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Compute.GetSnapshot.Invoke(new()
        ///     {
        ///         Location = "us/las",
        ///         Name = "Snapshot Example",
        ///         Size = 2,
        ///     });
        /// 
        /// });
        /// ```
        /// Note: The size argument is in GB
        /// </summary>
        public static Output<GetSnapshotResult> Invoke(GetSnapshotInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetSnapshotResult>("ionoscloud:compute/getSnapshot:getSnapshot", args ?? new GetSnapshotInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSnapshotArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// UUID of an existing snapshot that you want to search for.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// Existing snapshot's location.
        /// </summary>
        [Input("location")]
        public string? Location { get; set; }

        /// <summary>
        /// Name of an existing snapshot that you want to search for.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// The size of the snapshot to look for.
        /// 
        /// Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
        /// Additionally, you can add `location` and `size` along with the `name` argument for a more refined search.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// </summary>
        [Input("size")]
        public int? Size { get; set; }

        public GetSnapshotArgs()
        {
        }
        public static new GetSnapshotArgs Empty => new GetSnapshotArgs();
    }

    public sealed class GetSnapshotInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// UUID of an existing snapshot that you want to search for.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Existing snapshot's location.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// Name of an existing snapshot that you want to search for.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The size of the snapshot to look for.
        /// 
        /// Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
        /// Additionally, you can add `location` and `size` along with the `name` argument for a more refined search.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// </summary>
        [Input("size")]
        public Input<int>? Size { get; set; }

        public GetSnapshotInvokeArgs()
        {
        }
        public static new GetSnapshotInvokeArgs Empty => new GetSnapshotInvokeArgs();
    }


    [OutputType]
    public sealed class GetSnapshotResult
    {
        /// <summary>
        /// Is capable of CPU hot plug (no reboot required)
        /// </summary>
        public readonly bool CpuHotPlug;
        /// <summary>
        /// Is capable of CPU hot unplug (no reboot required)
        /// </summary>
        public readonly bool CpuHotUnplug;
        /// <summary>
        /// Human readable description
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// Is capable of SCSI drive hot plug (no reboot required)
        /// </summary>
        public readonly bool DiscScsiHotPlug;
        /// <summary>
        /// Is capable of SCSI drive hot unplug (no reboot required). This works only for non-Windows virtual Machines.
        /// </summary>
        public readonly bool DiscScsiHotUnplug;
        /// <summary>
        /// Is capable of Virt-IO drive hot plug (no reboot required)
        /// </summary>
        public readonly bool DiscVirtioHotPlug;
        /// <summary>
        /// Is capable of Virt-IO drive hot unplug (no reboot required). This works only for non-Windows virtual Machines.
        /// </summary>
        public readonly bool DiscVirtioHotUnplug;
        /// <summary>
        /// UUID of the snapshot
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// OS type of this Snapshot
        /// </summary>
        public readonly string LicenceType;
        /// <summary>
        /// Location of that image/snapshot
        /// </summary>
        public readonly string Location;
        /// <summary>
        /// The name of the snapshot.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Is capable of nic hot plug (no reboot required)
        /// </summary>
        public readonly bool NicHotPlug;
        /// <summary>
        /// Is capable of nic hot unplug (no reboot required)
        /// </summary>
        public readonly bool NicHotUnplug;
        /// <summary>
        /// Is capable of memory hot plug (no reboot required)
        /// </summary>
        public readonly bool RamHotPlug;
        /// <summary>
        /// Is capable of memory hot unplug (no reboot required)
        /// </summary>
        public readonly bool RamHotUnplug;
        /// <summary>
        /// Boolean value representing if the snapshot requires extra protection e.g. two factor protection
        /// </summary>
        public readonly bool SecAuthProtection;
        /// <summary>
        /// The size of the image in GB
        /// </summary>
        public readonly int Size;

        [OutputConstructor]
        private GetSnapshotResult(
            bool cpuHotPlug,

            bool cpuHotUnplug,

            string description,

            bool discScsiHotPlug,

            bool discScsiHotUnplug,

            bool discVirtioHotPlug,

            bool discVirtioHotUnplug,

            string? id,

            string licenceType,

            string location,

            string name,

            bool nicHotPlug,

            bool nicHotUnplug,

            bool ramHotPlug,

            bool ramHotUnplug,

            bool secAuthProtection,

            int size)
        {
            CpuHotPlug = cpuHotPlug;
            CpuHotUnplug = cpuHotUnplug;
            Description = description;
            DiscScsiHotPlug = discScsiHotPlug;
            DiscScsiHotUnplug = discScsiHotUnplug;
            DiscVirtioHotPlug = discVirtioHotPlug;
            DiscVirtioHotUnplug = discVirtioHotUnplug;
            Id = id;
            LicenceType = licenceType;
            Location = location;
            Name = name;
            NicHotPlug = nicHotPlug;
            NicHotUnplug = nicHotUnplug;
            RamHotPlug = ramHotPlug;
            RamHotUnplug = ramHotUnplug;
            SecAuthProtection = secAuthProtection;
            Size = size;
        }
    }
}
