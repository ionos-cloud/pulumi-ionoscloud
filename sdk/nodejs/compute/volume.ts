// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a **Volume** on IonosCloud.
 *
 * ## Import
 *
 * Resource Volume can be imported using the `resource id`, e.g.
 *
 * ```sh
 * $ pulumi import ionoscloud:compute/volume:Volume myvolume {datacenter uuid}/{server uuid}/{volume uuid}
 * ```
 */
export class Volume extends pulumi.CustomResource {
    /**
     * Get an existing Volume resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VolumeState, opts?: pulumi.CustomResourceOptions): Volume {
        return new Volume(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:compute/volume:Volume';

    /**
     * Returns true if the given object is an instance of Volume.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Volume {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Volume.__pulumiType;
    }

    /**
     * [string] The storage availability zone assigned to the volume: AUTO, ZONE_1, ZONE_2, or ZONE_3. This property is immutable
     */
    public readonly availabilityZone!: pulumi.Output<string>;
    /**
     * [string] The uuid of the Backup Unit that user has access to. The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either 'public image' or 'imageAlias' in conjunction with this property.
     */
    public readonly backupUnitId!: pulumi.Output<string>;
    /**
     * [string] The UUID of the attached server.
     * > **⚠ WARNING**
     * >
     * > sshKeyPath and sshKeys fields are immutable.
     * > If you want to create a **CUBE** server, the type of the inline volume must be set to **DAS**. In this case, you can not set the `size` argument since it is taken from the `templateUuid` you set in the server.
     */
    public /*out*/ readonly bootServer!: pulumi.Output<string>;
    /**
     * [Boolean] The bus type of the volume: VIRTIO or IDE.
     */
    public readonly bus!: pulumi.Output<string>;
    /**
     * [string] Is capable of CPU hot plug (no reboot required)
     */
    public /*out*/ readonly cpuHotPlug!: pulumi.Output<boolean>;
    /**
     * [string] The ID of a Virtual Data Center.
     */
    public readonly datacenterId!: pulumi.Output<string>;
    /**
     * The Logical Unit Number of the storage volume. Null for volumes not mounted to any VM.
     */
    public /*out*/ readonly deviceNumber!: pulumi.Output<number>;
    /**
     * [string] Is capable of Virt-IO drive hot plug (no reboot required)
     */
    public /*out*/ readonly discVirtioHotPlug!: pulumi.Output<boolean>;
    /**
     * [string] Is capable of Virt-IO drive hot unplug (no reboot required). This works only for non-Windows virtual Machines.
     */
    public /*out*/ readonly discVirtioHotUnplug!: pulumi.Output<boolean>;
    /**
     * [string] The volume type: HDD or SSD. This property is immutable.
     */
    public readonly diskType!: pulumi.Output<string>;
    /**
     * The image or snapshot UUID.
     */
    public /*out*/ readonly image!: pulumi.Output<string>;
    public /*out*/ readonly imageId!: pulumi.Output<string>;
    /**
     * [string] The name, ID or alias of the image. May also be a snapshot ID. It is required if `licenceType` is not provided. Attribute is immutable.
     */
    public readonly imageName!: pulumi.Output<string | undefined>;
    /**
     * [string] Required if `sshkeyPath` is not provided.
     */
    public readonly imagePassword!: pulumi.Output<string | undefined>;
    /**
     * [string] Required if `imageName` is not provided.
     */
    public readonly licenceType!: pulumi.Output<string>;
    /**
     * [string] The name of the volume.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * [string] Is capable of nic hot plug (no reboot required)
     */
    public /*out*/ readonly nicHotPlug!: pulumi.Output<boolean>;
    /**
     * [string] Is capable of nic hot unplug (no reboot required)
     */
    public /*out*/ readonly nicHotUnplug!: pulumi.Output<boolean>;
    /**
     * The PCI slot number of the storage volume. Null for volumes not mounted to any VM.
     */
    public /*out*/ readonly pciSlot!: pulumi.Output<number>;
    /**
     * [string] Is capable of memory hot plug (no reboot required)
     */
    public /*out*/ readonly ramHotPlug!: pulumi.Output<boolean>;
    /**
     * [string] The ID of a server.
     */
    public readonly serverId!: pulumi.Output<string>;
    /**
     * [integer] The size of the volume in GB.
     */
    public readonly size!: pulumi.Output<number>;
    /**
     * [list] List of absolute paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Required for IonosCloud Linux images. Required if `imagePassword` is not provided. This property is immutable.
     */
    public readonly sshKeyPaths!: pulumi.Output<string[] | undefined>;
    /**
     * [list] List of absolute paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Required for IonosCloud Linux images. Required if `imagePassword` is not provided. This property is immutable.
     */
    public readonly sshKeys!: pulumi.Output<string[] | undefined>;
    /**
     * The associated public SSH key.
     */
    public /*out*/ readonly sshkey!: pulumi.Output<string>;
    /**
     * [string] The cloud-init configuration for the volume as base64 encoded string. The property is immutable and is only allowed to be set on a new volume creation. This option will work only with cloud-init compatible images.
     */
    public readonly userData!: pulumi.Output<string>;

    /**
     * Create a Volume resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VolumeArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: VolumeArgs | VolumeState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as VolumeState | undefined;
            resourceInputs["availabilityZone"] = state ? state.availabilityZone : undefined;
            resourceInputs["backupUnitId"] = state ? state.backupUnitId : undefined;
            resourceInputs["bootServer"] = state ? state.bootServer : undefined;
            resourceInputs["bus"] = state ? state.bus : undefined;
            resourceInputs["cpuHotPlug"] = state ? state.cpuHotPlug : undefined;
            resourceInputs["datacenterId"] = state ? state.datacenterId : undefined;
            resourceInputs["deviceNumber"] = state ? state.deviceNumber : undefined;
            resourceInputs["discVirtioHotPlug"] = state ? state.discVirtioHotPlug : undefined;
            resourceInputs["discVirtioHotUnplug"] = state ? state.discVirtioHotUnplug : undefined;
            resourceInputs["diskType"] = state ? state.diskType : undefined;
            resourceInputs["image"] = state ? state.image : undefined;
            resourceInputs["imageId"] = state ? state.imageId : undefined;
            resourceInputs["imageName"] = state ? state.imageName : undefined;
            resourceInputs["imagePassword"] = state ? state.imagePassword : undefined;
            resourceInputs["licenceType"] = state ? state.licenceType : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["nicHotPlug"] = state ? state.nicHotPlug : undefined;
            resourceInputs["nicHotUnplug"] = state ? state.nicHotUnplug : undefined;
            resourceInputs["pciSlot"] = state ? state.pciSlot : undefined;
            resourceInputs["ramHotPlug"] = state ? state.ramHotPlug : undefined;
            resourceInputs["serverId"] = state ? state.serverId : undefined;
            resourceInputs["size"] = state ? state.size : undefined;
            resourceInputs["sshKeyPaths"] = state ? state.sshKeyPaths : undefined;
            resourceInputs["sshKeys"] = state ? state.sshKeys : undefined;
            resourceInputs["sshkey"] = state ? state.sshkey : undefined;
            resourceInputs["userData"] = state ? state.userData : undefined;
        } else {
            const args = argsOrState as VolumeArgs | undefined;
            if ((!args || args.datacenterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'datacenterId'");
            }
            if ((!args || args.diskType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'diskType'");
            }
            if ((!args || args.serverId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serverId'");
            }
            if ((!args || args.size === undefined) && !opts.urn) {
                throw new Error("Missing required property 'size'");
            }
            resourceInputs["availabilityZone"] = args ? args.availabilityZone : undefined;
            resourceInputs["backupUnitId"] = args ? args.backupUnitId : undefined;
            resourceInputs["bus"] = args ? args.bus : undefined;
            resourceInputs["datacenterId"] = args ? args.datacenterId : undefined;
            resourceInputs["diskType"] = args ? args.diskType : undefined;
            resourceInputs["imageName"] = args ? args.imageName : undefined;
            resourceInputs["imagePassword"] = args ? args.imagePassword : undefined;
            resourceInputs["licenceType"] = args ? args.licenceType : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["serverId"] = args ? args.serverId : undefined;
            resourceInputs["size"] = args ? args.size : undefined;
            resourceInputs["sshKeyPaths"] = args ? args.sshKeyPaths : undefined;
            resourceInputs["sshKeys"] = args ? args.sshKeys : undefined;
            resourceInputs["userData"] = args ? args.userData : undefined;
            resourceInputs["bootServer"] = undefined /*out*/;
            resourceInputs["cpuHotPlug"] = undefined /*out*/;
            resourceInputs["deviceNumber"] = undefined /*out*/;
            resourceInputs["discVirtioHotPlug"] = undefined /*out*/;
            resourceInputs["discVirtioHotUnplug"] = undefined /*out*/;
            resourceInputs["image"] = undefined /*out*/;
            resourceInputs["imageId"] = undefined /*out*/;
            resourceInputs["nicHotPlug"] = undefined /*out*/;
            resourceInputs["nicHotUnplug"] = undefined /*out*/;
            resourceInputs["pciSlot"] = undefined /*out*/;
            resourceInputs["ramHotPlug"] = undefined /*out*/;
            resourceInputs["sshkey"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Volume.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Volume resources.
 */
export interface VolumeState {
    /**
     * [string] The storage availability zone assigned to the volume: AUTO, ZONE_1, ZONE_2, or ZONE_3. This property is immutable
     */
    availabilityZone?: pulumi.Input<string>;
    /**
     * [string] The uuid of the Backup Unit that user has access to. The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either 'public image' or 'imageAlias' in conjunction with this property.
     */
    backupUnitId?: pulumi.Input<string>;
    /**
     * [string] The UUID of the attached server.
     * > **⚠ WARNING**
     * >
     * > sshKeyPath and sshKeys fields are immutable.
     * > If you want to create a **CUBE** server, the type of the inline volume must be set to **DAS**. In this case, you can not set the `size` argument since it is taken from the `templateUuid` you set in the server.
     */
    bootServer?: pulumi.Input<string>;
    /**
     * [Boolean] The bus type of the volume: VIRTIO or IDE.
     */
    bus?: pulumi.Input<string>;
    /**
     * [string] Is capable of CPU hot plug (no reboot required)
     */
    cpuHotPlug?: pulumi.Input<boolean>;
    /**
     * [string] The ID of a Virtual Data Center.
     */
    datacenterId?: pulumi.Input<string>;
    /**
     * The Logical Unit Number of the storage volume. Null for volumes not mounted to any VM.
     */
    deviceNumber?: pulumi.Input<number>;
    /**
     * [string] Is capable of Virt-IO drive hot plug (no reboot required)
     */
    discVirtioHotPlug?: pulumi.Input<boolean>;
    /**
     * [string] Is capable of Virt-IO drive hot unplug (no reboot required). This works only for non-Windows virtual Machines.
     */
    discVirtioHotUnplug?: pulumi.Input<boolean>;
    /**
     * [string] The volume type: HDD or SSD. This property is immutable.
     */
    diskType?: pulumi.Input<string>;
    /**
     * The image or snapshot UUID.
     */
    image?: pulumi.Input<string>;
    imageId?: pulumi.Input<string>;
    /**
     * [string] The name, ID or alias of the image. May also be a snapshot ID. It is required if `licenceType` is not provided. Attribute is immutable.
     */
    imageName?: pulumi.Input<string>;
    /**
     * [string] Required if `sshkeyPath` is not provided.
     */
    imagePassword?: pulumi.Input<string>;
    /**
     * [string] Required if `imageName` is not provided.
     */
    licenceType?: pulumi.Input<string>;
    /**
     * [string] The name of the volume.
     */
    name?: pulumi.Input<string>;
    /**
     * [string] Is capable of nic hot plug (no reboot required)
     */
    nicHotPlug?: pulumi.Input<boolean>;
    /**
     * [string] Is capable of nic hot unplug (no reboot required)
     */
    nicHotUnplug?: pulumi.Input<boolean>;
    /**
     * The PCI slot number of the storage volume. Null for volumes not mounted to any VM.
     */
    pciSlot?: pulumi.Input<number>;
    /**
     * [string] Is capable of memory hot plug (no reboot required)
     */
    ramHotPlug?: pulumi.Input<boolean>;
    /**
     * [string] The ID of a server.
     */
    serverId?: pulumi.Input<string>;
    /**
     * [integer] The size of the volume in GB.
     */
    size?: pulumi.Input<number>;
    /**
     * [list] List of absolute paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Required for IonosCloud Linux images. Required if `imagePassword` is not provided. This property is immutable.
     */
    sshKeyPaths?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [list] List of absolute paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Required for IonosCloud Linux images. Required if `imagePassword` is not provided. This property is immutable.
     */
    sshKeys?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The associated public SSH key.
     */
    sshkey?: pulumi.Input<string>;
    /**
     * [string] The cloud-init configuration for the volume as base64 encoded string. The property is immutable and is only allowed to be set on a new volume creation. This option will work only with cloud-init compatible images.
     */
    userData?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Volume resource.
 */
export interface VolumeArgs {
    /**
     * [string] The storage availability zone assigned to the volume: AUTO, ZONE_1, ZONE_2, or ZONE_3. This property is immutable
     */
    availabilityZone?: pulumi.Input<string>;
    /**
     * [string] The uuid of the Backup Unit that user has access to. The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either 'public image' or 'imageAlias' in conjunction with this property.
     */
    backupUnitId?: pulumi.Input<string>;
    /**
     * [Boolean] The bus type of the volume: VIRTIO or IDE.
     */
    bus?: pulumi.Input<string>;
    /**
     * [string] The ID of a Virtual Data Center.
     */
    datacenterId: pulumi.Input<string>;
    /**
     * [string] The volume type: HDD or SSD. This property is immutable.
     */
    diskType: pulumi.Input<string>;
    /**
     * [string] The name, ID or alias of the image. May also be a snapshot ID. It is required if `licenceType` is not provided. Attribute is immutable.
     */
    imageName?: pulumi.Input<string>;
    /**
     * [string] Required if `sshkeyPath` is not provided.
     */
    imagePassword?: pulumi.Input<string>;
    /**
     * [string] Required if `imageName` is not provided.
     */
    licenceType?: pulumi.Input<string>;
    /**
     * [string] The name of the volume.
     */
    name?: pulumi.Input<string>;
    /**
     * [string] The ID of a server.
     */
    serverId: pulumi.Input<string>;
    /**
     * [integer] The size of the volume in GB.
     */
    size: pulumi.Input<number>;
    /**
     * [list] List of absolute paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Required for IonosCloud Linux images. Required if `imagePassword` is not provided. This property is immutable.
     */
    sshKeyPaths?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [list] List of absolute paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Required for IonosCloud Linux images. Required if `imagePassword` is not provided. This property is immutable.
     */
    sshKeys?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [string] The cloud-init configuration for the volume as base64 encoded string. The property is immutable and is only allowed to be set on a new volume creation. This option will work only with cloud-init compatible images.
     */
    userData?: pulumi.Input<string>;
}
