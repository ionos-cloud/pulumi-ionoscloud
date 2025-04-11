<p align="center">
  <title="Pulumi Ionoscloud Provider - Build and Deploy Infrastructure as Code Solutions on Any Cloud">
    <img src="https://www.pulumi.com/images/logo/logo-on-white-box.svg?" width="350">
  </a>
</p>

[![PkgGoDev](https://pkg.go.dev/badge/github.com/pulumi/pulumi-ionoscloud/sdk/go)](https://pkg.go.dev/github.com/pulumi/pulumi-ionoscloud/sdk/go)

# Ionoscloud provider

The Ionoscloud resource provider for Pulumi lets you use Ionoscloud resources in your cloud programs. To use this package, [install the Pulumi CLI](https://www.pulumi.com/docs/get-started/install/).


## Installing

This package is available in many languages in the standard packaging formats.

### Node.js (Java/TypeScript)

To use JavaScript or TypeScript in Node.js, install using either `npm`:

    npm install @ionos-cloud/sdk-pulumi

or `yarn`:

    yarn add @ionos-cloud/sdk-pulumi

### Python

To use Python, install using `pip`:

    pip install pulumi_ionoscloud

### Go

To use Go, use `go get` to grab the latest version of the library

    $ go get github.com/pulumi/pulumi-ionoscloud/sdk/go

### .NET

To use from .NET, install using `dotnet add package`:

    dotnet add package Ionoscloud.Pulumi.Ionoscloud

## Environment Variables

| Environment Variable    | Description                                                                                                                                                              |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `IONOS_USERNAME`        | Specify the username used to login, to authenticate against the IONOS Cloud API                                                                                          |
| `IONOS_PASSWORD`        | Specify the password used to login, to authenticate against the IONOS Cloud API                                                                                          |
| `IONOS_TOKEN`           | Specify the token used to login, if a token is being used instead of username and password                                                                               |
| `IONOS_API_URL`         | Specify the API URL. It will overwrite the API endpoint default value `api.ionos.com`. It is not necessary to override this value unless you have special routing config |
| `IONOS_LOG_LEVEL`       | Specify the Log Level used to log messages. Possible values: Off, Debug, Trace                                                                                           |
| `IONOS_PINNED_CERT`     | Specify the SHA-256 public fingerprint here, enables certificate pinning                                                                                                 |
| `IONOS_CONTRACT_NUMBER` | Specify the contract number on which you wish to provision. Only valid for reseller accounts, for other types of accounts the header will be ignored                     |
| `IONOS_S3_ACCESS_KEY`   | Specify the access key used to authenticate against the IONOS Object Storage API                                                                                         |
| `IONOS_S3_SECRET_KEY`   | Specify the secret key used to authenticate against the IONOS Object Storage API                                                                                         |
| `IONOS_S3_REGION`       | Region for IONOS Object Storage operations. Default value: eu-central-3. **If you use IONOS_API_URL_OBJECT_STORAGE, `IONOS_S3_REGION` is mandatory**                     |

## Certificate pinning:

You can enable certificate pinning if you want to bypass the normal certificate checking procedure, by doing the following:

Set env variable IONOS_PINNED_CERT=`<insert_sha256_public_fingerprint_here>`

You can get the sha256 fingerprint most easily from the browser by inspecting the certificate.

## Debugging

You can enable logging now using the `IONOS_LOG_LEVEL` env variable. Allowed values: `off`, `debug` and `trace`. Defaults to `off`.

⚠️ **Note:** We recommend you only use `trace` level for debugging purposes. Disable it in your production environments because it can log sensitive data. It logs the full request and response without encryption, even for an HTTPS call.
Verbose request and response logging can also significantly impact your application’s performance.

```bash
$ export IONOS_LOG_LEVEL=debug
```
