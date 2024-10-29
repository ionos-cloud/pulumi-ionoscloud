// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.ionoscloud.ContainerRegistryTokenArgs;
import com.pulumi.ionoscloud.Utilities;
import com.pulumi.ionoscloud.inputs.ContainerRegistryTokenState;
import com.pulumi.ionoscloud.outputs.ContainerRegistryTokenCredential;
import com.pulumi.ionoscloud.outputs.ContainerRegistryTokenScope;
import java.lang.String;
import java.util.List;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * Manages an **Container Registry Token** on IonosCloud.
 * 
 * ## Example Usage
 * 
 * &lt;!--Start PulumiCodeChooser --&gt;
 * <pre>
 * {@code
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.ionoscloud.ContainerRegistry;
 * import com.pulumi.ionoscloud.ContainerRegistryArgs;
 * import com.pulumi.ionoscloud.inputs.ContainerRegistryGarbageCollectionScheduleArgs;
 * import com.pulumi.ionoscloud.ContainerRegistryToken;
 * import com.pulumi.ionoscloud.ContainerRegistryTokenArgs;
 * import com.pulumi.ionoscloud.inputs.ContainerRegistryTokenScopeArgs;
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
 *         var exampleContainerRegistry = new ContainerRegistry("exampleContainerRegistry", ContainerRegistryArgs.builder()        
 *             .garbageCollectionSchedule(ContainerRegistryGarbageCollectionScheduleArgs.builder()
 *                 .days(                
 *                     "Monday",
 *                     "Tuesday")
 *                 .time("05:19:00+00:00")
 *                 .build())
 *             .location("de/fra")
 *             .build());
 * 
 *         var exampleContainerRegistryToken = new ContainerRegistryToken("exampleContainerRegistryToken", ContainerRegistryTokenArgs.builder()        
 *             .expiryDate("2023-01-13 16:27:42Z")
 *             .scopes(ContainerRegistryTokenScopeArgs.builder()
 *                 .actions("push")
 *                 .name("Scope1")
 *                 .type("repository")
 *                 .build())
 *             .status("enabled")
 *             .registryId(exampleContainerRegistry.id())
 *             .savePasswordToFile("pass.txt")
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
 * Resource Container Registry Token can be imported using the `container registry id` and `resource id`, e.g.
 * 
 * ```sh
 * $ pulumi import ionoscloud:index/containerRegistryToken:ContainerRegistryToken mycrtoken {container_registry uuid}/{container_registry_token uuid}
 * ```
 * 
 */
@ResourceType(type="ionoscloud:index/containerRegistryToken:ContainerRegistryToken")
public class ContainerRegistryToken extends com.pulumi.resources.CustomResource {
    @Export(name="credentials", refs={List.class,ContainerRegistryTokenCredential.class}, tree="[0,1]")
    private Output<List<ContainerRegistryTokenCredential>> credentials;

    public Output<List<ContainerRegistryTokenCredential>> credentials() {
        return this.credentials;
    }
    @Export(name="expiryDate", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> expiryDate;

    public Output<Optional<String>> expiryDate() {
        return Codegen.optional(this.expiryDate);
    }
    /**
     * [string]
     * 
     */
    @Export(name="name", refs={String.class}, tree="[0]")
    private Output<String> name;

    /**
     * @return [string]
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    @Export(name="registryId", refs={String.class}, tree="[0]")
    private Output<String> registryId;

    public Output<String> registryId() {
        return this.registryId;
    }
    /**
     * [string] Saves token password to file. Only works on create. Takes as argument a file name, or a file path
     * 
     * &gt; **⚠ WARNING** `save_password_to_file` must be used with caution.
     * It will save the password(token) returned on create to a file. This is the only way to get the token.
     * 
     */
    @Export(name="savePasswordToFile", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> savePasswordToFile;

    /**
     * @return [string] Saves token password to file. Only works on create. Takes as argument a file name, or a file path
     * 
     * &gt; **⚠ WARNING** `save_password_to_file` must be used with caution.
     * It will save the password(token) returned on create to a file. This is the only way to get the token.
     * 
     */
    public Output<Optional<String>> savePasswordToFile() {
        return Codegen.optional(this.savePasswordToFile);
    }
    /**
     * [map]
     * 
     */
    @Export(name="scopes", refs={List.class,ContainerRegistryTokenScope.class}, tree="[0,1]")
    private Output<List<ContainerRegistryTokenScope>> scopes;

    /**
     * @return [map]
     * 
     */
    public Output<List<ContainerRegistryTokenScope>> scopes() {
        return this.scopes;
    }
    /**
     * [string] Must have on of the values: `enabled`, `disabled`
     * 
     */
    @Export(name="status", refs={String.class}, tree="[0]")
    private Output<String> status;

    /**
     * @return [string] Must have on of the values: `enabled`, `disabled`
     * 
     */
    public Output<String> status() {
        return this.status;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public ContainerRegistryToken(java.lang.String name) {
        this(name, ContainerRegistryTokenArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public ContainerRegistryToken(java.lang.String name, ContainerRegistryTokenArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public ContainerRegistryToken(java.lang.String name, ContainerRegistryTokenArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ionoscloud:index/containerRegistryToken:ContainerRegistryToken", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()), false);
    }

    private ContainerRegistryToken(java.lang.String name, Output<java.lang.String> id, @Nullable ContainerRegistryTokenState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ionoscloud:index/containerRegistryToken:ContainerRegistryToken", name, state, makeResourceOptions(options, id), false);
    }

    private static ContainerRegistryTokenArgs makeArgs(ContainerRegistryTokenArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? ContainerRegistryTokenArgs.Empty : args;
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
    public static ContainerRegistryToken get(java.lang.String name, Output<java.lang.String> id, @Nullable ContainerRegistryTokenState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new ContainerRegistryToken(name, id, state, options);
    }
}
