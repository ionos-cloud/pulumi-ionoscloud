// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

export class Server extends pulumi.CustomResource {
    /**
     * Get an existing Server resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServerState, opts?: pulumi.CustomResourceOptions): Server {
        return new Server(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:compute/server:Server';

    /**
     * Returns true if the given object is an instance of Server.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Server {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Server.__pulumiType;
    }

    public readonly availabilityZone!: pulumi.Output<string>;
    /**
     * The associated boot drive, if any. Must be the UUID of a bootable CDROM image that you can retrieve using the image data
     * source
     *
     * @deprecated Please use the 'ionoscloud_server_boot_device_selection' resource for managing the boot device of the server.
     */
    public readonly bootCdrom!: pulumi.Output<string>;
    public readonly bootImage!: pulumi.Output<string>;
    public /*out*/ readonly bootVolume!: pulumi.Output<string>;
    public readonly cores!: pulumi.Output<number>;
    public readonly cpuFamily!: pulumi.Output<string>;
    public readonly datacenterId!: pulumi.Output<string>;
    public /*out*/ readonly firewallruleId!: pulumi.Output<string>;
    public readonly firewallruleIds!: pulumi.Output<string[]>;
    public readonly imageName!: pulumi.Output<string>;
    public readonly imagePassword!: pulumi.Output<string>;
    /**
     * A list that contains the IDs for the volumes defined inside the server resource.
     */
    public /*out*/ readonly inlineVolumeIds!: pulumi.Output<string[]>;
    public readonly labels!: pulumi.Output<outputs.compute.ServerLabel[] | undefined>;
    public readonly name!: pulumi.Output<string>;
    public readonly nic!: pulumi.Output<outputs.compute.ServerNic | undefined>;
    public /*out*/ readonly primaryIp!: pulumi.Output<string>;
    /**
     * Id of the primary network interface
     */
    public /*out*/ readonly primaryNic!: pulumi.Output<string>;
    public readonly ram!: pulumi.Output<number>;
    /**
     * Immutable List of absolute or relative paths to files containing public SSH key that will be injected into IonosCloud
     * provided Linux images. Does not support `~` expansion to homedir in the given path. Public SSH keys are set on the image
     * as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be
     * set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is
     * used for the volume creation. This property is immutable.
     *
     * @deprecated Will be renamed to sshKeys in the future, to allow users to set both the ssh key path or directly the ssh key
     */
    public readonly sshKeyPaths!: pulumi.Output<string[] | undefined>;
    /**
     * Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the
     * corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH
     * keys are only supported if a public Linux image is used for the volume creation.
     */
    public readonly sshKeys!: pulumi.Output<string[] | undefined>;
    public readonly templateUuid!: pulumi.Output<string | undefined>;
    /**
     * server usages: ENTERPRISE or CUBE
     */
    public readonly type!: pulumi.Output<string>;
    /**
     * Sets the power state of the server. Possible values: `RUNNING`, `SHUTOFF` or `SUSPENDED`. SUSPENDED state is only valid
     * for cube. SHUTOFF state is only valid for enterprise
     */
    public readonly vmState!: pulumi.Output<string>;
    public readonly volume!: pulumi.Output<outputs.compute.ServerVolume>;

    /**
     * Create a Server resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ServerArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ServerArgs | ServerState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ServerState | undefined;
            resourceInputs["availabilityZone"] = state ? state.availabilityZone : undefined;
            resourceInputs["bootCdrom"] = state ? state.bootCdrom : undefined;
            resourceInputs["bootImage"] = state ? state.bootImage : undefined;
            resourceInputs["bootVolume"] = state ? state.bootVolume : undefined;
            resourceInputs["cores"] = state ? state.cores : undefined;
            resourceInputs["cpuFamily"] = state ? state.cpuFamily : undefined;
            resourceInputs["datacenterId"] = state ? state.datacenterId : undefined;
            resourceInputs["firewallruleId"] = state ? state.firewallruleId : undefined;
            resourceInputs["firewallruleIds"] = state ? state.firewallruleIds : undefined;
            resourceInputs["imageName"] = state ? state.imageName : undefined;
            resourceInputs["imagePassword"] = state ? state.imagePassword : undefined;
            resourceInputs["inlineVolumeIds"] = state ? state.inlineVolumeIds : undefined;
            resourceInputs["labels"] = state ? state.labels : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["nic"] = state ? state.nic : undefined;
            resourceInputs["primaryIp"] = state ? state.primaryIp : undefined;
            resourceInputs["primaryNic"] = state ? state.primaryNic : undefined;
            resourceInputs["ram"] = state ? state.ram : undefined;
            resourceInputs["sshKeyPaths"] = state ? state.sshKeyPaths : undefined;
            resourceInputs["sshKeys"] = state ? state.sshKeys : undefined;
            resourceInputs["templateUuid"] = state ? state.templateUuid : undefined;
            resourceInputs["type"] = state ? state.type : undefined;
            resourceInputs["vmState"] = state ? state.vmState : undefined;
            resourceInputs["volume"] = state ? state.volume : undefined;
        } else {
            const args = argsOrState as ServerArgs | undefined;
            if ((!args || args.datacenterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'datacenterId'");
            }
            if ((!args || args.volume === undefined) && !opts.urn) {
                throw new Error("Missing required property 'volume'");
            }
            resourceInputs["availabilityZone"] = args ? args.availabilityZone : undefined;
            resourceInputs["bootCdrom"] = args ? args.bootCdrom : undefined;
            resourceInputs["bootImage"] = args ? args.bootImage : undefined;
            resourceInputs["cores"] = args ? args.cores : undefined;
            resourceInputs["cpuFamily"] = args ? args.cpuFamily : undefined;
            resourceInputs["datacenterId"] = args ? args.datacenterId : undefined;
            resourceInputs["firewallruleIds"] = args ? args.firewallruleIds : undefined;
            resourceInputs["imageName"] = args ? args.imageName : undefined;
            resourceInputs["imagePassword"] = args?.imagePassword ? pulumi.secret(args.imagePassword) : undefined;
            resourceInputs["labels"] = args ? args.labels : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["nic"] = args ? args.nic : undefined;
            resourceInputs["ram"] = args ? args.ram : undefined;
            resourceInputs["sshKeyPaths"] = args ? args.sshKeyPaths : undefined;
            resourceInputs["sshKeys"] = args ? args.sshKeys : undefined;
            resourceInputs["templateUuid"] = args ? args.templateUuid : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
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
        super(Server.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Server resources.
 */
export interface ServerState {
    availabilityZone?: pulumi.Input<string>;
    /**
     * The associated boot drive, if any. Must be the UUID of a bootable CDROM image that you can retrieve using the image data
     * source
     *
     * @deprecated Please use the 'ionoscloud_server_boot_device_selection' resource for managing the boot device of the server.
     */
    bootCdrom?: pulumi.Input<string>;
    bootImage?: pulumi.Input<string>;
    bootVolume?: pulumi.Input<string>;
    cores?: pulumi.Input<number>;
    cpuFamily?: pulumi.Input<string>;
    datacenterId?: pulumi.Input<string>;
    firewallruleId?: pulumi.Input<string>;
    firewallruleIds?: pulumi.Input<pulumi.Input<string>[]>;
    imageName?: pulumi.Input<string>;
    imagePassword?: pulumi.Input<string>;
    /**
     * A list that contains the IDs for the volumes defined inside the server resource.
     */
    inlineVolumeIds?: pulumi.Input<pulumi.Input<string>[]>;
    labels?: pulumi.Input<pulumi.Input<inputs.compute.ServerLabel>[]>;
    name?: pulumi.Input<string>;
    nic?: pulumi.Input<inputs.compute.ServerNic>;
    primaryIp?: pulumi.Input<string>;
    /**
     * Id of the primary network interface
     */
    primaryNic?: pulumi.Input<string>;
    ram?: pulumi.Input<number>;
    /**
     * Immutable List of absolute or relative paths to files containing public SSH key that will be injected into IonosCloud
     * provided Linux images. Does not support `~` expansion to homedir in the given path. Public SSH keys are set on the image
     * as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be
     * set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is
     * used for the volume creation. This property is immutable.
     *
     * @deprecated Will be renamed to sshKeys in the future, to allow users to set both the ssh key path or directly the ssh key
     */
    sshKeyPaths?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the
     * corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH
     * keys are only supported if a public Linux image is used for the volume creation.
     */
    sshKeys?: pulumi.Input<pulumi.Input<string>[]>;
    templateUuid?: pulumi.Input<string>;
    /**
     * server usages: ENTERPRISE or CUBE
     */
    type?: pulumi.Input<string>;
    /**
     * Sets the power state of the server. Possible values: `RUNNING`, `SHUTOFF` or `SUSPENDED`. SUSPENDED state is only valid
     * for cube. SHUTOFF state is only valid for enterprise
     */
    vmState?: pulumi.Input<string>;
    volume?: pulumi.Input<inputs.compute.ServerVolume>;
}

/**
 * The set of arguments for constructing a Server resource.
 */
export interface ServerArgs {
    availabilityZone?: pulumi.Input<string>;
    /**
     * The associated boot drive, if any. Must be the UUID of a bootable CDROM image that you can retrieve using the image data
     * source
     *
     * @deprecated Please use the 'ionoscloud_server_boot_device_selection' resource for managing the boot device of the server.
     */
    bootCdrom?: pulumi.Input<string>;
    bootImage?: pulumi.Input<string>;
    cores?: pulumi.Input<number>;
    cpuFamily?: pulumi.Input<string>;
    datacenterId: pulumi.Input<string>;
    firewallruleIds?: pulumi.Input<pulumi.Input<string>[]>;
    imageName?: pulumi.Input<string>;
    imagePassword?: pulumi.Input<string>;
    labels?: pulumi.Input<pulumi.Input<inputs.compute.ServerLabel>[]>;
    name?: pulumi.Input<string>;
    nic?: pulumi.Input<inputs.compute.ServerNic>;
    ram?: pulumi.Input<number>;
    /**
     * Immutable List of absolute or relative paths to files containing public SSH key that will be injected into IonosCloud
     * provided Linux images. Does not support `~` expansion to homedir in the given path. Public SSH keys are set on the image
     * as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be
     * set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is
     * used for the volume creation. This property is immutable.
     *
     * @deprecated Will be renamed to sshKeys in the future, to allow users to set both the ssh key path or directly the ssh key
     */
    sshKeyPaths?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the
     * corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH
     * keys are only supported if a public Linux image is used for the volume creation.
     */
    sshKeys?: pulumi.Input<pulumi.Input<string>[]>;
    templateUuid?: pulumi.Input<string>;
    /**
     * server usages: ENTERPRISE or CUBE
     */
    type?: pulumi.Input<string>;
    /**
     * Sets the power state of the server. Possible values: `RUNNING`, `SHUTOFF` or `SUSPENDED`. SUSPENDED state is only valid
     * for cube. SHUTOFF state is only valid for enterprise
     */
    vmState?: pulumi.Input<string>;
    volume: pulumi.Input<inputs.compute.ServerVolume>;
}
