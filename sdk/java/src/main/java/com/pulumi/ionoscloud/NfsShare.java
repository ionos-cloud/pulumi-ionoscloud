// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.ionoscloud.NfsShareArgs;
import com.pulumi.ionoscloud.Utilities;
import com.pulumi.ionoscloud.inputs.NfsShareState;
import com.pulumi.ionoscloud.outputs.NfsShareClientGroup;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * Creates and manages Network File Storage (NFS) Share objects on IonosCloud.
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
 * import com.pulumi.ionoscloud.compute.Datacenter;
 * import com.pulumi.ionoscloud.compute.DatacenterArgs;
 * import com.pulumi.ionoscloud.Lan;
 * import com.pulumi.ionoscloud.LanArgs;
 * import com.pulumi.ionoscloud.NfsCluster;
 * import com.pulumi.ionoscloud.NfsClusterArgs;
 * import com.pulumi.ionoscloud.inputs.NfsClusterNfsArgs;
 * import com.pulumi.ionoscloud.inputs.NfsClusterConnectionsArgs;
 * import com.pulumi.ionoscloud.NfsShare;
 * import com.pulumi.ionoscloud.NfsShareArgs;
 * import com.pulumi.ionoscloud.inputs.NfsShareClientGroupArgs;
 * import com.pulumi.ionoscloud.inputs.NfsShareClientGroupNfsArgs;
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
 *         // Basic example
 *         var nfsDc = new Datacenter("nfsDc", DatacenterArgs.builder()        
 *             .location("de/txl")
 *             .description("Datacenter Description")
 *             .secAuthProtection(false)
 *             .build());
 * 
 *         var nfsLan = new Lan("nfsLan", LanArgs.builder()        
 *             .datacenterId(nfsDc.id())
 *             .public_(false)
 *             .build());
 * 
 *         var exampleNfsCluster = new NfsCluster("exampleNfsCluster", NfsClusterArgs.builder()        
 *             .location("de/txl")
 *             .size(2)
 *             .nfs(NfsClusterNfsArgs.builder()
 *                 .minVersion("4.2")
 *                 .build())
 *             .connections(NfsClusterConnectionsArgs.builder()
 *                 .datacenterId(nfsDc.id())
 *                 .ipAddress("192.168.100.10/24")
 *                 .lan(nfsLan.id())
 *                 .build())
 *             .build());
 * 
 *         var exampleNfsShare = new NfsShare("exampleNfsShare", NfsShareArgs.builder()        
 *             .location("de/txl")
 *             .clusterId(exampleNfsCluster.id())
 *             .quota(512)
 *             .gid(512)
 *             .uid(512)
 *             .clientGroups(NfsShareClientGroupArgs.builder()
 *                 .description("Client Group 1")
 *                 .ipNetworks("10.234.50.0/24")
 *                 .hosts("10.234.62.123")
 *                 .nfs(NfsShareClientGroupNfsArgs.builder()
 *                     .squash("all-anonymous")
 *                     .build())
 *                 .build())
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
 * A Network File Storage Share resource can be imported using its `location`, `cluster_id` and `resource id`:
 * 
 * ```sh
 * $ pulumi import ionoscloud:index/nfsShare:NfsShare name location:cluster_id:resource_id
 * ```
 * 
 */
@ResourceType(type="ionoscloud:index/nfsShare:NfsShare")
public class NfsShare extends com.pulumi.resources.CustomResource {
    /**
     * The groups of clients are the systems connecting to the Network File Storage cluster. Each group includes:
     * 
     */
    @Export(name="clientGroups", refs={List.class,NfsShareClientGroup.class}, tree="[0,1]")
    private Output<List<NfsShareClientGroup>> clientGroups;

    /**
     * @return The groups of clients are the systems connecting to the Network File Storage cluster. Each group includes:
     * 
     */
    public Output<List<NfsShareClientGroup>> clientGroups() {
        return this.clientGroups;
    }
    /**
     * The ID of the Network File Storage Cluster.
     * 
     */
    @Export(name="clusterId", refs={String.class}, tree="[0]")
    private Output<String> clusterId;

    /**
     * @return The ID of the Network File Storage Cluster.
     * 
     */
    public Output<String> clusterId() {
        return this.clusterId;
    }
    /**
     * The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
     * 
     */
    @Export(name="gid", refs={Integer.class}, tree="[0]")
    private Output</* @Nullable */ Integer> gid;

    /**
     * @return The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
     * 
     */
    public Output<Optional<Integer>> gid() {
        return Codegen.optional(this.gid);
    }
    /**
     * The location of the Network File Storage Cluster.
     * 
     */
    @Export(name="location", refs={String.class}, tree="[0]")
    private Output<String> location;

    /**
     * @return The location of the Network File Storage Cluster.
     * 
     */
    public Output<String> location() {
        return this.location;
    }
    /**
     * The directory being exported.
     * 
     */
    @Export(name="name", refs={String.class}, tree="[0]")
    private Output<String> name;

    /**
     * @return The directory being exported.
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    /**
     * Path to the NFS export. The NFS path is the path to the directory being exported.
     * 
     */
    @Export(name="nfsPath", refs={String.class}, tree="[0]")
    private Output<String> nfsPath;

    /**
     * @return Path to the NFS export. The NFS path is the path to the directory being exported.
     * 
     */
    public Output<String> nfsPath() {
        return this.nfsPath;
    }
    /**
     * The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The quota can be disabled using `0`. Default is `0`.
     * 
     */
    @Export(name="quota", refs={Integer.class}, tree="[0]")
    private Output</* @Nullable */ Integer> quota;

    /**
     * @return The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The quota can be disabled using `0`. Default is `0`.
     * 
     */
    public Output<Optional<Integer>> quota() {
        return Codegen.optional(this.quota);
    }
    /**
     * The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
     * 
     */
    @Export(name="uid", refs={Integer.class}, tree="[0]")
    private Output</* @Nullable */ Integer> uid;

    /**
     * @return The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
     * 
     */
    public Output<Optional<Integer>> uid() {
        return Codegen.optional(this.uid);
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public NfsShare(java.lang.String name) {
        this(name, NfsShareArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public NfsShare(java.lang.String name, NfsShareArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public NfsShare(java.lang.String name, NfsShareArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ionoscloud:index/nfsShare:NfsShare", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()), false);
    }

    private NfsShare(java.lang.String name, Output<java.lang.String> id, @Nullable NfsShareState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ionoscloud:index/nfsShare:NfsShare", name, state, makeResourceOptions(options, id), false);
    }

    private static NfsShareArgs makeArgs(NfsShareArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? NfsShareArgs.Empty : args;
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
    public static NfsShare get(java.lang.String name, Output<java.lang.String> id, @Nullable NfsShareState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new NfsShare(name, id, state, options);
    }
}
