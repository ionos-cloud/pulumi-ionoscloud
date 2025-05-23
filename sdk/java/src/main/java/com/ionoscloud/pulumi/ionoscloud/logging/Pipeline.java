// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.logging;

import com.ionoscloud.pulumi.ionoscloud.Utilities;
import com.ionoscloud.pulumi.ionoscloud.logging.PipelineArgs;
import com.ionoscloud.pulumi.ionoscloud.logging.inputs.PipelineState;
import com.ionoscloud.pulumi.ionoscloud.logging.outputs.PipelineLog;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import java.lang.String;
import java.util.List;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * Manages a **Logging pipeline**.
 * 
 * &gt; ⚠️  Only tokens are accepted for authorization in the **logging_pipeline** resource. Please ensure you are using tokens as other methods will not be valid.
 * 
 * ## Usage example
 * 
 * &lt;!--Start PulumiCodeChooser --&gt;
 * <pre>
 * {@code
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.ionoscloud.logging.Pipeline;
 * import com.pulumi.ionoscloud.logging.PipelineArgs;
 * import com.pulumi.ionoscloud.logging.inputs.PipelineLogArgs;
 * import java.util.List;
 * import java.util.ArrayList;
 * import java.util.Map;
 * import java.io.File;
 * import java.nio.file.Files;
 * import java.nio.file.Paths;
 * 
 * public class App {
 *     public static void main(String[] args) {
 *         Pulumi.run(App::stack);
 *     }
 * 
 *     public static void stack(Context ctx) {
 *         var example = new Pipeline("example", PipelineArgs.builder()
 *             .location("es/vit")
 *             .name("pipelineexample")
 *             .logs(            
 *                 PipelineLogArgs.builder()
 *                     .source("kubernetes")
 *                     .tag("tagexample")
 *                     .protocol("http")
 *                     .destinations(PipelineLogDestinationArgs.builder()
 *                         .type("loki")
 *                         .retentionInDays(7)
 *                         .build())
 *                     .build(),
 *                 PipelineLogArgs.builder()
 *                     .source("kubernetes")
 *                     .tag("anothertagexample")
 *                     .protocol("tcp")
 *                     .destinations(PipelineLogDestinationArgs.builder()
 *                         .type("loki")
 *                         .retentionInDays(7)
 *                         .build())
 *                     .build())
 *             .build());
 * 
 *     }
 * }
 * }
 * </pre>
 * &lt;!--End PulumiCodeChooser --&gt;
 * 
 * ## Import
 * 
 * In order to import a Logging pipeline, you can define an empty Logging pipeline resource in the plan:
 * 
 * hcl
 * 
 * resource &#34;ionoscloud_logging_pipeline&#34; &#34;example&#34; {
 * 
 * }
 * 
 * The resource can be imported using the `location` and `pipeline_id`, for example:
 * 
 * ```sh
 * $ pulumi import ionoscloud:logging/pipeline:Pipeline example location:pipeline_id
 * ```
 * 
 */
@ResourceType(type="ionoscloud:logging/pipeline:Pipeline")
public class Pipeline extends com.pulumi.resources.CustomResource {
    /**
     * [string] The address of the client&#39;s grafana instance.
     * 
     */
    @Export(name="grafanaAddress", refs={String.class}, tree="[0]")
    private Output<String> grafanaAddress;

    /**
     * @return [string] The address of the client&#39;s grafana instance.
     * 
     */
    public Output<String> grafanaAddress() {
        return this.grafanaAddress;
    }
    /**
     * [string] The location of the Logging pipeline. Default: `de/txl` One of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`. If this is not set and if no value is provided for the `IONOS_API_URL` env var, the default `location` will be: `de/fra`.
     * 
     */
    @Export(name="location", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> location;

    /**
     * @return [string] The location of the Logging pipeline. Default: `de/txl` One of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`. If this is not set and if no value is provided for the `IONOS_API_URL` env var, the default `location` will be: `de/fra`.
     * 
     */
    public Output<Optional<String>> location() {
        return Codegen.optional(this.location);
    }
    /**
     * [list] Pipeline logs, a list that contains elements with the following structure:
     * 
     */
    @Export(name="logs", refs={List.class,PipelineLog.class}, tree="[0,1]")
    private Output<List<PipelineLog>> logs;

    /**
     * @return [list] Pipeline logs, a list that contains elements with the following structure:
     * 
     */
    public Output<List<PipelineLog>> logs() {
        return this.logs;
    }
    /**
     * [string] The name of the Logging pipeline.
     * 
     */
    @Export(name="name", refs={String.class}, tree="[0]")
    private Output<String> name;

    /**
     * @return [string] The name of the Logging pipeline.
     * 
     */
    public Output<String> name() {
        return this.name;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public Pipeline(java.lang.String name) {
        this(name, PipelineArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public Pipeline(java.lang.String name, PipelineArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public Pipeline(java.lang.String name, PipelineArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ionoscloud:logging/pipeline:Pipeline", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()), false);
    }

    private Pipeline(java.lang.String name, Output<java.lang.String> id, @Nullable PipelineState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ionoscloud:logging/pipeline:Pipeline", name, state, makeResourceOptions(options, id), false);
    }

    private static PipelineArgs makeArgs(PipelineArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? PipelineArgs.Empty : args;
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<java.lang.String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .build();
        return com.pulumi.resources.CustomResourceOptions.merge(defaultOptions, options, id);
    }

    /**
     * Get an existing Host resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state
     * @param options Optional settings to control the behavior of the CustomResource.
     */
    public static Pipeline get(java.lang.String name, Output<java.lang.String> id, @Nullable PipelineState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new Pipeline(name, id, state, options);
    }
}
