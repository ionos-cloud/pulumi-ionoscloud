// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.logging.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class PipelineLogDestinationArgs extends com.pulumi.resources.ResourceArgs {

    public static final PipelineLogDestinationArgs Empty = new PipelineLogDestinationArgs();

    /**
     * [int] Defines the number of days a log record should be kept in loki. Works with loki destination type only. Can be one of: 7, 14, 30.
     * 
     */
    @Import(name="retentionInDays")
    private @Nullable Output<Integer> retentionInDays;

    /**
     * @return [int] Defines the number of days a log record should be kept in loki. Works with loki destination type only. Can be one of: 7, 14, 30.
     * 
     */
    public Optional<Output<Integer>> retentionInDays() {
        return Optional.ofNullable(this.retentionInDays);
    }

    /**
     * [string] The internal output stream to send logs to.
     * 
     */
    @Import(name="type")
    private @Nullable Output<String> type;

    /**
     * @return [string] The internal output stream to send logs to.
     * 
     */
    public Optional<Output<String>> type() {
        return Optional.ofNullable(this.type);
    }

    private PipelineLogDestinationArgs() {}

    private PipelineLogDestinationArgs(PipelineLogDestinationArgs $) {
        this.retentionInDays = $.retentionInDays;
        this.type = $.type;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(PipelineLogDestinationArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private PipelineLogDestinationArgs $;

        public Builder() {
            $ = new PipelineLogDestinationArgs();
        }

        public Builder(PipelineLogDestinationArgs defaults) {
            $ = new PipelineLogDestinationArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param retentionInDays [int] Defines the number of days a log record should be kept in loki. Works with loki destination type only. Can be one of: 7, 14, 30.
         * 
         * @return builder
         * 
         */
        public Builder retentionInDays(@Nullable Output<Integer> retentionInDays) {
            $.retentionInDays = retentionInDays;
            return this;
        }

        /**
         * @param retentionInDays [int] Defines the number of days a log record should be kept in loki. Works with loki destination type only. Can be one of: 7, 14, 30.
         * 
         * @return builder
         * 
         */
        public Builder retentionInDays(Integer retentionInDays) {
            return retentionInDays(Output.of(retentionInDays));
        }

        /**
         * @param type [string] The internal output stream to send logs to.
         * 
         * @return builder
         * 
         */
        public Builder type(@Nullable Output<String> type) {
            $.type = type;
            return this;
        }

        /**
         * @param type [string] The internal output stream to send logs to.
         * 
         * @return builder
         * 
         */
        public Builder type(String type) {
            return type(Output.of(type));
        }

        public PipelineLogDestinationArgs build() {
            return $;
        }
    }

}
