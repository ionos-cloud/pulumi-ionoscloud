// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.ionoscloud.ApplicationLoadbalancerArgs;
import com.pulumi.ionoscloud.Utilities;
import com.pulumi.ionoscloud.inputs.ApplicationLoadbalancerState;
import com.pulumi.ionoscloud.outputs.ApplicationLoadbalancerFlowlog;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * Manages an **Application Load Balancer** on IonosCloud.
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
 * import com.pulumi.ionoscloud.ApplicationLoadbalancer;
 * import com.pulumi.ionoscloud.ApplicationLoadbalancerArgs;
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
 *         var exampleDatacenter = new Datacenter("exampleDatacenter", DatacenterArgs.builder()        
 *             .location("us/las")
 *             .description("datacenter description")
 *             .secAuthProtection(false)
 *             .build());
 * 
 *         var example1 = new Lan("example1", LanArgs.builder()        
 *             .datacenterId(exampleDatacenter.id())
 *             .public_(true)
 *             .build());
 * 
 *         var example2 = new Lan("example2", LanArgs.builder()        
 *             .datacenterId(exampleDatacenter.id())
 *             .public_(true)
 *             .build());
 * 
 *         var exampleApplicationLoadbalancer = new ApplicationLoadbalancer("exampleApplicationLoadbalancer", ApplicationLoadbalancerArgs.builder()        
 *             .datacenterId(exampleDatacenter.id())
 *             .listenerLan(example1.id())
 *             .ips("10.12.118.224")
 *             .targetLan(example2.id())
 *             .lbPrivateIps("10.13.72.225/24")
 *             .centralLogging(true)
 *             .loggingFormat("%{+Q}o %{-Q}ci - - [%trg] %r %ST %B \"\" \"\" %cp %ms %ft %b %s %TR %Tw %Tc %Tr %Ta %tsc %ac %fc %bc %sc %rc %sq %bq %CC %CS %hrl %hsl")
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
 * Resource Application Load Balancer can be imported using the `resource id` and `datacenter id`, e.g.
 * 
 * ```sh
 * $ pulumi import ionoscloud:index/applicationLoadbalancer:ApplicationLoadbalancer myalb {datacenter uuid}/{applicationLoadBalancer uuid}
 * ```
 * 
 */
@ResourceType(type="ionoscloud:index/applicationLoadbalancer:ApplicationLoadbalancer")
public class ApplicationLoadbalancer extends com.pulumi.resources.CustomResource {
    /**
     * [bool] Turn logging on and off for this product. Default value is &#39;false&#39;.
     * 
     */
    @Export(name="centralLogging", refs={Boolean.class}, tree="[0]")
    private Output</* @Nullable */ Boolean> centralLogging;

    /**
     * @return [bool] Turn logging on and off for this product. Default value is &#39;false&#39;.
     * 
     */
    public Output<Optional<Boolean>> centralLogging() {
        return Codegen.optional(this.centralLogging);
    }
    /**
     * [string] ID of the datacenter.
     * 
     */
    @Export(name="datacenterId", refs={String.class}, tree="[0]")
    private Output<String> datacenterId;

    /**
     * @return [string] ID of the datacenter.
     * 
     */
    public Output<String> datacenterId() {
        return this.datacenterId;
    }
    /**
     * [list] Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
     * 
     */
    @Export(name="flowlog", refs={ApplicationLoadbalancerFlowlog.class}, tree="[0]")
    private Output</* @Nullable */ ApplicationLoadbalancerFlowlog> flowlog;

    /**
     * @return [list] Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
     * 
     */
    public Output<Optional<ApplicationLoadbalancerFlowlog>> flowlog() {
        return Codegen.optional(this.flowlog);
    }
    /**
     * [set] Collection of the Application Load Balancer IP addresses. (Inbound and outbound) IPs of the listenerLan are customer-reserved public IPs for the public Load Balancers, and private IPs for the private Load Balancers.
     * 
     */
    @Export(name="ips", refs={List.class,String.class}, tree="[0,1]")
    private Output</* @Nullable */ List<String>> ips;

    /**
     * @return [set] Collection of the Application Load Balancer IP addresses. (Inbound and outbound) IPs of the listenerLan are customer-reserved public IPs for the public Load Balancers, and private IPs for the private Load Balancers.
     * 
     */
    public Output<Optional<List<String>>> ips() {
        return Codegen.optional(this.ips);
    }
    /**
     * [set] Collection of private IP addresses with the subnet mask of the Application Load Balancer. IPs must contain valid a subnet mask. If no IP is provided, the system will generate an IP with /24 subnet.
     * 
     */
    @Export(name="lbPrivateIps", refs={List.class,String.class}, tree="[0,1]")
    private Output</* @Nullable */ List<String>> lbPrivateIps;

    /**
     * @return [set] Collection of private IP addresses with the subnet mask of the Application Load Balancer. IPs must contain valid a subnet mask. If no IP is provided, the system will generate an IP with /24 subnet.
     * 
     */
    public Output<Optional<List<String>>> lbPrivateIps() {
        return Codegen.optional(this.lbPrivateIps);
    }
    /**
     * [int] ID of the listening (inbound) LAN.
     * 
     */
    @Export(name="listenerLan", refs={Integer.class}, tree="[0]")
    private Output<Integer> listenerLan;

    /**
     * @return [int] ID of the listening (inbound) LAN.
     * 
     */
    public Output<Integer> listenerLan() {
        return this.listenerLan;
    }
    /**
     * Specifies the format of the logs.
     * 
     */
    @Export(name="loggingFormat", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> loggingFormat;

    /**
     * @return Specifies the format of the logs.
     * 
     */
    public Output<Optional<String>> loggingFormat() {
        return Codegen.optional(this.loggingFormat);
    }
    /**
     * [string] Specifies the name of the flow log.
     * 
     * ⚠️ **Note:**: Removing the `flowlog` forces re-creation of the application load balancer resource.
     * 
     */
    @Export(name="name", refs={String.class}, tree="[0]")
    private Output<String> name;

    /**
     * @return [string] Specifies the name of the flow log.
     * 
     * ⚠️ **Note:**: Removing the `flowlog` forces re-creation of the application load balancer resource.
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    /**
     * [int] ID of the balanced private target LAN (outbound).
     * 
     */
    @Export(name="targetLan", refs={Integer.class}, tree="[0]")
    private Output<Integer> targetLan;

    /**
     * @return [int] ID of the balanced private target LAN (outbound).
     * 
     */
    public Output<Integer> targetLan() {
        return this.targetLan;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public ApplicationLoadbalancer(java.lang.String name) {
        this(name, ApplicationLoadbalancerArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public ApplicationLoadbalancer(java.lang.String name, ApplicationLoadbalancerArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public ApplicationLoadbalancer(java.lang.String name, ApplicationLoadbalancerArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ionoscloud:index/applicationLoadbalancer:ApplicationLoadbalancer", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()), false);
    }

    private ApplicationLoadbalancer(java.lang.String name, Output<java.lang.String> id, @Nullable ApplicationLoadbalancerState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ionoscloud:index/applicationLoadbalancer:ApplicationLoadbalancer", name, state, makeResourceOptions(options, id), false);
    }

    private static ApplicationLoadbalancerArgs makeArgs(ApplicationLoadbalancerArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? ApplicationLoadbalancerArgs.Empty : args;
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
    public static ApplicationLoadbalancer get(java.lang.String name, Output<java.lang.String> id, @Nullable ApplicationLoadbalancerState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new ApplicationLoadbalancer(name, id, state, options);
    }
}
