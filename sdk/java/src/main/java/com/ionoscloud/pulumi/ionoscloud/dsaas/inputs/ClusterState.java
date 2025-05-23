// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.dsaas.inputs;

import com.ionoscloud.pulumi.ionoscloud.dsaas.inputs.ClusterLanArgs;
import com.ionoscloud.pulumi.ionoscloud.dsaas.inputs.ClusterMaintenanceWindowArgs;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class ClusterState extends com.pulumi.resources.ResourceArgs {

    public static final ClusterState Empty = new ClusterState();

    /**
     * [string] The UUID of the virtual data center (VDC) the cluster is provisioned.
     * 
     */
    @Import(name="datacenterId")
    private @Nullable Output<String> datacenterId;

    /**
     * @return [string] The UUID of the virtual data center (VDC) the cluster is provisioned.
     * 
     */
    public Optional<Output<String>> datacenterId() {
        return Optional.ofNullable(this.datacenterId);
    }

    /**
     * [list] A list of LANs you want this node pool to be part of.
     * 
     */
    @Import(name="lans")
    private @Nullable Output<List<ClusterLanArgs>> lans;

    /**
     * @return [list] A list of LANs you want this node pool to be part of.
     * 
     */
    public Optional<Output<List<ClusterLanArgs>>> lans() {
        return Optional.ofNullable(this.lans);
    }

    /**
     * Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
     * 
     */
    @Import(name="maintenanceWindows")
    private @Nullable Output<List<ClusterMaintenanceWindowArgs>> maintenanceWindows;

    /**
     * @return Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
     * 
     */
    public Optional<Output<List<ClusterMaintenanceWindowArgs>>> maintenanceWindows() {
        return Optional.ofNullable(this.maintenanceWindows);
    }

    /**
     * [string] The name of your cluster. Must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return [string] The name of your cluster. Must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * [int] The version of the Data Platform.
     * 
     */
    @Import(name="version")
    private @Nullable Output<String> version;

    /**
     * @return [int] The version of the Data Platform.
     * 
     */
    public Optional<Output<String>> version() {
        return Optional.ofNullable(this.version);
    }

    private ClusterState() {}

    private ClusterState(ClusterState $) {
        this.datacenterId = $.datacenterId;
        this.lans = $.lans;
        this.maintenanceWindows = $.maintenanceWindows;
        this.name = $.name;
        this.version = $.version;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ClusterState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ClusterState $;

        public Builder() {
            $ = new ClusterState();
        }

        public Builder(ClusterState defaults) {
            $ = new ClusterState(Objects.requireNonNull(defaults));
        }

        /**
         * @param datacenterId [string] The UUID of the virtual data center (VDC) the cluster is provisioned.
         * 
         * @return builder
         * 
         */
        public Builder datacenterId(@Nullable Output<String> datacenterId) {
            $.datacenterId = datacenterId;
            return this;
        }

        /**
         * @param datacenterId [string] The UUID of the virtual data center (VDC) the cluster is provisioned.
         * 
         * @return builder
         * 
         */
        public Builder datacenterId(String datacenterId) {
            return datacenterId(Output.of(datacenterId));
        }

        /**
         * @param lans [list] A list of LANs you want this node pool to be part of.
         * 
         * @return builder
         * 
         */
        public Builder lans(@Nullable Output<List<ClusterLanArgs>> lans) {
            $.lans = lans;
            return this;
        }

        /**
         * @param lans [list] A list of LANs you want this node pool to be part of.
         * 
         * @return builder
         * 
         */
        public Builder lans(List<ClusterLanArgs> lans) {
            return lans(Output.of(lans));
        }

        /**
         * @param lans [list] A list of LANs you want this node pool to be part of.
         * 
         * @return builder
         * 
         */
        public Builder lans(ClusterLanArgs... lans) {
            return lans(List.of(lans));
        }

        /**
         * @param maintenanceWindows Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
         * 
         * @return builder
         * 
         */
        public Builder maintenanceWindows(@Nullable Output<List<ClusterMaintenanceWindowArgs>> maintenanceWindows) {
            $.maintenanceWindows = maintenanceWindows;
            return this;
        }

        /**
         * @param maintenanceWindows Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
         * 
         * @return builder
         * 
         */
        public Builder maintenanceWindows(List<ClusterMaintenanceWindowArgs> maintenanceWindows) {
            return maintenanceWindows(Output.of(maintenanceWindows));
        }

        /**
         * @param maintenanceWindows Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
         * 
         * @return builder
         * 
         */
        public Builder maintenanceWindows(ClusterMaintenanceWindowArgs... maintenanceWindows) {
            return maintenanceWindows(List.of(maintenanceWindows));
        }

        /**
         * @param name [string] The name of your cluster. Must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name [string] The name of your cluster. Must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param version [int] The version of the Data Platform.
         * 
         * @return builder
         * 
         */
        public Builder version(@Nullable Output<String> version) {
            $.version = version;
            return this;
        }

        /**
         * @param version [int] The version of the Data Platform.
         * 
         * @return builder
         * 
         */
        public Builder version(String version) {
            return version(Output.of(version));
        }

        public ClusterState build() {
            return $;
        }
    }

}
