// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Inputs
{

    public sealed class AutoscalingGroupReplicaConfigurationVolumeArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] The uuid of the Backup Unit that user has access to. The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either `public image` or `imageAlias` in conjunction with this property.
        /// </summary>
        [Input("backupUnitId")]
        public Input<string>? BackupUnitId { get; set; }

        /// <summary>
        /// [string] Determines whether the volume will be used as a boot volume. Set to NONE, the volume will not be used as boot volume. Set to PRIMARY, the volume will be used as boot volume and set to AUTO will delegate the decision to the provisioning engine to decide whether to use the volume as boot volume.
        /// Notice that exactly one volume can be set to PRIMARY or all of them set to AUTO.
        /// </summary>
        [Input("bootOrder", required: true)]
        public Input<string> BootOrder { get; set; } = null!;

        /// <summary>
        /// [string] The bus type of the volume. Default setting is `VIRTIO`. The bus type `IDE` is also supported.
        /// </summary>
        [Input("bus")]
        public Input<string>? Bus { get; set; }

        /// <summary>
        /// [string] The image installed on the volume. Only the UUID of the image is presently supported.
        /// </summary>
        [Input("image")]
        public Input<string>? Image { get; set; }

        /// <summary>
        /// [string] The image installed on the volume. Must be an `imageAlias` as specified via the images API. Note that one of `image` or `imageAlias` must be set, but not both.
        /// </summary>
        [Input("imageAlias")]
        public Input<string>? ImageAlias { get; set; }

        [Input("imagePassword")]
        private Input<string>? _imagePassword;

        /// <summary>
        /// [string] Image password for this replica volume.
        /// </summary>
        public Input<string>? ImagePassword
        {
            get => _imagePassword;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _imagePassword = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// [string] Name for this replica volume.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// [int] Name for this replica volume.
        /// </summary>
        [Input("size", required: true)]
        public Input<int> Size { get; set; } = null!;

        [Input("sshKeys")]
        private InputList<string>? _sshKeys;

        /// <summary>
        /// List of ssh keys, supports values or paths to files. Cannot be changed at update.
        /// </summary>
        public InputList<string> SshKeys
        {
            get => _sshKeys ?? (_sshKeys = new InputList<string>());
            set => _sshKeys = value;
        }

        /// <summary>
        /// [string] Storage Type for this replica volume. Possible values: `SSD`, `HDD`, `SSD_STANDARD` or `SSD_PREMIUM`.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        /// <summary>
        /// [string] User-data (Cloud Init) for this replica volume. Make sure you provide a Cloud Init compatible image in conjunction with this parameter.
        /// </summary>
        [Input("userData")]
        public Input<string>? UserData { get; set; }

        public AutoscalingGroupReplicaConfigurationVolumeArgs()
        {
        }
        public static new AutoscalingGroupReplicaConfigurationVolumeArgs Empty => new AutoscalingGroupReplicaConfigurationVolumeArgs();
    }
}
