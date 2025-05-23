// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.nlb.inputs;

import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetForwardingRulePlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetForwardingRulePlainArgs Empty = new GetForwardingRulePlainArgs();

    /**
     * Datacenter&#39;s UUID.
     * 
     */
    @Import(name="datacenterId", required=true)
    private String datacenterId;

    /**
     * @return Datacenter&#39;s UUID.
     * 
     */
    public String datacenterId() {
        return this.datacenterId;
    }

    /**
     * ID of the network load balancer forwarding rule you want to search for.
     * 
     * Both `datacenter_id` and `networkloadbalancer_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
     * 
     */
    @Import(name="id")
    private @Nullable String id;

    /**
     * @return ID of the network load balancer forwarding rule you want to search for.
     * 
     * Both `datacenter_id` and `networkloadbalancer_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
     * 
     */
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }

    /**
     * Name of an existing network load balancer forwarding rule that you want to search for.
     * 
     */
    @Import(name="name")
    private @Nullable String name;

    /**
     * @return Name of an existing network load balancer forwarding rule that you want to search for.
     * 
     */
    public Optional<String> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * Network Load Balancer&#39;s UUID.
     * 
     */
    @Import(name="networkloadbalancerId", required=true)
    private String networkloadbalancerId;

    /**
     * @return Network Load Balancer&#39;s UUID.
     * 
     */
    public String networkloadbalancerId() {
        return this.networkloadbalancerId;
    }

    private GetForwardingRulePlainArgs() {}

    private GetForwardingRulePlainArgs(GetForwardingRulePlainArgs $) {
        this.datacenterId = $.datacenterId;
        this.id = $.id;
        this.name = $.name;
        this.networkloadbalancerId = $.networkloadbalancerId;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetForwardingRulePlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetForwardingRulePlainArgs $;

        public Builder() {
            $ = new GetForwardingRulePlainArgs();
        }

        public Builder(GetForwardingRulePlainArgs defaults) {
            $ = new GetForwardingRulePlainArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param datacenterId Datacenter&#39;s UUID.
         * 
         * @return builder
         * 
         */
        public Builder datacenterId(String datacenterId) {
            $.datacenterId = datacenterId;
            return this;
        }

        /**
         * @param id ID of the network load balancer forwarding rule you want to search for.
         * 
         * Both `datacenter_id` and `networkloadbalancer_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
         * 
         * @return builder
         * 
         */
        public Builder id(@Nullable String id) {
            $.id = id;
            return this;
        }

        /**
         * @param name Name of an existing network load balancer forwarding rule that you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable String name) {
            $.name = name;
            return this;
        }

        /**
         * @param networkloadbalancerId Network Load Balancer&#39;s UUID.
         * 
         * @return builder
         * 
         */
        public Builder networkloadbalancerId(String networkloadbalancerId) {
            $.networkloadbalancerId = networkloadbalancerId;
            return this;
        }

        public GetForwardingRulePlainArgs build() {
            if ($.datacenterId == null) {
                throw new MissingRequiredPropertyException("GetForwardingRulePlainArgs", "datacenterId");
            }
            if ($.networkloadbalancerId == null) {
                throw new MissingRequiredPropertyException("GetForwardingRulePlainArgs", "networkloadbalancerId");
            }
            return $;
        }
    }

}
