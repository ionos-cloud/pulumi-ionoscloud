// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.alb;

import com.ionoscloud.pulumi.ionoscloud.alb.inputs.ForwardingRuleHttpRuleArgs;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class ForwardingRuleArgs extends com.pulumi.resources.ResourceArgs {

    public static final ForwardingRuleArgs Empty = new ForwardingRuleArgs();

    /**
     * [string] The ID of Application Load Balancer.
     * 
     */
    @Import(name="applicationLoadbalancerId", required=true)
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
    @Import(name="clientTimeout")
    private @Nullable Output<Integer> clientTimeout;

    /**
     * @return [int] The maximum time in milliseconds to wait for the client to acknowledge or send data; default is 50,000 (50 seconds).
     * 
     */
    public Optional<Output<Integer>> clientTimeout() {
        return Optional.ofNullable(this.clientTimeout);
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
     * [list] Array of items in that collection
     * 
     */
    @Import(name="httpRules")
    private @Nullable Output<List<ForwardingRuleHttpRuleArgs>> httpRules;

    /**
     * @return [list] Array of items in that collection
     * 
     */
    public Optional<Output<List<ForwardingRuleHttpRuleArgs>>> httpRules() {
        return Optional.ofNullable(this.httpRules);
    }

    /**
     * [string] Listening (inbound) IP.
     * 
     */
    @Import(name="listenerIp", required=true)
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
    @Import(name="listenerPort", required=true)
    private Output<Integer> listenerPort;

    /**
     * @return [int] Listening (inbound) port number; valid range is 1 to 65535.
     * 
     */
    public Output<Integer> listenerPort() {
        return this.listenerPort;
    }

    /**
     * [string] The name of the Application Load Balancer forwarding rule.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return [string] The name of the Application Load Balancer forwarding rule.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * [string] Balancing protocol.
     * 
     */
    @Import(name="protocol", required=true)
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
    @Import(name="serverCertificates")
    private @Nullable Output<List<String>> serverCertificates;

    /**
     * @return [list] Array of certificate ids. You can create certificates with the certificate resource.
     * 
     */
    public Optional<Output<List<String>>> serverCertificates() {
        return Optional.ofNullable(this.serverCertificates);
    }

    private ForwardingRuleArgs() {}

    private ForwardingRuleArgs(ForwardingRuleArgs $) {
        this.applicationLoadbalancerId = $.applicationLoadbalancerId;
        this.clientTimeout = $.clientTimeout;
        this.datacenterId = $.datacenterId;
        this.httpRules = $.httpRules;
        this.listenerIp = $.listenerIp;
        this.listenerPort = $.listenerPort;
        this.name = $.name;
        this.protocol = $.protocol;
        this.serverCertificates = $.serverCertificates;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ForwardingRuleArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ForwardingRuleArgs $;

        public Builder() {
            $ = new ForwardingRuleArgs();
        }

        public Builder(ForwardingRuleArgs defaults) {
            $ = new ForwardingRuleArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param applicationLoadbalancerId [string] The ID of Application Load Balancer.
         * 
         * @return builder
         * 
         */
        public Builder applicationLoadbalancerId(Output<String> applicationLoadbalancerId) {
            $.applicationLoadbalancerId = applicationLoadbalancerId;
            return this;
        }

        /**
         * @param applicationLoadbalancerId [string] The ID of Application Load Balancer.
         * 
         * @return builder
         * 
         */
        public Builder applicationLoadbalancerId(String applicationLoadbalancerId) {
            return applicationLoadbalancerId(Output.of(applicationLoadbalancerId));
        }

        /**
         * @param clientTimeout [int] The maximum time in milliseconds to wait for the client to acknowledge or send data; default is 50,000 (50 seconds).
         * 
         * @return builder
         * 
         */
        public Builder clientTimeout(@Nullable Output<Integer> clientTimeout) {
            $.clientTimeout = clientTimeout;
            return this;
        }

        /**
         * @param clientTimeout [int] The maximum time in milliseconds to wait for the client to acknowledge or send data; default is 50,000 (50 seconds).
         * 
         * @return builder
         * 
         */
        public Builder clientTimeout(Integer clientTimeout) {
            return clientTimeout(Output.of(clientTimeout));
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
         * @param httpRules [list] Array of items in that collection
         * 
         * @return builder
         * 
         */
        public Builder httpRules(@Nullable Output<List<ForwardingRuleHttpRuleArgs>> httpRules) {
            $.httpRules = httpRules;
            return this;
        }

        /**
         * @param httpRules [list] Array of items in that collection
         * 
         * @return builder
         * 
         */
        public Builder httpRules(List<ForwardingRuleHttpRuleArgs> httpRules) {
            return httpRules(Output.of(httpRules));
        }

        /**
         * @param httpRules [list] Array of items in that collection
         * 
         * @return builder
         * 
         */
        public Builder httpRules(ForwardingRuleHttpRuleArgs... httpRules) {
            return httpRules(List.of(httpRules));
        }

        /**
         * @param listenerIp [string] Listening (inbound) IP.
         * 
         * @return builder
         * 
         */
        public Builder listenerIp(Output<String> listenerIp) {
            $.listenerIp = listenerIp;
            return this;
        }

        /**
         * @param listenerIp [string] Listening (inbound) IP.
         * 
         * @return builder
         * 
         */
        public Builder listenerIp(String listenerIp) {
            return listenerIp(Output.of(listenerIp));
        }

        /**
         * @param listenerPort [int] Listening (inbound) port number; valid range is 1 to 65535.
         * 
         * @return builder
         * 
         */
        public Builder listenerPort(Output<Integer> listenerPort) {
            $.listenerPort = listenerPort;
            return this;
        }

        /**
         * @param listenerPort [int] Listening (inbound) port number; valid range is 1 to 65535.
         * 
         * @return builder
         * 
         */
        public Builder listenerPort(Integer listenerPort) {
            return listenerPort(Output.of(listenerPort));
        }

        /**
         * @param name [string] The name of the Application Load Balancer forwarding rule.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name [string] The name of the Application Load Balancer forwarding rule.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param protocol [string] Balancing protocol.
         * 
         * @return builder
         * 
         */
        public Builder protocol(Output<String> protocol) {
            $.protocol = protocol;
            return this;
        }

        /**
         * @param protocol [string] Balancing protocol.
         * 
         * @return builder
         * 
         */
        public Builder protocol(String protocol) {
            return protocol(Output.of(protocol));
        }

        /**
         * @param serverCertificates [list] Array of certificate ids. You can create certificates with the certificate resource.
         * 
         * @return builder
         * 
         */
        public Builder serverCertificates(@Nullable Output<List<String>> serverCertificates) {
            $.serverCertificates = serverCertificates;
            return this;
        }

        /**
         * @param serverCertificates [list] Array of certificate ids. You can create certificates with the certificate resource.
         * 
         * @return builder
         * 
         */
        public Builder serverCertificates(List<String> serverCertificates) {
            return serverCertificates(Output.of(serverCertificates));
        }

        /**
         * @param serverCertificates [list] Array of certificate ids. You can create certificates with the certificate resource.
         * 
         * @return builder
         * 
         */
        public Builder serverCertificates(String... serverCertificates) {
            return serverCertificates(List.of(serverCertificates));
        }

        public ForwardingRuleArgs build() {
            if ($.applicationLoadbalancerId == null) {
                throw new MissingRequiredPropertyException("ForwardingRuleArgs", "applicationLoadbalancerId");
            }
            if ($.datacenterId == null) {
                throw new MissingRequiredPropertyException("ForwardingRuleArgs", "datacenterId");
            }
            if ($.listenerIp == null) {
                throw new MissingRequiredPropertyException("ForwardingRuleArgs", "listenerIp");
            }
            if ($.listenerPort == null) {
                throw new MissingRequiredPropertyException("ForwardingRuleArgs", "listenerPort");
            }
            if ($.protocol == null) {
                throw new MissingRequiredPropertyException("ForwardingRuleArgs", "protocol");
            }
            return $;
        }
    }

}
