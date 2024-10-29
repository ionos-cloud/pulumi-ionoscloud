// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

declare var exports: any;
const __config = new pulumi.Config("ionoscloud");

export declare const contractNumber: string | undefined;
Object.defineProperty(exports, "contractNumber", {
    get() {
        return __config.get("contractNumber");
    },
    enumerable: true,
});

/**
 * IonosCloud REST API URL. Usually not necessary to be set, SDKs know internally how to route requests to the API.
 */
export declare const endpoint: string | undefined;
Object.defineProperty(exports, "endpoint", {
    get() {
        return __config.get("endpoint");
    },
    enumerable: true,
});

/**
 * IonosCloud password for API operations. If token is provided, token is preferred
 */
export declare const password: string | undefined;
Object.defineProperty(exports, "password", {
    get() {
        return __config.get("password");
    },
    enumerable: true,
});

export declare const retries: number | undefined;
Object.defineProperty(exports, "retries", {
    get() {
        return __config.getObject<number>("retries");
    },
    enumerable: true,
});

/**
 * Access key for IONOS Object Storage operations.
 */
export declare const s3AccessKey: string | undefined;
Object.defineProperty(exports, "s3AccessKey", {
    get() {
        return __config.get("s3AccessKey");
    },
    enumerable: true,
});

/**
 * Region for IONOS Object Storage operations.
 */
export declare const s3Region: string | undefined;
Object.defineProperty(exports, "s3Region", {
    get() {
        return __config.get("s3Region");
    },
    enumerable: true,
});

/**
 * Secret key for IONOS Object Storage operations.
 */
export declare const s3SecretKey: string | undefined;
Object.defineProperty(exports, "s3SecretKey", {
    get() {
        return __config.get("s3SecretKey");
    },
    enumerable: true,
});

/**
 * IonosCloud bearer token for API operations.
 */
export declare const token: string | undefined;
Object.defineProperty(exports, "token", {
    get() {
        return __config.get("token");
    },
    enumerable: true,
});

/**
 * IonosCloud username for API operations. If token is provided, token is preferred
 */
export declare const username: string | undefined;
Object.defineProperty(exports, "username", {
    get() {
        return __config.get("username");
    },
    enumerable: true,
});

