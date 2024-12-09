// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Outputs
{

    [OutputType]
    public sealed class GetServerVolumeResult
    {
        /// <summary>
        /// The availability zone in which the volume should exist
        /// </summary>
        public readonly string AvailabilityZone;
        /// <summary>
        /// The uuid of the Backup Unit that user has access to
        /// </summary>
        public readonly string BackupUnitId;
        /// <summary>
        /// The UUID of the attached server.
        /// </summary>
        public readonly string BootServer;
        /// <summary>
        /// The bus type of the volume
        /// </summary>
        public readonly string Bus;
        /// <summary>
        /// Is capable of CPU hot plug (no reboot required)
        /// </summary>
        public readonly bool CpuHotPlug;
        /// <summary>
        /// The Logical Unit Number (LUN) of the storage volume
        /// </summary>
        public readonly int DeviceNumber;
        /// <summary>
        /// Is capable of Virt-IO drive hot plug (no reboot required)
        /// </summary>
        public readonly bool DiscVirtioHotPlug;
        /// <summary>
        /// Is capable of Virt-IO drive hot unplug (no reboot required)
        /// </summary>
        public readonly bool DiscVirtioHotUnplug;
        /// <summary>
        /// ID of the server you want to search for.
        /// 
        /// `datacenter_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
        /// </summary>
        public readonly string Id;
        public readonly string ImageName;
        /// <summary>
        /// Initial password to be set for installed OS
        /// </summary>
        public readonly string ImagePassword;
        /// <summary>
        /// OS type of this volume
        /// </summary>
        public readonly string LicenceType;
        /// <summary>
        /// Name of an existing server that you want to search for.
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
        /// The PCI slot number of the Nic
        /// </summary>
        public readonly int PciSlot;
        /// <summary>
        /// Is capable of memory hot plug (no reboot required)
        /// </summary>
        public readonly bool RamHotPlug;
        /// <summary>
        /// The size of the volume in GB
        /// </summary>
        public readonly int Size;
        /// <summary>
        /// Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key
        /// </summary>
        public readonly ImmutableArray<string> SshKeys;
        /// <summary>
        /// The type of firewall rule
        /// </summary>
        public readonly string Type;
        /// <summary>
        /// The cloud-init configuration for the volume as base64 encoded string
        /// </summary>
        public readonly string? UserData;

        [OutputConstructor]
        private GetServerVolumeResult(
            string availabilityZone,

            string backupUnitId,

            string bootServer,

            string bus,

            bool cpuHotPlug,

            int deviceNumber,

            bool discVirtioHotPlug,

            bool discVirtioHotUnplug,

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

            string type,

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
            Type = type;
            UserData = userData;
        }
    }
}
