// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.ionoscloud.ApplicationLoadbalancerForwardingruleArgs;
import com.pulumi.ionoscloud.Utilities;
import com.pulumi.ionoscloud.inputs.ApplicationLoadbalancerForwardingruleState;
import com.pulumi.ionoscloud.outputs.ApplicationLoadbalancerForwardingruleHttpRule;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * Manages an **Application Load Balancer Forwarding Rule** on IonosCloud.
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
 * import com.pulumi.ionoscloud.Certificate;
 * import com.pulumi.ionoscloud.CertificateArgs;
 * import com.pulumi.ionoscloud.ApplicationLoadbalancerForwardingrule;
 * import com.pulumi.ionoscloud.ApplicationLoadbalancerForwardingruleArgs;
 * import com.pulumi.ionoscloud.inputs.ApplicationLoadbalancerForwardingruleHttpRuleArgs;
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
 *             .build());
 * 
 *         //optionally you can add a certificate to the application load balancer
 *         var cert = new Certificate("cert", CertificateArgs.builder()        
 *             .certificate(Files.readString(Paths.get("path_to_cert")))
 *             .certificateChain(Files.readString(Paths.get("path_to_cert_chain")))
 *             .privateKey(Files.readString(Paths.get("path_to_private_key")))
 *             .build());
 * 
 *         var exampleApplicationLoadbalancerForwardingrule = new ApplicationLoadbalancerForwardingrule("exampleApplicationLoadbalancerForwardingrule", ApplicationLoadbalancerForwardingruleArgs.builder()        
 *             .datacenterId(exampleDatacenter.id())
 *             .applicationLoadbalancerId(exampleApplicationLoadbalancer.id())
 *             .protocol("HTTP")
 *             .listenerIp("10.12.118.224")
 *             .listenerPort(8080)
 *             .clientTimeout(1000)
 *             .httpRules(            
 *                 ApplicationLoadbalancerForwardingruleHttpRuleArgs.builder()
 *                     .name("http_rule")
 *                     .type("REDIRECT")
 *                     .dropQuery(true)
 *                     .location("www.ionos.com")
 *                     .statusCode(301)
 *                     .conditions(ApplicationLoadbalancerForwardingruleHttpRuleConditionArgs.builder()
 *                         .type("HEADER")
 *                         .condition("EQUALS")
 *                         .negate(true)
 *                         .key("key")
 *                         .value("10.12.120.224/24")
 *                         .build())
 *                     .build(),
 *                 ApplicationLoadbalancerForwardingruleHttpRuleArgs.builder()
 *                     .name("http_rule_2")
 *                     .type("STATIC")
 *                     .dropQuery(false)
 *                     .statusCode(303)
 *                     .responseMessage("Response")
 *                     .contentType("text/plain")
 *                     .conditions(ApplicationLoadbalancerForwardingruleHttpRuleConditionArgs.builder()
 *                         .type("QUERY")
 *                         .condition("MATCHES")
 *                         .negate(false)
 *                         .key("key")
 *                         .value("10.12.120.224/24")
 *                         .build())
 *                     .build())
 *             .serverCertificates(cert.id())
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
 * Resource Application Load Balancer Forwarding Rule can be imported using the `resource id`, `alb id` and `datacenter id`, e.g.
 * 
 * ```sh
 * $ pulumi import ionoscloud:index/applicationLoadbalancerForwardingrule:ApplicationLoadbalancerForwardingrule myAlbRule {datacenter uuid}/{applicationLoadBalancer uuid}/{applicationLoadBalancerForwardingRule uuid}
 * ```
 * 
 */
@ResourceType(type="ionoscloud:index/applicationLoadbalancerForwardingrule:ApplicationLoadbalancerForwardingrule")
public class ApplicationLoadbalancerForwardingrule extends com.pulumi.resources.CustomResource {
    /**
     * [string] The ID of Application Load Balancer.
     * 
     */
    @Export(name="applicationLoadbalancerId", refs={String.class}, tree="[0]")
    private Output<String> applicationLoadbalancerId;

    /**
     * @return [string] The ID of Application Load Balancer.
     * 
     */
    public Output<String> applicationLoadbalancerId() {
        return this.applicationLoadbalancerId;
    }
    /**
     * [int] The maximum time in milliseconds to wait for the client to acknowledge or send data; default is 50,000 (50 seconds).
     * 
     */
    @Export(name="clientTimeout", refs={Integer.class}, tree="[0]")
    private Output<Integer> clientTimeout;

    /**
     * @return [int] The maximum time in milliseconds to wait for the client to acknowledge or send data; default is 50,000 (50 seconds).
     * 
     */
    public Output<Integer> clientTimeout() {
        return this.clientTimeout;
    }
    /**
     * [string] The ID of a Virtual Data Center.
     * 
     */
    @Export(name="datacenterId", refs={String.class}, tree="[0]")
    private Output<String> datacenterId;

    /**
     * @return [string] The ID of a Virtual Data Center.
     * 
     */
    public Output<String> datacenterId() {
        return this.datacenterId;
    }
    /**
     * [list] Array of items in that collection
     * 
     */
    @Export(name="httpRules", refs={List.class,ApplicationLoadbalancerForwardingruleHttpRule.class}, tree="[0,1]")
    private Output</* @Nullable */ List<ApplicationLoadbalancerForwardingruleHttpRule>> httpRules;

    /**
     * @return [list] Array of items in that collection
     * 
     */
    public Output<Optional<List<ApplicationLoadbalancerForwardingruleHttpRule>>> httpRules() {
        return Codegen.optional(this.httpRules);
    }
    /**
     * [string] Listening (inbound) IP.
     * 
     */
    @Export(name="listenerIp", refs={String.class}, tree="[0]")
    private Output<String> listenerIp;

    /**
     * @return [string] Listening (inbound) IP.
     * 
     */
    public Output<String> listenerIp() {
        return this.listenerIp;
    }
    /**
     * [int] Listening (inbound) port number; valid range is 1 to 65535.
     * 
     */
    @Export(name="listenerPort", refs={Integer.class}, tree="[0]")
    private Output<Integer> listenerPort;

    /**
     * @return [int] Listening (inbound) port number; valid range is 1 to 65535.
     * 
     */
    public Output<Integer> listenerPort() {
        return this.listenerPort;
    }
    /**
     * [string] The unique name of the Application Load Balancer HTTP rule.
     * 
     */
    @Export(name="name", refs={String.class}, tree="[0]")
    private Output<String> name;

    /**
     * @return [string] The unique name of the Application Load Balancer HTTP rule.
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    /**
     * [string] Balancing protocol.
     * 
     */
    @Export(name="protocol", refs={String.class}, tree="[0]")
    private Output<String> protocol;

    /**
     * @return [string] Balancing protocol.
     * 
     */
    public Output<String> protocol() {
        return this.protocol;
    }
    /**
     * [list] Array of certificate ids. You can create certificates with the certificate resource.
     * 
     */
    @Export(name="serverCertificates", refs={List.class,String.class}, tree="[0,1]")
    private Output</* @Nullable */ List<String>> serverCertificates;

    /**
     * @return [list] Array of certificate ids. You can create certificates with the certificate resource.
     * 
     */
    public Output<Optional<List<String>>> serverCertificates() {
        return Codegen.optional(this.serverCertificates);
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public ApplicationLoadbalancerForwardingrule(java.lang.String name) {
        this(name, ApplicationLoadbalancerForwardingruleArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public ApplicationLoadbalancerForwardingrule(java.lang.String name, ApplicationLoadbalancerForwardingruleArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public ApplicationLoadbalancerForwardingrule(java.lang.String name, ApplicationLoadbalancerForwardingruleArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ionoscloud:index/applicationLoadbalancerForwardingrule:ApplicationLoadbalancerForwardingrule", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()), false);
    }

    private ApplicationLoadbalancerForwardingrule(java.lang.String name, Output<java.lang.String> id, @Nullable ApplicationLoadbalancerForwardingruleState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ionoscloud:index/applicationLoadbalancerForwardingrule:ApplicationLoadbalancerForwardingrule", name, state, makeResourceOptions(options, id), false);
    }

    private static ApplicationLoadbalancerForwardingruleArgs makeArgs(ApplicationLoadbalancerForwardingruleArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? ApplicationLoadbalancerForwardingruleArgs.Empty : args;
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
    public static ApplicationLoadbalancerForwardingrule get(java.lang.String name, Output<java.lang.String> id, @Nullable ApplicationLoadbalancerForwardingruleState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new ApplicationLoadbalancerForwardingrule(name, id, state, options);
    }
}
