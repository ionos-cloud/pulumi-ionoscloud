// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.compute;

import com.ionoscloud.pulumi.ionoscloud.compute.inputs.VCPUServerLabelArgs;
import com.ionoscloud.pulumi.ionoscloud.compute.inputs.VCPUServerNicArgs;
import com.ionoscloud.pulumi.ionoscloud.compute.inputs.VCPUServerVolumeArgs;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class VCPUServerArgs extends com.pulumi.resources.ResourceArgs {

    public static final VCPUServerArgs Empty = new VCPUServerArgs();

    /**
     * [string] The availability zone in which the server should exist. E.g: `AUTO`, `ZONE_1`, `ZONE_2`. This property is immutable.
     * 
     */
    @Import(name="availabilityZone")
    private @Nullable Output<String> availabilityZone;

    /**
     * @return [string] The availability zone in which the server should exist. E.g: `AUTO`, `ZONE_1`, `ZONE_2`. This property is immutable.
     * 
     */
    public Optional<Output<String>> availabilityZone() {
        return Optional.ofNullable(this.availabilityZone);
    }

    /**
     * ***DEPRECATED*** Please refer to ionoscloud.compute.BootDeviceSelection (Optional)[string] The associated boot drive, if any. Must be the UUID of a bootable CDROM image that can be retrieved using the ionoscloud.compute.getImage data source.
     * 
     * @deprecated
     * Please use the &#39;ionoscloud_server_boot_device_selection&#39; resource for managing the boot device of the server.
     * 
     */
    @Deprecated /* Please use the 'ionoscloud_server_boot_device_selection' resource for managing the boot device of the server. */
    @Import(name="bootCdrom")
    private @Nullable Output<String> bootCdrom;

    /**
     * @return ***DEPRECATED*** Please refer to ionoscloud.compute.BootDeviceSelection (Optional)[string] The associated boot drive, if any. Must be the UUID of a bootable CDROM image that can be retrieved using the ionoscloud.compute.getImage data source.
     * 
     * @deprecated
     * Please use the &#39;ionoscloud_server_boot_device_selection&#39; resource for managing the boot device of the server.
     * 
     */
    @Deprecated /* Please use the 'ionoscloud_server_boot_device_selection' resource for managing the boot device of the server. */
    public Optional<Output<String>> bootCdrom() {
        return Optional.ofNullable(this.bootCdrom);
    }

    /**
     * [string] The image or snapshot UUID / name. May also be an image alias. It is required if `licence_type` is not provided.
     * 
     */
    @Import(name="bootImage")
    private @Nullable Output<String> bootImage;

    /**
     * @return [string] The image or snapshot UUID / name. May also be an image alias. It is required if `licence_type` is not provided.
     * 
     */
    public Optional<Output<String>> bootImage() {
        return Optional.ofNullable(this.bootImage);
    }

    /**
     * [integer] Number of server CPU cores.
     * 
     */
    @Import(name="cores", required=true)
    private Output<Integer> cores;

    /**
     * @return [integer] Number of server CPU cores.
     * 
     */
    public Output<Integer> cores() {
        return this.cores;
    }

    /**
     * [string] The ID of a Virtual Data Center.
     * 
     */
    @Import(name="datacenterId", required=true)
    private Output<String> datacenterId;

    /**
     * @return [string] The ID of a Virtual Data Center.
     * 
     */
    public Output<String> datacenterId() {
        return this.datacenterId;
    }

    /**
     * The associated firewall rules.
     * 
     */
    @Import(name="firewallruleIds")
    private @Nullable Output<List<String>> firewallruleIds;

    /**
     * @return The associated firewall rules.
     * 
     */
    public Optional<Output<List<String>>> firewallruleIds() {
        return Optional.ofNullable(this.firewallruleIds);
    }

    /**
     * (Computed)[string] The hostname of the resource. Allowed characters are a-z, 0-9 and - (minus). Hostname should not start with minus and should not be longer than 63 characters. If no value provided explicitly, it will be populated with the name of the server
     * 
     */
    @Import(name="hostname")
    private @Nullable Output<String> hostname;

    /**
     * @return (Computed)[string] The hostname of the resource. Allowed characters are a-z, 0-9 and - (minus). Hostname should not start with minus and should not be longer than 63 characters. If no value provided explicitly, it will be populated with the name of the server
     * 
     */
    public Optional<Output<String>> hostname() {
        return Optional.ofNullable(this.hostname);
    }

    /**
     * [string] The name, ID or alias of the image. May also be a snapshot ID. It is required if `licence_type` is not provided. Attribute is immutable.
     * 
     */
    @Import(name="imageName")
    private @Nullable Output<String> imageName;

    /**
     * @return [string] The name, ID or alias of the image. May also be a snapshot ID. It is required if `licence_type` is not provided. Attribute is immutable.
     * 
     */
    public Optional<Output<String>> imageName() {
        return Optional.ofNullable(this.imageName);
    }

    /**
     * [string] The password for the image.
     * 
     */
    @Import(name="imagePassword")
    private @Nullable Output<String> imagePassword;

    /**
     * @return [string] The password for the image.
     * 
     */
    public Optional<Output<String>> imagePassword() {
        return Optional.ofNullable(this.imagePassword);
    }

    /**
     * A label can be seen as an object with only two required fields: `key` and `value`, both of the `string` type. Please check the example presented above to see how a `label` can be used in the plan. A server can have multiple labels.
     * 
     */
    @Import(name="labels")
    private @Nullable Output<List<VCPUServerLabelArgs>> labels;

    /**
     * @return A label can be seen as an object with only two required fields: `key` and `value`, both of the `string` type. Please check the example presented above to see how a `label` can be used in the plan. A server can have multiple labels.
     * 
     */
    public Optional<Output<List<VCPUServerLabelArgs>>> labels() {
        return Optional.ofNullable(this.labels);
    }

    /**
     * [string] The name of the server.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return [string] The name of the server.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * See the Nic section.
     * 
     */
    @Import(name="nic")
    private @Nullable Output<VCPUServerNicArgs> nic;

    /**
     * @return See the Nic section.
     * 
     */
    public Optional<Output<VCPUServerNicArgs>> nic() {
        return Optional.ofNullable(this.nic);
    }

    /**
     * [integer] The amount of memory for the server in MB.
     * 
     */
    @Import(name="ram", required=true)
    private Output<Integer> ram;

    /**
     * @return [integer] The amount of memory for the server in MB.
     * 
     */
    public Output<Integer> ram() {
        return this.ram;
    }

    /**
     * The list of Security Group IDs for the resource.
     * 
     * &gt; **⚠ WARNING**
     * &gt; 
     * &gt; ssh_keys field is immutable.
     * 
     */
    @Import(name="securityGroupsIds")
    private @Nullable Output<List<String>> securityGroupsIds;

    /**
     * @return The list of Security Group IDs for the resource.
     * 
     * &gt; **⚠ WARNING**
     * &gt; 
     * &gt; ssh_keys field is immutable.
     * 
     */
    public Optional<Output<List<String>>> securityGroupsIds() {
        return Optional.ofNullable(this.securityGroupsIds);
    }

    /**
     * [list] Immutable List of absolute or relative paths to files containing public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation. Does not support `~` expansion to homedir in the given path.
     * 
     */
    @Import(name="sshKeys")
    private @Nullable Output<List<String>> sshKeys;

    /**
     * @return [list] Immutable List of absolute or relative paths to files containing public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation. Does not support `~` expansion to homedir in the given path.
     * 
     */
    public Optional<Output<List<String>>> sshKeys() {
        return Optional.ofNullable(this.sshKeys);
    }

    /**
     * Sets the power state of the vcpu server. Possible values: `RUNNING` or `SHUTOFF`.
     * 
     */
    @Import(name="vmState")
    private @Nullable Output<String> vmState;

    /**
     * @return Sets the power state of the vcpu server. Possible values: `RUNNING` or `SHUTOFF`.
     * 
     */
    public Optional<Output<String>> vmState() {
        return Optional.ofNullable(this.vmState);
    }

    /**
     * See the Volume section.
     * 
     */
    @Import(name="volume", required=true)
    private Output<VCPUServerVolumeArgs> volume;

    /**
     * @return See the Volume section.
     * 
     */
    public Output<VCPUServerVolumeArgs> volume() {
        return this.volume;
    }

    private VCPUServerArgs() {}

    private VCPUServerArgs(VCPUServerArgs $) {
        this.availabilityZone = $.availabilityZone;
        this.bootCdrom = $.bootCdrom;
        this.bootImage = $.bootImage;
        this.cores = $.cores;
        this.datacenterId = $.datacenterId;
        this.firewallruleIds = $.firewallruleIds;
        this.hostname = $.hostname;
        this.imageName = $.imageName;
        this.imagePassword = $.imagePassword;
        this.labels = $.labels;
        this.name = $.name;
        this.nic = $.nic;
        this.ram = $.ram;
        this.securityGroupsIds = $.securityGroupsIds;
        this.sshKeys = $.sshKeys;
        this.vmState = $.vmState;
        this.volume = $.volume;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(VCPUServerArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private VCPUServerArgs $;

        public Builder() {
            $ = new VCPUServerArgs();
        }

        public Builder(VCPUServerArgs defaults) {
            $ = new VCPUServerArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param availabilityZone [string] The availability zone in which the server should exist. E.g: `AUTO`, `ZONE_1`, `ZONE_2`. This property is immutable.
         * 
         * @return builder
         * 
         */
        public Builder availabilityZone(@Nullable Output<String> availabilityZone) {
            $.availabilityZone = availabilityZone;
            return this;
        }

        /**
         * @param availabilityZone [string] The availability zone in which the server should exist. E.g: `AUTO`, `ZONE_1`, `ZONE_2`. This property is immutable.
         * 
         * @return builder
         * 
         */
        public Builder availabilityZone(String availabilityZone) {
            return availabilityZone(Output.of(availabilityZone));
        }

        /**
         * @param bootCdrom ***DEPRECATED*** Please refer to ionoscloud.compute.BootDeviceSelection (Optional)[string] The associated boot drive, if any. Must be the UUID of a bootable CDROM image that can be retrieved using the ionoscloud.compute.getImage data source.
         * 
         * @return builder
         * 
         * @deprecated
         * Please use the &#39;ionoscloud_server_boot_device_selection&#39; resource for managing the boot device of the server.
         * 
         */
        @Deprecated /* Please use the 'ionoscloud_server_boot_device_selection' resource for managing the boot device of the server. */
        public Builder bootCdrom(@Nullable Output<String> bootCdrom) {
            $.bootCdrom = bootCdrom;
            return this;
        }

        /**
         * @param bootCdrom ***DEPRECATED*** Please refer to ionoscloud.compute.BootDeviceSelection (Optional)[string] The associated boot drive, if any. Must be the UUID of a bootable CDROM image that can be retrieved using the ionoscloud.compute.getImage data source.
         * 
         * @return builder
         * 
         * @deprecated
         * Please use the &#39;ionoscloud_server_boot_device_selection&#39; resource for managing the boot device of the server.
         * 
         */
        @Deprecated /* Please use the 'ionoscloud_server_boot_device_selection' resource for managing the boot device of the server. */
        public Builder bootCdrom(String bootCdrom) {
            return bootCdrom(Output.of(bootCdrom));
        }

        /**
         * @param bootImage [string] The image or snapshot UUID / name. May also be an image alias. It is required if `licence_type` is not provided.
         * 
         * @return builder
         * 
         */
        public Builder bootImage(@Nullable Output<String> bootImage) {
            $.bootImage = bootImage;
            return this;
        }

        /**
         * @param bootImage [string] The image or snapshot UUID / name. May also be an image alias. It is required if `licence_type` is not provided.
         * 
         * @return builder
         * 
         */
        public Builder bootImage(String bootImage) {
            return bootImage(Output.of(bootImage));
        }

        /**
         * @param cores [integer] Number of server CPU cores.
         * 
         * @return builder
         * 
         */
        public Builder cores(Output<Integer> cores) {
            $.cores = cores;
            return this;
        }

        /**
         * @param cores [integer] Number of server CPU cores.
         * 
         * @return builder
         * 
         */
        public Builder cores(Integer cores) {
            return cores(Output.of(cores));
        }

        /**
         * @param datacenterId [string] The ID of a Virtual Data Center.
         * 
         * @return builder
         * 
         */
        public Builder datacenterId(Output<String> datacenterId) {
            $.datacenterId = datacenterId;
            return this;
        }

        /**
         * @param datacenterId [string] The ID of a Virtual Data Center.
         * 
         * @return builder
         * 
         */
        public Builder datacenterId(String datacenterId) {
            return datacenterId(Output.of(datacenterId));
        }

        /**
         * @param firewallruleIds The associated firewall rules.
         * 
         * @return builder
         * 
         */
        public Builder firewallruleIds(@Nullable Output<List<String>> firewallruleIds) {
            $.firewallruleIds = firewallruleIds;
            return this;
        }

        /**
         * @param firewallruleIds The associated firewall rules.
         * 
         * @return builder
         * 
         */
        public Builder firewallruleIds(List<String> firewallruleIds) {
            return firewallruleIds(Output.of(firewallruleIds));
        }

        /**
         * @param firewallruleIds The associated firewall rules.
         * 
         * @return builder
         * 
         */
        public Builder firewallruleIds(String... firewallruleIds) {
            return firewallruleIds(List.of(firewallruleIds));
        }

        /**
         * @param hostname (Computed)[string] The hostname of the resource. Allowed characters are a-z, 0-9 and - (minus). Hostname should not start with minus and should not be longer than 63 characters. If no value provided explicitly, it will be populated with the name of the server
         * 
         * @return builder
         * 
         */
        public Builder hostname(@Nullable Output<String> hostname) {
            $.hostname = hostname;
            return this;
        }

        /**
         * @param hostname (Computed)[string] The hostname of the resource. Allowed characters are a-z, 0-9 and - (minus). Hostname should not start with minus and should not be longer than 63 characters. If no value provided explicitly, it will be populated with the name of the server
         * 
         * @return builder
         * 
         */
        public Builder hostname(String hostname) {
            return hostname(Output.of(hostname));
        }

        /**
         * @param imageName [string] The name, ID or alias of the image. May also be a snapshot ID. It is required if `licence_type` is not provided. Attribute is immutable.
         * 
         * @return builder
         * 
         */
        public Builder imageName(@Nullable Output<String> imageName) {
            $.imageName = imageName;
            return this;
        }

        /**
         * @param imageName [string] The name, ID or alias of the image. May also be a snapshot ID. It is required if `licence_type` is not provided. Attribute is immutable.
         * 
         * @return builder
         * 
         */
        public Builder imageName(String imageName) {
            return imageName(Output.of(imageName));
        }

        /**
         * @param imagePassword [string] The password for the image.
         * 
         * @return builder
         * 
         */
        public Builder imagePassword(@Nullable Output<String> imagePassword) {
            $.imagePassword = imagePassword;
            return this;
        }

        /**
         * @param imagePassword [string] The password for the image.
         * 
         * @return builder
         * 
         */
        public Builder imagePassword(String imagePassword) {
            return imagePassword(Output.of(imagePassword));
        }

        /**
         * @param labels A label can be seen as an object with only two required fields: `key` and `value`, both of the `string` type. Please check the example presented above to see how a `label` can be used in the plan. A server can have multiple labels.
         * 
         * @return builder
         * 
         */
        public Builder labels(@Nullable Output<List<VCPUServerLabelArgs>> labels) {
            $.labels = labels;
            return this;
        }

        /**
         * @param labels A label can be seen as an object with only two required fields: `key` and `value`, both of the `string` type. Please check the example presented above to see how a `label` can be used in the plan. A server can have multiple labels.
         * 
         * @return builder
         * 
         */
        public Builder labels(List<VCPUServerLabelArgs> labels) {
            return labels(Output.of(labels));
        }

        /**
         * @param labels A label can be seen as an object with only two required fields: `key` and `value`, both of the `string` type. Please check the example presented above to see how a `label` can be used in the plan. A server can have multiple labels.
         * 
         * @return builder
         * 
         */
        public Builder labels(VCPUServerLabelArgs... labels) {
            return labels(List.of(labels));
        }

        /**
         * @param name [string] The name of the server.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name [string] The name of the server.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param nic See the Nic section.
         * 
         * @return builder
         * 
         */
        public Builder nic(@Nullable Output<VCPUServerNicArgs> nic) {
            $.nic = nic;
            return this;
        }

        /**
         * @param nic See the Nic section.
         * 
         * @return builder
         * 
         */
        public Builder nic(VCPUServerNicArgs nic) {
            return nic(Output.of(nic));
        }

        /**
         * @param ram [integer] The amount of memory for the server in MB.
         * 
         * @return builder
         * 
         */
        public Builder ram(Output<Integer> ram) {
            $.ram = ram;
            return this;
        }

        /**
         * @param ram [integer] The amount of memory for the server in MB.
         * 
         * @return builder
         * 
         */
        public Builder ram(Integer ram) {
            return ram(Output.of(ram));
        }

        /**
         * @param securityGroupsIds The list of Security Group IDs for the resource.
         * 
         * &gt; **⚠ WARNING**
         * &gt; 
         * &gt; ssh_keys field is immutable.
         * 
         * @return builder
         * 
         */
        public Builder securityGroupsIds(@Nullable Output<List<String>> securityGroupsIds) {
            $.securityGroupsIds = securityGroupsIds;
            return this;
        }

        /**
         * @param securityGroupsIds The list of Security Group IDs for the resource.
         * 
         * &gt; **⚠ WARNING**
         * &gt; 
         * &gt; ssh_keys field is immutable.
         * 
         * @return builder
         * 
         */
        public Builder securityGroupsIds(List<String> securityGroupsIds) {
            return securityGroupsIds(Output.of(securityGroupsIds));
        }

        /**
         * @param securityGroupsIds The list of Security Group IDs for the resource.
         * 
         * &gt; **⚠ WARNING**
         * &gt; 
         * &gt; ssh_keys field is immutable.
         * 
         * @return builder
         * 
         */
        public Builder securityGroupsIds(String... securityGroupsIds) {
            return securityGroupsIds(List.of(securityGroupsIds));
        }

        /**
         * @param sshKeys [list] Immutable List of absolute or relative paths to files containing public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation. Does not support `~` expansion to homedir in the given path.
         * 
         * @return builder
         * 
         */
        public Builder sshKeys(@Nullable Output<List<String>> sshKeys) {
            $.sshKeys = sshKeys;
            return this;
        }

        /**
         * @param sshKeys [list] Immutable List of absolute or relative paths to files containing public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation. Does not support `~` expansion to homedir in the given path.
         * 
         * @return builder
         * 
         */
        public Builder sshKeys(List<String> sshKeys) {
            return sshKeys(Output.of(sshKeys));
        }

        /**
         * @param sshKeys [list] Immutable List of absolute or relative paths to files containing public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation. Does not support `~` expansion to homedir in the given path.
         * 
         * @return builder
         * 
         */
        public Builder sshKeys(String... sshKeys) {
            return sshKeys(List.of(sshKeys));
        }

        /**
         * @param vmState Sets the power state of the vcpu server. Possible values: `RUNNING` or `SHUTOFF`.
         * 
         * @return builder
         * 
         */
        public Builder vmState(@Nullable Output<String> vmState) {
            $.vmState = vmState;
            return this;
        }

        /**
         * @param vmState Sets the power state of the vcpu server. Possible values: `RUNNING` or `SHUTOFF`.
         * 
         * @return builder
         * 
         */
        public Builder vmState(String vmState) {
            return vmState(Output.of(vmState));
        }

        /**
         * @param volume See the Volume section.
         * 
         * @return builder
         * 
         */
        public Builder volume(Output<VCPUServerVolumeArgs> volume) {
            $.volume = volume;
            return this;
        }

        /**
         * @param volume See the Volume section.
         * 
         * @return builder
         * 
         */
        public Builder volume(VCPUServerVolumeArgs volume) {
            return volume(Output.of(volume));
        }

        public VCPUServerArgs build() {
            if ($.cores == null) {
                throw new MissingRequiredPropertyException("VCPUServerArgs", "cores");
            }
            if ($.datacenterId == null) {
                throw new MissingRequiredPropertyException("VCPUServerArgs", "datacenterId");
            }
            if ($.ram == null) {
                throw new MissingRequiredPropertyException("VCPUServerArgs", "ram");
            }
            if ($.volume == null) {
                throw new MissingRequiredPropertyException("VCPUServerArgs", "volume");
            }
            return $;
        }
    }

}
