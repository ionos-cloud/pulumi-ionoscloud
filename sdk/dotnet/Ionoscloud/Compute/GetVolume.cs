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
    public static class GetVolume
    {
        /// <summary>
        /// The volume data source can be used to search for and return existing volumes.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ### By ID
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Compute.GetVolume.Invoke(new()
        ///     {
        ///         DatacenterId = "datacenter_id",
        ///         Id = "volume_id",
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
        ///     var example = Ionoscloud.Compute.GetVolume.Invoke(new()
        ///     {
        ///         DatacenterId = "datacenter_id",
        ///         Name = "Volume Example",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetVolumeResult> InvokeAsync(GetVolumeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetVolumeResult>("ionoscloud:compute/getVolume:getVolume", args ?? new GetVolumeArgs(), options.WithDefaults());

        /// <summary>
        /// The volume data source can be used to search for and return existing volumes.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ### By ID
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Compute.GetVolume.Invoke(new()
        ///     {
        ///         DatacenterId = "datacenter_id",
        ///         Id = "volume_id",
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
        ///     var example = Ionoscloud.Compute.GetVolume.Invoke(new()
        ///     {
        ///         DatacenterId = "datacenter_id",
        ///         Name = "Volume Example",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetVolumeResult> Invoke(GetVolumeInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetVolumeResult>("ionoscloud:compute/getVolume:getVolume", args ?? new GetVolumeInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The volume data source can be used to search for and return existing volumes.
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// 
        /// ### By ID
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Ionoscloud.Compute.GetVolume.Invoke(new()
        ///     {
        ///         DatacenterId = "datacenter_id",
        ///         Id = "volume_id",
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
        ///     var example = Ionoscloud.Compute.GetVolume.Invoke(new()
        ///     {
        ///         DatacenterId = "datacenter_id",
        ///         Name = "Volume Example",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetVolumeResult> Invoke(GetVolumeInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetVolumeResult>("ionoscloud:compute/getVolume:getVolume", args ?? new GetVolumeInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetVolumeArgs : global::Pulumi.InvokeArgs
    {
        [Input("datacenterId", required: true)]
        public string DatacenterId { get; set; } = null!;

        /// <summary>
        /// ID of the volume you want to search for.
        /// 
        /// Either `volume` or `id` must be provided. If none, or both are provided, the datasource will return an error.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// Name of an existing volume that you want to search for.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        public GetVolumeArgs()
        {
        }
        public static new GetVolumeArgs Empty => new GetVolumeArgs();
    }

    public sealed class GetVolumeInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("datacenterId", required: true)]
        public Input<string> DatacenterId { get; set; } = null!;

        /// <summary>
        /// ID of the volume you want to search for.
        /// 
        /// Either `volume` or `id` must be provided. If none, or both are provided, the datasource will return an error.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Name of an existing volume that you want to search for.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public GetVolumeInvokeArgs()
        {
        }
        public static new GetVolumeInvokeArgs Empty => new GetVolumeInvokeArgs();
    }


    [OutputType]
    public sealed class GetVolumeResult
    {
        /// <summary>
        /// The storage availability zone assigned to the volume: AUTO, ZONE_1, ZONE_2, or ZONE_3. This property is immutable.
        /// </summary>
        public readonly string AvailabilityZone;
        /// <summary>
        /// The uuid of the Backup Unit that user has access to. The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either 'public image' or 'imageAlias' in conjunction with this property.
        /// </summary>
        public readonly string BackupUnitId;
        /// <summary>
        /// The UUID of the attached server.
        /// </summary>
        public readonly string BootServer;
        /// <summary>
        /// The bus type of the volume: VIRTIO or IDE.
        /// </summary>
        public readonly string Bus;
        /// <summary>
        /// Is capable of CPU hot plug (no reboot required)
        /// </summary>
        public readonly bool CpuHotPlug;
        public readonly string DatacenterId;
        /// <summary>
        /// The LUN ID of the storage volume. Null for volumes not mounted to any VM
        /// </summary>
        public readonly int DeviceNumber;
        /// <summary>
        /// Is capable of Virt-IO drive hot plug (no reboot required)
        /// </summary>
        public readonly bool DiscVirtioHotPlug;
        /// <summary>
        /// Is capable of Virt-IO drive hot unplug (no reboot required). This works only for non-Windows virtual Machines.
        /// </summary>
        public readonly bool DiscVirtioHotUnplug;
        /// <summary>
        /// The volume type: HDD or SSD.
        /// </summary>
        public readonly string DiskType;
        /// <summary>
        /// The id of the volume.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The image or snapshot UUID.
        /// </summary>
        public readonly string Image;
        /// <summary>
        /// Required if `sshkey_path` is not provided.
        /// </summary>
        public readonly string ImagePassword;
        /// <summary>
        /// The type of the licence.
        /// </summary>
        public readonly string LicenceType;
        /// <summary>
        /// The name of the volume.
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
        /// The size of the volume in GB.
        /// </summary>
        public readonly int Size;
        /// <summary>
        /// The associated public SSH key.
        /// </summary>
        public readonly string Sshkey;
        /// <summary>
        /// The cloud-init configuration for the volume as base64 encoded string. The property is immutable and is only allowed to be set on a new volume creation. This option will work only with cloud-init compatible images.
        /// </summary>
        public readonly string UserData;

        [OutputConstructor]
        private GetVolumeResult(
            string availabilityZone,

            string backupUnitId,

            string bootServer,

            string bus,

            bool cpuHotPlug,

            string datacenterId,

            int deviceNumber,

            bool discVirtioHotPlug,

            bool discVirtioHotUnplug,

            string diskType,

            string id,

            string image,

            string imagePassword,

            string licenceType,

            string name,

            bool nicHotPlug,

            bool nicHotUnplug,

            bool ramHotPlug,

            int size,

            string sshkey,

            string userData)
        {
            AvailabilityZone = availabilityZone;
            BackupUnitId = backupUnitId;
            BootServer = bootServer;
            Bus = bus;
            CpuHotPlug = cpuHotPlug;
            DatacenterId = datacenterId;
            DeviceNumber = deviceNumber;
            DiscVirtioHotPlug = discVirtioHotPlug;
            DiscVirtioHotUnplug = discVirtioHotUnplug;
            DiskType = diskType;
            Id = id;
            Image = image;
            ImagePassword = imagePassword;
            LicenceType = licenceType;
            Name = name;
            NicHotPlug = nicHotPlug;
            NicHotUnplug = nicHotUnplug;
            RamHotPlug = ramHotPlug;
            Size = size;
            Sshkey = sshkey;
            UserData = userData;
        }
    }
}
