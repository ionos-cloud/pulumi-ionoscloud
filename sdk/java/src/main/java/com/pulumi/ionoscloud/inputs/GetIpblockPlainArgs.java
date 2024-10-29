// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.annotations.Import;
import com.pulumi.ionoscloud.inputs.GetIpblockIpConsumer;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetIpblockPlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetIpblockPlainArgs Empty = new GetIpblockPlainArgs();

    /**
     * ID of an existing Ip Block that you want to search for.
     * 
     */
    @Import(name="id")
    private @Nullable String id;

    /**
     * @return ID of an existing Ip Block that you want to search for.
     * 
     */
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }

    /**
     * Read-Only attribute. Lists consumption detail of an individual ip
     * 
     */
    @Import(name="ipConsumers")
    private @Nullable List<GetIpblockIpConsumer> ipConsumers;

    /**
     * @return Read-Only attribute. Lists consumption detail of an individual ip
     * 
     */
    public Optional<List<GetIpblockIpConsumer>> ipConsumers() {
        return Optional.ofNullable(this.ipConsumers);
    }

    /**
     * The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
     * 
     */
    @Import(name="location")
    private @Nullable String location;

    /**
     * @return The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
     * 
     */
    public Optional<String> location() {
        return Optional.ofNullable(this.location);
    }

    /**
     * Name of an existing Ip Block that you want to search for.
     * 
     */
    @Import(name="name")
    private @Nullable String name;

    /**
     * @return Name of an existing Ip Block that you want to search for.
     * 
     */
    public Optional<String> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * The number of IP addresses to reserve for this block.
     * 
     */
    @Import(name="size")
    private @Nullable Integer size;

    /**
     * @return The number of IP addresses to reserve for this block.
     * 
     */
    public Optional<Integer> size() {
        return Optional.ofNullable(this.size);
    }

    private GetIpblockPlainArgs() {}

    private GetIpblockPlainArgs(GetIpblockPlainArgs $) {
        this.id = $.id;
        this.ipConsumers = $.ipConsumers;
        this.location = $.location;
        this.name = $.name;
        this.size = $.size;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetIpblockPlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetIpblockPlainArgs $;

        public Builder() {
            $ = new GetIpblockPlainArgs();
        }

        public Builder(GetIpblockPlainArgs defaults) {
            $ = new GetIpblockPlainArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param id ID of an existing Ip Block that you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder id(@Nullable String id) {
            $.id = id;
            return this;
        }

        /**
         * @param ipConsumers Read-Only attribute. Lists consumption detail of an individual ip
         * 
         * @return builder
         * 
         */
        public Builder ipConsumers(@Nullable List<GetIpblockIpConsumer> ipConsumers) {
            $.ipConsumers = ipConsumers;
            return this;
        }

        /**
         * @param ipConsumers Read-Only attribute. Lists consumption detail of an individual ip
         * 
         * @return builder
         * 
         */
        public Builder ipConsumers(GetIpblockIpConsumer... ipConsumers) {
            return ipConsumers(List.of(ipConsumers));
        }

        /**
         * @param location The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
         * 
         * @return builder
         * 
         */
        public Builder location(@Nullable String location) {
            $.location = location;
            return this;
        }

        /**
         * @param name Name of an existing Ip Block that you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable String name) {
            $.name = name;
            return this;
        }

        /**
         * @param size The number of IP addresses to reserve for this block.
         * 
         * @return builder
         * 
         */
        public Builder size(@Nullable Integer size) {
            $.size = size;
            return this;
        }

        public GetIpblockPlainArgs build() {
            return $;
        }
    }

}
