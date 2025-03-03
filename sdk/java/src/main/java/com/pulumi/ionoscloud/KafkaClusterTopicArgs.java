// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class KafkaClusterTopicArgs extends com.pulumi.resources.ResourceArgs {

    public static final KafkaClusterTopicArgs Empty = new KafkaClusterTopicArgs();

    /**
     * The ID of the Kafka Cluster to which the topic belongs.
     * 
     */
    @Import(name="clusterId", required=true)
    private Output<String> clusterId;

    /**
     * @return The ID of the Kafka Cluster to which the topic belongs.
     * 
     */
    public Output<String> clusterId() {
        return this.clusterId;
    }

    /**
     * The location of your Kafka Cluster Topic. Supported locations: de/fra, de/txl
     * 
     */
    @Import(name="location", required=true)
    private Output<String> location;

    /**
     * @return The location of your Kafka Cluster Topic. Supported locations: de/fra, de/txl
     * 
     */
    public Output<String> location() {
        return this.location;
    }

    /**
     * The name of your Kafka Cluster Topic. Must be 63 characters or less and must begin and end with an alphanumeric
     * character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return The name of your Kafka Cluster Topic. Must be 63 characters or less and must begin and end with an alphanumeric
     * character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * The number of partitions of the topic. Partitions allow for parallel processing of messages. The partition count must be
     * greater than or equal to the replication factor.
     * 
     */
    @Import(name="numberOfPartitions")
    private @Nullable Output<Integer> numberOfPartitions;

    /**
     * @return The number of partitions of the topic. Partitions allow for parallel processing of messages. The partition count must be
     * greater than or equal to the replication factor.
     * 
     */
    public Optional<Output<Integer>> numberOfPartitions() {
        return Optional.ofNullable(this.numberOfPartitions);
    }

    /**
     * The number of replicas of the topic. The replication factor determines how many copies of the topic are stored on
     * different brokers. The replication factor must be less than or equal to the number of brokers in the Kafka Cluster.
     * 
     */
    @Import(name="replicationFactor")
    private @Nullable Output<Integer> replicationFactor;

    /**
     * @return The number of replicas of the topic. The replication factor determines how many copies of the topic are stored on
     * different brokers. The replication factor must be less than or equal to the number of brokers in the Kafka Cluster.
     * 
     */
    public Optional<Output<Integer>> replicationFactor() {
        return Optional.ofNullable(this.replicationFactor);
    }

    /**
     * This configuration controls the maximum time we will retain a log before we will discard old log segments to free up
     * space. This represents an SLA on how soon consumers must read their data. If set to -1, no time limit is applied.
     * 
     */
    @Import(name="retentionTime")
    private @Nullable Output<Integer> retentionTime;

    /**
     * @return This configuration controls the maximum time we will retain a log before we will discard old log segments to free up
     * space. This represents an SLA on how soon consumers must read their data. If set to -1, no time limit is applied.
     * 
     */
    public Optional<Output<Integer>> retentionTime() {
        return Optional.ofNullable(this.retentionTime);
    }

    /**
     * This configuration controls the segment file size for the log. Retention and cleaning is always done a file at a time so
     * a larger segment size means fewer files but less granular control over retention.
     * 
     */
    @Import(name="segmentBytes")
    private @Nullable Output<Integer> segmentBytes;

    /**
     * @return This configuration controls the segment file size for the log. Retention and cleaning is always done a file at a time so
     * a larger segment size means fewer files but less granular control over retention.
     * 
     */
    public Optional<Output<Integer>> segmentBytes() {
        return Optional.ofNullable(this.segmentBytes);
    }

    private KafkaClusterTopicArgs() {}

    private KafkaClusterTopicArgs(KafkaClusterTopicArgs $) {
        this.clusterId = $.clusterId;
        this.location = $.location;
        this.name = $.name;
        this.numberOfPartitions = $.numberOfPartitions;
        this.replicationFactor = $.replicationFactor;
        this.retentionTime = $.retentionTime;
        this.segmentBytes = $.segmentBytes;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(KafkaClusterTopicArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private KafkaClusterTopicArgs $;

        public Builder() {
            $ = new KafkaClusterTopicArgs();
        }

        public Builder(KafkaClusterTopicArgs defaults) {
            $ = new KafkaClusterTopicArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param clusterId The ID of the Kafka Cluster to which the topic belongs.
         * 
         * @return builder
         * 
         */
        public Builder clusterId(Output<String> clusterId) {
            $.clusterId = clusterId;
            return this;
        }

        /**
         * @param clusterId The ID of the Kafka Cluster to which the topic belongs.
         * 
         * @return builder
         * 
         */
        public Builder clusterId(String clusterId) {
            return clusterId(Output.of(clusterId));
        }

        /**
         * @param location The location of your Kafka Cluster Topic. Supported locations: de/fra, de/txl
         * 
         * @return builder
         * 
         */
        public Builder location(Output<String> location) {
            $.location = location;
            return this;
        }

        /**
         * @param location The location of your Kafka Cluster Topic. Supported locations: de/fra, de/txl
         * 
         * @return builder
         * 
         */
        public Builder location(String location) {
            return location(Output.of(location));
        }

        /**
         * @param name The name of your Kafka Cluster Topic. Must be 63 characters or less and must begin and end with an alphanumeric
         * character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name The name of your Kafka Cluster Topic. Must be 63 characters or less and must begin and end with an alphanumeric
         * character (`[a-z0-9A-Z]`) with dashes (`-`), underscores (`_`), dots (`.`), and alphanumerics between.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param numberOfPartitions The number of partitions of the topic. Partitions allow for parallel processing of messages. The partition count must be
         * greater than or equal to the replication factor.
         * 
         * @return builder
         * 
         */
        public Builder numberOfPartitions(@Nullable Output<Integer> numberOfPartitions) {
            $.numberOfPartitions = numberOfPartitions;
            return this;
        }

        /**
         * @param numberOfPartitions The number of partitions of the topic. Partitions allow for parallel processing of messages. The partition count must be
         * greater than or equal to the replication factor.
         * 
         * @return builder
         * 
         */
        public Builder numberOfPartitions(Integer numberOfPartitions) {
            return numberOfPartitions(Output.of(numberOfPartitions));
        }

        /**
         * @param replicationFactor The number of replicas of the topic. The replication factor determines how many copies of the topic are stored on
         * different brokers. The replication factor must be less than or equal to the number of brokers in the Kafka Cluster.
         * 
         * @return builder
         * 
         */
        public Builder replicationFactor(@Nullable Output<Integer> replicationFactor) {
            $.replicationFactor = replicationFactor;
            return this;
        }

        /**
         * @param replicationFactor The number of replicas of the topic. The replication factor determines how many copies of the topic are stored on
         * different brokers. The replication factor must be less than or equal to the number of brokers in the Kafka Cluster.
         * 
         * @return builder
         * 
         */
        public Builder replicationFactor(Integer replicationFactor) {
            return replicationFactor(Output.of(replicationFactor));
        }

        /**
         * @param retentionTime This configuration controls the maximum time we will retain a log before we will discard old log segments to free up
         * space. This represents an SLA on how soon consumers must read their data. If set to -1, no time limit is applied.
         * 
         * @return builder
         * 
         */
        public Builder retentionTime(@Nullable Output<Integer> retentionTime) {
            $.retentionTime = retentionTime;
            return this;
        }

        /**
         * @param retentionTime This configuration controls the maximum time we will retain a log before we will discard old log segments to free up
         * space. This represents an SLA on how soon consumers must read their data. If set to -1, no time limit is applied.
         * 
         * @return builder
         * 
         */
        public Builder retentionTime(Integer retentionTime) {
            return retentionTime(Output.of(retentionTime));
        }

        /**
         * @param segmentBytes This configuration controls the segment file size for the log. Retention and cleaning is always done a file at a time so
         * a larger segment size means fewer files but less granular control over retention.
         * 
         * @return builder
         * 
         */
        public Builder segmentBytes(@Nullable Output<Integer> segmentBytes) {
            $.segmentBytes = segmentBytes;
            return this;
        }

        /**
         * @param segmentBytes This configuration controls the segment file size for the log. Retention and cleaning is always done a file at a time so
         * a larger segment size means fewer files but less granular control over retention.
         * 
         * @return builder
         * 
         */
        public Builder segmentBytes(Integer segmentBytes) {
            return segmentBytes(Output.of(segmentBytes));
        }

        public KafkaClusterTopicArgs build() {
            if ($.clusterId == null) {
                throw new MissingRequiredPropertyException("KafkaClusterTopicArgs", "clusterId");
            }
            if ($.location == null) {
                throw new MissingRequiredPropertyException("KafkaClusterTopicArgs", "location");
            }
            return $;
        }
    }

}
