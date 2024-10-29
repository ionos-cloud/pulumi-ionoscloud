// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.ionoscloud.ApigatewayArgs;
import com.pulumi.ionoscloud.Utilities;
import com.pulumi.ionoscloud.inputs.ApigatewayState;
import com.pulumi.ionoscloud.outputs.ApigatewayCustomDomain;
import java.lang.Boolean;
import java.lang.String;
import java.util.List;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * An API gateway consists of the generic rules and configurations.
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
 * import com.pulumi.ionoscloud.Apigateway;
 * import com.pulumi.ionoscloud.ApigatewayArgs;
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
 *         var example = new Apigateway("example", ApigatewayArgs.builder()        
 *             .metrics(true)
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
 * In order to import an API Gateway, you can define an empty API Gateway resource in the plan:
 * 
 * resource &#34;ionoscloud_apigateway&#34; &#34;example&#34; {
 * 
 * }
 * 
 * The resource can be imported using the `gateway_id`, for example:
 * 
 * ```sh
 * $ pulumi import ionoscloud:index/apigateway:Apigateway example {gateway_id}
 * ```
 * 
 */
@ResourceType(type="ionoscloud:index/apigateway:Apigateway")
public class Apigateway extends com.pulumi.resources.CustomResource {
    /**
     * [list] Custom domains for the API Gateway, a list that contains elements with the following structure:
     * 
     */
    @Export(name="customDomains", refs={List.class,ApigatewayCustomDomain.class}, tree="[0,1]")
    private Output</* @Nullable */ List<ApigatewayCustomDomain>> customDomains;

    /**
     * @return [list] Custom domains for the API Gateway, a list that contains elements with the following structure:
     * 
     */
    public Output<Optional<List<ApigatewayCustomDomain>>> customDomains() {
        return Codegen.optional(this.customDomains);
    }
    /**
     * [bool] Enable or disable logging. Defaults to `false`. **NOTE**: Central Logging must be enabled through the Logging API to enable this feature.
     * 
     */
    @Export(name="logs", refs={Boolean.class}, tree="[0]")
    private Output</* @Nullable */ Boolean> logs;

    /**
     * @return [bool] Enable or disable logging. Defaults to `false`. **NOTE**: Central Logging must be enabled through the Logging API to enable this feature.
     * 
     */
    public Output<Optional<Boolean>> logs() {
        return Codegen.optional(this.logs);
    }
    /**
     * [bool] Enable or disable metrics. Defaults to `false`.
     * 
     */
    @Export(name="metrics", refs={Boolean.class}, tree="[0]")
    private Output</* @Nullable */ Boolean> metrics;

    /**
     * @return [bool] Enable or disable metrics. Defaults to `false`.
     * 
     */
    public Output<Optional<Boolean>> metrics() {
        return Codegen.optional(this.metrics);
    }
    /**
     * [string] The domain name. Externally reachable.
     * 
     */
    @Export(name="name", refs={String.class}, tree="[0]")
    private Output<String> name;

    /**
     * @return [string] The domain name. Externally reachable.
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    /**
     * [string] The public endpoint of the API Gateway.
     * 
     */
    @Export(name="publicEndpoint", refs={String.class}, tree="[0]")
    private Output<String> publicEndpoint;

    /**
     * @return [string] The public endpoint of the API Gateway.
     * 
     */
    public Output<String> publicEndpoint() {
        return this.publicEndpoint;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public Apigateway(java.lang.String name) {
        this(name, ApigatewayArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public Apigateway(java.lang.String name, @Nullable ApigatewayArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public Apigateway(java.lang.String name, @Nullable ApigatewayArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ionoscloud:index/apigateway:Apigateway", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()), false);
    }

    private Apigateway(java.lang.String name, Output<java.lang.String> id, @Nullable ApigatewayState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ionoscloud:index/apigateway:Apigateway", name, state, makeResourceOptions(options, id), false);
    }

    private static ApigatewayArgs makeArgs(@Nullable ApigatewayArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? ApigatewayArgs.Empty : args;
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
    public static Apigateway get(java.lang.String name, Output<java.lang.String> id, @Nullable ApigatewayState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new Apigateway(name, id, state, options);
    }
}
