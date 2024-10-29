// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * The **Logging pipeline** datasource can be used to search for and return an existing Logging pipeline.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 *
 * > ⚠️  Only tokens are accepted for authorization in the **logging_pipeline** data source. Please ensure you are using tokens as other methods will not be valid.
 *
 * ## Example Usage
 *
 * ### By name
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.getLoggingPipeline({
 *     location: "de/txl",
 *     name: "pipeline_name",
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 */
export function getLoggingPipeline(args?: GetLoggingPipelineArgs, opts?: pulumi.InvokeOptions): Promise<GetLoggingPipelineResult> {
    args = args || {};

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:index/getLoggingPipeline:getLoggingPipeline", {
        "id": args.id,
        "location": args.location,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getLoggingPipeline.
 */
export interface GetLoggingPipelineArgs {
    /**
     * [string] The ID of the Logging pipeline you want to search for.
     */
    id?: string;
    /**
     * [string] The location of the Logging pipeline. Default: `de/txl`. One of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`.
     */
    location?: string;
    /**
     * [string] The name of the Logging pipeline you want to search for.
     *
     * Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
     */
    name?: string;
}

/**
 * A collection of values returned by getLoggingPipeline.
 */
export interface GetLoggingPipelineResult {
    /**
     * The address of the client's grafana instance.
     */
    readonly grafanaAddress: string;
    /**
     * The UUID of the Logging pipeline.
     */
    readonly id?: string;
    readonly location?: string;
    /**
     * [list] Pipeline logs, a list that contains elements with the following structure:
     */
    readonly logs: outputs.GetLoggingPipelineLog[];
    /**
     * The name of the Logging pipeline.
     */
    readonly name: string;
}
/**
 * The **Logging pipeline** datasource can be used to search for and return an existing Logging pipeline.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 *
 * > ⚠️  Only tokens are accepted for authorization in the **logging_pipeline** data source. Please ensure you are using tokens as other methods will not be valid.
 *
 * ## Example Usage
 *
 * ### By name
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.getLoggingPipeline({
 *     location: "de/txl",
 *     name: "pipeline_name",
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 */
export function getLoggingPipelineOutput(args?: GetLoggingPipelineOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetLoggingPipelineResult> {
    return pulumi.output(args).apply((a: any) => getLoggingPipeline(a, opts))
}

/**
 * A collection of arguments for invoking getLoggingPipeline.
 */
export interface GetLoggingPipelineOutputArgs {
    /**
     * [string] The ID of the Logging pipeline you want to search for.
     */
    id?: pulumi.Input<string>;
    /**
     * [string] The location of the Logging pipeline. Default: `de/txl`. One of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`.
     */
    location?: pulumi.Input<string>;
    /**
     * [string] The name of the Logging pipeline you want to search for.
     *
     * Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
     */
    name?: pulumi.Input<string>;
}
