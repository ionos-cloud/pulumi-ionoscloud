// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * The **Cube Server data source** can be used to search for and return existing servers.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 */
export function getCubeServer(args: GetCubeServerArgs, opts?: pulumi.InvokeOptions): Promise<GetCubeServerResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:index/getCubeServer:getCubeServer", {
        "datacenterId": args.datacenterId,
        "id": args.id,
        "name": args.name,
        "templateUuid": args.templateUuid,
    }, opts);
}

/**
 * A collection of arguments for invoking getCubeServer.
 */
export interface GetCubeServerArgs {
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
}

/**
 * A collection of values returned by getCubeServer.
 */
export interface GetCubeServerResult {
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
    readonly cdroms: outputs.GetCubeServerCdrom[];
    readonly cores: number;
    readonly cpuFamily: string;
    /**
     * The id of the datacenter
     */
    readonly datacenterId: string;
    /**
     * Id of the firewall rule
     */
    readonly id?: string;
    /**
     * Name of the firewall rule
     */
    readonly name?: string;
    /**
     * list of
     */
    readonly nics: outputs.GetCubeServerNic[];
    readonly ram: number;
    /**
     * The UUID of the template for creating a CUBE server; the available templates for CUBE servers can be found on the templates resource
     */
    readonly templateUuid?: string;
    readonly token: string;
    /**
     * Status of the virtual Machine
     */
    readonly vmState: string;
    /**
     * list of
     */
    readonly volumes: outputs.GetCubeServerVolume[];
}
/**
 * The **Cube Server data source** can be used to search for and return existing servers.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 */
export function getCubeServerOutput(args: GetCubeServerOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetCubeServerResult> {
    return pulumi.output(args).apply((a: any) => getCubeServer(a, opts))
}

/**
 * A collection of arguments for invoking getCubeServer.
 */
export interface GetCubeServerOutputArgs {
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
}
