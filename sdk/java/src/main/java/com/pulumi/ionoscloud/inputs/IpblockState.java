// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.ionoscloud.inputs.IpblockIpConsumerArgs;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class IpblockState extends com.pulumi.resources.ResourceArgs {

    public static final IpblockState Empty = new IpblockState();

    /**
     * Read-Only attribute. Lists consumption detail of an individual ip
     * 
     */
    @Import(name="ipConsumers")
    private @Nullable Output<List<IpblockIpConsumerArgs>> ipConsumers;

    /**
     * @return Read-Only attribute. Lists consumption detail of an individual ip
     * 
     */
    public Optional<Output<List<IpblockIpConsumerArgs>>> ipConsumers() {
        return Optional.ofNullable(this.ipConsumers);
    }

    /**
     * [integer] The list of IP addresses associated with this block.
     * 
     */
    @Import(name="ips")
    private @Nullable Output<List<String>> ips;

    /**
     * @return [integer] The list of IP addresses associated with this block.
     * 
     */
    public Optional<Output<List<String>>> ips() {
        return Optional.ofNullable(this.ips);
    }

    /**
     * [string] The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
     * 
     */
    @Import(name="location")
    private @Nullable Output<String> location;

    /**
     * @return [string] The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
     * 
     */
    public Optional<Output<String>> location() {
        return Optional.ofNullable(this.location);
    }

    /**
     * [string] The name of Ip Block
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return [string] The name of Ip Block
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * [integer] The number of IP addresses to reserve for this block.
     * 
     */
    @Import(name="size")
    private @Nullable Output<Integer> size;

    /**
     * @return [integer] The number of IP addresses to reserve for this block.
     * 
     */
    public Optional<Output<Integer>> size() {
        return Optional.ofNullable(this.size);
    }

    private IpblockState() {}

    private IpblockState(IpblockState $) {
        this.ipConsumers = $.ipConsumers;
        this.ips = $.ips;
        this.location = $.location;
        this.name = $.name;
        this.size = $.size;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(IpblockState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private IpblockState $;

        public Builder() {
            $ = new IpblockState();
        }

        public Builder(IpblockState defaults) {
            $ = new IpblockState(Objects.requireNonNull(defaults));
        }

        /**
         * @param ipConsumers Read-Only attribute. Lists consumption detail of an individual ip
         * 
         * @return builder
         * 
         */
        public Builder ipConsumers(@Nullable Output<List<IpblockIpConsumerArgs>> ipConsumers) {
            $.ipConsumers = ipConsumers;
            return this;
        }

        /**
         * @param ipConsumers Read-Only attribute. Lists consumption detail of an individual ip
         * 
         * @return builder
         * 
         */
        public Builder ipConsumers(List<IpblockIpConsumerArgs> ipConsumers) {
            return ipConsumers(Output.of(ipConsumers));
        }

        /**
         * @param ipConsumers Read-Only attribute. Lists consumption detail of an individual ip
         * 
         * @return builder
         * 
         */
        public Builder ipConsumers(IpblockIpConsumerArgs... ipConsumers) {
            return ipConsumers(List.of(ipConsumers));
        }

        /**
         * @param ips [integer] The list of IP addresses associated with this block.
         * 
         * @return builder
         * 
         */
        public Builder ips(@Nullable Output<List<String>> ips) {
            $.ips = ips;
            return this;
        }

        /**
         * @param ips [integer] The list of IP addresses associated with this block.
         * 
         * @return builder
         * 
         */
        public Builder ips(List<String> ips) {
            return ips(Output.of(ips));
        }

        /**
         * @param ips [integer] The list of IP addresses associated with this block.
         * 
         * @return builder
         * 
         */
        public Builder ips(String... ips) {
            return ips(List.of(ips));
        }

        /**
         * @param location [string] The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
         * 
         * @return builder
         * 
         */
        public Builder location(@Nullable Output<String> location) {
            $.location = location;
            return this;
        }

        /**
         * @param location [string] The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
         * 
         * @return builder
         * 
         */
        public Builder location(String location) {
            return location(Output.of(location));
        }

        /**
         * @param name [string] The name of Ip Block
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name [string] The name of Ip Block
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param size [integer] The number of IP addresses to reserve for this block.
         * 
         * @return builder
         * 
         */
        public Builder size(@Nullable Output<Integer> size) {
            $.size = size;
            return this;
        }

        /**
         * @param size [integer] The number of IP addresses to reserve for this block.
         * 
         * @return builder
         * 
         */
        public Builder size(Integer size) {
            return size(Output.of(size));
        }

        public IpblockState build() {
            return $;
        }
    }

}
