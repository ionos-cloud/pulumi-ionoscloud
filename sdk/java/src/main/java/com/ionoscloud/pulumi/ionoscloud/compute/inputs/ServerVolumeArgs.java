// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.compute.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class ServerVolumeArgs extends com.pulumi.resources.ResourceArgs {

    public static final ServerVolumeArgs Empty = new ServerVolumeArgs();

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
     * The uuid of the Backup Unit that user has access to. The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either &#39;public image&#39; or &#39;imageAlias&#39; in conjunction with this property.
     * 
     */
    @Import(name="backupUnitId")
    private @Nullable Output<String> backupUnitId;

    /**
     * @return The uuid of the Backup Unit that user has access to. The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either &#39;public image&#39; or &#39;imageAlias&#39; in conjunction with this property.
     * 
     */
    public Optional<Output<String>> backupUnitId() {
        return Optional.ofNullable(this.backupUnitId);
    }

    /**
     * The UUID of the attached server.
     * 
     */
    @Import(name="bootServer")
    private @Nullable Output<String> bootServer;

    /**
     * @return The UUID of the attached server.
     * 
     */
    public Optional<Output<String>> bootServer() {
        return Optional.ofNullable(this.bootServer);
    }

    @Import(name="bus")
    private @Nullable Output<String> bus;

    public Optional<Output<String>> bus() {
        return Optional.ofNullable(this.bus);
    }

    @Import(name="cpuHotPlug")
    private @Nullable Output<Boolean> cpuHotPlug;

    public Optional<Output<Boolean>> cpuHotPlug() {
        return Optional.ofNullable(this.cpuHotPlug);
    }

    @Import(name="deviceNumber")
    private @Nullable Output<Integer> deviceNumber;

    public Optional<Output<Integer>> deviceNumber() {
        return Optional.ofNullable(this.deviceNumber);
    }

    @Import(name="discVirtioHotPlug")
    private @Nullable Output<Boolean> discVirtioHotPlug;

    public Optional<Output<Boolean>> discVirtioHotPlug() {
        return Optional.ofNullable(this.discVirtioHotPlug);
    }

    @Import(name="discVirtioHotUnplug")
    private @Nullable Output<Boolean> discVirtioHotUnplug;

    public Optional<Output<Boolean>> discVirtioHotUnplug() {
        return Optional.ofNullable(this.discVirtioHotUnplug);
    }

    @Import(name="diskType", required=true)
    private Output<String> diskType;

    public Output<String> diskType() {
        return this.diskType;
    }

    /**
     * [string] Required if `ssh_key_path` is not provided.
     * 
     * @deprecated
     * Please use image_password under server level
     * 
     */
    @Deprecated /* Please use image_password under server level */
    @Import(name="imagePassword")
    private @Nullable Output<String> imagePassword;

    /**
     * @return [string] Required if `ssh_key_path` is not provided.
     * 
     * @deprecated
     * Please use image_password under server level
     * 
     */
    @Deprecated /* Please use image_password under server level */
    public Optional<Output<String>> imagePassword() {
        return Optional.ofNullable(this.imagePassword);
    }

    /**
     * [string] Sets the OS type of the server.
     * 
     */
    @Import(name="licenceType")
    private @Nullable Output<String> licenceType;

    /**
     * @return [string] Sets the OS type of the server.
     * 
     */
    public Optional<Output<String>> licenceType() {
        return Optional.ofNullable(this.licenceType);
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

    @Import(name="nicHotPlug")
    private @Nullable Output<Boolean> nicHotPlug;

    public Optional<Output<Boolean>> nicHotPlug() {
        return Optional.ofNullable(this.nicHotPlug);
    }

    @Import(name="nicHotUnplug")
    private @Nullable Output<Boolean> nicHotUnplug;

    public Optional<Output<Boolean>> nicHotUnplug() {
        return Optional.ofNullable(this.nicHotUnplug);
    }

    @Import(name="pciSlot")
    private @Nullable Output<Integer> pciSlot;

    public Optional<Output<Integer>> pciSlot() {
        return Optional.ofNullable(this.pciSlot);
    }

    @Import(name="ramHotPlug")
    private @Nullable Output<Boolean> ramHotPlug;

    public Optional<Output<Boolean>> ramHotPlug() {
        return Optional.ofNullable(this.ramHotPlug);
    }

    /**
     * The size of the volume in GB.
     * 
     */
    @Import(name="size")
    private @Nullable Output<Integer> size;

    /**
     * @return The size of the volume in GB.
     * 
     */
    public Optional<Output<Integer>> size() {
        return Optional.ofNullable(this.size);
    }

    /**
     * [list] List of absolute paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images.  Also accepts ssh keys directly. Required for IonosCloud Linux images. Required if `image_password` is not provided. Does not support `~` expansion to homedir in the given path. This property is immutable.
     * 
     * @deprecated
     * Please use ssh_key_path under server level
     * 
     */
    @Deprecated /* Please use ssh_key_path under server level */
    @Import(name="sshKeyPaths")
    private @Nullable Output<List<String>> sshKeyPaths;

    /**
     * @return [list] List of absolute paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images.  Also accepts ssh keys directly. Required for IonosCloud Linux images. Required if `image_password` is not provided. Does not support `~` expansion to homedir in the given path. This property is immutable.
     * 
     * @deprecated
     * Please use ssh_key_path under server level
     * 
     */
    @Deprecated /* Please use ssh_key_path under server level */
    public Optional<Output<List<String>>> sshKeyPaths() {
        return Optional.ofNullable(this.sshKeyPaths);
    }

    /**
     * [list] Immutable List of absolute or relative paths to files containing public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation. Does not support `~` expansion to homedir in the given path.
     * 
     * @deprecated
     * Please use ssh_keys under server level
     * 
     */
    @Deprecated /* Please use ssh_keys under server level */
    @Import(name="sshKeys")
    private @Nullable Output<List<String>> sshKeys;

    /**
     * @return [list] Immutable List of absolute or relative paths to files containing public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation. Does not support `~` expansion to homedir in the given path.
     * 
     * @deprecated
     * Please use ssh_keys under server level
     * 
     */
    @Deprecated /* Please use ssh_keys under server level */
    public Optional<Output<List<String>>> sshKeys() {
        return Optional.ofNullable(this.sshKeys);
    }

    /**
     * The cloud-init configuration for the volume as base64 encoded string. The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either &#39;public image&#39; or &#39;imageAlias&#39; that has cloud-init compatibility in conjunction with this property.
     * 
     */
    @Import(name="userData")
    private @Nullable Output<String> userData;

    /**
     * @return The cloud-init configuration for the volume as base64 encoded string. The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either &#39;public image&#39; or &#39;imageAlias&#39; that has cloud-init compatibility in conjunction with this property.
     * 
     */
    public Optional<Output<String>> userData() {
        return Optional.ofNullable(this.userData);
    }

    private ServerVolumeArgs() {}

    private ServerVolumeArgs(ServerVolumeArgs $) {
        this.availabilityZone = $.availabilityZone;
        this.backupUnitId = $.backupUnitId;
        this.bootServer = $.bootServer;
        this.bus = $.bus;
        this.cpuHotPlug = $.cpuHotPlug;
        this.deviceNumber = $.deviceNumber;
        this.discVirtioHotPlug = $.discVirtioHotPlug;
        this.discVirtioHotUnplug = $.discVirtioHotUnplug;
        this.diskType = $.diskType;
        this.imagePassword = $.imagePassword;
        this.licenceType = $.licenceType;
        this.name = $.name;
        this.nicHotPlug = $.nicHotPlug;
        this.nicHotUnplug = $.nicHotUnplug;
        this.pciSlot = $.pciSlot;
        this.ramHotPlug = $.ramHotPlug;
        this.size = $.size;
        this.sshKeyPaths = $.sshKeyPaths;
        this.sshKeys = $.sshKeys;
        this.userData = $.userData;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ServerVolumeArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ServerVolumeArgs $;

        public Builder() {
            $ = new ServerVolumeArgs();
        }

        public Builder(ServerVolumeArgs defaults) {
            $ = new ServerVolumeArgs(Objects.requireNonNull(defaults));
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
         * @param backupUnitId The uuid of the Backup Unit that user has access to. The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either &#39;public image&#39; or &#39;imageAlias&#39; in conjunction with this property.
         * 
         * @return builder
         * 
         */
        public Builder backupUnitId(@Nullable Output<String> backupUnitId) {
            $.backupUnitId = backupUnitId;
            return this;
        }

        /**
         * @param backupUnitId The uuid of the Backup Unit that user has access to. The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either &#39;public image&#39; or &#39;imageAlias&#39; in conjunction with this property.
         * 
         * @return builder
         * 
         */
        public Builder backupUnitId(String backupUnitId) {
            return backupUnitId(Output.of(backupUnitId));
        }

        /**
         * @param bootServer The UUID of the attached server.
         * 
         * @return builder
         * 
         */
        public Builder bootServer(@Nullable Output<String> bootServer) {
            $.bootServer = bootServer;
            return this;
        }

        /**
         * @param bootServer The UUID of the attached server.
         * 
         * @return builder
         * 
         */
        public Builder bootServer(String bootServer) {
            return bootServer(Output.of(bootServer));
        }

        public Builder bus(@Nullable Output<String> bus) {
            $.bus = bus;
            return this;
        }

        public Builder bus(String bus) {
            return bus(Output.of(bus));
        }

        public Builder cpuHotPlug(@Nullable Output<Boolean> cpuHotPlug) {
            $.cpuHotPlug = cpuHotPlug;
            return this;
        }

        public Builder cpuHotPlug(Boolean cpuHotPlug) {
            return cpuHotPlug(Output.of(cpuHotPlug));
        }

        public Builder deviceNumber(@Nullable Output<Integer> deviceNumber) {
            $.deviceNumber = deviceNumber;
            return this;
        }

        public Builder deviceNumber(Integer deviceNumber) {
            return deviceNumber(Output.of(deviceNumber));
        }

        public Builder discVirtioHotPlug(@Nullable Output<Boolean> discVirtioHotPlug) {
            $.discVirtioHotPlug = discVirtioHotPlug;
            return this;
        }

        public Builder discVirtioHotPlug(Boolean discVirtioHotPlug) {
            return discVirtioHotPlug(Output.of(discVirtioHotPlug));
        }

        public Builder discVirtioHotUnplug(@Nullable Output<Boolean> discVirtioHotUnplug) {
            $.discVirtioHotUnplug = discVirtioHotUnplug;
            return this;
        }

        public Builder discVirtioHotUnplug(Boolean discVirtioHotUnplug) {
            return discVirtioHotUnplug(Output.of(discVirtioHotUnplug));
        }

        public Builder diskType(Output<String> diskType) {
            $.diskType = diskType;
            return this;
        }

        public Builder diskType(String diskType) {
            return diskType(Output.of(diskType));
        }

        /**
         * @param imagePassword [string] Required if `ssh_key_path` is not provided.
         * 
         * @return builder
         * 
         * @deprecated
         * Please use image_password under server level
         * 
         */
        @Deprecated /* Please use image_password under server level */
        public Builder imagePassword(@Nullable Output<String> imagePassword) {
            $.imagePassword = imagePassword;
            return this;
        }

        /**
         * @param imagePassword [string] Required if `ssh_key_path` is not provided.
         * 
         * @return builder
         * 
         * @deprecated
         * Please use image_password under server level
         * 
         */
        @Deprecated /* Please use image_password under server level */
        public Builder imagePassword(String imagePassword) {
            return imagePassword(Output.of(imagePassword));
        }

        /**
         * @param licenceType [string] Sets the OS type of the server.
         * 
         * @return builder
         * 
         */
        public Builder licenceType(@Nullable Output<String> licenceType) {
            $.licenceType = licenceType;
            return this;
        }

        /**
         * @param licenceType [string] Sets the OS type of the server.
         * 
         * @return builder
         * 
         */
        public Builder licenceType(String licenceType) {
            return licenceType(Output.of(licenceType));
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

        public Builder nicHotPlug(@Nullable Output<Boolean> nicHotPlug) {
            $.nicHotPlug = nicHotPlug;
            return this;
        }

        public Builder nicHotPlug(Boolean nicHotPlug) {
            return nicHotPlug(Output.of(nicHotPlug));
        }

        public Builder nicHotUnplug(@Nullable Output<Boolean> nicHotUnplug) {
            $.nicHotUnplug = nicHotUnplug;
            return this;
        }

        public Builder nicHotUnplug(Boolean nicHotUnplug) {
            return nicHotUnplug(Output.of(nicHotUnplug));
        }

        public Builder pciSlot(@Nullable Output<Integer> pciSlot) {
            $.pciSlot = pciSlot;
            return this;
        }

        public Builder pciSlot(Integer pciSlot) {
            return pciSlot(Output.of(pciSlot));
        }

        public Builder ramHotPlug(@Nullable Output<Boolean> ramHotPlug) {
            $.ramHotPlug = ramHotPlug;
            return this;
        }

        public Builder ramHotPlug(Boolean ramHotPlug) {
            return ramHotPlug(Output.of(ramHotPlug));
        }

        /**
         * @param size The size of the volume in GB.
         * 
         * @return builder
         * 
         */
        public Builder size(@Nullable Output<Integer> size) {
            $.size = size;
            return this;
        }

        /**
         * @param size The size of the volume in GB.
         * 
         * @return builder
         * 
         */
        public Builder size(Integer size) {
            return size(Output.of(size));
        }

        /**
         * @param sshKeyPaths [list] List of absolute paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images.  Also accepts ssh keys directly. Required for IonosCloud Linux images. Required if `image_password` is not provided. Does not support `~` expansion to homedir in the given path. This property is immutable.
         * 
         * @return builder
         * 
         * @deprecated
         * Please use ssh_key_path under server level
         * 
         */
        @Deprecated /* Please use ssh_key_path under server level */
        public Builder sshKeyPaths(@Nullable Output<List<String>> sshKeyPaths) {
            $.sshKeyPaths = sshKeyPaths;
            return this;
        }

        /**
         * @param sshKeyPaths [list] List of absolute paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images.  Also accepts ssh keys directly. Required for IonosCloud Linux images. Required if `image_password` is not provided. Does not support `~` expansion to homedir in the given path. This property is immutable.
         * 
         * @return builder
         * 
         * @deprecated
         * Please use ssh_key_path under server level
         * 
         */
        @Deprecated /* Please use ssh_key_path under server level */
        public Builder sshKeyPaths(List<String> sshKeyPaths) {
            return sshKeyPaths(Output.of(sshKeyPaths));
        }

        /**
         * @param sshKeyPaths [list] List of absolute paths to files containing a public SSH key that will be injected into IonosCloud provided Linux images.  Also accepts ssh keys directly. Required for IonosCloud Linux images. Required if `image_password` is not provided. Does not support `~` expansion to homedir in the given path. This property is immutable.
         * 
         * @return builder
         * 
         * @deprecated
         * Please use ssh_key_path under server level
         * 
         */
        @Deprecated /* Please use ssh_key_path under server level */
        public Builder sshKeyPaths(String... sshKeyPaths) {
            return sshKeyPaths(List.of(sshKeyPaths));
        }

        /**
         * @param sshKeys [list] Immutable List of absolute or relative paths to files containing public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation. Does not support `~` expansion to homedir in the given path.
         * 
         * @return builder
         * 
         * @deprecated
         * Please use ssh_keys under server level
         * 
         */
        @Deprecated /* Please use ssh_keys under server level */
        public Builder sshKeys(@Nullable Output<List<String>> sshKeys) {
            $.sshKeys = sshKeys;
            return this;
        }

        /**
         * @param sshKeys [list] Immutable List of absolute or relative paths to files containing public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation. Does not support `~` expansion to homedir in the given path.
         * 
         * @return builder
         * 
         * @deprecated
         * Please use ssh_keys under server level
         * 
         */
        @Deprecated /* Please use ssh_keys under server level */
        public Builder sshKeys(List<String> sshKeys) {
            return sshKeys(Output.of(sshKeys));
        }

        /**
         * @param sshKeys [list] Immutable List of absolute or relative paths to files containing public SSH key that will be injected into IonosCloud provided Linux images. Also accepts ssh keys directly. Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key. This field may only be set in creation requests. When reading, it always returns null. SSH keys are only supported if a public Linux image is used for the volume creation. Does not support `~` expansion to homedir in the given path.
         * 
         * @return builder
         * 
         * @deprecated
         * Please use ssh_keys under server level
         * 
         */
        @Deprecated /* Please use ssh_keys under server level */
        public Builder sshKeys(String... sshKeys) {
            return sshKeys(List.of(sshKeys));
        }

        /**
         * @param userData The cloud-init configuration for the volume as base64 encoded string. The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either &#39;public image&#39; or &#39;imageAlias&#39; that has cloud-init compatibility in conjunction with this property.
         * 
         * @return builder
         * 
         */
        public Builder userData(@Nullable Output<String> userData) {
            $.userData = userData;
            return this;
        }

        /**
         * @param userData The cloud-init configuration for the volume as base64 encoded string. The property is immutable and is only allowed to be set on a new volume creation. It is mandatory to provide either &#39;public image&#39; or &#39;imageAlias&#39; that has cloud-init compatibility in conjunction with this property.
         * 
         * @return builder
         * 
         */
        public Builder userData(String userData) {
            return userData(Output.of(userData));
        }

        public ServerVolumeArgs build() {
            if ($.diskType == null) {
                throw new MissingRequiredPropertyException("ServerVolumeArgs", "diskType");
            }
            return $;
        }
    }

}
