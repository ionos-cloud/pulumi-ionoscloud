// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Compute.Inputs
{

    public sealed class CubeServerVolumeArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] The availability zone in which the server should exist. This property is immutable.
        /// </summary>
        [Input("availabilityZone")]
        public Input<string>? AvailabilityZone { get; set; }

        /// <summary>
        /// The uuid of the Backup Unit that user has access to. The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either 'public image' or 'imageAlias' in conjunction with this property.
        /// </summary>
        [Input("backupUnitId")]
        public Input<string>? BackupUnitId { get; set; }

        /// <summary>
        /// The UUID of the attached server.
        /// </summary>
        [Input("bootServer")]
        public Input<string>? BootServer { get; set; }

        [Input("bus")]
        public Input<string>? Bus { get; set; }

        [Input("cpuHotPlug")]
        public Input<bool>? CpuHotPlug { get; set; }

        [Input("deviceNumber")]
        public Input<int>? DeviceNumber { get; set; }

        [Input("discVirtioHotPlug")]
        public Input<bool>? DiscVirtioHotPlug { get; set; }

        [Input("discVirtioHotUnplug")]
        public Input<bool>? DiscVirtioHotUnplug { get; set; }

        [Input("diskType", required: true)]
        public Input<string> DiskType { get; set; } = null!;

        /// <summary>
        /// [string] Required if `ssh_key_path` is not provided.
        /// </summary>
        [Input("imagePassword")]
        public Input<string>? ImagePassword { get; set; }

        /// <summary>
        /// [string] Sets the OS type of the server.
        /// </summary>
        [Input("licenceType")]
        public Input<string>? LicenceType { get; set; }

        /// <summary>
        /// [string] The name of the server.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("nicHotPlug")]
        public Input<bool>? NicHotPlug { get; set; }

        [Input("nicHotUnplug")]
        public Input<bool>? NicHotUnplug { get; set; }

        [Input("pciSlot")]
        public Input<int>? PciSlot { get; set; }

        [Input("ramHotPlug")]
        public Input<bool>? RamHotPlug { get; set; }

        [Input("sshKeyPaths")]
        private InputList<string>? _sshKeyPaths;

        /// <summary>
        /// [list] List of paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images. Required for IonosCloud Linux images. Required if `image_password` is not provided.
        /// </summary>
        [Obsolete(@"Please use ssh_key_path under server level")]
        public InputList<string> SshKeyPaths
        {
            get => _sshKeyPaths ?? (_sshKeyPaths = new InputList<string>());
            set => _sshKeyPaths = value;
        }

        /// <summary>
        /// The cloud-init configuration for the volume as base64 encoded string. The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either 'public image' or 'imageAlias' that has cloud-init compatibility in conjunction with this property.
        /// </summary>
        [Input("userData")]
        public Input<string>? UserData { get; set; }

        public CubeServerVolumeArgs()
        {
        }
        public static new CubeServerVolumeArgs Empty => new CubeServerVolumeArgs();
    }
}
