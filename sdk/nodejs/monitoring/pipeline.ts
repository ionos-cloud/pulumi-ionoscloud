// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Manages a **Monitoring pipeline**.
 *
 * > ⚠️  Only tokens are accepted for authorization in the **monitoring_pipeline** resource. Please ensure you are using tokens as other methods will not be valid.
 *
 * ## Usage example
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = new ionoscloud.monitoring.Pipeline("example", {
 *     location: "es/vit",
 *     name: "pipelineExample",
 * });
 * ```
 *
 * **NOTE:** The default timeout for all operations is 60 minutes. If you want to change the default value, you can use `timeouts` attribute inside the resource:
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = new ionoscloud.monitoring.Pipeline("example", {
 *     location: "es/vit",
 *     name: "pipelineExample",
 * });
 * ```
 *
 * ## Import
 *
 * In order to import a Monitoring pipeline, you can define an empty Monitoring pipeline resource in the plan:
 *
 * hcl
 *
 * resource "ionoscloud_monitoring_pipeline" "example" {
 *
 * }
 *
 * The resource can be imported using the `location` and `pipeline_id`, for example:
 *
 * ```sh
 * $ pulumi import ionoscloud:monitoring/pipeline:Pipeline example location:pipeline_id
 * ```
 */
export class Pipeline extends pulumi.CustomResource {
    /**
     * Get an existing Pipeline resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PipelineState, opts?: pulumi.CustomResourceOptions): Pipeline {
        return new Pipeline(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:monitoring/pipeline:Pipeline';

    /**
     * Returns true if the given object is an instance of Pipeline.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Pipeline {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Pipeline.__pulumiType;
    }

    /**
     * [string] The endpoint of the Grafana instance.
     */
    public /*out*/ readonly grafanaEndpoint!: pulumi.Output<string>;
    /**
     * [string] The HTTP endpoint of the monitoring instance.
     */
    public /*out*/ readonly httpEndpoint!: pulumi.Output<string>;
    /**
     * (Sensitive)[string] The key used to connect to the monitoring pipeline.
     *
     * > **⚠ NOTE:** `IONOS_API_URL_MONITORING` can be used to set a custom API URL for the resource. `location` field needs to be empty, otherwise it will override the custom API URL.
     */
    public /*out*/ readonly key!: pulumi.Output<string>;
    /**
     * [string] The location of the Monitoring pipeline. Default is `de/fra`. It can be one of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`. If this is not set and if no value is provided for the `IONOS_API_URL_MONITORING` env var, the default `location` will be: `de/fra`.
     */
    public readonly location!: pulumi.Output<string | undefined>;
    /**
     * [string] The name of the Monitoring pipeline.
     */
    public readonly name!: pulumi.Output<string>;
    public readonly timeouts!: pulumi.Output<outputs.monitoring.PipelineTimeouts | undefined>;

    /**
     * Create a Pipeline resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: PipelineArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PipelineArgs | PipelineState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as PipelineState | undefined;
            resourceInputs["grafanaEndpoint"] = state ? state.grafanaEndpoint : undefined;
            resourceInputs["httpEndpoint"] = state ? state.httpEndpoint : undefined;
            resourceInputs["key"] = state ? state.key : undefined;
            resourceInputs["location"] = state ? state.location : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["timeouts"] = state ? state.timeouts : undefined;
        } else {
            const args = argsOrState as PipelineArgs | undefined;
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["timeouts"] = args ? args.timeouts : undefined;
            resourceInputs["grafanaEndpoint"] = undefined /*out*/;
            resourceInputs["httpEndpoint"] = undefined /*out*/;
            resourceInputs["key"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const aliasOpts = { aliases: [{ type: "ionoscloud:objectstorage/monitoringPipeline:MonitoringPipeline" }] };
        opts = pulumi.mergeOptions(opts, aliasOpts);
        const secretOpts = { additionalSecretOutputs: ["key"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(Pipeline.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Pipeline resources.
 */
export interface PipelineState {
    /**
     * [string] The endpoint of the Grafana instance.
     */
    grafanaEndpoint?: pulumi.Input<string>;
    /**
     * [string] The HTTP endpoint of the monitoring instance.
     */
    httpEndpoint?: pulumi.Input<string>;
    /**
     * (Sensitive)[string] The key used to connect to the monitoring pipeline.
     *
     * > **⚠ NOTE:** `IONOS_API_URL_MONITORING` can be used to set a custom API URL for the resource. `location` field needs to be empty, otherwise it will override the custom API URL.
     */
    key?: pulumi.Input<string>;
    /**
     * [string] The location of the Monitoring pipeline. Default is `de/fra`. It can be one of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`. If this is not set and if no value is provided for the `IONOS_API_URL_MONITORING` env var, the default `location` will be: `de/fra`.
     */
    location?: pulumi.Input<string>;
    /**
     * [string] The name of the Monitoring pipeline.
     */
    name?: pulumi.Input<string>;
    timeouts?: pulumi.Input<inputs.monitoring.PipelineTimeouts>;
}

/**
 * The set of arguments for constructing a Pipeline resource.
 */
export interface PipelineArgs {
    /**
     * [string] The location of the Monitoring pipeline. Default is `de/fra`. It can be one of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`. If this is not set and if no value is provided for the `IONOS_API_URL_MONITORING` env var, the default `location` will be: `de/fra`.
     */
    location?: pulumi.Input<string>;
    /**
     * [string] The name of the Monitoring pipeline.
     */
    name?: pulumi.Input<string>;
    timeouts?: pulumi.Input<inputs.monitoring.PipelineTimeouts>;
}
