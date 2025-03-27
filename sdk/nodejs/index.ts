// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export { GetMonitoringPipelineArgs, GetMonitoringPipelineResult, GetMonitoringPipelineOutputArgs } from "./getMonitoringPipeline";
export const getMonitoringPipeline: typeof import("./getMonitoringPipeline").getMonitoringPipeline = null as any;
export const getMonitoringPipelineOutput: typeof import("./getMonitoringPipeline").getMonitoringPipelineOutput = null as any;
utilities.lazyLoad(exports, ["getMonitoringPipeline","getMonitoringPipelineOutput"], () => require("./getMonitoringPipeline"));

export { GetObjectStorageAccesskeyArgs, GetObjectStorageAccesskeyResult, GetObjectStorageAccesskeyOutputArgs } from "./getObjectStorageAccesskey";
export const getObjectStorageAccesskey: typeof import("./getObjectStorageAccesskey").getObjectStorageAccesskey = null as any;
export const getObjectStorageAccesskeyOutput: typeof import("./getObjectStorageAccesskey").getObjectStorageAccesskeyOutput = null as any;
utilities.lazyLoad(exports, ["getObjectStorageAccesskey","getObjectStorageAccesskeyOutput"], () => require("./getObjectStorageAccesskey"));

export { GetObjectStorageRegionArgs, GetObjectStorageRegionResult, GetObjectStorageRegionOutputArgs } from "./getObjectStorageRegion";
export const getObjectStorageRegion: typeof import("./getObjectStorageRegion").getObjectStorageRegion = null as any;
export const getObjectStorageRegionOutput: typeof import("./getObjectStorageRegion").getObjectStorageRegionOutput = null as any;
utilities.lazyLoad(exports, ["getObjectStorageRegion","getObjectStorageRegionOutput"], () => require("./getObjectStorageRegion"));

export { GetS3ObjectsArgs, GetS3ObjectsResult, GetS3ObjectsOutputArgs } from "./getS3Objects";
export const getS3Objects: typeof import("./getS3Objects").getS3Objects = null as any;
export const getS3ObjectsOutput: typeof import("./getS3Objects").getS3ObjectsOutput = null as any;
utilities.lazyLoad(exports, ["getS3Objects","getS3ObjectsOutput"], () => require("./getS3Objects"));

export { ObjectStorageAccesskeyArgs, ObjectStorageAccesskeyState } from "./objectStorageAccesskey";
export type ObjectStorageAccesskey = import("./objectStorageAccesskey").ObjectStorageAccesskey;
export const ObjectStorageAccesskey: typeof import("./objectStorageAccesskey").ObjectStorageAccesskey = null as any;
utilities.lazyLoad(exports, ["ObjectStorageAccesskey"], () => require("./objectStorageAccesskey"));

export { ProviderArgs } from "./provider";
export type Provider = import("./provider").Provider;
export const Provider: typeof import("./provider").Provider = null as any;
utilities.lazyLoad(exports, ["Provider"], () => require("./provider"));


// Export sub-modules:
import * as alb from "./alb";
import * as apigateway from "./apigateway";
import * as autoscaling from "./autoscaling";
import * as cdn from "./cdn";
import * as cert from "./cert";
import * as compute from "./compute";
import * as config from "./config";
import * as creg from "./creg";
import * as dbaas from "./dbaas";
import * as dns from "./dns";
import * as dsaas from "./dsaas";
import * as k8s from "./k8s";
import * as kafka from "./kafka";
import * as logging from "./logging";
import * as monitoring from "./monitoring";
import * as nfs from "./nfs";
import * as nlb from "./nlb";
import * as nsg from "./nsg";
import * as objectstorage from "./objectstorage";
import * as types from "./types";
import * as vpn from "./vpn";

export {
    alb,
    apigateway,
    autoscaling,
    cdn,
    cert,
    compute,
    config,
    creg,
    dbaas,
    dns,
    dsaas,
    k8s,
    kafka,
    logging,
    monitoring,
    nfs,
    nlb,
    nsg,
    objectstorage,
    types,
    vpn,
};

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "ionoscloud:index/objectStorageAccesskey:ObjectStorageAccesskey":
                return new ObjectStorageAccesskey(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("ionoscloud", "index/objectStorageAccesskey", _module)
pulumi.runtime.registerResourcePackage("ionoscloud", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:ionoscloud") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});
