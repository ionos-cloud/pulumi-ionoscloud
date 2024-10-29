// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Manages the selection of a boot device for IonosCloud Servers.
 *
 * ## Example Usage
 *
 * The boot device of a `ionoscloud.compute.Server`, `ionoscloud.VcpuServer` or `ionoscloud.CubeServer` can be selected with this resource.
 * Deleting this resource will revert the boot device back to the default volume, which is the first inline volume created together with the server.
 * This resource also allows switching between a `volume` and a `ionoscloud.getImage` CDROM. Note that CDROM images are detached after they are no longer set as boot devices.
 *
 * ### Select an external volume
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const exampleServer = new ionoscloud.compute.Server("exampleServer", {
 *     availabilityZone: "ZONE_2",
 *     imageName: "ubuntu:latest",
 *     cores: 2,
 *     ram: 2048,
 *     imagePassword: random_password.server_image_password.result,
 *     datacenterId: ionoscloud_datacenter.example.id,
 *     volume: {
 *         name: "Inline Updated",
 *         size: 20,
 *         diskType: "SSD Standard",
 *         bus: "VIRTIO",
 *         availabilityZone: "AUTO",
 *     },
 *     nic: {
 *         lan: ionoscloud_lan.example.id,
 *         name: "Nic Example",
 *         dhcp: true,
 *         firewallActive: true,
 *     },
 * });
 * const exampleVolume = new ionoscloud.compute.Volume("exampleVolume", {
 *     serverId: exampleServer.id,
 *     datacenterId: ionoscloud_datacenter.example.id,
 *     size: 10,
 *     diskType: "HDD",
 *     availabilityZone: "AUTO",
 *     imageName: "debian:latest",
 *     imagePassword: random_password.server_image_password.result,
 * });
 * const exampleServerBootDeviceSelection = new ionoscloud.ServerBootDeviceSelection("exampleServerBootDeviceSelection", {
 *     datacenterId: ionoscloud_datacenter.example.id,
 *     serverId: exampleServer.id,
 *     bootDeviceId: exampleVolume.id,
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 *
 * ### Select an inline volume again
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const exampleServer = new ionoscloud.compute.Server("exampleServer", {
 *     availabilityZone: "ZONE_2",
 *     imageName: "ubuntu:latest",
 *     cores: 2,
 *     ram: 2048,
 *     imagePassword: random_password.server_image_password.result,
 *     datacenterId: ionoscloud_datacenter.example.id,
 *     volume: {
 *         name: "Inline Updated",
 *         size: 20,
 *         diskType: "SSD Standard",
 *         bus: "VIRTIO",
 *         availabilityZone: "AUTO",
 *     },
 *     nic: {
 *         lan: ionoscloud_lan.example.id,
 *         name: "Nic Example",
 *         dhcp: true,
 *         firewallActive: true,
 *     },
 * });
 * const exampleServerBootDeviceSelection = new ionoscloud.ServerBootDeviceSelection("exampleServerBootDeviceSelection", {
 *     datacenterId: ionoscloud_datacenter.example.id,
 *     serverId: exampleServer.id,
 *     bootDeviceId: exampleServer.inlineVolumeIds[0],
 * });
 * const exampleVolume = new ionoscloud.compute.Volume("exampleVolume", {
 *     serverId: exampleServer.id,
 *     datacenterId: ionoscloud_datacenter.example.id,
 *     size: 10,
 *     diskType: "HDD",
 *     availabilityZone: "AUTO",
 *     imageName: "debian:latest",
 *     imagePassword: random_password.server_image_password.result,
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 *
 * ### Select a CDROM image
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const exampleServer = new ionoscloud.compute.Server("exampleServer", {
 *     availabilityZone: "ZONE_2",
 *     imageName: "ubuntu:latest",
 *     cores: 2,
 *     ram: 2048,
 *     imagePassword: random_password.server_image_password.result,
 *     datacenterId: ionoscloud_datacenter.example.id,
 *     volume: {
 *         name: "Inline Updated",
 *         size: 20,
 *         diskType: "SSD Standard",
 *         bus: "VIRTIO",
 *         availabilityZone: "AUTO",
 *     },
 *     nic: {
 *         lan: ionoscloud_lan.example.id,
 *         name: "Nic Example",
 *         dhcp: true,
 *         firewallActive: true,
 *     },
 * });
 * const exampleImage = ionoscloud.getImage({
 *     name: "ubuntu-20.04",
 *     location: "de/txl",
 *     type: "CDROM",
 * });
 * const exampleServerBootDeviceSelection = new ionoscloud.ServerBootDeviceSelection("exampleServerBootDeviceSelection", {
 *     datacenterId: ionoscloud_datacenter.example.id,
 *     serverId: exampleServer.inlineVolumeIds[0],
 *     bootDeviceId: exampleImage.then(exampleImage => exampleImage.id),
 * });
 * const exampleVolume = new ionoscloud.compute.Volume("exampleVolume", {
 *     serverId: exampleServer.id,
 *     datacenterId: ionoscloud_datacenter.example.id,
 *     size: 10,
 *     diskType: "HDD",
 *     availabilityZone: "AUTO",
 *     imageName: "debian:latest",
 *     imagePassword: random_password.server_image_password.result,
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 *
 * ### Perform a network boot
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const exampleServer = new ionoscloud.compute.Server("exampleServer", {
 *     availabilityZone: "ZONE_2",
 *     imageName: "ubuntu:latest",
 *     cores: 2,
 *     ram: 2048,
 *     imagePassword: random_password.server_image_password.result,
 *     datacenterId: ionoscloud_datacenter.example.id,
 *     volume: {
 *         name: "Inline volume",
 *         size: 20,
 *         diskType: "SSD Standard",
 *         bus: "VIRTIO",
 *         availabilityZone: "AUTO",
 *     },
 *     nic: {
 *         lan: ionoscloud_lan.example.id,
 *         name: "Nic Example",
 *         dhcp: true,
 *         firewallActive: true,
 *     },
 * });
 * const exampleServerBootDeviceSelection = new ionoscloud.ServerBootDeviceSelection("exampleServerBootDeviceSelection", {
 *     datacenterId: ionoscloud_datacenter.example.id,
 *     serverId: exampleServer.inlineVolumeIds[0],
 * });
 * // boot_device_id = data.ionoscloud_image.example.id   VM will boot in the PXE shell when boot_device_id is omitted
 * const exampleVolume = new ionoscloud.compute.Volume("exampleVolume", {
 *     serverId: exampleServer.id,
 *     datacenterId: ionoscloud_datacenter.example.id,
 *     size: 10,
 *     diskType: "HDD",
 *     availabilityZone: "AUTO",
 *     imageName: "debian:latest",
 *     imagePassword: random_password.server_image_password.result,
 * });
 * const exampleImage = ionoscloud.getImage({
 *     name: "ubuntu-20.04",
 *     location: "de/txl",
 *     type: "CDROM",
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 */
export class ServerBootDeviceSelection extends pulumi.CustomResource {
    /**
     * Get an existing ServerBootDeviceSelection resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServerBootDeviceSelectionState, opts?: pulumi.CustomResourceOptions): ServerBootDeviceSelection {
        return new ServerBootDeviceSelection(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:index/serverBootDeviceSelection:ServerBootDeviceSelection';

    /**
     * Returns true if the given object is an instance of ServerBootDeviceSelection.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ServerBootDeviceSelection {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ServerBootDeviceSelection.__pulumiType;
    }

    /**
     * [string] The ID of a bootable device such as a volume or an image data source. If this field is omitted from the configuration, the VM will be restarted with no primary boot device, and it will enter the PXE shell for network booting. 
     * ***Note***: If the network booting process started by the PXE shell fails, the VM will still boot into the image of the attached storage as a fallback. This behavior imitates the "Boot from Network" option from [DCD](https://dcd.ionos.com/).
     */
    public readonly bootDeviceId!: pulumi.Output<string | undefined>;
    /**
     * [string] The ID of a Virtual Data Center.
     */
    public readonly datacenterId!: pulumi.Output<string>;
    /**
     * ID of the first attached volume of the Server, which will be the default boot volume.
     */
    public /*out*/ readonly defaultBootVolumeId!: pulumi.Output<string>;
    /**
     * [string] The ID of a server.
     */
    public readonly serverId!: pulumi.Output<string>;

    /**
     * Create a ServerBootDeviceSelection resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ServerBootDeviceSelectionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ServerBootDeviceSelectionArgs | ServerBootDeviceSelectionState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ServerBootDeviceSelectionState | undefined;
            resourceInputs["bootDeviceId"] = state ? state.bootDeviceId : undefined;
            resourceInputs["datacenterId"] = state ? state.datacenterId : undefined;
            resourceInputs["defaultBootVolumeId"] = state ? state.defaultBootVolumeId : undefined;
            resourceInputs["serverId"] = state ? state.serverId : undefined;
        } else {
            const args = argsOrState as ServerBootDeviceSelectionArgs | undefined;
            if ((!args || args.datacenterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'datacenterId'");
            }
            if ((!args || args.serverId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serverId'");
            }
            resourceInputs["bootDeviceId"] = args ? args.bootDeviceId : undefined;
            resourceInputs["datacenterId"] = args ? args.datacenterId : undefined;
            resourceInputs["serverId"] = args ? args.serverId : undefined;
            resourceInputs["defaultBootVolumeId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ServerBootDeviceSelection.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ServerBootDeviceSelection resources.
 */
export interface ServerBootDeviceSelectionState {
    /**
     * [string] The ID of a bootable device such as a volume or an image data source. If this field is omitted from the configuration, the VM will be restarted with no primary boot device, and it will enter the PXE shell for network booting. 
     * ***Note***: If the network booting process started by the PXE shell fails, the VM will still boot into the image of the attached storage as a fallback. This behavior imitates the "Boot from Network" option from [DCD](https://dcd.ionos.com/).
     */
    bootDeviceId?: pulumi.Input<string>;
    /**
     * [string] The ID of a Virtual Data Center.
     */
    datacenterId?: pulumi.Input<string>;
    /**
     * ID of the first attached volume of the Server, which will be the default boot volume.
     */
    defaultBootVolumeId?: pulumi.Input<string>;
    /**
     * [string] The ID of a server.
     */
    serverId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ServerBootDeviceSelection resource.
 */
export interface ServerBootDeviceSelectionArgs {
    /**
     * [string] The ID of a bootable device such as a volume or an image data source. If this field is omitted from the configuration, the VM will be restarted with no primary boot device, and it will enter the PXE shell for network booting. 
     * ***Note***: If the network booting process started by the PXE shell fails, the VM will still boot into the image of the attached storage as a fallback. This behavior imitates the "Boot from Network" option from [DCD](https://dcd.ionos.com/).
     */
    bootDeviceId?: pulumi.Input<string>;
    /**
     * [string] The ID of a Virtual Data Center.
     */
    datacenterId: pulumi.Input<string>;
    /**
     * [string] The ID of a server.
     */
    serverId: pulumi.Input<string>;
}
