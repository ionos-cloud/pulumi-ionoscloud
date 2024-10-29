// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.ionoscloud.ServerArgs;
import com.pulumi.ionoscloud.Utilities;
import com.pulumi.ionoscloud.inputs.ServerState;
import com.pulumi.ionoscloud.outputs.ServerLabel;
import com.pulumi.ionoscloud.outputs.ServerNic;
import com.pulumi.ionoscloud.outputs.ServerVolume;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * ## Import
 * 
 * Resource Server can be imported using the `resource id` and the `datacenter id`, e.g.. Passing only resource id and datacenter id means that the first nic found linked to the server will be attached to it.
 * 
 * ```sh
 * $ pulumi import ionoscloud:index/server:Server myserver {datacenter uuid}/{server uuid}
 * ```
 * 
 * Optionally, you can pass `primary_nic` and `firewallrule_id` so terraform will know to import also the first nic and firewall rule (if it exists on the server):
 * 
 * ```sh
 * $ pulumi import ionoscloud:index/server:Server myserver {datacenter uuid}/{server uuid}/{primary nic id}/{firewall rule id}
 * ```
 * 
 */
@ResourceType(type="ionoscloud:index/server:Server")
public class Server extends com.pulumi.resources.CustomResource {
    /**
     * [string] The availability zone in which the server should exist. E.g: `AUTO`, `ZONE_1`, `ZONE_2`. This property is immutable.
     * 
     */
    @Export(name="availabilityZone", refs={String.class}, tree="[0]")
    private Output<String> availabilityZone;

    /**
     * @return [string] The availability zone in which the server should exist. E.g: `AUTO`, `ZONE_1`, `ZONE_2`. This property is immutable.
     * 
     */
    public Output<String> availabilityZone() {
        return this.availabilityZone;
    }
    /**
     * ***DEPRECATED*** Please refer to ionoscloud.ServerBootDeviceSelection (Optional)(Computed)[string] The associated boot drive, if any. Must be the UUID of a bootable CDROM image that can be retrieved using the ionoscloud.getImage data source.
     * 
     * @deprecated
     * Please use the &#39;ionoscloud_server_boot_device_selection&#39; resource for managing the boot device of the server.
     * 
     */
    @Deprecated /* Please use the 'ionoscloud_server_boot_device_selection' resource for managing the boot device of the server. */
    @Export(name="bootCdrom", refs={String.class}, tree="[0]")
    private Output<String> bootCdrom;

    /**
     * @return ***DEPRECATED*** Please refer to ionoscloud.ServerBootDeviceSelection (Optional)(Computed)[string] The associated boot drive, if any. Must be the UUID of a bootable CDROM image that can be retrieved using the ionoscloud.getImage data source.
     * 
     */
    public Output<String> bootCdrom() {
        return this.bootCdrom;
    }
    /**
     * [string] The image or snapshot UUID / name. May also be an image alias. It is required if `licence_type` is not provided.
     * 
     */
    @Export(name="bootImage", refs={String.class}, tree="[0]")
    private Output<String> bootImage;

    /**
     * @return [string] The image or snapshot UUID / name. May also be an image alias. It is required if `licence_type` is not provided.
     * 
     */
    public Output<String> bootImage() {
        return this.bootImage;
    }
    /**
     * The associated boot volume.
     * 
     */
    @Export(name="bootVolume", refs={String.class}, tree="[0]")
    private Output<String> bootVolume;

    /**
     * @return The associated boot volume.
     * 
     */
    public Output<String> bootVolume() {
        return this.bootVolume;
    }
    /**
     * (Computed)[integer] Number of server CPU cores.
     * 
     */
    @Export(name="cores", refs={Integer.class}, tree="[0]")
    private Output<Integer> cores;

    /**
     * @return (Computed)[integer] Number of server CPU cores.
     * 
     */
    public Output<Integer> cores() {
        return this.cores;
    }
    /**
     * [string] CPU architecture on which server gets provisioned; not all CPU architectures are available in all datacenter regions; available CPU architectures can be retrieved from the datacenter resource. E.g.: &#34;INTEL_SKYLAKE&#34; or &#34;INTEL_XEON&#34;.
     * 
     */
    @Export(name="cpuFamily", refs={String.class}, tree="[0]")
    private Output<String> cpuFamily;

    /**
     * @return [string] CPU architecture on which server gets provisioned; not all CPU architectures are available in all datacenter regions; available CPU architectures can be retrieved from the datacenter resource. E.g.: &#34;INTEL_SKYLAKE&#34; or &#34;INTEL_XEON&#34;.
     * 
     */
    public Output<String> cpuFamily() {
        return this.cpuFamily;
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
     * The associated firewall rule.
     * 
     */
    @Export(name="firewallruleId", refs={String.class}, tree="[0]")
    private Output<String> firewallruleId;

    /**
     * @return The associated firewall rule.
     * 
     */
    public Output<String> firewallruleId() {
        return this.firewallruleId;
    }
    /**
     * The associated firewall rules.
     * 
     */
    @Export(name="firewallruleIds", refs={List.class,String.class}, tree="[0,1]")
    private Output<List<String>> firewallruleIds;

    /**
     * @return The associated firewall rules.
     * 
     */
    public Output<List<String>> firewallruleIds() {
        return this.firewallruleIds;
    }
    /**
     * [string] The name, ID or alias of the image. May also be a snapshot ID. It is required if `licence_type` is not provided. Attribute is immutable.
     * 
     */
    @Export(name="imageName", refs={String.class}, tree="[0]")
    private Output<String> imageName;

    /**
     * @return [string] The name, ID or alias of the image. May also be a snapshot ID. It is required if `licence_type` is not provided. Attribute is immutable.
     * 
     */
    public Output<String> imageName() {
        return this.imageName;
    }
    /**
     * [string] Required if `ssh_key_path` is not provided.
     * 
     */
    @Export(name="imagePassword", refs={String.class}, tree="[0]")
    private Output<String> imagePassword;

    /**
     * @return [string] Required if `ssh_key_path` is not provided.
     * 
     */
    public Output<String> imagePassword() {
        return this.imagePassword;
    }
    /**
     * A list with the IDs for the volumes that are defined inside the server resource.
     * 
     * &gt; **⚠ WARNING**
     * &gt; 
     * &gt; Image_name under volume level is deprecated, please use image_name under server level
     * ssh_key_path and ssh_keys fields are immutable.
     * 
     * &gt; **⚠ WARNING**
     * &gt; 
     * &gt; If you want to create a **CUBE** server, you have to provide the `template_uuid`. In this case you can not set `cores`, `ram` and `volume.size` arguments, these being mutually exclusive with `template_uuid`.
     * &gt; 
     * &gt; In all the other cases (**ENTERPRISE** servers) you have to provide values for `cores`, `ram` and `volume size`.
     * 
     */
    @Export(name="inlineVolumeIds", refs={List.class,String.class}, tree="[0,1]")
    private Output<List<String>> inlineVolumeIds;

    /**
     * @return A list with the IDs for the volumes that are defined inside the server resource.
     * 
     * &gt; **⚠ WARNING**
     * &gt; 
     * &gt; Image_name under volume level is deprecated, please use image_name under server level
     * ssh_key_path and ssh_keys fields are immutable.
     * 
     * &gt; **⚠ WARNING**
     * &gt; 
     * &gt; If you want to create a **CUBE** server, you have to provide the `template_uuid`. In this case you can not set `cores`, `ram` and `volume.size` arguments, these being mutually exclusive with `template_uuid`.
     * &gt; 
     * &gt; In all the other cases (**ENTERPRISE** servers) you have to provide values for `cores`, `ram` and `volume size`.
     * 
     */
    public Output<List<String>> inlineVolumeIds() {
        return this.inlineVolumeIds;
    }
    /**
     * [set] A label can be seen as an object with only two required fields: `key` and `value`, both of the `string` type. Please check the example presented above to see how a `label` can be used in the plan. A server can have multiple labels.
     * 
     */
    @Export(name="labels", refs={List.class,ServerLabel.class}, tree="[0,1]")
    private Output</* @Nullable */ List<ServerLabel>> labels;

    /**
     * @return [set] A label can be seen as an object with only two required fields: `key` and `value`, both of the `string` type. Please check the example presented above to see how a `label` can be used in the plan. A server can have multiple labels.
     * 
     */
    public Output<Optional<List<ServerLabel>>> labels() {
        return Codegen.optional(this.labels);
    }
    /**
     * [string] The name of the server.
     * 
     */
    @Export(name="name", refs={String.class}, tree="[0]")
    private Output<String> name;

    /**
     * @return [string] The name of the server.
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    /**
     * See the Nic section.
     * 
     */
    @Export(name="nic", refs={ServerNic.class}, tree="[0]")
    private Output</* @Nullable */ ServerNic> nic;

    /**
     * @return See the Nic section.
     * 
     */
    public Output<Optional<ServerNic>> nic() {
        return Codegen.optional(this.nic);
    }
    /**
     * The associated IP address.
     * 
     */
    @Export(name="primaryIp", refs={String.class}, tree="[0]")
    private Output<String> primaryIp;

    /**
     * @return The associated IP address.
     * 
     */
    public Output<String> primaryIp() {
        return this.primaryIp;
    }
    /**
     * The associated NIC.
     * 
     */
    @Export(name="primaryNic", refs={String.class}, tree="[0]")
    private Output<String> primaryNic;

    /**
     * @return The associated NIC.
     * 
     */
    public Output<String> primaryNic() {
        return this.primaryNic;
    }
    /**
     * (Computed)[integer] The amount of memory for the server in MB.
     * 
     */
    @Export(name="ram", refs={Integer.class}, tree="[0]")
    private Output<Integer> ram;

    /**
     * @return (Computed)[integer] The amount of memory for the server in MB.
     * 
     */
    public Output<Integer> ram() {
        return this.ram;
    }
    /**
     * [list] List of absolute paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images.  Also accepts ssh keys directly. Required for IonosCloud Linux images. Required if `image_password` is not provided. Does not support `~` expansion to homedir in the given path. This property is immutable.
     * 
     * @deprecated
     * Will be renamed to ssh_keys in the future, to allow users to set both the ssh key path or directly the ssh key
     * 
     */
    @Deprecated /* Will be renamed to ssh_keys in the future, to allow users to set both the ssh key path or directly the ssh key */
    @Export(name="sshKeyPaths", refs={List.class,String.class}, tree="[0,1]")
    private Output</* @Nullable */ List<String>> sshKeyPaths;

    /**
     * @return [list] List of absolute paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images.  Also accepts ssh keys directly. Required for IonosCloud Linux images. Required if `image_password` is not provided. Does not support `~` expansion to homedir in the given path. This property is immutable.
     * 
     */
    public Output<Optional<List<String>>> sshKeyPaths() {
        return Codegen.optional(this.sshKeyPaths);
    }
    /**
     * [list] Immutable List of absolute or relative paths to files containing public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation. Does not support `~` expansion to homedir in the given path.
     * 
     */
    @Export(name="sshKeys", refs={List.class,String.class}, tree="[0,1]")
    private Output</* @Nullable */ List<String>> sshKeys;

    /**
     * @return [list] Immutable List of absolute or relative paths to files containing public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation. Does not support `~` expansion to homedir in the given path.
     * 
     */
    public Output<Optional<List<String>>> sshKeys() {
        return Codegen.optional(this.sshKeys);
    }
    /**
     * [string] The UUID of the template for creating a CUBE server; the available templates for CUBE servers can be found on the templates resource
     * 
     */
    @Export(name="templateUuid", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> templateUuid;

    /**
     * @return [string] The UUID of the template for creating a CUBE server; the available templates for CUBE servers can be found on the templates resource
     * 
     */
    public Output<Optional<String>> templateUuid() {
        return Codegen.optional(this.templateUuid);
    }
    /**
     * (Computed)[string] Server usages: [ENTERPRISE](https://docs.ionos.com/cloud/compute-engine/virtual-servers/virtual-servers) or [CUBE](https://docs.ionos.com/cloud/compute-engine/virtual-servers/cloud-cubes). This property is immutable.
     * 
     */
    @Export(name="type", refs={String.class}, tree="[0]")
    private Output<String> type;

    /**
     * @return (Computed)[string] Server usages: [ENTERPRISE](https://docs.ionos.com/cloud/compute-engine/virtual-servers/virtual-servers) or [CUBE](https://docs.ionos.com/cloud/compute-engine/virtual-servers/cloud-cubes). This property is immutable.
     * 
     */
    public Output<String> type() {
        return this.type;
    }
    /**
     * [string] Sets the power state of the server. E.g: `RUNNING`, `SHUTOFF` or `SUSPENDED`. SUSPENDED state is only valid for cube. SHUTOFF state is only valid for enterprise.
     * 
     */
    @Export(name="vmState", refs={String.class}, tree="[0]")
    private Output<String> vmState;

    /**
     * @return [string] Sets the power state of the server. E.g: `RUNNING`, `SHUTOFF` or `SUSPENDED`. SUSPENDED state is only valid for cube. SHUTOFF state is only valid for enterprise.
     * 
     */
    public Output<String> vmState() {
        return this.vmState;
    }
    /**
     * See the Volume section.
     * 
     */
    @Export(name="volume", refs={ServerVolume.class}, tree="[0]")
    private Output<ServerVolume> volume;

    /**
     * @return See the Volume section.
     * 
     */
    public Output<ServerVolume> volume() {
        return this.volume;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public Server(java.lang.String name) {
        this(name, ServerArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public Server(java.lang.String name, ServerArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public Server(java.lang.String name, ServerArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ionoscloud:index/server:Server", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()), false);
    }

    private Server(java.lang.String name, Output<java.lang.String> id, @Nullable ServerState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ionoscloud:index/server:Server", name, state, makeResourceOptions(options, id), false);
    }

    private static ServerArgs makeArgs(ServerArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? ServerArgs.Empty : args;
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<java.lang.String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .additionalSecretOutputs(List.of(
                "imagePassword"
            ))
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
    public static Server get(java.lang.String name, Output<java.lang.String> id, @Nullable ServerState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new Server(name, id, state, options);
    }
}
