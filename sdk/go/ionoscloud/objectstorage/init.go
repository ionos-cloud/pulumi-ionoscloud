// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package objectstorage

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "ionoscloud:objectstorage/bucket:Bucket":
		r = &Bucket{}
	case "ionoscloud:objectstorage/bucketLifecycleConfiguration:BucketLifecycleConfiguration":
		r = &BucketLifecycleConfiguration{}
	case "ionoscloud:objectstorage/bucketObject:BucketObject":
		r = &BucketObject{}
	case "ionoscloud:objectstorage/bucketPolicy:BucketPolicy":
		r = &BucketPolicy{}
	case "ionoscloud:objectstorage/bucketServerSideEncryptionConfiguration:BucketServerSideEncryptionConfiguration":
		r = &BucketServerSideEncryptionConfiguration{}
	case "ionoscloud:objectstorage/bucketVersioning:BucketVersioning":
		r = &BucketVersioning{}
	case "ionoscloud:objectstorage/corsConfiguration:CorsConfiguration":
		r = &CorsConfiguration{}
	case "ionoscloud:objectstorage/monitoringPipeline:MonitoringPipeline":
		r = &MonitoringPipeline{}
	case "ionoscloud:objectstorage/objectCopy:ObjectCopy":
		r = &ObjectCopy{}
	case "ionoscloud:objectstorage/objectLockConfiguration:ObjectLockConfiguration":
		r = &ObjectLockConfiguration{}
	case "ionoscloud:objectstorage/publicAccessBlock:PublicAccessBlock":
		r = &PublicAccessBlock{}
	case "ionoscloud:objectstorage/websiteConfiguration:WebsiteConfiguration":
		r = &WebsiteConfiguration{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

func init() {
	version, err := internal.PkgVersion()
	if err != nil {
		version = semver.Version{Major: 1}
	}
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"objectstorage/bucket",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"objectstorage/bucketLifecycleConfiguration",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"objectstorage/bucketObject",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"objectstorage/bucketPolicy",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"objectstorage/bucketServerSideEncryptionConfiguration",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"objectstorage/bucketVersioning",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"objectstorage/corsConfiguration",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"objectstorage/monitoringPipeline",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"objectstorage/objectCopy",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"objectstorage/objectLockConfiguration",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"objectstorage/publicAccessBlock",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ionoscloud",
		"objectstorage/websiteConfiguration",
		&module{version},
	)
}
