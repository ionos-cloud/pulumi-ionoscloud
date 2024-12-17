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
    /// Manages **Snapshots** on IonosCloud.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ionoscloud = Pulumi.Ionoscloud;
    /// using Random = Pulumi.Random;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var exampleImage = Ionoscloud.Compute.GetImage.Invoke(new()
    ///     {
    ///         Type = "HDD",
    ///         ImageAlias = "ubuntu:latest",
    ///         Location = "us/las",
    ///     });
    /// 
    ///     var exampleDatacenter = new Ionoscloud.Compute.Datacenter("exampleDatacenter", new()
    ///     {
    ///         Location = "us/las",
    ///         Description = "Datacenter Description",
    ///         SecAuthProtection = false,
    ///     });
    /// 
    ///     var exampleLan = new Ionoscloud.Compute.Lan("exampleLan", new()
    ///     {
    ///         DatacenterId = exampleDatacenter.Id,
    ///         Public = true,
    ///     });
    /// 
    ///     var serverImagePassword = new Random.RandomPassword("serverImagePassword", new()
    ///     {
    ///         Length = 16,
    ///         Special = false,
    ///     });
    /// 
    ///     var exampleServer = new Ionoscloud.Compute.Server("exampleServer", new()
    ///     {
    ///         DatacenterId = exampleDatacenter.Id,
    ///         Cores = 1,
    ///         Ram = 1024,
    ///         AvailabilityZone = "ZONE_1",
    ///         CpuFamily = "INTEL_XEON",
    ///         ImageName = exampleImage.Apply(getImageResult =&gt; getImageResult.Id),
    ///         ImagePassword = serverImagePassword.Result,
    ///         Type = "ENTERPRISE",
    ///         Volume = new Ionoscloud.Compute.Inputs.ServerVolumeArgs
    ///         {
    ///             Name = "system",
    ///             Size = 5,
    ///             DiskType = "SSD Standard",
    ///             UserData = "foo",
    ///             Bus = "VIRTIO",
    ///             AvailabilityZone = "ZONE_1",
    ///         },
    ///     });
    /// 
    ///     var testSnapshot = new Ionoscloud.Compute.Snapshot("testSnapshot", new()
    ///     {
    ///         DatacenterId = exampleDatacenter.Id,
    ///         VolumeId = exampleServer.BootVolume,
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// Resource Snapshot can be imported using the `snapshot id`, e.g.
    /// 
    /// ```sh
    /// $ pulumi import ionoscloud:compute/snapshot:Snapshot mysnapshot {snapshot uuid}
    /// ```
    /// </summary>
    [IonoscloudResourceType("ionoscloud:compute/snapshot:Snapshot")]
    public partial class Snapshot : global::Pulumi.CustomResource
    {
        /// <summary>
        /// (Computed)[string] Is capable of CPU hot plug (no reboot required). Can only be updated.
        /// </summary>
        [Output("cpuHotPlug")]
        public Output<bool> CpuHotPlug { get; private set; } = null!;

        /// <summary>
        /// Is capable of CPU hot unplug (no reboot required)
        /// </summary>
        [Output("cpuHotUnplug")]
        public Output<bool> CpuHotUnplug { get; private set; } = null!;

        /// <summary>
        /// [string] The ID of the Virtual Data Center.
        /// </summary>
        [Output("datacenterId")]
        public Output<string> DatacenterId { get; private set; } = null!;

        /// <summary>
        /// (Computed)[string] Human readable description
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// Is capable of SCSI drive hot plug (no reboot required)
        /// </summary>
        [Output("discScsiHotPlug")]
        public Output<bool> DiscScsiHotPlug { get; private set; } = null!;

        /// <summary>
        /// Is capable of SCSI drive hot unplug (no reboot required). This works only for non-Windows virtual Machines.
        /// </summary>
        [Output("discScsiHotUnplug")]
        public Output<bool> DiscScsiHotUnplug { get; private set; } = null!;

        /// <summary>
        /// (Computed)[string] Is capable of Virt-IO drive hot plug (no reboot required). Can only be updated.
        /// </summary>
        [Output("discVirtioHotPlug")]
        public Output<bool> DiscVirtioHotPlug { get; private set; } = null!;

        /// <summary>
        /// (Computed)[string] Is capable of Virt-IO drive hot unplug (no reboot required). This works only for non-Windows virtual Machines. Can only be updated.
        /// </summary>
        [Output("discVirtioHotUnplug")]
        public Output<bool> DiscVirtioHotUnplug { get; private set; } = null!;

        /// <summary>
        /// (Computed)[string] OS type of this Snapshot
        /// </summary>
        [Output("licenceType")]
        public Output<string> LicenceType { get; private set; } = null!;

        /// <summary>
        /// Location of that image/snapshot
        /// </summary>
        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// [string] The name of the snapshot.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// (Computed)[string] Is capable of nic hot plug (no reboot required). Can only be updated.
        /// </summary>
        [Output("nicHotPlug")]
        public Output<bool> NicHotPlug { get; private set; } = null!;

        /// <summary>
        /// (Computed)[string] Is capable of nic hot unplug (no reboot required). Can only be updated.
        /// </summary>
        [Output("nicHotUnplug")]
        public Output<bool> NicHotUnplug { get; private set; } = null!;

        /// <summary>
        /// (Computed)[string] Is capable of memory hot plug (no reboot required). Can only be updated.
        /// </summary>
        [Output("ramHotPlug")]
        public Output<bool> RamHotPlug { get; private set; } = null!;

        /// <summary>
        /// Is capable of memory hot unplug (no reboot required)
        /// </summary>
        [Output("ramHotUnplug")]
        public Output<bool> RamHotUnplug { get; private set; } = null!;

        /// <summary>
        /// Boolean value representing if the snapshot requires extra protection e.g. two factor protection
        /// </summary>
        [Output("secAuthProtection")]
        public Output<bool> SecAuthProtection { get; private set; } = null!;

        /// <summary>
        /// The size of the image in GB
        /// </summary>
        [Output("size")]
        public Output<int> Size { get; private set; } = null!;

        /// <summary>
        /// [string] The ID of the specific volume to take the snapshot from.
        /// </summary>
        [Output("volumeId")]
        public Output<string> VolumeId { get; private set; } = null!;


        /// <summary>
        /// Create a Snapshot resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Snapshot(string name, SnapshotArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:compute/snapshot:Snapshot", name, args ?? new SnapshotArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Snapshot(string name, Input<string> id, SnapshotState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:compute/snapshot:Snapshot", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Snapshot resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Snapshot Get(string name, Input<string> id, SnapshotState? state = null, CustomResourceOptions? options = null)
        {
            return new Snapshot(name, id, state, options);
        }
    }

    public sealed class SnapshotArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// (Computed)[string] Is capable of CPU hot plug (no reboot required). Can only be updated.
        /// </summary>
        [Input("cpuHotPlug")]
        public Input<bool>? CpuHotPlug { get; set; }

        /// <summary>
        /// [string] The ID of the Virtual Data Center.
        /// </summary>
        [Input("datacenterId", required: true)]
        public Input<string> DatacenterId { get; set; } = null!;

        /// <summary>
        /// (Computed)[string] Human readable description
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// (Computed)[string] Is capable of Virt-IO drive hot plug (no reboot required). Can only be updated.
        /// </summary>
        [Input("discVirtioHotPlug")]
        public Input<bool>? DiscVirtioHotPlug { get; set; }

        /// <summary>
        /// (Computed)[string] Is capable of Virt-IO drive hot unplug (no reboot required). This works only for non-Windows virtual Machines. Can only be updated.
        /// </summary>
        [Input("discVirtioHotUnplug")]
        public Input<bool>? DiscVirtioHotUnplug { get; set; }

        /// <summary>
        /// (Computed)[string] OS type of this Snapshot
        /// </summary>
        [Input("licenceType")]
        public Input<string>? LicenceType { get; set; }

        /// <summary>
        /// [string] The name of the snapshot.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// (Computed)[string] Is capable of nic hot plug (no reboot required). Can only be updated.
        /// </summary>
        [Input("nicHotPlug")]
        public Input<bool>? NicHotPlug { get; set; }

        /// <summary>
        /// (Computed)[string] Is capable of nic hot unplug (no reboot required). Can only be updated.
        /// </summary>
        [Input("nicHotUnplug")]
        public Input<bool>? NicHotUnplug { get; set; }

        /// <summary>
        /// (Computed)[string] Is capable of memory hot plug (no reboot required). Can only be updated.
        /// </summary>
        [Input("ramHotPlug")]
        public Input<bool>? RamHotPlug { get; set; }

        /// <summary>
        /// Boolean value representing if the snapshot requires extra protection e.g. two factor protection
        /// </summary>
        [Input("secAuthProtection")]
        public Input<bool>? SecAuthProtection { get; set; }

        /// <summary>
        /// [string] The ID of the specific volume to take the snapshot from.
        /// </summary>
        [Input("volumeId", required: true)]
        public Input<string> VolumeId { get; set; } = null!;

        public SnapshotArgs()
        {
        }
        public static new SnapshotArgs Empty => new SnapshotArgs();
    }

    public sealed class SnapshotState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// (Computed)[string] Is capable of CPU hot plug (no reboot required). Can only be updated.
        /// </summary>
        [Input("cpuHotPlug")]
        public Input<bool>? CpuHotPlug { get; set; }

        /// <summary>
        /// Is capable of CPU hot unplug (no reboot required)
        /// </summary>
        [Input("cpuHotUnplug")]
        public Input<bool>? CpuHotUnplug { get; set; }

        /// <summary>
        /// [string] The ID of the Virtual Data Center.
        /// </summary>
        [Input("datacenterId")]
        public Input<string>? DatacenterId { get; set; }

        /// <summary>
        /// (Computed)[string] Human readable description
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Is capable of SCSI drive hot plug (no reboot required)
        /// </summary>
        [Input("discScsiHotPlug")]
        public Input<bool>? DiscScsiHotPlug { get; set; }

        /// <summary>
        /// Is capable of SCSI drive hot unplug (no reboot required). This works only for non-Windows virtual Machines.
        /// </summary>
        [Input("discScsiHotUnplug")]
        public Input<bool>? DiscScsiHotUnplug { get; set; }

        /// <summary>
        /// (Computed)[string] Is capable of Virt-IO drive hot plug (no reboot required). Can only be updated.
        /// </summary>
        [Input("discVirtioHotPlug")]
        public Input<bool>? DiscVirtioHotPlug { get; set; }

        /// <summary>
        /// (Computed)[string] Is capable of Virt-IO drive hot unplug (no reboot required). This works only for non-Windows virtual Machines. Can only be updated.
        /// </summary>
        [Input("discVirtioHotUnplug")]
        public Input<bool>? DiscVirtioHotUnplug { get; set; }

        /// <summary>
        /// (Computed)[string] OS type of this Snapshot
        /// </summary>
        [Input("licenceType")]
        public Input<string>? LicenceType { get; set; }

        /// <summary>
        /// Location of that image/snapshot
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// [string] The name of the snapshot.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// (Computed)[string] Is capable of nic hot plug (no reboot required). Can only be updated.
        /// </summary>
        [Input("nicHotPlug")]
        public Input<bool>? NicHotPlug { get; set; }

        /// <summary>
        /// (Computed)[string] Is capable of nic hot unplug (no reboot required). Can only be updated.
        /// </summary>
        [Input("nicHotUnplug")]
        public Input<bool>? NicHotUnplug { get; set; }

        /// <summary>
        /// (Computed)[string] Is capable of memory hot plug (no reboot required). Can only be updated.
        /// </summary>
        [Input("ramHotPlug")]
        public Input<bool>? RamHotPlug { get; set; }

        /// <summary>
        /// Is capable of memory hot unplug (no reboot required)
        /// </summary>
        [Input("ramHotUnplug")]
        public Input<bool>? RamHotUnplug { get; set; }

        /// <summary>
        /// Boolean value representing if the snapshot requires extra protection e.g. two factor protection
        /// </summary>
        [Input("secAuthProtection")]
        public Input<bool>? SecAuthProtection { get; set; }

        /// <summary>
        /// The size of the image in GB
        /// </summary>
        [Input("size")]
        public Input<int>? Size { get; set; }

        /// <summary>
        /// [string] The ID of the specific volume to take the snapshot from.
        /// </summary>
        [Input("volumeId")]
        public Input<string>? VolumeId { get; set; }

        public SnapshotState()
        {
        }
        public static new SnapshotState Empty => new SnapshotState();
    }
}
