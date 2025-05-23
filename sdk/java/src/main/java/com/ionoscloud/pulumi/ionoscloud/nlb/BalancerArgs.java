// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.nlb;

import com.ionoscloud.pulumi.ionoscloud.nlb.inputs.BalancerFlowlogArgs;
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


public final class BalancerArgs extends com.pulumi.resources.ResourceArgs {

    public static final BalancerArgs Empty = new BalancerArgs();

    /**
     * [bool] Turn logging on and off for this product. Default value is &#39;false&#39;.
     * 
     */
    @Import(name="centralLogging")
    private @Nullable Output<Boolean> centralLogging;

    /**
     * @return [bool] Turn logging on and off for this product. Default value is &#39;false&#39;.
     * 
     */
    public Optional<Output<Boolean>> centralLogging() {
        return Optional.ofNullable(this.centralLogging);
    }

    /**
     * [string] A Datacenter&#39;s UUID.
     * 
     */
    @Import(name="datacenterId", required=true)
    private Output<String> datacenterId;

    /**
     * @return [string] A Datacenter&#39;s UUID.
     * 
     */
    public Output<String> datacenterId() {
        return this.datacenterId;
    }

    /**
     * [list] Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
     * 
     */
    @Import(name="flowlog")
    private @Nullable Output<BalancerFlowlogArgs> flowlog;

    /**
     * @return [list] Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
     * 
     */
    public Optional<Output<BalancerFlowlogArgs>> flowlog() {
        return Optional.ofNullable(this.flowlog);
    }

    /**
     * [list] Collection of IP addresses of the Network Load Balancer. (inbound and outbound) IP of the listenerLan must be a customer reserved IP for the public load balancer and private IP for the private load balancer.
     * 
     */
    @Import(name="ips")
    private @Nullable Output<List<String>> ips;

    /**
     * @return [list] Collection of IP addresses of the Network Load Balancer. (inbound and outbound) IP of the listenerLan must be a customer reserved IP for the public load balancer and private IP for the private load balancer.
     * 
     */
    public Optional<Output<List<String>>> ips() {
        return Optional.ofNullable(this.ips);
    }

    /**
     * [list] Collection of private IP addresses with subnet mask of the Network Load Balancer. IPs must contain valid subnet mask. If user will not provide any IP then the system will generate one IP with /24 subnet.
     * 
     */
    @Import(name="lbPrivateIps")
    private @Nullable Output<List<String>> lbPrivateIps;

    /**
     * @return [list] Collection of private IP addresses with subnet mask of the Network Load Balancer. IPs must contain valid subnet mask. If user will not provide any IP then the system will generate one IP with /24 subnet.
     * 
     */
    public Optional<Output<List<String>>> lbPrivateIps() {
        return Optional.ofNullable(this.lbPrivateIps);
    }

    /**
     * [int] Id of the listening LAN. (inbound)
     * 
     */
    @Import(name="listenerLan", required=true)
    private Output<Integer> listenerLan;

    /**
     * @return [int] Id of the listening LAN. (inbound)
     * 
     */
    public Output<Integer> listenerLan() {
        return this.listenerLan;
    }

    /**
     * Specifies the format of the logs.
     * 
     */
    @Import(name="loggingFormat")
    private @Nullable Output<String> loggingFormat;

    /**
     * @return Specifies the format of the logs.
     * 
     */
    public Optional<Output<String>> loggingFormat() {
        return Optional.ofNullable(this.loggingFormat);
    }

    /**
     * [string] A name of that Network Load Balancer.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return [string] A name of that Network Load Balancer.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * [int] Id of the balanced private target LAN. (outbound)
     * 
     */
    @Import(name="targetLan", required=true)
    private Output<Integer> targetLan;

    /**
     * @return [int] Id of the balanced private target LAN. (outbound)
     * 
     */
    public Output<Integer> targetLan() {
        return this.targetLan;
    }

    private BalancerArgs() {}

    private BalancerArgs(BalancerArgs $) {
        this.centralLogging = $.centralLogging;
        this.datacenterId = $.datacenterId;
        this.flowlog = $.flowlog;
        this.ips = $.ips;
        this.lbPrivateIps = $.lbPrivateIps;
        this.listenerLan = $.listenerLan;
        this.loggingFormat = $.loggingFormat;
        this.name = $.name;
        this.targetLan = $.targetLan;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(BalancerArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private BalancerArgs $;

        public Builder() {
            $ = new BalancerArgs();
        }

        public Builder(BalancerArgs defaults) {
            $ = new BalancerArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param centralLogging [bool] Turn logging on and off for this product. Default value is &#39;false&#39;.
         * 
         * @return builder
         * 
         */
        public Builder centralLogging(@Nullable Output<Boolean> centralLogging) {
            $.centralLogging = centralLogging;
            return this;
        }

        /**
         * @param centralLogging [bool] Turn logging on and off for this product. Default value is &#39;false&#39;.
         * 
         * @return builder
         * 
         */
        public Builder centralLogging(Boolean centralLogging) {
            return centralLogging(Output.of(centralLogging));
        }

        /**
         * @param datacenterId [string] A Datacenter&#39;s UUID.
         * 
         * @return builder
         * 
         */
        public Builder datacenterId(Output<String> datacenterId) {
            $.datacenterId = datacenterId;
            return this;
        }

        /**
         * @param datacenterId [string] A Datacenter&#39;s UUID.
         * 
         * @return builder
         * 
         */
        public Builder datacenterId(String datacenterId) {
            return datacenterId(Output.of(datacenterId));
        }

        /**
         * @param flowlog [list] Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
         * 
         * @return builder
         * 
         */
        public Builder flowlog(@Nullable Output<BalancerFlowlogArgs> flowlog) {
            $.flowlog = flowlog;
            return this;
        }

        /**
         * @param flowlog [list] Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
         * 
         * @return builder
         * 
         */
        public Builder flowlog(BalancerFlowlogArgs flowlog) {
            return flowlog(Output.of(flowlog));
        }

        /**
         * @param ips [list] Collection of IP addresses of the Network Load Balancer. (inbound and outbound) IP of the listenerLan must be a customer reserved IP for the public load balancer and private IP for the private load balancer.
         * 
         * @return builder
         * 
         */
        public Builder ips(@Nullable Output<List<String>> ips) {
            $.ips = ips;
            return this;
        }

        /**
         * @param ips [list] Collection of IP addresses of the Network Load Balancer. (inbound and outbound) IP of the listenerLan must be a customer reserved IP for the public load balancer and private IP for the private load balancer.
         * 
         * @return builder
         * 
         */
        public Builder ips(List<String> ips) {
            return ips(Output.of(ips));
        }

        /**
         * @param ips [list] Collection of IP addresses of the Network Load Balancer. (inbound and outbound) IP of the listenerLan must be a customer reserved IP for the public load balancer and private IP for the private load balancer.
         * 
         * @return builder
         * 
         */
        public Builder ips(String... ips) {
            return ips(List.of(ips));
        }

        /**
         * @param lbPrivateIps [list] Collection of private IP addresses with subnet mask of the Network Load Balancer. IPs must contain valid subnet mask. If user will not provide any IP then the system will generate one IP with /24 subnet.
         * 
         * @return builder
         * 
         */
        public Builder lbPrivateIps(@Nullable Output<List<String>> lbPrivateIps) {
            $.lbPrivateIps = lbPrivateIps;
            return this;
        }

        /**
         * @param lbPrivateIps [list] Collection of private IP addresses with subnet mask of the Network Load Balancer. IPs must contain valid subnet mask. If user will not provide any IP then the system will generate one IP with /24 subnet.
         * 
         * @return builder
         * 
         */
        public Builder lbPrivateIps(List<String> lbPrivateIps) {
            return lbPrivateIps(Output.of(lbPrivateIps));
        }

        /**
         * @param lbPrivateIps [list] Collection of private IP addresses with subnet mask of the Network Load Balancer. IPs must contain valid subnet mask. If user will not provide any IP then the system will generate one IP with /24 subnet.
         * 
         * @return builder
         * 
         */
        public Builder lbPrivateIps(String... lbPrivateIps) {
            return lbPrivateIps(List.of(lbPrivateIps));
        }

        /**
         * @param listenerLan [int] Id of the listening LAN. (inbound)
         * 
         * @return builder
         * 
         */
        public Builder listenerLan(Output<Integer> listenerLan) {
            $.listenerLan = listenerLan;
            return this;
        }

        /**
         * @param listenerLan [int] Id of the listening LAN. (inbound)
         * 
         * @return builder
         * 
         */
        public Builder listenerLan(Integer listenerLan) {
            return listenerLan(Output.of(listenerLan));
        }

        /**
         * @param loggingFormat Specifies the format of the logs.
         * 
         * @return builder
         * 
         */
        public Builder loggingFormat(@Nullable Output<String> loggingFormat) {
            $.loggingFormat = loggingFormat;
            return this;
        }

        /**
         * @param loggingFormat Specifies the format of the logs.
         * 
         * @return builder
         * 
         */
        public Builder loggingFormat(String loggingFormat) {
            return loggingFormat(Output.of(loggingFormat));
        }

        /**
         * @param name [string] A name of that Network Load Balancer.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name [string] A name of that Network Load Balancer.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param targetLan [int] Id of the balanced private target LAN. (outbound)
         * 
         * @return builder
         * 
         */
        public Builder targetLan(Output<Integer> targetLan) {
            $.targetLan = targetLan;
            return this;
        }

        /**
         * @param targetLan [int] Id of the balanced private target LAN. (outbound)
         * 
         * @return builder
         * 
         */
        public Builder targetLan(Integer targetLan) {
            return targetLan(Output.of(targetLan));
        }

        public BalancerArgs build() {
            if ($.datacenterId == null) {
                throw new MissingRequiredPropertyException("BalancerArgs", "datacenterId");
            }
            if ($.listenerLan == null) {
                throw new MissingRequiredPropertyException("BalancerArgs", "listenerLan");
            }
            if ($.targetLan == null) {
                throw new MissingRequiredPropertyException("BalancerArgs", "targetLan");
            }
            return $;
        }
    }

}
