// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.ionoscloud.IpblockArgs;
import com.pulumi.ionoscloud.Utilities;
import com.pulumi.ionoscloud.inputs.IpblockState;
import com.pulumi.ionoscloud.outputs.IpblockIpConsumer;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import javax.annotation.Nullable;

/**
 * Manages **IP Blocks** on IonosCloud. IP Blocks contain reserved public IP addresses that can be assigned servers or other resources.
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
 * import com.pulumi.ionoscloud.Ipblock;
 * import com.pulumi.ionoscloud.IpblockArgs;
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
 *         var example = new Ipblock("example", IpblockArgs.builder()        
 *             .location("us/las")
 *             .size(1)
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
 * Resource Ipblock can be imported using the `resource id`, e.g.
 * 
 * ```sh
 * $ pulumi import ionoscloud:index/ipblock:Ipblock myipblock {ipblock uuid}
 * ```
 * 
 */
@ResourceType(type="ionoscloud:index/ipblock:Ipblock")
public class Ipblock extends com.pulumi.resources.CustomResource {
    /**
     * Read-Only attribute. Lists consumption detail of an individual ip
     * 
     */
    @Export(name="ipConsumers", refs={List.class,IpblockIpConsumer.class}, tree="[0,1]")
    private Output<List<IpblockIpConsumer>> ipConsumers;

    /**
     * @return Read-Only attribute. Lists consumption detail of an individual ip
     * 
     */
    public Output<List<IpblockIpConsumer>> ipConsumers() {
        return this.ipConsumers;
    }
    /**
     * [integer] The list of IP addresses associated with this block.
     * 
     */
    @Export(name="ips", refs={List.class,String.class}, tree="[0,1]")
    private Output<List<String>> ips;

    /**
     * @return [integer] The list of IP addresses associated with this block.
     * 
     */
    public Output<List<String>> ips() {
        return this.ips;
    }
    /**
     * [string] The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
     * 
     */
    @Export(name="location", refs={String.class}, tree="[0]")
    private Output<String> location;

    /**
     * @return [string] The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
     * 
     */
    public Output<String> location() {
        return this.location;
    }
    /**
     * [string] The name of Ip Block
     * 
     */
    @Export(name="name", refs={String.class}, tree="[0]")
    private Output<String> name;

    /**
     * @return [string] The name of Ip Block
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    /**
     * [integer] The number of IP addresses to reserve for this block.
     * 
     */
    @Export(name="size", refs={Integer.class}, tree="[0]")
    private Output<Integer> size;

    /**
     * @return [integer] The number of IP addresses to reserve for this block.
     * 
     */
    public Output<Integer> size() {
        return this.size;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public Ipblock(java.lang.String name) {
        this(name, IpblockArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public Ipblock(java.lang.String name, IpblockArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public Ipblock(java.lang.String name, IpblockArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ionoscloud:index/ipblock:Ipblock", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()), false);
    }

    private Ipblock(java.lang.String name, Output<java.lang.String> id, @Nullable IpblockState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ionoscloud:index/ipblock:Ipblock", name, state, makeResourceOptions(options, id), false);
    }

    private static IpblockArgs makeArgs(IpblockArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? IpblockArgs.Empty : args;
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
    public static Ipblock get(java.lang.String name, Output<java.lang.String> id, @Nullable IpblockState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new Ipblock(name, id, state, options);
    }
}
