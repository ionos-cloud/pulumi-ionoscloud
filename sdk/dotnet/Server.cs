// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    /// <summary>
    /// ## Import
    /// 
    /// Resource Server can be imported using the `resource id` and the `datacenter id`, e.g.. Passing only resource id and datacenter id means that the first nic found linked to the server will be attached to it.
    /// 
    /// ```sh
    /// $ pulumi import ionoscloud:index/server:Server myserver {datacenter uuid}/{server uuid}
    /// ```
    /// 
    /// Optionally, you can pass `primary_nic` and `firewallrule_id` so terraform will know to import also the first nic and firewall rule (if it exists on the server):
    /// 
    /// ```sh
    /// $ pulumi import ionoscloud:index/server:Server myserver {datacenter uuid}/{server uuid}/{primary nic id}/{firewall rule id}
    /// ```
    /// </summary>
    [IonoscloudResourceType("ionoscloud:index/server:Server")]
    public partial class Server : global::Pulumi.CustomResource
    {
        /// <summary>
        /// [string] The availability zone in which the server should exist. E.g: `AUTO`, `ZONE_1`, `ZONE_2`. This property is immutable.
        /// </summary>
        [Output("availabilityZone")]
        public Output<string> AvailabilityZone { get; private set; } = null!;

        /// <summary>
        /// ***DEPRECATED*** Please refer to ionoscloud.ServerBootDeviceSelection (Optional)(Computed)[string] The associated boot drive, if any. Must be the UUID of a bootable CDROM image that can be retrieved using the ionoscloud.getImage data source.
        /// </summary>
        [Output("bootCdrom")]
        public Output<string> BootCdrom { get; private set; } = null!;

        /// <summary>
        /// [string] The image or snapshot UUID / name. May also be an image alias. It is required if `licence_type` is not provided.
        /// </summary>
        [Output("bootImage")]
        public Output<string> BootImage { get; private set; } = null!;

        /// <summary>
        /// The associated boot volume.
        /// </summary>
        [Output("bootVolume")]
        public Output<string> BootVolume { get; private set; } = null!;

        /// <summary>
        /// (Computed)[integer] Number of server CPU cores.
        /// </summary>
        [Output("cores")]
        public Output<int> Cores { get; private set; } = null!;

        /// <summary>
        /// [string] CPU architecture on which server gets provisioned; not all CPU architectures are available in all datacenter regions; available CPU architectures can be retrieved from the datacenter resource. E.g.: "INTEL_SKYLAKE" or "INTEL_XEON".
        /// </summary>
        [Output("cpuFamily")]
        public Output<string> CpuFamily { get; private set; } = null!;

        /// <summary>
        /// [string] The ID of a Virtual Data Center.
        /// </summary>
        [Output("datacenterId")]
        public Output<string> DatacenterId { get; private set; } = null!;

        /// <summary>
        /// The associated firewall rule.
        /// </summary>
        [Output("firewallruleId")]
        public Output<string> FirewallruleId { get; private set; } = null!;

        /// <summary>
        /// The associated firewall rules.
        /// </summary>
        [Output("firewallruleIds")]
        public Output<ImmutableArray<string>> FirewallruleIds { get; private set; } = null!;

        /// <summary>
        /// [string] The name, ID or alias of the image. May also be a snapshot ID. It is required if `licence_type` is not provided. Attribute is immutable.
        /// </summary>
        [Output("imageName")]
        public Output<string> ImageName { get; private set; } = null!;

        /// <summary>
        /// [string] Required if `ssh_key_path` is not provided.
        /// </summary>
        [Output("imagePassword")]
        public Output<string> ImagePassword { get; private set; } = null!;

        /// <summary>
        /// A list with the IDs for the volumes that are defined inside the server resource.
        /// 
        /// &gt; **⚠ WARNING**
        /// &gt;
        /// &gt; Image_name under volume level is deprecated, please use image_name under server level
        /// &gt; ssh_key_path and ssh_keys fields are immutable.
        /// 
        /// 
        /// &gt; **⚠ WARNING**
        /// &gt;
        /// &gt; If you want to create a **CUBE** server, you have to provide the `template_uuid`. In this case you can not set `cores`, `ram` and `volume.size` arguments, these being mutually exclusive with `template_uuid`.
        /// &gt;
        /// &gt; In all the other cases (**ENTERPRISE** servers) you have to provide values for `cores`, `ram` and `volume size`.
        /// </summary>
        [Output("inlineVolumeIds")]
        public Output<ImmutableArray<string>> InlineVolumeIds { get; private set; } = null!;

        /// <summary>
        /// [set] A label can be seen as an object with only two required fields: `key` and `value`, both of the `string` type. Please check the example presented above to see how a `label` can be used in the plan. A server can have multiple labels.
        /// </summary>
        [Output("labels")]
        public Output<ImmutableArray<Outputs.ServerLabel>> Labels { get; private set; } = null!;

        /// <summary>
        /// [string] The name of the server.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// See the Nic section.
        /// </summary>
        [Output("nic")]
        public Output<Outputs.ServerNic?> Nic { get; private set; } = null!;

        /// <summary>
        /// The associated IP address.
        /// </summary>
        [Output("primaryIp")]
        public Output<string> PrimaryIp { get; private set; } = null!;

        /// <summary>
        /// The associated NIC.
        /// </summary>
        [Output("primaryNic")]
        public Output<string> PrimaryNic { get; private set; } = null!;

        /// <summary>
        /// (Computed)[integer] The amount of memory for the server in MB.
        /// </summary>
        [Output("ram")]
        public Output<int> Ram { get; private set; } = null!;

        /// <summary>
        /// [list] List of absolute paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images.  Also accepts ssh keys directly. Required for IonosCloud Linux images. Required if `image_password` is not provided. Does not support `~` expansion to homedir in the given path. This property is immutable.
        /// </summary>
        [Output("sshKeyPaths")]
        public Output<ImmutableArray<string>> SshKeyPaths { get; private set; } = null!;

        /// <summary>
        /// [list] Immutable List of absolute or relative paths to files containing public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation. Does not support `~` expansion to homedir in the given path.
        /// </summary>
        [Output("sshKeys")]
        public Output<ImmutableArray<string>> SshKeys { get; private set; } = null!;

        /// <summary>
        /// [string] The UUID of the template for creating a CUBE server; the available templates for CUBE servers can be found on the templates resource
        /// </summary>
        [Output("templateUuid")]
        public Output<string?> TemplateUuid { get; private set; } = null!;

        /// <summary>
        /// (Computed)[string] Server usages: [ENTERPRISE](https://docs.ionos.com/cloud/compute-engine/virtual-servers/virtual-servers) or [CUBE](https://docs.ionos.com/cloud/compute-engine/virtual-servers/cloud-cubes). This property is immutable.
        /// </summary>
        [Output("type")]
        public Output<string> Type { get; private set; } = null!;

        /// <summary>
        /// [string] Sets the power state of the server. E.g: `RUNNING`, `SHUTOFF` or `SUSPENDED`. SUSPENDED state is only valid for cube. SHUTOFF state is only valid for enterprise.
        /// </summary>
        [Output("vmState")]
        public Output<string> VmState { get; private set; } = null!;

        /// <summary>
        /// See the Volume section.
        /// </summary>
        [Output("volume")]
        public Output<Outputs.ServerVolume> Volume { get; private set; } = null!;


        /// <summary>
        /// Create a Server resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Server(string name, ServerArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:index/server:Server", name, args ?? new ServerArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Server(string name, Input<string> id, ServerState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:index/server:Server", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "https://github.com/ionos-cloud/pulumi-ionoscloud/",
                AdditionalSecretOutputs =
                {
                    "imagePassword",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Server resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Server Get(string name, Input<string> id, ServerState? state = null, CustomResourceOptions? options = null)
        {
            return new Server(name, id, state, options);
        }
    }

    public sealed class ServerArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] The availability zone in which the server should exist. E.g: `AUTO`, `ZONE_1`, `ZONE_2`. This property is immutable.
        /// </summary>
        [Input("availabilityZone")]
        public Input<string>? AvailabilityZone { get; set; }

        /// <summary>
        /// ***DEPRECATED*** Please refer to ionoscloud.ServerBootDeviceSelection (Optional)(Computed)[string] The associated boot drive, if any. Must be the UUID of a bootable CDROM image that can be retrieved using the ionoscloud.getImage data source.
        /// </summary>
        [Input("bootCdrom")]
        public Input<string>? BootCdrom { get; set; }

        /// <summary>
        /// [string] The image or snapshot UUID / name. May also be an image alias. It is required if `licence_type` is not provided.
        /// </summary>
        [Input("bootImage")]
        public Input<string>? BootImage { get; set; }

        /// <summary>
        /// (Computed)[integer] Number of server CPU cores.
        /// </summary>
        [Input("cores")]
        public Input<int>? Cores { get; set; }

        /// <summary>
        /// [string] CPU architecture on which server gets provisioned; not all CPU architectures are available in all datacenter regions; available CPU architectures can be retrieved from the datacenter resource. E.g.: "INTEL_SKYLAKE" or "INTEL_XEON".
        /// </summary>
        [Input("cpuFamily")]
        public Input<string>? CpuFamily { get; set; }

        /// <summary>
        /// [string] The ID of a Virtual Data Center.
        /// </summary>
        [Input("datacenterId", required: true)]
        public Input<string> DatacenterId { get; set; } = null!;

        [Input("firewallruleIds")]
        private InputList<string>? _firewallruleIds;

        /// <summary>
        /// The associated firewall rules.
        /// </summary>
        public InputList<string> FirewallruleIds
        {
            get => _firewallruleIds ?? (_firewallruleIds = new InputList<string>());
            set => _firewallruleIds = value;
        }

        /// <summary>
        /// [string] The name, ID or alias of the image. May also be a snapshot ID. It is required if `licence_type` is not provided. Attribute is immutable.
        /// </summary>
        [Input("imageName")]
        public Input<string>? ImageName { get; set; }

        [Input("imagePassword")]
        private Input<string>? _imagePassword;

        /// <summary>
        /// [string] Required if `ssh_key_path` is not provided.
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

        [Input("labels")]
        private InputList<Inputs.ServerLabelArgs>? _labels;

        /// <summary>
        /// [set] A label can be seen as an object with only two required fields: `key` and `value`, both of the `string` type. Please check the example presented above to see how a `label` can be used in the plan. A server can have multiple labels.
        /// </summary>
        public InputList<Inputs.ServerLabelArgs> Labels
        {
            get => _labels ?? (_labels = new InputList<Inputs.ServerLabelArgs>());
            set => _labels = value;
        }

        /// <summary>
        /// [string] The name of the server.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// See the Nic section.
        /// </summary>
        [Input("nic")]
        public Input<Inputs.ServerNicArgs>? Nic { get; set; }

        /// <summary>
        /// (Computed)[integer] The amount of memory for the server in MB.
        /// </summary>
        [Input("ram")]
        public Input<int>? Ram { get; set; }

        [Input("sshKeyPaths")]
        private InputList<string>? _sshKeyPaths;

        /// <summary>
        /// [list] List of absolute paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images.  Also accepts ssh keys directly. Required for IonosCloud Linux images. Required if `image_password` is not provided. Does not support `~` expansion to homedir in the given path. This property is immutable.
        /// </summary>
        [Obsolete(@"Will be renamed to ssh_keys in the future, to allow users to set both the ssh key path or directly the ssh key")]
        public InputList<string> SshKeyPaths
        {
            get => _sshKeyPaths ?? (_sshKeyPaths = new InputList<string>());
            set => _sshKeyPaths = value;
        }

        [Input("sshKeys")]
        private InputList<string>? _sshKeys;

        /// <summary>
        /// [list] Immutable List of absolute or relative paths to files containing public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation. Does not support `~` expansion to homedir in the given path.
        /// </summary>
        public InputList<string> SshKeys
        {
            get => _sshKeys ?? (_sshKeys = new InputList<string>());
            set => _sshKeys = value;
        }

        /// <summary>
        /// [string] The UUID of the template for creating a CUBE server; the available templates for CUBE servers can be found on the templates resource
        /// </summary>
        [Input("templateUuid")]
        public Input<string>? TemplateUuid { get; set; }

        /// <summary>
        /// (Computed)[string] Server usages: [ENTERPRISE](https://docs.ionos.com/cloud/compute-engine/virtual-servers/virtual-servers) or [CUBE](https://docs.ionos.com/cloud/compute-engine/virtual-servers/cloud-cubes). This property is immutable.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        /// <summary>
        /// [string] Sets the power state of the server. E.g: `RUNNING`, `SHUTOFF` or `SUSPENDED`. SUSPENDED state is only valid for cube. SHUTOFF state is only valid for enterprise.
        /// </summary>
        [Input("vmState")]
        public Input<string>? VmState { get; set; }

        /// <summary>
        /// See the Volume section.
        /// </summary>
        [Input("volume", required: true)]
        public Input<Inputs.ServerVolumeArgs> Volume { get; set; } = null!;

        public ServerArgs()
        {
        }
        public static new ServerArgs Empty => new ServerArgs();
    }

    public sealed class ServerState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] The availability zone in which the server should exist. E.g: `AUTO`, `ZONE_1`, `ZONE_2`. This property is immutable.
        /// </summary>
        [Input("availabilityZone")]
        public Input<string>? AvailabilityZone { get; set; }

        /// <summary>
        /// ***DEPRECATED*** Please refer to ionoscloud.ServerBootDeviceSelection (Optional)(Computed)[string] The associated boot drive, if any. Must be the UUID of a bootable CDROM image that can be retrieved using the ionoscloud.getImage data source.
        /// </summary>
        [Input("bootCdrom")]
        public Input<string>? BootCdrom { get; set; }

        /// <summary>
        /// [string] The image or snapshot UUID / name. May also be an image alias. It is required if `licence_type` is not provided.
        /// </summary>
        [Input("bootImage")]
        public Input<string>? BootImage { get; set; }

        /// <summary>
        /// The associated boot volume.
        /// </summary>
        [Input("bootVolume")]
        public Input<string>? BootVolume { get; set; }

        /// <summary>
        /// (Computed)[integer] Number of server CPU cores.
        /// </summary>
        [Input("cores")]
        public Input<int>? Cores { get; set; }

        /// <summary>
        /// [string] CPU architecture on which server gets provisioned; not all CPU architectures are available in all datacenter regions; available CPU architectures can be retrieved from the datacenter resource. E.g.: "INTEL_SKYLAKE" or "INTEL_XEON".
        /// </summary>
        [Input("cpuFamily")]
        public Input<string>? CpuFamily { get; set; }

        /// <summary>
        /// [string] The ID of a Virtual Data Center.
        /// </summary>
        [Input("datacenterId")]
        public Input<string>? DatacenterId { get; set; }

        /// <summary>
        /// The associated firewall rule.
        /// </summary>
        [Input("firewallruleId")]
        public Input<string>? FirewallruleId { get; set; }

        [Input("firewallruleIds")]
        private InputList<string>? _firewallruleIds;

        /// <summary>
        /// The associated firewall rules.
        /// </summary>
        public InputList<string> FirewallruleIds
        {
            get => _firewallruleIds ?? (_firewallruleIds = new InputList<string>());
            set => _firewallruleIds = value;
        }

        /// <summary>
        /// [string] The name, ID or alias of the image. May also be a snapshot ID. It is required if `licence_type` is not provided. Attribute is immutable.
        /// </summary>
        [Input("imageName")]
        public Input<string>? ImageName { get; set; }

        [Input("imagePassword")]
        private Input<string>? _imagePassword;

        /// <summary>
        /// [string] Required if `ssh_key_path` is not provided.
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

        [Input("inlineVolumeIds")]
        private InputList<string>? _inlineVolumeIds;

        /// <summary>
        /// A list with the IDs for the volumes that are defined inside the server resource.
        /// 
        /// &gt; **⚠ WARNING**
        /// &gt;
        /// &gt; Image_name under volume level is deprecated, please use image_name under server level
        /// &gt; ssh_key_path and ssh_keys fields are immutable.
        /// 
        /// 
        /// &gt; **⚠ WARNING**
        /// &gt;
        /// &gt; If you want to create a **CUBE** server, you have to provide the `template_uuid`. In this case you can not set `cores`, `ram` and `volume.size` arguments, these being mutually exclusive with `template_uuid`.
        /// &gt;
        /// &gt; In all the other cases (**ENTERPRISE** servers) you have to provide values for `cores`, `ram` and `volume size`.
        /// </summary>
        public InputList<string> InlineVolumeIds
        {
            get => _inlineVolumeIds ?? (_inlineVolumeIds = new InputList<string>());
            set => _inlineVolumeIds = value;
        }

        [Input("labels")]
        private InputList<Inputs.ServerLabelGetArgs>? _labels;

        /// <summary>
        /// [set] A label can be seen as an object with only two required fields: `key` and `value`, both of the `string` type. Please check the example presented above to see how a `label` can be used in the plan. A server can have multiple labels.
        /// </summary>
        public InputList<Inputs.ServerLabelGetArgs> Labels
        {
            get => _labels ?? (_labels = new InputList<Inputs.ServerLabelGetArgs>());
            set => _labels = value;
        }

        /// <summary>
        /// [string] The name of the server.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// See the Nic section.
        /// </summary>
        [Input("nic")]
        public Input<Inputs.ServerNicGetArgs>? Nic { get; set; }

        /// <summary>
        /// The associated IP address.
        /// </summary>
        [Input("primaryIp")]
        public Input<string>? PrimaryIp { get; set; }

        /// <summary>
        /// The associated NIC.
        /// </summary>
        [Input("primaryNic")]
        public Input<string>? PrimaryNic { get; set; }

        /// <summary>
        /// (Computed)[integer] The amount of memory for the server in MB.
        /// </summary>
        [Input("ram")]
        public Input<int>? Ram { get; set; }

        [Input("sshKeyPaths")]
        private InputList<string>? _sshKeyPaths;

        /// <summary>
        /// [list] List of absolute paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images.  Also accepts ssh keys directly. Required for IonosCloud Linux images. Required if `image_password` is not provided. Does not support `~` expansion to homedir in the given path. This property is immutable.
        /// </summary>
        [Obsolete(@"Will be renamed to ssh_keys in the future, to allow users to set both the ssh key path or directly the ssh key")]
        public InputList<string> SshKeyPaths
        {
            get => _sshKeyPaths ?? (_sshKeyPaths = new InputList<string>());
            set => _sshKeyPaths = value;
        }

        [Input("sshKeys")]
        private InputList<string>? _sshKeys;

        /// <summary>
        /// [list] Immutable List of absolute or relative paths to files containing public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation. Does not support `~` expansion to homedir in the given path.
        /// </summary>
        public InputList<string> SshKeys
        {
            get => _sshKeys ?? (_sshKeys = new InputList<string>());
            set => _sshKeys = value;
        }

        /// <summary>
        /// [string] The UUID of the template for creating a CUBE server; the available templates for CUBE servers can be found on the templates resource
        /// </summary>
        [Input("templateUuid")]
        public Input<string>? TemplateUuid { get; set; }

        /// <summary>
        /// (Computed)[string] Server usages: [ENTERPRISE](https://docs.ionos.com/cloud/compute-engine/virtual-servers/virtual-servers) or [CUBE](https://docs.ionos.com/cloud/compute-engine/virtual-servers/cloud-cubes). This property is immutable.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        /// <summary>
        /// [string] Sets the power state of the server. E.g: `RUNNING`, `SHUTOFF` or `SUSPENDED`. SUSPENDED state is only valid for cube. SHUTOFF state is only valid for enterprise.
        /// </summary>
        [Input("vmState")]
        public Input<string>? VmState { get; set; }

        /// <summary>
        /// See the Volume section.
        /// </summary>
        [Input("volume")]
        public Input<Inputs.ServerVolumeGetArgs>? Volume { get; set; }

        public ServerState()
        {
        }
        public static new ServerState Empty => new ServerState();
    }
}
