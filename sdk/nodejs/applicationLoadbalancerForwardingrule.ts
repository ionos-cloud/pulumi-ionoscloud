// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Manages an **Application Load Balancer Forwarding Rule** on IonosCloud.
 *
 * ## Example Usage
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as fs from "fs";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const exampleDatacenter = new ionoscloud.compute.Datacenter("exampleDatacenter", {
 *     location: "us/las",
 *     description: "datacenter description",
 *     secAuthProtection: false,
 * });
 * const example1 = new ionoscloud.compute.Lan("example1", {
 *     datacenterId: exampleDatacenter.id,
 *     "public": true,
 * });
 * const example2 = new ionoscloud.compute.Lan("example2", {
 *     datacenterId: exampleDatacenter.id,
 *     "public": true,
 * });
 * const exampleApplicationLoadbalancer = new ionoscloud.ApplicationLoadbalancer("exampleApplicationLoadbalancer", {
 *     datacenterId: exampleDatacenter.id,
 *     listenerLan: example1.id,
 *     ips: ["10.12.118.224"],
 *     targetLan: example2.id,
 *     lbPrivateIps: ["10.13.72.225/24"],
 * });
 * //optionally you can add a certificate to the application load balancer
 * const cert = new ionoscloud.Certificate("cert", {
 *     certificate: fs.readFileSync("path_to_cert", "utf8"),
 *     certificateChain: fs.readFileSync("path_to_cert_chain", "utf8"),
 *     privateKey: fs.readFileSync("path_to_private_key", "utf8"),
 * });
 * const exampleApplicationLoadbalancerForwardingrule = new ionoscloud.ApplicationLoadbalancerForwardingrule("exampleApplicationLoadbalancerForwardingrule", {
 *     datacenterId: exampleDatacenter.id,
 *     applicationLoadbalancerId: exampleApplicationLoadbalancer.id,
 *     protocol: "HTTP",
 *     listenerIp: "10.12.118.224",
 *     listenerPort: 8080,
 *     clientTimeout: 1000,
 *     httpRules: [
 *         {
 *             name: "http_rule",
 *             type: "REDIRECT",
 *             dropQuery: true,
 *             location: "www.ionos.com",
 *             statusCode: 301,
 *             conditions: [{
 *                 type: "HEADER",
 *                 condition: "EQUALS",
 *                 negate: true,
 *                 key: "key",
 *                 value: "10.12.120.224/24",
 *             }],
 *         },
 *         {
 *             name: "http_rule_2",
 *             type: "STATIC",
 *             dropQuery: false,
 *             statusCode: 303,
 *             responseMessage: "Response",
 *             contentType: "text/plain",
 *             conditions: [{
 *                 type: "QUERY",
 *                 condition: "MATCHES",
 *                 negate: false,
 *                 key: "key",
 *                 value: "10.12.120.224/24",
 *             }],
 *         },
 *     ],
 *     serverCertificates: [cert.id],
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 *
 * ## Import
 *
 * Resource Application Load Balancer Forwarding Rule can be imported using the `resource id`, `alb id` and `datacenter id`, e.g.
 *
 * ```sh
 * $ pulumi import ionoscloud:index/applicationLoadbalancerForwardingrule:ApplicationLoadbalancerForwardingrule my_application_loadbalancer_forwardingrule {datacenter uuid}/{application_loadbalancer uuid}/{application_loadbalancer_forwardingrule uuid}
 * ```
 */
export class ApplicationLoadbalancerForwardingrule extends pulumi.CustomResource {
    /**
     * Get an existing ApplicationLoadbalancerForwardingrule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ApplicationLoadbalancerForwardingruleState, opts?: pulumi.CustomResourceOptions): ApplicationLoadbalancerForwardingrule {
        return new ApplicationLoadbalancerForwardingrule(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:index/applicationLoadbalancerForwardingrule:ApplicationLoadbalancerForwardingrule';

    /**
     * Returns true if the given object is an instance of ApplicationLoadbalancerForwardingrule.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ApplicationLoadbalancerForwardingrule {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ApplicationLoadbalancerForwardingrule.__pulumiType;
    }

    /**
     * [string] The ID of Application Load Balancer.
     */
    public readonly applicationLoadbalancerId!: pulumi.Output<string>;
    /**
     * [int] The maximum time in milliseconds to wait for the client to acknowledge or send data; default is 50,000 (50 seconds).
     */
    public readonly clientTimeout!: pulumi.Output<number>;
    /**
     * [string] The ID of a Virtual Data Center.
     */
    public readonly datacenterId!: pulumi.Output<string>;
    /**
     * [list] Array of items in that collection
     */
    public readonly httpRules!: pulumi.Output<outputs.ApplicationLoadbalancerForwardingruleHttpRule[] | undefined>;
    /**
     * [string] Listening (inbound) IP.
     */
    public readonly listenerIp!: pulumi.Output<string>;
    /**
     * [int] Listening (inbound) port number; valid range is 1 to 65535.
     */
    public readonly listenerPort!: pulumi.Output<number>;
    /**
     * [string] The unique name of the Application Load Balancer HTTP rule.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * [string] Balancing protocol.
     */
    public readonly protocol!: pulumi.Output<string>;
    /**
     * [list] Array of certificate ids. You can create certificates with the certificate resource.
     */
    public readonly serverCertificates!: pulumi.Output<string[] | undefined>;

    /**
     * Create a ApplicationLoadbalancerForwardingrule resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ApplicationLoadbalancerForwardingruleArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ApplicationLoadbalancerForwardingruleArgs | ApplicationLoadbalancerForwardingruleState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ApplicationLoadbalancerForwardingruleState | undefined;
            resourceInputs["applicationLoadbalancerId"] = state ? state.applicationLoadbalancerId : undefined;
            resourceInputs["clientTimeout"] = state ? state.clientTimeout : undefined;
            resourceInputs["datacenterId"] = state ? state.datacenterId : undefined;
            resourceInputs["httpRules"] = state ? state.httpRules : undefined;
            resourceInputs["listenerIp"] = state ? state.listenerIp : undefined;
            resourceInputs["listenerPort"] = state ? state.listenerPort : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["protocol"] = state ? state.protocol : undefined;
            resourceInputs["serverCertificates"] = state ? state.serverCertificates : undefined;
        } else {
            const args = argsOrState as ApplicationLoadbalancerForwardingruleArgs | undefined;
            if ((!args || args.applicationLoadbalancerId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'applicationLoadbalancerId'");
            }
            if ((!args || args.datacenterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'datacenterId'");
            }
            if ((!args || args.listenerIp === undefined) && !opts.urn) {
                throw new Error("Missing required property 'listenerIp'");
            }
            if ((!args || args.listenerPort === undefined) && !opts.urn) {
                throw new Error("Missing required property 'listenerPort'");
            }
            if ((!args || args.protocol === undefined) && !opts.urn) {
                throw new Error("Missing required property 'protocol'");
            }
            resourceInputs["applicationLoadbalancerId"] = args ? args.applicationLoadbalancerId : undefined;
            resourceInputs["clientTimeout"] = args ? args.clientTimeout : undefined;
            resourceInputs["datacenterId"] = args ? args.datacenterId : undefined;
            resourceInputs["httpRules"] = args ? args.httpRules : undefined;
            resourceInputs["listenerIp"] = args ? args.listenerIp : undefined;
            resourceInputs["listenerPort"] = args ? args.listenerPort : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["protocol"] = args ? args.protocol : undefined;
            resourceInputs["serverCertificates"] = args ? args.serverCertificates : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ApplicationLoadbalancerForwardingrule.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ApplicationLoadbalancerForwardingrule resources.
 */
export interface ApplicationLoadbalancerForwardingruleState {
    /**
     * [string] The ID of Application Load Balancer.
     */
    applicationLoadbalancerId?: pulumi.Input<string>;
    /**
     * [int] The maximum time in milliseconds to wait for the client to acknowledge or send data; default is 50,000 (50 seconds).
     */
    clientTimeout?: pulumi.Input<number>;
    /**
     * [string] The ID of a Virtual Data Center.
     */
    datacenterId?: pulumi.Input<string>;
    /**
     * [list] Array of items in that collection
     */
    httpRules?: pulumi.Input<pulumi.Input<inputs.ApplicationLoadbalancerForwardingruleHttpRule>[]>;
    /**
     * [string] Listening (inbound) IP.
     */
    listenerIp?: pulumi.Input<string>;
    /**
     * [int] Listening (inbound) port number; valid range is 1 to 65535.
     */
    listenerPort?: pulumi.Input<number>;
    /**
     * [string] The unique name of the Application Load Balancer HTTP rule.
     */
    name?: pulumi.Input<string>;
    /**
     * [string] Balancing protocol.
     */
    protocol?: pulumi.Input<string>;
    /**
     * [list] Array of certificate ids. You can create certificates with the certificate resource.
     */
    serverCertificates?: pulumi.Input<pulumi.Input<string>[]>;
}

/**
 * The set of arguments for constructing a ApplicationLoadbalancerForwardingrule resource.
 */
export interface ApplicationLoadbalancerForwardingruleArgs {
    /**
     * [string] The ID of Application Load Balancer.
     */
    applicationLoadbalancerId: pulumi.Input<string>;
    /**
     * [int] The maximum time in milliseconds to wait for the client to acknowledge or send data; default is 50,000 (50 seconds).
     */
    clientTimeout?: pulumi.Input<number>;
    /**
     * [string] The ID of a Virtual Data Center.
     */
    datacenterId: pulumi.Input<string>;
    /**
     * [list] Array of items in that collection
     */
    httpRules?: pulumi.Input<pulumi.Input<inputs.ApplicationLoadbalancerForwardingruleHttpRule>[]>;
    /**
     * [string] Listening (inbound) IP.
     */
    listenerIp: pulumi.Input<string>;
    /**
     * [int] Listening (inbound) port number; valid range is 1 to 65535.
     */
    listenerPort: pulumi.Input<number>;
    /**
     * [string] The unique name of the Application Load Balancer HTTP rule.
     */
    name?: pulumi.Input<string>;
    /**
     * [string] Balancing protocol.
     */
    protocol: pulumi.Input<string>;
    /**
     * [list] Array of certificate ids. You can create certificates with the certificate resource.
     */
    serverCertificates?: pulumi.Input<pulumi.Input<string>[]>;
}
