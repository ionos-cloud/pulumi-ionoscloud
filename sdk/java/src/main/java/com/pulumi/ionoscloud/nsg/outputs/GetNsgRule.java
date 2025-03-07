// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.nsg.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetNsgRule {
    private String icmpCode;
    private String icmpType;
    /**
     * @return Id of an existing Network Security Group that you want to search for.
     * 
     */
    private String id;
    /**
     * @return Name of an existing Network Security Group that you want to search for.
     * 
     * Either `name`, or `id` must be provided. If none, the datasource will return an error.
     * 
     */
    private String name;
    private Integer portRangeEnd;
    private Integer portRangeStart;
    private String protocol;
    private String sourceIp;
    private String sourceMac;
    private String targetIp;
    private String type;

    private GetNsgRule() {}
    public String icmpCode() {
        return this.icmpCode;
    }
    public String icmpType() {
        return this.icmpType;
    }
    /**
     * @return Id of an existing Network Security Group that you want to search for.
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return Name of an existing Network Security Group that you want to search for.
     * 
     * Either `name`, or `id` must be provided. If none, the datasource will return an error.
     * 
     */
    public String name() {
        return this.name;
    }
    public Integer portRangeEnd() {
        return this.portRangeEnd;
    }
    public Integer portRangeStart() {
        return this.portRangeStart;
    }
    public String protocol() {
        return this.protocol;
    }
    public String sourceIp() {
        return this.sourceIp;
    }
    public String sourceMac() {
        return this.sourceMac;
    }
    public String targetIp() {
        return this.targetIp;
    }
    public String type() {
        return this.type;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetNsgRule defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String icmpCode;
        private String icmpType;
        private String id;
        private String name;
        private Integer portRangeEnd;
        private Integer portRangeStart;
        private String protocol;
        private String sourceIp;
        private String sourceMac;
        private String targetIp;
        private String type;
        public Builder() {}
        public Builder(GetNsgRule defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.icmpCode = defaults.icmpCode;
    	      this.icmpType = defaults.icmpType;
    	      this.id = defaults.id;
    	      this.name = defaults.name;
    	      this.portRangeEnd = defaults.portRangeEnd;
    	      this.portRangeStart = defaults.portRangeStart;
    	      this.protocol = defaults.protocol;
    	      this.sourceIp = defaults.sourceIp;
    	      this.sourceMac = defaults.sourceMac;
    	      this.targetIp = defaults.targetIp;
    	      this.type = defaults.type;
        }

        @CustomType.Setter
        public Builder icmpCode(String icmpCode) {
            if (icmpCode == null) {
              throw new MissingRequiredPropertyException("GetNsgRule", "icmpCode");
            }
            this.icmpCode = icmpCode;
            return this;
        }
        @CustomType.Setter
        public Builder icmpType(String icmpType) {
            if (icmpType == null) {
              throw new MissingRequiredPropertyException("GetNsgRule", "icmpType");
            }
            this.icmpType = icmpType;
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetNsgRule", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            if (name == null) {
              throw new MissingRequiredPropertyException("GetNsgRule", "name");
            }
            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder portRangeEnd(Integer portRangeEnd) {
            if (portRangeEnd == null) {
              throw new MissingRequiredPropertyException("GetNsgRule", "portRangeEnd");
            }
            this.portRangeEnd = portRangeEnd;
            return this;
        }
        @CustomType.Setter
        public Builder portRangeStart(Integer portRangeStart) {
            if (portRangeStart == null) {
              throw new MissingRequiredPropertyException("GetNsgRule", "portRangeStart");
            }
            this.portRangeStart = portRangeStart;
            return this;
        }
        @CustomType.Setter
        public Builder protocol(String protocol) {
            if (protocol == null) {
              throw new MissingRequiredPropertyException("GetNsgRule", "protocol");
            }
            this.protocol = protocol;
            return this;
        }
        @CustomType.Setter
        public Builder sourceIp(String sourceIp) {
            if (sourceIp == null) {
              throw new MissingRequiredPropertyException("GetNsgRule", "sourceIp");
            }
            this.sourceIp = sourceIp;
            return this;
        }
        @CustomType.Setter
        public Builder sourceMac(String sourceMac) {
            if (sourceMac == null) {
              throw new MissingRequiredPropertyException("GetNsgRule", "sourceMac");
            }
            this.sourceMac = sourceMac;
            return this;
        }
        @CustomType.Setter
        public Builder targetIp(String targetIp) {
            if (targetIp == null) {
              throw new MissingRequiredPropertyException("GetNsgRule", "targetIp");
            }
            this.targetIp = targetIp;
            return this;
        }
        @CustomType.Setter
        public Builder type(String type) {
            if (type == null) {
              throw new MissingRequiredPropertyException("GetNsgRule", "type");
            }
            this.type = type;
            return this;
        }
        public GetNsgRule build() {
            final var _resultValue = new GetNsgRule();
            _resultValue.icmpCode = icmpCode;
            _resultValue.icmpType = icmpType;
            _resultValue.id = id;
            _resultValue.name = name;
            _resultValue.portRangeEnd = portRangeEnd;
            _resultValue.portRangeStart = portRangeStart;
            _resultValue.protocol = protocol;
            _resultValue.sourceIp = sourceIp;
            _resultValue.sourceMac = sourceMac;
            _resultValue.targetIp = targetIp;
            _resultValue.type = type;
            return _resultValue;
        }
    }
}
