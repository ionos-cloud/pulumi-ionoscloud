// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * The **Server data source** can be used to search for and return existing servers.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 */
export function getServer(args: GetServerArgs, opts?: pulumi.InvokeOptions): Promise<GetServerResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:compute/getServer:getServer", {
        "datacenterId": args.datacenterId,
        "id": args.id,
        "name": args.name,
        "templateUuid": args.templateUuid,
        "type": args.type,
    }, opts);
}

/**
 * A collection of arguments for invoking getServer.
 */
export interface GetServerArgs {
    /**
     * Datacenter's UUID.
     */
    datacenterId: string;
    /**
     * ID of the server you want to search for.
     *
     * `datacenterId` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
     */
    id?: string;
    /**
     * Name of an existing server that you want to search for.
     */
    name?: string;
    /**
     * The UUID of the template for creating a CUBE server; the available templates for CUBE servers can be found on the templates resource
     */
    templateUuid?: string;
    /**
     * The type of firewall rule
     */
    type?: string;
}

/**
 * A collection of values returned by getServer.
 */
export interface GetServerResult {
    /**
     * The availability zone in which the volume should exist
     */
    readonly availabilityZone: string;
    readonly bootCdrom: string;
    readonly bootImage: string;
    readonly bootVolume: string;
    /**
     * list of
     */
    readonly cdroms: outputs.compute.GetServerCdrom[];
    /**
     * The total number of cores for the server
     */
    readonly cores: number;
    /**
     * CPU architecture on which server gets provisioned; not all CPU architectures are available in all datacenter regions; available CPU architectures can be retrieved from the datacenter resource.
     */
    readonly cpuFamily: string;
    /**
     * The id of the datacenter
     */
    readonly datacenterId: string;
    /**
     * The Id of the label
     */
    readonly id?: string;
    /**
     * list of
     */
    readonly labels: outputs.compute.GetServerLabel[];
    /**
     * Name of the firewall rule
     */
    readonly name?: string;
    /**
     * list of
     */
    readonly nics: outputs.compute.GetServerNic[];
    /**
     * The amount of memory for the server in MB
     */
    readonly ram: number;
    /**
     * The UUID of the template for creating a CUBE server; the available templates for CUBE servers can be found on the templates resource
     */
    readonly templateUuid?: string;
    readonly token: string;
    /**
     * The type of firewall rule
     */
    readonly type: string;
    /**
     * Status of the virtual Machine
     */
    readonly vmState: string;
    /**
     * list of
     */
    readonly volumes: outputs.compute.GetServerVolume[];
}
/**
 * The **Server data source** can be used to search for and return existing servers.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 */
export function getServerOutput(args: GetServerOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetServerResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:compute/getServer:getServer", {
        "datacenterId": args.datacenterId,
        "id": args.id,
        "name": args.name,
        "templateUuid": args.templateUuid,
        "type": args.type,
    }, opts);
}

/**
 * A collection of arguments for invoking getServer.
 */
export interface GetServerOutputArgs {
    /**
     * Datacenter's UUID.
     */
    datacenterId: pulumi.Input<string>;
    /**
     * ID of the server you want to search for.
     *
     * `datacenterId` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
     */
    id?: pulumi.Input<string>;
    /**
     * Name of an existing server that you want to search for.
     */
    name?: pulumi.Input<string>;
    /**
     * The UUID of the template for creating a CUBE server; the available templates for CUBE servers can be found on the templates resource
     */
    templateUuid?: pulumi.Input<string>;
    /**
     * The type of firewall rule
     */
    type?: pulumi.Input<string>;
}
