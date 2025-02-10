import * as pulumi from "@pulumi/pulumi";
import * as ionoscloud from "@pulumi/ionoscloud";

const resource = new ionoscloud.Resource("Resource", { sampleAttribute: "attr" });

export const sampleAttribute = resource.sampleAttribute;
