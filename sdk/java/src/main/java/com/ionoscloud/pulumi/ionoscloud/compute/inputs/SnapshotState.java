// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.compute.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class SnapshotState extends com.pulumi.resources.ResourceArgs {

    public static final SnapshotState Empty = new SnapshotState();

    /**
     * (Computed)[string] Is capable of CPU hot plug (no reboot required). Can only be updated.
     * 
     */
    @Import(name="cpuHotPlug")
    private @Nullable Output<Boolean> cpuHotPlug;

    /**
     * @return (Computed)[string] Is capable of CPU hot plug (no reboot required). Can only be updated.
     * 
     */
    public Optional<Output<Boolean>> cpuHotPlug() {
        return Optional.ofNullable(this.cpuHotPlug);
    }

    /**
     * Is capable of CPU hot unplug (no reboot required)
     * 
     */
    @Import(name="cpuHotUnplug")
    private @Nullable Output<Boolean> cpuHotUnplug;

    /**
     * @return Is capable of CPU hot unplug (no reboot required)
     * 
     */
    public Optional<Output<Boolean>> cpuHotUnplug() {
        return Optional.ofNullable(this.cpuHotUnplug);
    }

    /**
     * [string] The ID of the Virtual Data Center.
     * 
     */
    @Import(name="datacenterId")
    private @Nullable Output<String> datacenterId;

    /**
     * @return [string] The ID of the Virtual Data Center.
     * 
     */
    public Optional<Output<String>> datacenterId() {
        return Optional.ofNullable(this.datacenterId);
    }

    /**
     * (Computed)[string] Human readable description
     * 
     */
    @Import(name="description")
    private @Nullable Output<String> description;

    /**
     * @return (Computed)[string] Human readable description
     * 
     */
    public Optional<Output<String>> description() {
        return Optional.ofNullable(this.description);
    }

    /**
     * Is capable of SCSI drive hot plug (no reboot required)
     * 
     */
    @Import(name="discScsiHotPlug")
    private @Nullable Output<Boolean> discScsiHotPlug;

    /**
     * @return Is capable of SCSI drive hot plug (no reboot required)
     * 
     */
    public Optional<Output<Boolean>> discScsiHotPlug() {
        return Optional.ofNullable(this.discScsiHotPlug);
    }

    /**
     * Is capable of SCSI drive hot unplug (no reboot required). This works only for non-Windows virtual Machines.
     * 
     */
    @Import(name="discScsiHotUnplug")
    private @Nullable Output<Boolean> discScsiHotUnplug;

    /**
     * @return Is capable of SCSI drive hot unplug (no reboot required). This works only for non-Windows virtual Machines.
     * 
     */
    public Optional<Output<Boolean>> discScsiHotUnplug() {
        return Optional.ofNullable(this.discScsiHotUnplug);
    }

    /**
     * (Computed)[string] Is capable of Virt-IO drive hot plug (no reboot required). Can only be updated.
     * 
     */
    @Import(name="discVirtioHotPlug")
    private @Nullable Output<Boolean> discVirtioHotPlug;

    /**
     * @return (Computed)[string] Is capable of Virt-IO drive hot plug (no reboot required). Can only be updated.
     * 
     */
    public Optional<Output<Boolean>> discVirtioHotPlug() {
        return Optional.ofNullable(this.discVirtioHotPlug);
    }

    /**
     * (Computed)[string] Is capable of Virt-IO drive hot unplug (no reboot required). This works only for non-Windows virtual Machines. Can only be updated.
     * 
     */
    @Import(name="discVirtioHotUnplug")
    private @Nullable Output<Boolean> discVirtioHotUnplug;

    /**
     * @return (Computed)[string] Is capable of Virt-IO drive hot unplug (no reboot required). This works only for non-Windows virtual Machines. Can only be updated.
     * 
     */
    public Optional<Output<Boolean>> discVirtioHotUnplug() {
        return Optional.ofNullable(this.discVirtioHotUnplug);
    }

    /**
     * (Computed)[string] OS type of this Snapshot
     * 
     */
    @Import(name="licenceType")
    private @Nullable Output<String> licenceType;

    /**
     * @return (Computed)[string] OS type of this Snapshot
     * 
     */
    public Optional<Output<String>> licenceType() {
        return Optional.ofNullable(this.licenceType);
    }

    /**
     * Location of that image/snapshot
     * 
     */
    @Import(name="location")
    private @Nullable Output<String> location;

    /**
     * @return Location of that image/snapshot
     * 
     */
    public Optional<Output<String>> location() {
        return Optional.ofNullable(this.location);
    }

    /**
     * [string] The name of the snapshot.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return [string] The name of the snapshot.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * (Computed)[string] Is capable of nic hot plug (no reboot required). Can only be updated.
     * 
     */
    @Import(name="nicHotPlug")
    private @Nullable Output<Boolean> nicHotPlug;

    /**
     * @return (Computed)[string] Is capable of nic hot plug (no reboot required). Can only be updated.
     * 
     */
    public Optional<Output<Boolean>> nicHotPlug() {
        return Optional.ofNullable(this.nicHotPlug);
    }

    /**
     * (Computed)[string] Is capable of nic hot unplug (no reboot required). Can only be updated.
     * 
     */
    @Import(name="nicHotUnplug")
    private @Nullable Output<Boolean> nicHotUnplug;

    /**
     * @return (Computed)[string] Is capable of nic hot unplug (no reboot required). Can only be updated.
     * 
     */
    public Optional<Output<Boolean>> nicHotUnplug() {
        return Optional.ofNullable(this.nicHotUnplug);
    }

    /**
     * (Computed)[string] Is capable of memory hot plug (no reboot required). Can only be updated.
     * 
     */
    @Import(name="ramHotPlug")
    private @Nullable Output<Boolean> ramHotPlug;

    /**
     * @return (Computed)[string] Is capable of memory hot plug (no reboot required). Can only be updated.
     * 
     */
    public Optional<Output<Boolean>> ramHotPlug() {
        return Optional.ofNullable(this.ramHotPlug);
    }

    /**
     * Is capable of memory hot unplug (no reboot required)
     * 
     */
    @Import(name="ramHotUnplug")
    private @Nullable Output<Boolean> ramHotUnplug;

    /**
     * @return Is capable of memory hot unplug (no reboot required)
     * 
     */
    public Optional<Output<Boolean>> ramHotUnplug() {
        return Optional.ofNullable(this.ramHotUnplug);
    }

    /**
     * Boolean value representing if the snapshot requires extra protection e.g. two factor protection
     * 
     */
    @Import(name="secAuthProtection")
    private @Nullable Output<Boolean> secAuthProtection;

    /**
     * @return Boolean value representing if the snapshot requires extra protection e.g. two factor protection
     * 
     */
    public Optional<Output<Boolean>> secAuthProtection() {
        return Optional.ofNullable(this.secAuthProtection);
    }

    /**
     * The size of the image in GB
     * 
     */
    @Import(name="size")
    private @Nullable Output<Integer> size;

    /**
     * @return The size of the image in GB
     * 
     */
    public Optional<Output<Integer>> size() {
        return Optional.ofNullable(this.size);
    }

    /**
     * [string] The ID of the specific volume to take the snapshot from.
     * 
     */
    @Import(name="volumeId")
    private @Nullable Output<String> volumeId;

    /**
     * @return [string] The ID of the specific volume to take the snapshot from.
     * 
     */
    public Optional<Output<String>> volumeId() {
        return Optional.ofNullable(this.volumeId);
    }

    private SnapshotState() {}

    private SnapshotState(SnapshotState $) {
        this.cpuHotPlug = $.cpuHotPlug;
        this.cpuHotUnplug = $.cpuHotUnplug;
        this.datacenterId = $.datacenterId;
        this.description = $.description;
        this.discScsiHotPlug = $.discScsiHotPlug;
        this.discScsiHotUnplug = $.discScsiHotUnplug;
        this.discVirtioHotPlug = $.discVirtioHotPlug;
        this.discVirtioHotUnplug = $.discVirtioHotUnplug;
        this.licenceType = $.licenceType;
        this.location = $.location;
        this.name = $.name;
        this.nicHotPlug = $.nicHotPlug;
        this.nicHotUnplug = $.nicHotUnplug;
        this.ramHotPlug = $.ramHotPlug;
        this.ramHotUnplug = $.ramHotUnplug;
        this.secAuthProtection = $.secAuthProtection;
        this.size = $.size;
        this.volumeId = $.volumeId;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(SnapshotState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private SnapshotState $;

        public Builder() {
            $ = new SnapshotState();
        }

        public Builder(SnapshotState defaults) {
            $ = new SnapshotState(Objects.requireNonNull(defaults));
        }

        /**
         * @param cpuHotPlug (Computed)[string] Is capable of CPU hot plug (no reboot required). Can only be updated.
         * 
         * @return builder
         * 
         */
        public Builder cpuHotPlug(@Nullable Output<Boolean> cpuHotPlug) {
            $.cpuHotPlug = cpuHotPlug;
            return this;
        }

        /**
         * @param cpuHotPlug (Computed)[string] Is capable of CPU hot plug (no reboot required). Can only be updated.
         * 
         * @return builder
         * 
         */
        public Builder cpuHotPlug(Boolean cpuHotPlug) {
            return cpuHotPlug(Output.of(cpuHotPlug));
        }

        /**
         * @param cpuHotUnplug Is capable of CPU hot unplug (no reboot required)
         * 
         * @return builder
         * 
         */
        public Builder cpuHotUnplug(@Nullable Output<Boolean> cpuHotUnplug) {
            $.cpuHotUnplug = cpuHotUnplug;
            return this;
        }

        /**
         * @param cpuHotUnplug Is capable of CPU hot unplug (no reboot required)
         * 
         * @return builder
         * 
         */
        public Builder cpuHotUnplug(Boolean cpuHotUnplug) {
            return cpuHotUnplug(Output.of(cpuHotUnplug));
        }

        /**
         * @param datacenterId [string] The ID of the Virtual Data Center.
         * 
         * @return builder
         * 
         */
        public Builder datacenterId(@Nullable Output<String> datacenterId) {
            $.datacenterId = datacenterId;
            return this;
        }

        /**
         * @param datacenterId [string] The ID of the Virtual Data Center.
         * 
         * @return builder
         * 
         */
        public Builder datacenterId(String datacenterId) {
            return datacenterId(Output.of(datacenterId));
        }

        /**
         * @param description (Computed)[string] Human readable description
         * 
         * @return builder
         * 
         */
        public Builder description(@Nullable Output<String> description) {
            $.description = description;
            return this;
        }

        /**
         * @param description (Computed)[string] Human readable description
         * 
         * @return builder
         * 
         */
        public Builder description(String description) {
            return description(Output.of(description));
        }

        /**
         * @param discScsiHotPlug Is capable of SCSI drive hot plug (no reboot required)
         * 
         * @return builder
         * 
         */
        public Builder discScsiHotPlug(@Nullable Output<Boolean> discScsiHotPlug) {
            $.discScsiHotPlug = discScsiHotPlug;
            return this;
        }

        /**
         * @param discScsiHotPlug Is capable of SCSI drive hot plug (no reboot required)
         * 
         * @return builder
         * 
         */
        public Builder discScsiHotPlug(Boolean discScsiHotPlug) {
            return discScsiHotPlug(Output.of(discScsiHotPlug));
        }

        /**
         * @param discScsiHotUnplug Is capable of SCSI drive hot unplug (no reboot required). This works only for non-Windows virtual Machines.
         * 
         * @return builder
         * 
         */
        public Builder discScsiHotUnplug(@Nullable Output<Boolean> discScsiHotUnplug) {
            $.discScsiHotUnplug = discScsiHotUnplug;
            return this;
        }

        /**
         * @param discScsiHotUnplug Is capable of SCSI drive hot unplug (no reboot required). This works only for non-Windows virtual Machines.
         * 
         * @return builder
         * 
         */
        public Builder discScsiHotUnplug(Boolean discScsiHotUnplug) {
            return discScsiHotUnplug(Output.of(discScsiHotUnplug));
        }

        /**
         * @param discVirtioHotPlug (Computed)[string] Is capable of Virt-IO drive hot plug (no reboot required). Can only be updated.
         * 
         * @return builder
         * 
         */
        public Builder discVirtioHotPlug(@Nullable Output<Boolean> discVirtioHotPlug) {
            $.discVirtioHotPlug = discVirtioHotPlug;
            return this;
        }

        /**
         * @param discVirtioHotPlug (Computed)[string] Is capable of Virt-IO drive hot plug (no reboot required). Can only be updated.
         * 
         * @return builder
         * 
         */
        public Builder discVirtioHotPlug(Boolean discVirtioHotPlug) {
            return discVirtioHotPlug(Output.of(discVirtioHotPlug));
        }

        /**
         * @param discVirtioHotUnplug (Computed)[string] Is capable of Virt-IO drive hot unplug (no reboot required). This works only for non-Windows virtual Machines. Can only be updated.
         * 
         * @return builder
         * 
         */
        public Builder discVirtioHotUnplug(@Nullable Output<Boolean> discVirtioHotUnplug) {
            $.discVirtioHotUnplug = discVirtioHotUnplug;
            return this;
        }

        /**
         * @param discVirtioHotUnplug (Computed)[string] Is capable of Virt-IO drive hot unplug (no reboot required). This works only for non-Windows virtual Machines. Can only be updated.
         * 
         * @return builder
         * 
         */
        public Builder discVirtioHotUnplug(Boolean discVirtioHotUnplug) {
            return discVirtioHotUnplug(Output.of(discVirtioHotUnplug));
        }

        /**
         * @param licenceType (Computed)[string] OS type of this Snapshot
         * 
         * @return builder
         * 
         */
        public Builder licenceType(@Nullable Output<String> licenceType) {
            $.licenceType = licenceType;
            return this;
        }

        /**
         * @param licenceType (Computed)[string] OS type of this Snapshot
         * 
         * @return builder
         * 
         */
        public Builder licenceType(String licenceType) {
            return licenceType(Output.of(licenceType));
        }

        /**
         * @param location Location of that image/snapshot
         * 
         * @return builder
         * 
         */
        public Builder location(@Nullable Output<String> location) {
            $.location = location;
            return this;
        }

        /**
         * @param location Location of that image/snapshot
         * 
         * @return builder
         * 
         */
        public Builder location(String location) {
            return location(Output.of(location));
        }

        /**
         * @param name [string] The name of the snapshot.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name [string] The name of the snapshot.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param nicHotPlug (Computed)[string] Is capable of nic hot plug (no reboot required). Can only be updated.
         * 
         * @return builder
         * 
         */
        public Builder nicHotPlug(@Nullable Output<Boolean> nicHotPlug) {
            $.nicHotPlug = nicHotPlug;
            return this;
        }

        /**
         * @param nicHotPlug (Computed)[string] Is capable of nic hot plug (no reboot required). Can only be updated.
         * 
         * @return builder
         * 
         */
        public Builder nicHotPlug(Boolean nicHotPlug) {
            return nicHotPlug(Output.of(nicHotPlug));
        }

        /**
         * @param nicHotUnplug (Computed)[string] Is capable of nic hot unplug (no reboot required). Can only be updated.
         * 
         * @return builder
         * 
         */
        public Builder nicHotUnplug(@Nullable Output<Boolean> nicHotUnplug) {
            $.nicHotUnplug = nicHotUnplug;
            return this;
        }

        /**
         * @param nicHotUnplug (Computed)[string] Is capable of nic hot unplug (no reboot required). Can only be updated.
         * 
         * @return builder
         * 
         */
        public Builder nicHotUnplug(Boolean nicHotUnplug) {
            return nicHotUnplug(Output.of(nicHotUnplug));
        }

        /**
         * @param ramHotPlug (Computed)[string] Is capable of memory hot plug (no reboot required). Can only be updated.
         * 
         * @return builder
         * 
         */
        public Builder ramHotPlug(@Nullable Output<Boolean> ramHotPlug) {
            $.ramHotPlug = ramHotPlug;
            return this;
        }

        /**
         * @param ramHotPlug (Computed)[string] Is capable of memory hot plug (no reboot required). Can only be updated.
         * 
         * @return builder
         * 
         */
        public Builder ramHotPlug(Boolean ramHotPlug) {
            return ramHotPlug(Output.of(ramHotPlug));
        }

        /**
         * @param ramHotUnplug Is capable of memory hot unplug (no reboot required)
         * 
         * @return builder
         * 
         */
        public Builder ramHotUnplug(@Nullable Output<Boolean> ramHotUnplug) {
            $.ramHotUnplug = ramHotUnplug;
            return this;
        }

        /**
         * @param ramHotUnplug Is capable of memory hot unplug (no reboot required)
         * 
         * @return builder
         * 
         */
        public Builder ramHotUnplug(Boolean ramHotUnplug) {
            return ramHotUnplug(Output.of(ramHotUnplug));
        }

        /**
         * @param secAuthProtection Boolean value representing if the snapshot requires extra protection e.g. two factor protection
         * 
         * @return builder
         * 
         */
        public Builder secAuthProtection(@Nullable Output<Boolean> secAuthProtection) {
            $.secAuthProtection = secAuthProtection;
            return this;
        }

        /**
         * @param secAuthProtection Boolean value representing if the snapshot requires extra protection e.g. two factor protection
         * 
         * @return builder
         * 
         */
        public Builder secAuthProtection(Boolean secAuthProtection) {
            return secAuthProtection(Output.of(secAuthProtection));
        }

        /**
         * @param size The size of the image in GB
         * 
         * @return builder
         * 
         */
        public Builder size(@Nullable Output<Integer> size) {
            $.size = size;
            return this;
        }

        /**
         * @param size The size of the image in GB
         * 
         * @return builder
         * 
         */
        public Builder size(Integer size) {
            return size(Output.of(size));
        }

        /**
         * @param volumeId [string] The ID of the specific volume to take the snapshot from.
         * 
         * @return builder
         * 
         */
        public Builder volumeId(@Nullable Output<String> volumeId) {
            $.volumeId = volumeId;
            return this;
        }

        /**
         * @param volumeId [string] The ID of the specific volume to take the snapshot from.
         * 
         * @return builder
         * 
         */
        public Builder volumeId(String volumeId) {
            return volumeId(Output.of(volumeId));
        }

        public SnapshotState build() {
            return $;
        }
    }

}
