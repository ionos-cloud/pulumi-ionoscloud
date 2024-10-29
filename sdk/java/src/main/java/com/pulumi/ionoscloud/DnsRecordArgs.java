// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class DnsRecordArgs extends com.pulumi.resources.ResourceArgs {

    public static final DnsRecordArgs Empty = new DnsRecordArgs();

    /**
     * [string] The content of the DNS Record.
     * 
     */
    @Import(name="content", required=true)
    private Output<String> content;

    /**
     * @return [string] The content of the DNS Record.
     * 
     */
    public Output<String> content() {
        return this.content;
    }

    /**
     * [bool] Indicates if the DNS Record is active or not. Default is `true`.
     * 
     */
    @Import(name="enabled")
    private @Nullable Output<Boolean> enabled;

    /**
     * @return [bool] Indicates if the DNS Record is active or not. Default is `true`.
     * 
     */
    public Optional<Output<Boolean>> enabled() {
        return Optional.ofNullable(this.enabled);
    }

    /**
     * [string] The name of the DNS Record.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return [string] The name of the DNS Record.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * [int] The priority for the DNS Record.
     * 
     */
    @Import(name="priority")
    private @Nullable Output<Integer> priority;

    /**
     * @return [int] The priority for the DNS Record.
     * 
     */
    public Optional<Output<Integer>> priority() {
        return Optional.ofNullable(this.priority);
    }

    /**
     * [int] Time to live for the DNS Record. Default is `3600`.
     * 
     */
    @Import(name="ttl")
    private @Nullable Output<Integer> ttl;

    /**
     * @return [int] Time to live for the DNS Record. Default is `3600`.
     * 
     */
    public Optional<Output<Integer>> ttl() {
        return Optional.ofNullable(this.ttl);
    }

    /**
     * [string] The type of the DNS Record, can have one of these values: `A, AAAA, CNAME, ALIAS, MX, NS, SRV, TXT, CAA, SSHFP, TLSA, SMIMEA, DS, HTTPS, SVCB, OPENPGPKEY, CERT, URI, RP, LOC`. More details about types can be found [here](https://docs.ionos.com/dns-as-a-service/readme/api-how-tos/create-a-new-dns-record#create-records-of-other-types).
     * 
     */
    @Import(name="type", required=true)
    private Output<String> type;

    /**
     * @return [string] The type of the DNS Record, can have one of these values: `A, AAAA, CNAME, ALIAS, MX, NS, SRV, TXT, CAA, SSHFP, TLSA, SMIMEA, DS, HTTPS, SVCB, OPENPGPKEY, CERT, URI, RP, LOC`. More details about types can be found [here](https://docs.ionos.com/dns-as-a-service/readme/api-how-tos/create-a-new-dns-record#create-records-of-other-types).
     * 
     */
    public Output<String> type() {
        return this.type;
    }

    /**
     * [string] The DNS Zone ID in which the DNS Record will be created.
     * 
     */
    @Import(name="zoneId", required=true)
    private Output<String> zoneId;

    /**
     * @return [string] The DNS Zone ID in which the DNS Record will be created.
     * 
     */
    public Output<String> zoneId() {
        return this.zoneId;
    }

    private DnsRecordArgs() {}

    private DnsRecordArgs(DnsRecordArgs $) {
        this.content = $.content;
        this.enabled = $.enabled;
        this.name = $.name;
        this.priority = $.priority;
        this.ttl = $.ttl;
        this.type = $.type;
        this.zoneId = $.zoneId;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(DnsRecordArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private DnsRecordArgs $;

        public Builder() {
            $ = new DnsRecordArgs();
        }

        public Builder(DnsRecordArgs defaults) {
            $ = new DnsRecordArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param content [string] The content of the DNS Record.
         * 
         * @return builder
         * 
         */
        public Builder content(Output<String> content) {
            $.content = content;
            return this;
        }

        /**
         * @param content [string] The content of the DNS Record.
         * 
         * @return builder
         * 
         */
        public Builder content(String content) {
            return content(Output.of(content));
        }

        /**
         * @param enabled [bool] Indicates if the DNS Record is active or not. Default is `true`.
         * 
         * @return builder
         * 
         */
        public Builder enabled(@Nullable Output<Boolean> enabled) {
            $.enabled = enabled;
            return this;
        }

        /**
         * @param enabled [bool] Indicates if the DNS Record is active or not. Default is `true`.
         * 
         * @return builder
         * 
         */
        public Builder enabled(Boolean enabled) {
            return enabled(Output.of(enabled));
        }

        /**
         * @param name [string] The name of the DNS Record.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name [string] The name of the DNS Record.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param priority [int] The priority for the DNS Record.
         * 
         * @return builder
         * 
         */
        public Builder priority(@Nullable Output<Integer> priority) {
            $.priority = priority;
            return this;
        }

        /**
         * @param priority [int] The priority for the DNS Record.
         * 
         * @return builder
         * 
         */
        public Builder priority(Integer priority) {
            return priority(Output.of(priority));
        }

        /**
         * @param ttl [int] Time to live for the DNS Record. Default is `3600`.
         * 
         * @return builder
         * 
         */
        public Builder ttl(@Nullable Output<Integer> ttl) {
            $.ttl = ttl;
            return this;
        }

        /**
         * @param ttl [int] Time to live for the DNS Record. Default is `3600`.
         * 
         * @return builder
         * 
         */
        public Builder ttl(Integer ttl) {
            return ttl(Output.of(ttl));
        }

        /**
         * @param type [string] The type of the DNS Record, can have one of these values: `A, AAAA, CNAME, ALIAS, MX, NS, SRV, TXT, CAA, SSHFP, TLSA, SMIMEA, DS, HTTPS, SVCB, OPENPGPKEY, CERT, URI, RP, LOC`. More details about types can be found [here](https://docs.ionos.com/dns-as-a-service/readme/api-how-tos/create-a-new-dns-record#create-records-of-other-types).
         * 
         * @return builder
         * 
         */
        public Builder type(Output<String> type) {
            $.type = type;
            return this;
        }

        /**
         * @param type [string] The type of the DNS Record, can have one of these values: `A, AAAA, CNAME, ALIAS, MX, NS, SRV, TXT, CAA, SSHFP, TLSA, SMIMEA, DS, HTTPS, SVCB, OPENPGPKEY, CERT, URI, RP, LOC`. More details about types can be found [here](https://docs.ionos.com/dns-as-a-service/readme/api-how-tos/create-a-new-dns-record#create-records-of-other-types).
         * 
         * @return builder
         * 
         */
        public Builder type(String type) {
            return type(Output.of(type));
        }

        /**
         * @param zoneId [string] The DNS Zone ID in which the DNS Record will be created.
         * 
         * @return builder
         * 
         */
        public Builder zoneId(Output<String> zoneId) {
            $.zoneId = zoneId;
            return this;
        }

        /**
         * @param zoneId [string] The DNS Zone ID in which the DNS Record will be created.
         * 
         * @return builder
         * 
         */
        public Builder zoneId(String zoneId) {
            return zoneId(Output.of(zoneId));
        }

        public DnsRecordArgs build() {
            if ($.content == null) {
                throw new MissingRequiredPropertyException("DnsRecordArgs", "content");
            }
            if ($.type == null) {
                throw new MissingRequiredPropertyException("DnsRecordArgs", "type");
            }
            if ($.zoneId == null) {
                throw new MissingRequiredPropertyException("DnsRecordArgs", "zoneId");
            }
            return $;
        }
    }

}
