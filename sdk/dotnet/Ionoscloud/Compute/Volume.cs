// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Compute
{
    /// <summary>
    /// Manages a **Volume** on IonosCloud.
    /// 
    /// ## Example Usage
    /// 
    /// A primary volume will be created with the server. If there is a need for additional volumes, this resource handles it.
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ionoscloud = Ionoscloud.Pulumi.Ionoscloud;
    /// using Ionoscloud = Pulumi.Ionoscloud;
    /// using Random = Pulumi.Random;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var example = Ionoscloud.Compute.GetImage.Invoke(new()
    ///     {
    ///         Type = "HDD",
    ///         CloudInit = "V1",
    ///         ImageAlias = "ubuntu:latest",
    ///         Location = "us/las",
    ///     });
    /// 
    ///     var exampleDatacenter = new Ionoscloud.Compute.Datacenter("example", new()
    ///     {
    ///         Name = "Datacenter Example",
    ///         Location = "us/las",
    ///         Description = "Datacenter Description",
    ///         SecAuthProtection = false,
    ///     });
    /// 
    ///     var exampleLan = new Ionoscloud.Compute.Lan("example", new()
    ///     {
    ///         DatacenterId = exampleDatacenter.Id,
    ///         Public = true,
    ///         Name = "Lan Example",
    ///     });
    /// 
    ///     var exampleIPBlock = new Ionoscloud.Compute.IPBlock("example", new()
    ///     {
    ///         Location = exampleDatacenter.Location,
    ///         Size = 4,
    ///         Name = "IP Block Example",
    ///     });
    /// 
    ///     var serverImagePassword = new Random.Index.Password("server_image_password", new()
    ///     {
    ///         Length = 16,
    ///         Special = false,
    ///     });
    /// 
    ///     var exampleServer = new Ionoscloud.Compute.Server("example", new()
    ///     {
    ///         Name = "Server Example",
    ///         DatacenterId = exampleDatacenter.Id,
    ///         Cores = 1,
    ///         Ram = 1024,
    ///         AvailabilityZone = "ZONE_1",
    ///         CpuFamily = "INTEL_XEON",
    ///         ImageName = example.Apply(getImageResult =&gt; getImageResult.Name),
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
    ///         Nic = new Ionoscloud.Compute.Inputs.ServerNicArgs
    ///         {
    ///             Lan = exampleLan.Id,
    ///             Name = "system",
    ///             Dhcp = true,
    ///             FirewallActive = true,
    ///             FirewallType = "BIDIRECTIONAL",
    ///             Ips = new[]
    ///             {
    ///                 exampleIPBlock.Ips.Apply(ips =&gt; ips[0]),
    ///                 exampleIPBlock.Ips.Apply(ips =&gt; ips[1]),
    ///             },
    ///             Firewalls = new[]
    ///             {
    ///                 new Ionoscloud.Compute.Inputs.ServerNicFirewallArgs
    ///                 {
    ///                     Protocol = "TCP",
    ///                     Name = "SSH",
    ///                     PortRangeStart = 22,
    ///                     PortRangeEnd = 22,
    ///                     SourceMac = "00:0a:95:9d:68:17",
    ///                     SourceIp = exampleIPBlock.Ips.Apply(ips =&gt; ips[2]),
    ///                     TargetIp = exampleIPBlock.Ips.Apply(ips =&gt; ips[3]),
    ///                     Type = "EGRESS",
    ///                 },
    ///             },
    ///         },
    ///     });
    /// 
    ///     var volumeImagePassword = new Random.Index.Password("volume_image_password", new()
    ///     {
    ///         Length = 16,
    ///         Special = false,
    ///     });
    /// 
    ///     var exampleVolume = new Ionoscloud.Compute.Volume("example", new()
    ///     {
    ///         DatacenterId = exampleDatacenter.Id,
    ///         ServerId = exampleServer.Id,
    ///         Name = "Volume Example",
    ///         AvailabilityZone = "ZONE_1",
    ///         Size = 5,
    ///         DiskType = "SSD Standard",
    ///         Bus = "VIRTIO",
    ///         ImageName = example.Apply(getImageResult =&gt; getImageResult.Name),
    ///         ImagePassword = volumeImagePassword.Result,
    ///         UserData = "foo",
    ///     });
    /// 
    ///     var example2 = new Ionoscloud.Compute.Volume("example2", new()
    ///     {
    ///         DatacenterId = exampleDatacenter.Id,
    ///         ServerId = exampleServer.Id,
    ///         Name = "Another Volume Example",
    ///         AvailabilityZone = "ZONE_1",
    ///         Size = 5,
    ///         DiskType = "SSD Standard",
    ///         Bus = "VIRTIO",
    ///         LicenceType = "OTHER",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// Resource Volume can be imported using the `resource id`, e.g.
    /// 
    /// ```sh
    /// $ pulumi import ionoscloud:compute/volume:Volume myvolume datacenter uuid/server uuid/volume uuid
    /// ```
    /// </summary>
    [IonoscloudResourceType("ionoscloud:compute/volume:Volume")]
    public partial class Volume : global::Pulumi.CustomResource
    {
        /// <summary>
        /// [string] The storage availability zone assigned to the volume: AUTO, ZONE_1, ZONE_2, or ZONE_3. This property is immutable
        /// </summary>
        [Output("availabilityZone")]
        public Output<string> AvailabilityZone { get; private set; } = null!;

        /// <summary>
        /// [string] The uuid of the Backup Unit that user has access to. The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either 'public image' or 'imageAlias' in conjunction with this property.
        /// </summary>
        [Output("backupUnitId")]
        public Output<string> BackupUnitId { get; private set; } = null!;

        /// <summary>
        /// [string] The UUID of the attached server.
        /// &gt; **⚠ WARNING**
        /// &gt;
        /// &gt; ssh_key_path and ssh_keys fields are immutable.
        /// &gt; If you want to create a **CUBE** server, the type of the inline volume must be set to **DAS**. In this case, you can not set the `size` argument since it is taken from the `template_uuid` you set in the server.
        /// </summary>
        [Output("bootServer")]
        public Output<string> BootServer { get; private set; } = null!;

        /// <summary>
        /// [Boolean] The bus type of the volume: VIRTIO or IDE.
        /// </summary>
        [Output("bus")]
        public Output<string> Bus { get; private set; } = null!;

        /// <summary>
        /// [string] Is capable of CPU hot plug (no reboot required)
        /// </summary>
        [Output("cpuHotPlug")]
        public Output<bool> CpuHotPlug { get; private set; } = null!;

        /// <summary>
        /// [string] The ID of a Virtual Data Center.
        /// </summary>
        [Output("datacenterId")]
        public Output<string> DatacenterId { get; private set; } = null!;

        /// <summary>
        /// The Logical Unit Number of the storage volume. Null for volumes not mounted to any VM.
        /// </summary>
        [Output("deviceNumber")]
        public Output<int> DeviceNumber { get; private set; } = null!;

        /// <summary>
        /// [string] Is capable of Virt-IO drive hot plug (no reboot required)
        /// </summary>
        [Output("discVirtioHotPlug")]
        public Output<bool> DiscVirtioHotPlug { get; private set; } = null!;

        /// <summary>
        /// [string] Is capable of Virt-IO drive hot unplug (no reboot required). This works only for non-Windows virtual Machines.
        /// </summary>
        [Output("discVirtioHotUnplug")]
        public Output<bool> DiscVirtioHotUnplug { get; private set; } = null!;

        /// <summary>
        /// [string] The volume type: HDD or SSD. This property is immutable.
        /// </summary>
        [Output("diskType")]
        public Output<string> DiskType { get; private set; } = null!;

        /// <summary>
        /// The image or snapshot UUID.
        /// </summary>
        [Output("image")]
        public Output<string> Image { get; private set; } = null!;

        [Output("imageId")]
        public Output<string> ImageId { get; private set; } = null!;

        /// <summary>
        /// [string] The name, ID or alias of the image. May also be a snapshot ID. It is required if `licence_type` is not provided. Attribute is immutable.
        /// </summary>
        [Output("imageName")]
        public Output<string?> ImageName { get; private set; } = null!;

        /// <summary>
        /// [string] Required if `sshkey_path` is not provided.
        /// </summary>
        [Output("imagePassword")]
        public Output<string?> ImagePassword { get; private set; } = null!;

        /// <summary>
        /// [string] Required if `image_name` is not provided.
        /// </summary>
        [Output("licenceType")]
        public Output<string> LicenceType { get; private set; } = null!;

        /// <summary>
        /// [string] The name of the volume.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// [string] Is capable of nic hot plug (no reboot required)
        /// </summary>
        [Output("nicHotPlug")]
        public Output<bool> NicHotPlug { get; private set; } = null!;

        /// <summary>
        /// [string] Is capable of nic hot unplug (no reboot required)
        /// </summary>
        [Output("nicHotUnplug")]
        public Output<bool> NicHotUnplug { get; private set; } = null!;

        /// <summary>
        /// The PCI slot number of the storage volume. Null for volumes not mounted to any VM.
        /// </summary>
        [Output("pciSlot")]
        public Output<int> PciSlot { get; private set; } = null!;

        /// <summary>
        /// [string] Is capable of memory hot plug (no reboot required)
        /// </summary>
        [Output("ramHotPlug")]
        public Output<bool> RamHotPlug { get; private set; } = null!;

        /// <summary>
        /// [string] The ID of a server.
        /// </summary>
        [Output("serverId")]
        public Output<string> ServerId { get; private set; } = null!;

        /// <summary>
        /// [integer] The size of the volume in GB.
        /// </summary>
        [Output("size")]
        public Output<int> Size { get; private set; } = null!;

        /// <summary>
        /// [list] List of absolute paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Required for IonosCloud Linux images. Required if `image_password` is not provided. This property is immutable.
        /// </summary>
        [Output("sshKeyPaths")]
        public Output<ImmutableArray<string>> SshKeyPaths { get; private set; } = null!;

        /// <summary>
        /// [list] List of absolute paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Required for IonosCloud Linux images. Required if `image_password` is not provided. This property is immutable.
        /// </summary>
        [Output("sshKeys")]
        public Output<ImmutableArray<string>> SshKeys { get; private set; } = null!;

        /// <summary>
        /// The associated public SSH key.
        /// </summary>
        [Output("sshkey")]
        public Output<string> Sshkey { get; private set; } = null!;

        /// <summary>
        /// [string] The cloud-init configuration for the volume as base64 encoded string. The property is immutable and is only allowed to be set on a new volume creation. This option will work only with cloud-init compatible images.
        /// </summary>
        [Output("userData")]
        public Output<string> UserData { get; private set; } = null!;


        /// <summary>
        /// Create a Volume resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Volume(string name, VolumeArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:compute/volume:Volume", name, args ?? new VolumeArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Volume(string name, Input<string> id, VolumeState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:compute/volume:Volume", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Volume resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Volume Get(string name, Input<string> id, VolumeState? state = null, CustomResourceOptions? options = null)
        {
            return new Volume(name, id, state, options);
        }
    }

    public sealed class VolumeArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] The storage availability zone assigned to the volume: AUTO, ZONE_1, ZONE_2, or ZONE_3. This property is immutable
        /// </summary>
        [Input("availabilityZone")]
        public Input<string>? AvailabilityZone { get; set; }

        /// <summary>
        /// [string] The uuid of the Backup Unit that user has access to. The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either 'public image' or 'imageAlias' in conjunction with this property.
        /// </summary>
        [Input("backupUnitId")]
        public Input<string>? BackupUnitId { get; set; }

        /// <summary>
        /// [Boolean] The bus type of the volume: VIRTIO or IDE.
        /// </summary>
        [Input("bus")]
        public Input<string>? Bus { get; set; }

        /// <summary>
        /// [string] The ID of a Virtual Data Center.
        /// </summary>
        [Input("datacenterId", required: true)]
        public Input<string> DatacenterId { get; set; } = null!;

        /// <summary>
        /// [string] The volume type: HDD or SSD. This property is immutable.
        /// </summary>
        [Input("diskType", required: true)]
        public Input<string> DiskType { get; set; } = null!;

        /// <summary>
        /// [string] The name, ID or alias of the image. May also be a snapshot ID. It is required if `licence_type` is not provided. Attribute is immutable.
        /// </summary>
        [Input("imageName")]
        public Input<string>? ImageName { get; set; }

        /// <summary>
        /// [string] Required if `sshkey_path` is not provided.
        /// </summary>
        [Input("imagePassword")]
        public Input<string>? ImagePassword { get; set; }

        /// <summary>
        /// [string] Required if `image_name` is not provided.
        /// </summary>
        [Input("licenceType")]
        public Input<string>? LicenceType { get; set; }

        /// <summary>
        /// [string] The name of the volume.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// [string] The ID of a server.
        /// </summary>
        [Input("serverId", required: true)]
        public Input<string> ServerId { get; set; } = null!;

        /// <summary>
        /// [integer] The size of the volume in GB.
        /// </summary>
        [Input("size", required: true)]
        public Input<int> Size { get; set; } = null!;

        [Input("sshKeyPaths")]
        private InputList<string>? _sshKeyPaths;

        /// <summary>
        /// [list] List of absolute paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Required for IonosCloud Linux images. Required if `image_password` is not provided. This property is immutable.
        /// </summary>
        public InputList<string> SshKeyPaths
        {
            get => _sshKeyPaths ?? (_sshKeyPaths = new InputList<string>());
            set => _sshKeyPaths = value;
        }

        [Input("sshKeys")]
        private InputList<string>? _sshKeys;

        /// <summary>
        /// [list] List of absolute paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Required for IonosCloud Linux images. Required if `image_password` is not provided. This property is immutable.
        /// </summary>
        public InputList<string> SshKeys
        {
            get => _sshKeys ?? (_sshKeys = new InputList<string>());
            set => _sshKeys = value;
        }

        /// <summary>
        /// [string] The cloud-init configuration for the volume as base64 encoded string. The property is immutable and is only allowed to be set on a new volume creation. This option will work only with cloud-init compatible images.
        /// </summary>
        [Input("userData")]
        public Input<string>? UserData { get; set; }

        public VolumeArgs()
        {
        }
        public static new VolumeArgs Empty => new VolumeArgs();
    }

    public sealed class VolumeState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] The storage availability zone assigned to the volume: AUTO, ZONE_1, ZONE_2, or ZONE_3. This property is immutable
        /// </summary>
        [Input("availabilityZone")]
        public Input<string>? AvailabilityZone { get; set; }

        /// <summary>
        /// [string] The uuid of the Backup Unit that user has access to. The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either 'public image' or 'imageAlias' in conjunction with this property.
        /// </summary>
        [Input("backupUnitId")]
        public Input<string>? BackupUnitId { get; set; }

        /// <summary>
        /// [string] The UUID of the attached server.
        /// &gt; **⚠ WARNING**
        /// &gt;
        /// &gt; ssh_key_path and ssh_keys fields are immutable.
        /// &gt; If you want to create a **CUBE** server, the type of the inline volume must be set to **DAS**. In this case, you can not set the `size` argument since it is taken from the `template_uuid` you set in the server.
        /// </summary>
        [Input("bootServer")]
        public Input<string>? BootServer { get; set; }

        /// <summary>
        /// [Boolean] The bus type of the volume: VIRTIO or IDE.
        /// </summary>
        [Input("bus")]
        public Input<string>? Bus { get; set; }

        /// <summary>
        /// [string] Is capable of CPU hot plug (no reboot required)
        /// </summary>
        [Input("cpuHotPlug")]
        public Input<bool>? CpuHotPlug { get; set; }

        /// <summary>
        /// [string] The ID of a Virtual Data Center.
        /// </summary>
        [Input("datacenterId")]
        public Input<string>? DatacenterId { get; set; }

        /// <summary>
        /// The Logical Unit Number of the storage volume. Null for volumes not mounted to any VM.
        /// </summary>
        [Input("deviceNumber")]
        public Input<int>? DeviceNumber { get; set; }

        /// <summary>
        /// [string] Is capable of Virt-IO drive hot plug (no reboot required)
        /// </summary>
        [Input("discVirtioHotPlug")]
        public Input<bool>? DiscVirtioHotPlug { get; set; }

        /// <summary>
        /// [string] Is capable of Virt-IO drive hot unplug (no reboot required). This works only for non-Windows virtual Machines.
        /// </summary>
        [Input("discVirtioHotUnplug")]
        public Input<bool>? DiscVirtioHotUnplug { get; set; }

        /// <summary>
        /// [string] The volume type: HDD or SSD. This property is immutable.
        /// </summary>
        [Input("diskType")]
        public Input<string>? DiskType { get; set; }

        /// <summary>
        /// The image or snapshot UUID.
        /// </summary>
        [Input("image")]
        public Input<string>? Image { get; set; }

        [Input("imageId")]
        public Input<string>? ImageId { get; set; }

        /// <summary>
        /// [string] The name, ID or alias of the image. May also be a snapshot ID. It is required if `licence_type` is not provided. Attribute is immutable.
        /// </summary>
        [Input("imageName")]
        public Input<string>? ImageName { get; set; }

        /// <summary>
        /// [string] Required if `sshkey_path` is not provided.
        /// </summary>
        [Input("imagePassword")]
        public Input<string>? ImagePassword { get; set; }

        /// <summary>
        /// [string] Required if `image_name` is not provided.
        /// </summary>
        [Input("licenceType")]
        public Input<string>? LicenceType { get; set; }

        /// <summary>
        /// [string] The name of the volume.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// [string] Is capable of nic hot plug (no reboot required)
        /// </summary>
        [Input("nicHotPlug")]
        public Input<bool>? NicHotPlug { get; set; }

        /// <summary>
        /// [string] Is capable of nic hot unplug (no reboot required)
        /// </summary>
        [Input("nicHotUnplug")]
        public Input<bool>? NicHotUnplug { get; set; }

        /// <summary>
        /// The PCI slot number of the storage volume. Null for volumes not mounted to any VM.
        /// </summary>
        [Input("pciSlot")]
        public Input<int>? PciSlot { get; set; }

        /// <summary>
        /// [string] Is capable of memory hot plug (no reboot required)
        /// </summary>
        [Input("ramHotPlug")]
        public Input<bool>? RamHotPlug { get; set; }

        /// <summary>
        /// [string] The ID of a server.
        /// </summary>
        [Input("serverId")]
        public Input<string>? ServerId { get; set; }

        /// <summary>
        /// [integer] The size of the volume in GB.
        /// </summary>
        [Input("size")]
        public Input<int>? Size { get; set; }

        [Input("sshKeyPaths")]
        private InputList<string>? _sshKeyPaths;

        /// <summary>
        /// [list] List of absolute paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Required for IonosCloud Linux images. Required if `image_password` is not provided. This property is immutable.
        /// </summary>
        public InputList<string> SshKeyPaths
        {
            get => _sshKeyPaths ?? (_sshKeyPaths = new InputList<string>());
            set => _sshKeyPaths = value;
        }

        [Input("sshKeys")]
        private InputList<string>? _sshKeys;

        /// <summary>
        /// [list] List of absolute paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Required for IonosCloud Linux images. Required if `image_password` is not provided. This property is immutable.
        /// </summary>
        public InputList<string> SshKeys
        {
            get => _sshKeys ?? (_sshKeys = new InputList<string>());
            set => _sshKeys = value;
        }

        /// <summary>
        /// The associated public SSH key.
        /// </summary>
        [Input("sshkey")]
        public Input<string>? Sshkey { get; set; }

        /// <summary>
        /// [string] The cloud-init configuration for the volume as base64 encoded string. The property is immutable and is only allowed to be set on a new volume creation. This option will work only with cloud-init compatible images.
        /// </summary>
        [Input("userData")]
        public Input<string>? UserData { get; set; }

        public VolumeState()
        {
        }
        public static new VolumeState Empty => new VolumeState();
    }
}
