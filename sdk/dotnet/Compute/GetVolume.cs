// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Compute
{
    public static class GetVolume
    {
        public static Task<GetVolumeResult> InvokeAsync(GetVolumeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetVolumeResult>("ionoscloud:compute/getVolume:getVolume", args ?? new GetVolumeArgs(), options.WithDefaults());

        public static Output<GetVolumeResult> Invoke(GetVolumeInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetVolumeResult>("ionoscloud:compute/getVolume:getVolume", args ?? new GetVolumeInvokeArgs(), options.WithDefaults());

        public static Output<GetVolumeResult> Invoke(GetVolumeInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetVolumeResult>("ionoscloud:compute/getVolume:getVolume", args ?? new GetVolumeInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetVolumeArgs : global::Pulumi.InvokeArgs
    {
        [Input("datacenterId", required: true)]
        public string DatacenterId { get; set; } = null!;

        [Input("id")]
        public string? Id { get; set; }

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

        [Input("id")]
        public Input<string>? Id { get; set; }

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
        public readonly string AvailabilityZone;
        public readonly string BackupUnitId;
        public readonly string BootServer;
        public readonly string Bus;
        public readonly bool CpuHotPlug;
        public readonly string DatacenterId;
        public readonly int DeviceNumber;
        public readonly bool DiscVirtioHotPlug;
        public readonly bool DiscVirtioHotUnplug;
        public readonly string DiskType;
        public readonly string? Id;
        public readonly string Image;
        public readonly string ImagePassword;
        public readonly string LicenceType;
        public readonly string? Name;
        public readonly bool NicHotPlug;
        public readonly bool NicHotUnplug;
        public readonly bool RamHotPlug;
        public readonly int Size;
        public readonly string Sshkey;
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

            string? id,

            string image,

            string imagePassword,

            string licenceType,

            string? name,

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
