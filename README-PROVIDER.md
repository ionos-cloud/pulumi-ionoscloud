# IONOS Cloud Resource Provider

The IONOS Cloud Resource Provider lets you manage [IONOS Cloud](https://cloud.ionos.com/) resources.

## Installing

This package is available for several languages/platforms:

### Node.js (JavaScript/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

```bash
npm install @ionos-cloud/sdk-pulumi
```

or `yarn`:

```bash
yarn add @ionos-cloud/sdk-pulumi
```

### Python

To use from Python, install using `pip`:

```bash
pip install pulumi_ionoscloud
```

### Go

To use from Go, use `go get` to grab the latest version of the library:

```bash
go get github.com/ionos-cloud/pulumi-ionoscloud/sdk
```

### .NET

To use from .NET, install using `dotnet add package`:

```bash
dotnet add package Ionoscloud.Pulumi.Ionoscloud
```

## Configuration

The following configuration points are available for the `ionoscloud` provider:

- `ionoscloud:username` (environment: `IONOS_USERNAME`) - the username for IONOS Cloud API authentication
- `ionoscloud:password` (environment: `IONOS_PASSWORD`) - the password for IONOS Cloud API authentication
- `ionoscloud:token` (environment: `IONOS_TOKEN`) - the API token for authentication (alternative to username/password)

## Reference

For detailed reference documentation, please visit [the Pulumi registry](https://www.pulumi.com/registry/packages/ionoscloud/api-docs/).
