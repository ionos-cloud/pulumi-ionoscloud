// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Compute.Outputs
{

    [OutputType]
    public sealed class GetServersServerVolumeResult
    {
        public readonly string AvailabilityZone;
        public readonly string BackupUnitId;
        /// <summary>
        /// The UUID of the attached server.
        /// </summary>
        public readonly string BootServer;
        public readonly string Bus;
        public readonly bool CpuHotPlug;
        public readonly int DeviceNumber;
        public readonly bool DiscVirtioHotPlug;
        public readonly bool DiscVirtioHotUnplug;
        public readonly string DiskType;
        public readonly string Id;
        public readonly string ImageName;
        public readonly string ImagePassword;
        public readonly string LicenceType;
        public readonly string Name;
        public readonly bool NicHotPlug;
        public readonly bool NicHotUnplug;
        public readonly int PciSlot;
        public readonly bool RamHotPlug;
        public readonly int Size;
        public readonly ImmutableArray<string> SshKeys;
        public readonly string? UserData;

        [OutputConstructor]
        private GetServersServerVolumeResult(
            string availabilityZone,

            string backupUnitId,

            string bootServer,

            string bus,

            bool cpuHotPlug,

            int deviceNumber,

            bool discVirtioHotPlug,

            bool discVirtioHotUnplug,

            string diskType,

            string id,

            string imageName,

            string imagePassword,

            string licenceType,

            string name,

            bool nicHotPlug,

            bool nicHotUnplug,

            int pciSlot,

            bool ramHotPlug,

            int size,

            ImmutableArray<string> sshKeys,

            string? userData)
        {
            AvailabilityZone = availabilityZone;
            BackupUnitId = backupUnitId;
            BootServer = bootServer;
            Bus = bus;
            CpuHotPlug = cpuHotPlug;
            DeviceNumber = deviceNumber;
            DiscVirtioHotPlug = discVirtioHotPlug;
            DiscVirtioHotUnplug = discVirtioHotUnplug;
            DiskType = diskType;
            Id = id;
            ImageName = imageName;
            ImagePassword = imagePassword;
            LicenceType = licenceType;
            Name = name;
            NicHotPlug = nicHotPlug;
            NicHotUnplug = nicHotUnplug;
            PciSlot = pciSlot;
            RamHotPlug = ramHotPlug;
            Size = size;
            SshKeys = sshKeys;
            UserData = userData;
        }
    }
}
