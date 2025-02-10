# Terraform Bridge Provider Boilerplate

This repository is the template for authoring a Pulumi package from an existing Terraform provider as part of the guide for [authoring and publishing Pulumi packages](https://www.pulumi.com/docs/iac/packages-and-automation/pulumi-packages/authoring/).

This repository is initially set up as a fictitious provider named "ionoscloud" to demonstrate a resource, a data source and configuration derived from the [github.com/pulumi/terraform-provider-ionoscloud provider](https://github.com/pulumi/terraform-provider-ionoscloud).

Read the [setup instructions](SETUP.md) for step-by-step instructions on how to bridge a new provider and refer to our complete docs [guide for authoring and publishing a Pulumi Package](https://www.pulumi.com/docs/iac/packages-and-automation/pulumi-packages/authoring/).

# ionoscloud Resource Provider

The ionoscloud Resource Provider lets you manage [ionoscloud](http://example.com) resources.

## Installing

This package is available for several languages/platforms:

### Node.js (JavaScript/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

```bash
npm install @pulumi/ionoscloud
```

or `yarn`:

```bash
yarn add @pulumi/ionoscloud
```

### Python

To use from Python, install using `pip`:

```bash
pip install pulumi_ionoscloud
```

### Go

To use from Go, use `go get` to grab the latest version of the library:

```bash
go get github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/...
```

### .NET

To use from .NET, install using `dotnet add package`:

```bash
dotnet add package Pulumi.ionoscloud
```

## Configuration

The following configuration points are available for the `ionoscloud` provider:

- `ionoscloud:region` (environment: `ionoscloud_REGION`) - the region in which to deploy resources

## Reference

For detailed reference documentation, please visit [the Pulumi registry](https://www.pulumi.com/registry/packages/ionoscloud/api-docs/).
