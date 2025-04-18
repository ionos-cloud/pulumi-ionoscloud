// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Manages a **Server** on IonosCloud.
 *
 * ## Example Usage
 *
 * This resource will create an operational server. After this section completes, the provisioner can be called.
 *
 * ### ENTERPRISE Server
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@ionos-cloud/sdk-pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 * import * as random from "@pulumi/random";
 *
 * const example = ionoscloud.compute.getImage({
 *     type: "HDD",
 *     cloudInit: "V1",
 *     imageAlias: "ubuntu:latest",
 *     location: "us/las",
 * });
 * const exampleDatacenter = new ionoscloud.compute.Datacenter("example", {
 *     name: "Datacenter Example",
 *     location: "us/las",
 *     description: "Datacenter Description",
 *     secAuthProtection: false,
 * });
 * const exampleLan = new ionoscloud.compute.Lan("example", {
 *     datacenterId: exampleDatacenter.id,
 *     "public": true,
 *     name: "Lan Example",
 * });
 * const exampleIPBlock = new ionoscloud.compute.IPBlock("example", {
 *     location: exampleDatacenter.location,
 *     size: 4,
 *     name: "IP Block Example",
 * });
 * const serverImagePassword = new random.index.Password("server_image_password", {
 *     length: 16,
 *     special: false,
 * });
 * const exampleServer = new ionoscloud.compute.Server("example", {
 *     name: "Server Example",
 *     datacenterId: exampleDatacenter.id,
 *     cores: 1,
 *     ram: 1024,
 *     availabilityZone: "ZONE_1",
 *     cpuFamily: "INTEL_XEON",
 *     imageName: example.then(example => example.name),
 *     imagePassword: serverImagePassword.result,
 *     type: "ENTERPRISE",
 *     volume: {
 *         name: "system",
 *         size: 5,
 *         diskType: "SSD Standard",
 *         userData: "foo",
 *         bus: "VIRTIO",
 *         availabilityZone: "ZONE_1",
 *     },
 *     nic: {
 *         lan: exampleLan.id,
 *         name: "system",
 *         dhcp: true,
 *         firewallActive: true,
 *         firewallType: "BIDIRECTIONAL",
 *         ips: [
 *             exampleIPBlock.ips[0],
 *             exampleIPBlock.ips[1],
 *         ],
 *         firewalls: [{
 *             protocol: "TCP",
 *             name: "SSH",
 *             portRangeStart: 22,
 *             portRangeEnd: 22,
 *             sourceMac: "00:0a:95:9d:68:17",
 *             sourceIp: exampleIPBlock.ips[2],
 *             targetIp: exampleIPBlock.ips[3],
 *             type: "EGRESS",
 *         }],
 *     },
 *     labels: [
 *         {
 *             key: "labelkey1",
 *             value: "labelvalue1",
 *         },
 *         {
 *             key: "labelkey2",
 *             value: "labelvalue2",
 *         },
 *     ],
 * });
 * ```
 * ### With IPv6 Enabled
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@ionos-cloud/sdk-pulumi";
 * import * as random from "@pulumi/random";
 *
 * const example = new ionoscloud.compute.Datacenter("example", {
 *     name: "Resource Server Test",
 *     location: "us/las",
 * });
 * const webserverIpblock = new ionoscloud.compute.IPBlock("webserver_ipblock", {
 *     location: "us/las",
 *     size: 4,
 *     name: "webserver_ipblock",
 * });
 * const exampleLan = new ionoscloud.compute.Lan("example", {
 *     datacenterId: example.id,
 *     "public": true,
 *     name: "public",
 *     ipv6CidrBlock: "ipv6_cidr_block_from_lan",
 * });
 * const serverImagePassword = new random.index.Password("server_image_password", {
 *     length: 16,
 *     special: false,
 * });
 * const exampleServer = new ionoscloud.compute.Server("example", {
 *     name: "Resource Server Test",
 *     datacenterId: example.id,
 *     cores: 1,
 *     ram: 1024,
 *     availabilityZone: "ZONE_1",
 *     cpuFamily: "INTEL_XEON",
 *     imageName: "ubuntu:latest",
 *     imagePassword: serverImagePassword.result,
 *     type: "ENTERPRISE",
 *     volume: {
 *         name: "system",
 *         size: 5,
 *         diskType: "SSD Standard",
 *         userData: "foo",
 *         bus: "VIRTIO",
 *         availabilityZone: "ZONE_1",
 *     },
 *     nic: {
 *         lan: exampleLan.id,
 *         name: "system",
 *         dhcp: true,
 *         firewallActive: true,
 *         firewallType: "BIDIRECTIONAL",
 *         ips: [
 *             webserverIpblock.ips[0],
 *             webserverIpblock.ips[1],
 *         ],
 *         dhcpv6: true,
 *         ipv6CidrBlock: "ipv6_cidr_block_from_lan",
 *         ipv6Ips: [
 *             "ipv6_ip1",
 *             "ipv6_ip2",
 *             "ipv6_ip3",
 *         ],
 *         firewalls: [{
 *             protocol: "TCP",
 *             name: "SSH",
 *             portRangeStart: 22,
 *             portRangeEnd: 22,
 *             sourceMac: "00:0a:95:9d:68:17",
 *             sourceIp: webserverIpblock.ips[2],
 *             targetIp: webserverIpblock.ips[3],
 *             type: "EGRESS",
 *         }],
 *     },
 * });
 * ```
 *
 * ### CUBE Server
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@ionos-cloud/sdk-pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 * import * as random from "@pulumi/random";
 *
 * const example = ionoscloud.compute.getTemplate({
 *     name: "Basic Cube XS",
 * });
 * const exampleDatacenter = new ionoscloud.compute.Datacenter("example", {
 *     name: "Datacenter Example",
 *     location: "de/txl",
 * });
 * const exampleLan = new ionoscloud.compute.Lan("example", {
 *     datacenterId: exampleDatacenter.id,
 *     "public": true,
 *     name: "Lan Example",
 * });
 * const serverImagePassword = new random.index.Password("server_image_password", {
 *     length: 16,
 *     special: false,
 * });
 * const exampleServer = new ionoscloud.compute.Server("example", {
 *     name: "Server Example",
 *     availabilityZone: "ZONE_2",
 *     imageName: "ubuntu:latest",
 *     type: "CUBE",
 *     templateUuid: example.then(example => example.id),
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
 * ### Server that boots from CDROM
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@ionos-cloud/sdk-pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const cdromDatacenter = new ionoscloud.compute.Datacenter("cdrom", {
 *     name: "CDROM Test",
 *     location: "de/txl",
 *     description: "CDROM image test",
 *     secAuthProtection: false,
 * });
 * const _public = new ionoscloud.compute.Lan("public", {
 *     datacenterId: cdromDatacenter.id,
 *     "public": true,
 *     name: "Uplink",
 * });
 * const cdrom = ionoscloud.compute.getImage({
 *     imageAlias: "ubuntu:latest_iso",
 *     type: "CDROM",
 *     location: "de/txl",
 *     cloudInit: "NONE",
 * });
 * const test = new ionoscloud.compute.Server("test", {
 *     datacenterId: cdromDatacenter.id,
 *     name: "ubuntu_latest_from_cdrom",
 *     cores: 1,
 *     ram: 1024,
 *     cpuFamily: cdromDatacenter.cpuArchitectures.apply(cpuArchitectures => cpuArchitectures[0].cpuFamily),
 *     type: "ENTERPRISE",
 *     volume: {
 *         name: "hdd0",
 *         diskType: "HDD",
 *         size: 50,
 *         licenceType: "OTHER",
 *     },
 *     nic: {
 *         lan: 1,
 *         dhcp: true,
 *         firewallActive: false,
 *     },
 * });
 * ```
 *
 * ## Notes
 *
 * Please note that for any secondary volume, you need to set the **licence_type** property to **UNKNOWN**
 *
 * ⚠️ **Note:** Important for deleting an `firewall` rule from within a list of inline resources defined on the same nic. There is one limitation to removing one firewall rule
 * from the middle of the list of `firewall` rules. The existing rules will be modified and the last one will be deleted.
 *
 * ## Import
 *
 * Resource Server can be imported using the `resource id` and the `datacenter id`, e.g.. Passing only resource id and datacenter id means that the first nic found linked to the server will be attached to it.
 *
 * ```sh
 * $ pulumi import ionoscloud:compute/server:Server myserver datacenter uuid/server uuid
 * ```
 *
 * Optionally, you can pass `primary_nic` and `firewallrule_id` so pulumi will know to import also the first nic and firewall rule (if it exists on the server):
 *
 * ```sh
 * $ pulumi import ionoscloud:compute/server:Server myserver datacenter uuid/server uuid/primary nic id/firewall rule id
 * ```
 */
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

    /**
     * [bool] When set to true, allows the update of immutable fields by first destroying and then re-creating the server.
     *
     * ⚠️ **_Warning: `allowReplace` - lets you update immutable fields, but it first destroys and then re-creates the server in order to do it. This field should be used with care, understanding the risks._**
     *
     * > **⚠ WARNING**
     * >
     * > Image_name under volume level is deprecated, please use imageName under server level
     * > sshKeyPath and sshKeys fields are immutable.
     *
     *
     * > **⚠ WARNING**
     * >
     * > If you want to create a **CUBE** server, you have to provide the `templateUuid`. In this case you can not set `cores`, `ram` and `volume.size` arguments, these being mutually exclusive with `templateUuid`.
     * >
     * > In all the other cases (**ENTERPRISE** servers) you have to provide values for `cores`, `ram` and `volume size`.
     */
    public readonly allowReplace!: pulumi.Output<boolean | undefined>;
    /**
     * [string] The availability zone in which the server should exist. E.g: `AUTO`, `ZONE_1`, `ZONE_2`. This property is immutable.
     */
    public readonly availabilityZone!: pulumi.Output<string>;
    /**
     * ***DEPRECATED*** Please refer to ionoscloud.compute.BootDeviceSelection (Optional)(Computed)[string] The associated boot drive, if any. Must be the UUID of a bootable CDROM image that can be retrieved using the ionoscloud.compute.getImage data source.
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
     * (Computed)[integer] Number of server CPU cores.
     */
    public readonly cores!: pulumi.Output<number>;
    /**
     * [string] CPU architecture on which server gets provisioned; not all CPU architectures are available in all datacenter regions; available CPU architectures can be retrieved from the datacenter resource. E.g.: "INTEL_SKYLAKE" or "INTEL_XEON".
     */
    public readonly cpuFamily!: pulumi.Output<string>;
    /**
     * [string] The ID of a Virtual Data Center.
     */
    public readonly datacenterId!: pulumi.Output<string>;
    /**
     * The associated firewall rule.
     */
    public /*out*/ readonly firewallruleId!: pulumi.Output<string>;
    /**
     * The associated firewall rules.
     */
    public readonly firewallruleIds!: pulumi.Output<string[]>;
    /**
     * (Computed)[string] The hostname of the resource. Allowed characters are a-z, 0-9 and - (minus). Hostname should not start with minus and should not be longer than 63 characters. If no value provided explicitly, it will be populated with the name of the server
     */
    public readonly hostname!: pulumi.Output<string>;
    /**
     * [string] The name, ID or alias of the image. May also be a snapshot ID. It is required if `licenceType` is not provided. Attribute is immutable.
     */
    public readonly imageName!: pulumi.Output<string>;
    /**
     * [string] Required if `sshKeyPath` is not provided.
     */
    public readonly imagePassword!: pulumi.Output<string>;
    /**
     * A list with the IDs for the volumes that are defined inside the server resource.
     */
    public /*out*/ readonly inlineVolumeIds!: pulumi.Output<string[]>;
    /**
     * [set] A label can be seen as an object with only two required fields: `key` and `value`, both of the `string` type. Please check the example presented above to see how a `label` can be used in the plan. A server can have multiple labels.
     */
    public readonly labels!: pulumi.Output<outputs.compute.ServerLabel[] | undefined>;
    /**
     * [string] The name of the server.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * See the Nic section.
     */
    public readonly nic!: pulumi.Output<outputs.compute.ServerNic | undefined>;
    /**
     * The associated IP address.
     */
    public /*out*/ readonly primaryIp!: pulumi.Output<string>;
    /**
     * The associated NIC.
     */
    public /*out*/ readonly primaryNic!: pulumi.Output<string>;
    /**
     * (Computed)[integer] The amount of memory for the server in MB.
     */
    public readonly ram!: pulumi.Output<number>;
    /**
     * The list of Security Group IDs for the
     */
    public readonly securityGroupsIds!: pulumi.Output<string[] | undefined>;
    /**
     * [list] List of absolute paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images.  Also accepts ssh keys directly. Required for IonosCloud Linux images. Required if `imagePassword` is not provided. Does not support `~` expansion to homedir in the given path. This property is immutable.
     *
     * @deprecated Will be renamed to sshKeys in the future, to allow users to set both the ssh key path or directly the ssh key
     */
    public readonly sshKeyPaths!: pulumi.Output<string[] | undefined>;
    /**
     * [list] Immutable List of absolute or relative paths to files containing public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation. Does not support `~` expansion to homedir in the given path.
     */
    public readonly sshKeys!: pulumi.Output<string[] | undefined>;
    /**
     * [string] The UUID of the template for creating a CUBE server; the available templates for CUBE servers can be found on the templates resource
     */
    public readonly templateUuid!: pulumi.Output<string | undefined>;
    /**
     * (Computed)[string] Server usages: [ENTERPRISE](https://docs.ionos.com/cloud/compute-engine/virtual-servers/virtual-servers) or [CUBE](https://docs.ionos.com/cloud/compute-engine/virtual-servers/cloud-cubes). This property is immutable.
     */
    public readonly type!: pulumi.Output<string>;
    /**
     * [string] Sets the power state of the server. E.g: `RUNNING`, `SHUTOFF` or `SUSPENDED`. SUSPENDED state is only valid for cube. SHUTOFF state is only valid for enterprise.
     */
    public readonly vmState!: pulumi.Output<string>;
    /**
     * See the Volume section.
     */
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
            resourceInputs["allowReplace"] = state ? state.allowReplace : undefined;
            resourceInputs["availabilityZone"] = state ? state.availabilityZone : undefined;
            resourceInputs["bootCdrom"] = state ? state.bootCdrom : undefined;
            resourceInputs["bootImage"] = state ? state.bootImage : undefined;
            resourceInputs["bootVolume"] = state ? state.bootVolume : undefined;
            resourceInputs["cores"] = state ? state.cores : undefined;
            resourceInputs["cpuFamily"] = state ? state.cpuFamily : undefined;
            resourceInputs["datacenterId"] = state ? state.datacenterId : undefined;
            resourceInputs["firewallruleId"] = state ? state.firewallruleId : undefined;
            resourceInputs["firewallruleIds"] = state ? state.firewallruleIds : undefined;
            resourceInputs["hostname"] = state ? state.hostname : undefined;
            resourceInputs["imageName"] = state ? state.imageName : undefined;
            resourceInputs["imagePassword"] = state ? state.imagePassword : undefined;
            resourceInputs["inlineVolumeIds"] = state ? state.inlineVolumeIds : undefined;
            resourceInputs["labels"] = state ? state.labels : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["nic"] = state ? state.nic : undefined;
            resourceInputs["primaryIp"] = state ? state.primaryIp : undefined;
            resourceInputs["primaryNic"] = state ? state.primaryNic : undefined;
            resourceInputs["ram"] = state ? state.ram : undefined;
            resourceInputs["securityGroupsIds"] = state ? state.securityGroupsIds : undefined;
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
            resourceInputs["allowReplace"] = args ? args.allowReplace : undefined;
            resourceInputs["availabilityZone"] = args ? args.availabilityZone : undefined;
            resourceInputs["bootCdrom"] = args ? args.bootCdrom : undefined;
            resourceInputs["bootImage"] = args ? args.bootImage : undefined;
            resourceInputs["cores"] = args ? args.cores : undefined;
            resourceInputs["cpuFamily"] = args ? args.cpuFamily : undefined;
            resourceInputs["datacenterId"] = args ? args.datacenterId : undefined;
            resourceInputs["firewallruleIds"] = args ? args.firewallruleIds : undefined;
            resourceInputs["hostname"] = args ? args.hostname : undefined;
            resourceInputs["imageName"] = args ? args.imageName : undefined;
            resourceInputs["imagePassword"] = args?.imagePassword ? pulumi.secret(args.imagePassword) : undefined;
            resourceInputs["labels"] = args ? args.labels : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["nic"] = args ? args.nic : undefined;
            resourceInputs["ram"] = args ? args.ram : undefined;
            resourceInputs["securityGroupsIds"] = args ? args.securityGroupsIds : undefined;
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
    /**
     * [bool] When set to true, allows the update of immutable fields by first destroying and then re-creating the server.
     *
     * ⚠️ **_Warning: `allowReplace` - lets you update immutable fields, but it first destroys and then re-creates the server in order to do it. This field should be used with care, understanding the risks._**
     *
     * > **⚠ WARNING**
     * >
     * > Image_name under volume level is deprecated, please use imageName under server level
     * > sshKeyPath and sshKeys fields are immutable.
     *
     *
     * > **⚠ WARNING**
     * >
     * > If you want to create a **CUBE** server, you have to provide the `templateUuid`. In this case you can not set `cores`, `ram` and `volume.size` arguments, these being mutually exclusive with `templateUuid`.
     * >
     * > In all the other cases (**ENTERPRISE** servers) you have to provide values for `cores`, `ram` and `volume size`.
     */
    allowReplace?: pulumi.Input<boolean>;
    /**
     * [string] The availability zone in which the server should exist. E.g: `AUTO`, `ZONE_1`, `ZONE_2`. This property is immutable.
     */
    availabilityZone?: pulumi.Input<string>;
    /**
     * ***DEPRECATED*** Please refer to ionoscloud.compute.BootDeviceSelection (Optional)(Computed)[string] The associated boot drive, if any. Must be the UUID of a bootable CDROM image that can be retrieved using the ionoscloud.compute.getImage data source.
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
     * (Computed)[integer] Number of server CPU cores.
     */
    cores?: pulumi.Input<number>;
    /**
     * [string] CPU architecture on which server gets provisioned; not all CPU architectures are available in all datacenter regions; available CPU architectures can be retrieved from the datacenter resource. E.g.: "INTEL_SKYLAKE" or "INTEL_XEON".
     */
    cpuFamily?: pulumi.Input<string>;
    /**
     * [string] The ID of a Virtual Data Center.
     */
    datacenterId?: pulumi.Input<string>;
    /**
     * The associated firewall rule.
     */
    firewallruleId?: pulumi.Input<string>;
    /**
     * The associated firewall rules.
     */
    firewallruleIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * (Computed)[string] The hostname of the resource. Allowed characters are a-z, 0-9 and - (minus). Hostname should not start with minus and should not be longer than 63 characters. If no value provided explicitly, it will be populated with the name of the server
     */
    hostname?: pulumi.Input<string>;
    /**
     * [string] The name, ID or alias of the image. May also be a snapshot ID. It is required if `licenceType` is not provided. Attribute is immutable.
     */
    imageName?: pulumi.Input<string>;
    /**
     * [string] Required if `sshKeyPath` is not provided.
     */
    imagePassword?: pulumi.Input<string>;
    /**
     * A list with the IDs for the volumes that are defined inside the server resource.
     */
    inlineVolumeIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [set] A label can be seen as an object with only two required fields: `key` and `value`, both of the `string` type. Please check the example presented above to see how a `label` can be used in the plan. A server can have multiple labels.
     */
    labels?: pulumi.Input<pulumi.Input<inputs.compute.ServerLabel>[]>;
    /**
     * [string] The name of the server.
     */
    name?: pulumi.Input<string>;
    /**
     * See the Nic section.
     */
    nic?: pulumi.Input<inputs.compute.ServerNic>;
    /**
     * The associated IP address.
     */
    primaryIp?: pulumi.Input<string>;
    /**
     * The associated NIC.
     */
    primaryNic?: pulumi.Input<string>;
    /**
     * (Computed)[integer] The amount of memory for the server in MB.
     */
    ram?: pulumi.Input<number>;
    /**
     * The list of Security Group IDs for the
     */
    securityGroupsIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [list] List of absolute paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images.  Also accepts ssh keys directly. Required for IonosCloud Linux images. Required if `imagePassword` is not provided. Does not support `~` expansion to homedir in the given path. This property is immutable.
     *
     * @deprecated Will be renamed to sshKeys in the future, to allow users to set both the ssh key path or directly the ssh key
     */
    sshKeyPaths?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [list] Immutable List of absolute or relative paths to files containing public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation. Does not support `~` expansion to homedir in the given path.
     */
    sshKeys?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [string] The UUID of the template for creating a CUBE server; the available templates for CUBE servers can be found on the templates resource
     */
    templateUuid?: pulumi.Input<string>;
    /**
     * (Computed)[string] Server usages: [ENTERPRISE](https://docs.ionos.com/cloud/compute-engine/virtual-servers/virtual-servers) or [CUBE](https://docs.ionos.com/cloud/compute-engine/virtual-servers/cloud-cubes). This property is immutable.
     */
    type?: pulumi.Input<string>;
    /**
     * [string] Sets the power state of the server. E.g: `RUNNING`, `SHUTOFF` or `SUSPENDED`. SUSPENDED state is only valid for cube. SHUTOFF state is only valid for enterprise.
     */
    vmState?: pulumi.Input<string>;
    /**
     * See the Volume section.
     */
    volume?: pulumi.Input<inputs.compute.ServerVolume>;
}

/**
 * The set of arguments for constructing a Server resource.
 */
export interface ServerArgs {
    /**
     * [bool] When set to true, allows the update of immutable fields by first destroying and then re-creating the server.
     *
     * ⚠️ **_Warning: `allowReplace` - lets you update immutable fields, but it first destroys and then re-creates the server in order to do it. This field should be used with care, understanding the risks._**
     *
     * > **⚠ WARNING**
     * >
     * > Image_name under volume level is deprecated, please use imageName under server level
     * > sshKeyPath and sshKeys fields are immutable.
     *
     *
     * > **⚠ WARNING**
     * >
     * > If you want to create a **CUBE** server, you have to provide the `templateUuid`. In this case you can not set `cores`, `ram` and `volume.size` arguments, these being mutually exclusive with `templateUuid`.
     * >
     * > In all the other cases (**ENTERPRISE** servers) you have to provide values for `cores`, `ram` and `volume size`.
     */
    allowReplace?: pulumi.Input<boolean>;
    /**
     * [string] The availability zone in which the server should exist. E.g: `AUTO`, `ZONE_1`, `ZONE_2`. This property is immutable.
     */
    availabilityZone?: pulumi.Input<string>;
    /**
     * ***DEPRECATED*** Please refer to ionoscloud.compute.BootDeviceSelection (Optional)(Computed)[string] The associated boot drive, if any. Must be the UUID of a bootable CDROM image that can be retrieved using the ionoscloud.compute.getImage data source.
     *
     * @deprecated Please use the 'ionoscloud_server_boot_device_selection' resource for managing the boot device of the server.
     */
    bootCdrom?: pulumi.Input<string>;
    /**
     * [string] The image or snapshot UUID / name. May also be an image alias. It is required if `licenceType` is not provided.
     */
    bootImage?: pulumi.Input<string>;
    /**
     * (Computed)[integer] Number of server CPU cores.
     */
    cores?: pulumi.Input<number>;
    /**
     * [string] CPU architecture on which server gets provisioned; not all CPU architectures are available in all datacenter regions; available CPU architectures can be retrieved from the datacenter resource. E.g.: "INTEL_SKYLAKE" or "INTEL_XEON".
     */
    cpuFamily?: pulumi.Input<string>;
    /**
     * [string] The ID of a Virtual Data Center.
     */
    datacenterId: pulumi.Input<string>;
    /**
     * The associated firewall rules.
     */
    firewallruleIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * (Computed)[string] The hostname of the resource. Allowed characters are a-z, 0-9 and - (minus). Hostname should not start with minus and should not be longer than 63 characters. If no value provided explicitly, it will be populated with the name of the server
     */
    hostname?: pulumi.Input<string>;
    /**
     * [string] The name, ID or alias of the image. May also be a snapshot ID. It is required if `licenceType` is not provided. Attribute is immutable.
     */
    imageName?: pulumi.Input<string>;
    /**
     * [string] Required if `sshKeyPath` is not provided.
     */
    imagePassword?: pulumi.Input<string>;
    /**
     * [set] A label can be seen as an object with only two required fields: `key` and `value`, both of the `string` type. Please check the example presented above to see how a `label` can be used in the plan. A server can have multiple labels.
     */
    labels?: pulumi.Input<pulumi.Input<inputs.compute.ServerLabel>[]>;
    /**
     * [string] The name of the server.
     */
    name?: pulumi.Input<string>;
    /**
     * See the Nic section.
     */
    nic?: pulumi.Input<inputs.compute.ServerNic>;
    /**
     * (Computed)[integer] The amount of memory for the server in MB.
     */
    ram?: pulumi.Input<number>;
    /**
     * The list of Security Group IDs for the
     */
    securityGroupsIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [list] List of absolute paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images.  Also accepts ssh keys directly. Required for IonosCloud Linux images. Required if `imagePassword` is not provided. Does not support `~` expansion to homedir in the given path. This property is immutable.
     *
     * @deprecated Will be renamed to sshKeys in the future, to allow users to set both the ssh key path or directly the ssh key
     */
    sshKeyPaths?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [list] Immutable List of absolute or relative paths to files containing public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation. Does not support `~` expansion to homedir in the given path.
     */
    sshKeys?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [string] The UUID of the template for creating a CUBE server; the available templates for CUBE servers can be found on the templates resource
     */
    templateUuid?: pulumi.Input<string>;
    /**
     * (Computed)[string] Server usages: [ENTERPRISE](https://docs.ionos.com/cloud/compute-engine/virtual-servers/virtual-servers) or [CUBE](https://docs.ionos.com/cloud/compute-engine/virtual-servers/cloud-cubes). This property is immutable.
     */
    type?: pulumi.Input<string>;
    /**
     * [string] Sets the power state of the server. E.g: `RUNNING`, `SHUTOFF` or `SUSPENDED`. SUSPENDED state is only valid for cube. SHUTOFF state is only valid for enterprise.
     */
    vmState?: pulumi.Input<string>;
    /**
     * See the Volume section.
     */
    volume: pulumi.Input<inputs.compute.ServerVolume>;
}
