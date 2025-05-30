// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.alb.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetForwardingRuleArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetForwardingRuleArgs Empty = new GetForwardingRuleArgs();

    /**
     * Application Load Balancer&#39;s UUID.
     * 
     */
    @Import(name="applicationLoadbalancerId", required=true)
    private Output<String> applicationLoadbalancerId;

    /**
     * @return Application Load Balancer&#39;s UUID.
     * 
     */
    public Output<String> applicationLoadbalancerId() {
        return this.applicationLoadbalancerId;
    }

    /**
     * Datacenter&#39;s UUID.
     * 
     */
    @Import(name="datacenterId", required=true)
    private Output<String> datacenterId;

    /**
     * @return Datacenter&#39;s UUID.
     * 
     */
    public Output<String> datacenterId() {
        return this.datacenterId;
    }

    /**
     * ID of the application load balancer you want to search for.
     * 
     */
    @Import(name="id")
    private @Nullable Output<String> id;

    /**
     * @return ID of the application load balancer you want to search for.
     * 
     */
    public Optional<Output<String>> id() {
        return Optional.ofNullable(this.id);
    }

    /**
     * Name of an existing application load balancer that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return Name of an existing application load balancer that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * Whether partial matching is allowed or not when using name argument. Default value is false.
     * 
     * Both `datacenter_id` and `application_loadbalancer_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
     * 
     */
    @Import(name="partialMatch")
    private @Nullable Output<Boolean> partialMatch;

    /**
     * @return Whether partial matching is allowed or not when using name argument. Default value is false.
     * 
     * Both `datacenter_id` and `application_loadbalancer_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
     * 
     */
    public Optional<Output<Boolean>> partialMatch() {
        return Optional.ofNullable(this.partialMatch);
    }

    private GetForwardingRuleArgs() {}

    private GetForwardingRuleArgs(GetForwardingRuleArgs $) {
        this.applicationLoadbalancerId = $.applicationLoadbalancerId;
        this.datacenterId = $.datacenterId;
        this.id = $.id;
        this.name = $.name;
        this.partialMatch = $.partialMatch;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetForwardingRuleArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetForwardingRuleArgs $;

        public Builder() {
            $ = new GetForwardingRuleArgs();
        }

        public Builder(GetForwardingRuleArgs defaults) {
            $ = new GetForwardingRuleArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param applicationLoadbalancerId Application Load Balancer&#39;s UUID.
         * 
         * @return builder
         * 
         */
        public Builder applicationLoadbalancerId(Output<String> applicationLoadbalancerId) {
            $.applicationLoadbalancerId = applicationLoadbalancerId;
            return this;
        }

        /**
         * @param applicationLoadbalancerId Application Load Balancer&#39;s UUID.
         * 
         * @return builder
         * 
         */
        public Builder applicationLoadbalancerId(String applicationLoadbalancerId) {
            return applicationLoadbalancerId(Output.of(applicationLoadbalancerId));
        }

        /**
         * @param datacenterId Datacenter&#39;s UUID.
         * 
         * @return builder
         * 
         */
        public Builder datacenterId(Output<String> datacenterId) {
            $.datacenterId = datacenterId;
            return this;
        }

        /**
         * @param datacenterId Datacenter&#39;s UUID.
         * 
         * @return builder
         * 
         */
        public Builder datacenterId(String datacenterId) {
            return datacenterId(Output.of(datacenterId));
        }

        /**
         * @param id ID of the application load balancer you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder id(@Nullable Output<String> id) {
            $.id = id;
            return this;
        }

        /**
         * @param id ID of the application load balancer you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder id(String id) {
            return id(Output.of(id));
        }

        /**
         * @param name Name of an existing application load balancer that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name Name of an existing application load balancer that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param partialMatch Whether partial matching is allowed or not when using name argument. Default value is false.
         * 
         * Both `datacenter_id` and `application_loadbalancer_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
         * 
         * @return builder
         * 
         */
        public Builder partialMatch(@Nullable Output<Boolean> partialMatch) {
            $.partialMatch = partialMatch;
            return this;
        }

        /**
         * @param partialMatch Whether partial matching is allowed or not when using name argument. Default value is false.
         * 
         * Both `datacenter_id` and `application_loadbalancer_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
         * 
         * @return builder
         * 
         */
        public Builder partialMatch(Boolean partialMatch) {
            return partialMatch(Output.of(partialMatch));
        }

        public GetForwardingRuleArgs build() {
            if ($.applicationLoadbalancerId == null) {
                throw new MissingRequiredPropertyException("GetForwardingRuleArgs", "applicationLoadbalancerId");
            }
            if ($.datacenterId == null) {
                throw new MissingRequiredPropertyException("GetForwardingRuleArgs", "datacenterId");
            }
            return $;
        }
    }

}
