// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The **Template data source** can be used to search for and return existing templates by providing any of template properties (name, cores, ram, storage_size).
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 *
 * ### By Name
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.getTemplate({
 *     name: "CUBES S",
 * });
 * ```
 *
 * ### By Cores
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.getTemplate({
 *     cores: 6,
 * });
 * ```
 *
 * ### By Ram
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.getTemplate({
 *     ram: 49152,
 * });
 * ```
 *
 * ### By Storage Size
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.getTemplate({
 *     storageSize: 80,
 * });
 * ```
 */
export function getTemplate(args?: GetTemplateArgs, opts?: pulumi.InvokeOptions): Promise<GetTemplateResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:index/getTemplate:getTemplate", {
        "cores": args.cores,
        "name": args.name,
        "ram": args.ram,
        "storageSize": args.storageSize,
    }, opts);
}

/**
 * A collection of arguments for invoking getTemplate.
 */
export interface GetTemplateArgs {
    /**
     * The CPU cores count.
     */
    cores?: number;
    /**
     * A name of that resource.
     */
    name?: string;
    /**
     * The RAM size in MB.
     */
    ram?: number;
    /**
     * The storage size in GB.
     *
     * Any of the arguments ca be provided. If none, the datasource will return an error.
     */
    storageSize?: number;
}

/**
 * A collection of values returned by getTemplate.
 */
export interface GetTemplateResult {
    /**
     * The CPU cores count
     */
    readonly cores: number;
    /**
     * Id of template
     */
    readonly id: string;
    /**
     * Name of template
     */
    readonly name: string;
    /**
     * The RAM size in MB
     */
    readonly ram: number;
    /**
     * The storage size in GB
     */
    readonly storageSize: number;
}
/**
 * The **Template data source** can be used to search for and return existing templates by providing any of template properties (name, cores, ram, storage_size).
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 *
 * ### By Name
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.getTemplate({
 *     name: "CUBES S",
 * });
 * ```
 *
 * ### By Cores
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.getTemplate({
 *     cores: 6,
 * });
 * ```
 *
 * ### By Ram
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.getTemplate({
 *     ram: 49152,
 * });
 * ```
 *
 * ### By Storage Size
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.getTemplate({
 *     storageSize: 80,
 * });
 * ```
 */
export function getTemplateOutput(args?: GetTemplateOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetTemplateResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:index/getTemplate:getTemplate", {
        "cores": args.cores,
        "name": args.name,
        "ram": args.ram,
        "storageSize": args.storageSize,
    }, opts);
}

/**
 * A collection of arguments for invoking getTemplate.
 */
export interface GetTemplateOutputArgs {
    /**
     * The CPU cores count.
     */
    cores?: pulumi.Input<number>;
    /**
     * A name of that resource.
     */
    name?: pulumi.Input<string>;
    /**
     * The RAM size in MB.
     */
    ram?: pulumi.Input<number>;
    /**
     * The storage size in GB.
     *
     * Any of the arguments ca be provided. If none, the datasource will return an error.
     */
    storageSize?: pulumi.Input<number>;
}
