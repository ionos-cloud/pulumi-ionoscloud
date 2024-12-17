// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Manages a **Cube Server** on IonosCloud.
 *
 * ## Example Usage
 *
 * This resource will create an operational server. After this section completes, the provisioner can be called.
 *
 * ### CUBE Server
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 * import * as random from "@pulumi/random";
 *
 * const exampleTemplate = ionoscloud.getTemplate({
 *     name: "CUBES XS",
 * });
 * const exampleDatacenter = new ionoscloud.compute.Datacenter("exampleDatacenter", {location: "de/txl"});
 * const exampleLan = new ionoscloud.compute.Lan("exampleLan", {
 *     datacenterId: exampleDatacenter.id,
 *     "public": true,
 * });
 * const serverImagePassword = new random.RandomPassword("serverImagePassword", {
 *     length: 16,
 *     special: false,
 * });
 * const exampleCubeServer = new ionoscloud.compute.CubeServer("exampleCubeServer", {
 *     availabilityZone: "ZONE_2",
 *     imageName: "ubuntu:latest",
 *     templateUuid: exampleTemplate.then(exampleTemplate => exampleTemplate.id),
 *     imagePassword: serverImagePassword.result,
 *     datacenterId: exampleDatacenter.id,
 *     volume: {
 *         name: "Volume Example",
 *         licenceType: "LINUX",
 *         diskType: "DAS",
 *     },
 *     nic: {
 *         lan: exampleLan.id,
 *         name: "Nic Example",
 *         dhcp: true,
 *         firewallActive: true,
 *     },
 * });
 * ```
 *
 * ## Import
 *
 * Resource Server can be imported using the `resource id` and the `datacenter id`, e.g.
 *
 * ```sh
 * $ pulumi import ionoscloud:compute/cubeServer:CubeServer myserver {datacenter uuid}/{server uuid}
 * ```
 */
export class CubeServer extends pulumi.CustomResource {
    /**
     * Get an existing CubeServer resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CubeServerState, opts?: pulumi.CustomResourceOptions): CubeServer {
        return new CubeServer(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:compute/cubeServer:CubeServer';

    /**
     * Returns true if the given object is an instance of CubeServer.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CubeServer {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CubeServer.__pulumiType;
    }

    /**
     * [string] The availability zone in which the server should exist. This property is immutable.
     */
    public readonly availabilityZone!: pulumi.Output<string>;
    /**
     * ***DEPRECATED*** Please refer to ionoscloud.compute.BootDeviceSelection (Optional)[string] The associated boot drive, if any. Must be the UUID of a bootable CDROM image that can be retrieved using the ionoscloud.getImage data source.
     *
     * @deprecated Please use the 'ionoscloud_server_boot_device_selection' resource for managing the boot device of the server.
     */
    public readonly bootCdrom!: pulumi.Output<string>;
    /**
     * [string] The image or snapshot UUID / name. May also be an image alias. It is required if `licenceType` is not provided.
     */
    public readonly bootImage!: pulumi.Output<string>;
    /**
     * The associated boot volume.
     */
    public /*out*/ readonly bootVolume!: pulumi.Output<string>;
    /**
     * [string] The ID of a Virtual Data Center.
     */
    public readonly datacenterId!: pulumi.Output<string>;
    /**
     * The associated firewall rule.
     */
    public /*out*/ readonly firewallruleId!: pulumi.Output<string>;
    /**
     * [string] The name, ID or alias of the image. May also be a snapshot ID. It is required if `licenceType` is not provided. Attribute is immutable.
     */
    public readonly imageName!: pulumi.Output<string>;
    /**
     * [string] Required if `sshKeyPath` is not provided.
     *
     * > **⚠ WARNING**
     * >
     * > Image_name under volume level is deprecated, please use imageName under server level
     *
     *
     * > **⚠ WARNING**
     * >
     * > For creating a **CUBE** server, you can not set `volume.size` argument.
     * >
     */
    public readonly imagePassword!: pulumi.Output<string>;
    /**
     * A list that contains the IDs for the volumes defined inside the cube server resource.
     */
    public /*out*/ readonly inlineVolumeIds!: pulumi.Output<string[]>;
    /**
     * [string] The name of the server.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * See the Nic section.
     */
    public readonly nic!: pulumi.Output<outputs.compute.CubeServerNic>;
    /**
     * The associated IP address.
     */
    public /*out*/ readonly primaryIp!: pulumi.Output<string>;
    /**
     * The associated NIC.
     */
    public /*out*/ readonly primaryNic!: pulumi.Output<string>;
    /**
     * [list] List of paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images. Required for IonosCloud Linux images. Required if `imagePassword` is not provided.
     */
    public readonly sshKeyPaths!: pulumi.Output<string[]>;
    /**
     * [string] The UUID of the template for creating a CUBE server; the available templates for CUBE servers can be found on the templates resource
     */
    public readonly templateUuid!: pulumi.Output<string>;
    /**
     * [string] Sets the power state of the cube server. E.g: `RUNNING` or `SUSPENDED`.
     */
    public readonly vmState!: pulumi.Output<string>;
    /**
     * See the Volume section.
     */
    public readonly volume!: pulumi.Output<outputs.compute.CubeServerVolume>;

    /**
     * Create a CubeServer resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CubeServerArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: CubeServerArgs | CubeServerState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as CubeServerState | undefined;
            resourceInputs["availabilityZone"] = state ? state.availabilityZone : undefined;
            resourceInputs["bootCdrom"] = state ? state.bootCdrom : undefined;
            resourceInputs["bootImage"] = state ? state.bootImage : undefined;
            resourceInputs["bootVolume"] = state ? state.bootVolume : undefined;
            resourceInputs["datacenterId"] = state ? state.datacenterId : undefined;
            resourceInputs["firewallruleId"] = state ? state.firewallruleId : undefined;
            resourceInputs["imageName"] = state ? state.imageName : undefined;
            resourceInputs["imagePassword"] = state ? state.imagePassword : undefined;
            resourceInputs["inlineVolumeIds"] = state ? state.inlineVolumeIds : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["nic"] = state ? state.nic : undefined;
            resourceInputs["primaryIp"] = state ? state.primaryIp : undefined;
            resourceInputs["primaryNic"] = state ? state.primaryNic : undefined;
            resourceInputs["sshKeyPaths"] = state ? state.sshKeyPaths : undefined;
            resourceInputs["templateUuid"] = state ? state.templateUuid : undefined;
            resourceInputs["vmState"] = state ? state.vmState : undefined;
            resourceInputs["volume"] = state ? state.volume : undefined;
        } else {
            const args = argsOrState as CubeServerArgs | undefined;
            if ((!args || args.datacenterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'datacenterId'");
            }
            if ((!args || args.nic === undefined) && !opts.urn) {
                throw new Error("Missing required property 'nic'");
            }
            if ((!args || args.templateUuid === undefined) && !opts.urn) {
                throw new Error("Missing required property 'templateUuid'");
            }
            if ((!args || args.volume === undefined) && !opts.urn) {
                throw new Error("Missing required property 'volume'");
            }
            resourceInputs["availabilityZone"] = args ? args.availabilityZone : undefined;
            resourceInputs["bootCdrom"] = args ? args.bootCdrom : undefined;
            resourceInputs["bootImage"] = args ? args.bootImage : undefined;
            resourceInputs["datacenterId"] = args ? args.datacenterId : undefined;
            resourceInputs["imageName"] = args ? args.imageName : undefined;
            resourceInputs["imagePassword"] = args?.imagePassword ? pulumi.secret(args.imagePassword) : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["nic"] = args ? args.nic : undefined;
            resourceInputs["sshKeyPaths"] = args ? args.sshKeyPaths : undefined;
            resourceInputs["templateUuid"] = args ? args.templateUuid : undefined;
            resourceInputs["vmState"] = args ? args.vmState : undefined;
            resourceInputs["volume"] = args ? args.volume : undefined;
            resourceInputs["bootVolume"] = undefined /*out*/;
            resourceInputs["firewallruleId"] = undefined /*out*/;
            resourceInputs["inlineVolumeIds"] = undefined /*out*/;
            resourceInputs["primaryIp"] = undefined /*out*/;
            resourceInputs["primaryNic"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["imagePassword"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(CubeServer.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering CubeServer resources.
 */
export interface CubeServerState {
    /**
     * [string] The availability zone in which the server should exist. This property is immutable.
     */
    availabilityZone?: pulumi.Input<string>;
    /**
     * ***DEPRECATED*** Please refer to ionoscloud.compute.BootDeviceSelection (Optional)[string] The associated boot drive, if any. Must be the UUID of a bootable CDROM image that can be retrieved using the ionoscloud.getImage data source.
     *
     * @deprecated Please use the 'ionoscloud_server_boot_device_selection' resource for managing the boot device of the server.
     */
    bootCdrom?: pulumi.Input<string>;
    /**
     * [string] The image or snapshot UUID / name. May also be an image alias. It is required if `licenceType` is not provided.
     */
    bootImage?: pulumi.Input<string>;
    /**
     * The associated boot volume.
     */
    bootVolume?: pulumi.Input<string>;
    /**
     * [string] The ID of a Virtual Data Center.
     */
    datacenterId?: pulumi.Input<string>;
    /**
     * The associated firewall rule.
     */
    firewallruleId?: pulumi.Input<string>;
    /**
     * [string] The name, ID or alias of the image. May also be a snapshot ID. It is required if `licenceType` is not provided. Attribute is immutable.
     */
    imageName?: pulumi.Input<string>;
    /**
     * [string] Required if `sshKeyPath` is not provided.
     *
     * > **⚠ WARNING**
     * >
     * > Image_name under volume level is deprecated, please use imageName under server level
     *
     *
     * > **⚠ WARNING**
     * >
     * > For creating a **CUBE** server, you can not set `volume.size` argument.
     * >
     */
    imagePassword?: pulumi.Input<string>;
    /**
     * A list that contains the IDs for the volumes defined inside the cube server resource.
     */
    inlineVolumeIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [string] The name of the server.
     */
    name?: pulumi.Input<string>;
    /**
     * See the Nic section.
     */
    nic?: pulumi.Input<inputs.compute.CubeServerNic>;
    /**
     * The associated IP address.
     */
    primaryIp?: pulumi.Input<string>;
    /**
     * The associated NIC.
     */
    primaryNic?: pulumi.Input<string>;
    /**
     * [list] List of paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images. Required for IonosCloud Linux images. Required if `imagePassword` is not provided.
     */
    sshKeyPaths?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [string] The UUID of the template for creating a CUBE server; the available templates for CUBE servers can be found on the templates resource
     */
    templateUuid?: pulumi.Input<string>;
    /**
     * [string] Sets the power state of the cube server. E.g: `RUNNING` or `SUSPENDED`.
     */
    vmState?: pulumi.Input<string>;
    /**
     * See the Volume section.
     */
    volume?: pulumi.Input<inputs.compute.CubeServerVolume>;
}

/**
 * The set of arguments for constructing a CubeServer resource.
 */
export interface CubeServerArgs {
    /**
     * [string] The availability zone in which the server should exist. This property is immutable.
     */
    availabilityZone?: pulumi.Input<string>;
    /**
     * ***DEPRECATED*** Please refer to ionoscloud.compute.BootDeviceSelection (Optional)[string] The associated boot drive, if any. Must be the UUID of a bootable CDROM image that can be retrieved using the ionoscloud.getImage data source.
     *
     * @deprecated Please use the 'ionoscloud_server_boot_device_selection' resource for managing the boot device of the server.
     */
    bootCdrom?: pulumi.Input<string>;
    /**
     * [string] The image or snapshot UUID / name. May also be an image alias. It is required if `licenceType` is not provided.
     */
    bootImage?: pulumi.Input<string>;
    /**
     * [string] The ID of a Virtual Data Center.
     */
    datacenterId: pulumi.Input<string>;
    /**
     * [string] The name, ID or alias of the image. May also be a snapshot ID. It is required if `licenceType` is not provided. Attribute is immutable.
     */
    imageName?: pulumi.Input<string>;
    /**
     * [string] Required if `sshKeyPath` is not provided.
     *
     * > **⚠ WARNING**
     * >
     * > Image_name under volume level is deprecated, please use imageName under server level
     *
     *
     * > **⚠ WARNING**
     * >
     * > For creating a **CUBE** server, you can not set `volume.size` argument.
     * >
     */
    imagePassword?: pulumi.Input<string>;
    /**
     * [string] The name of the server.
     */
    name?: pulumi.Input<string>;
    /**
     * See the Nic section.
     */
    nic: pulumi.Input<inputs.compute.CubeServerNic>;
    /**
     * [list] List of paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images. Required for IonosCloud Linux images. Required if `imagePassword` is not provided.
     */
    sshKeyPaths?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [string] The UUID of the template for creating a CUBE server; the available templates for CUBE servers can be found on the templates resource
     */
    templateUuid: pulumi.Input<string>;
    /**
     * [string] Sets the power state of the cube server. E.g: `RUNNING` or `SUSPENDED`.
     */
    vmState?: pulumi.Input<string>;
    /**
     * See the Volume section.
     */
    volume: pulumi.Input<inputs.compute.CubeServerVolume>;
}
